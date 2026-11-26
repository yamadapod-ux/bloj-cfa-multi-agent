#!/usr/bin/env node
// scripts/check-triggers.js — WP3 of แผนปรับปรุงระบบ (CIO-approved 2026-11-24)
// Deterministic (no LLM) checker for 2 trigger types that news-pulse used to ask an LLM to
// eyeball by reading prose: (1) stop-loss breach on any OPEN position (2) VIX regime-tier
// change vs the ledger's last known tier. Adds a ledger item via scripts/actions.js when a
// NEW condition is found (idempotent — skips if an open item for the same ticker+type, or
// same VIX tier flip, already exists). Read-only otherwise.
//
// Usage:
//   node scripts/check-triggers.js [--dry-run] [--portfolio path] [--macro path] [--ledger path]
//
// Exit code: 0 = ran fine (regardless of whether triggers fired), 1 = could not read/parse
// a required data file (fail loud, don't silently skip).

const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { execFileSync } = require('child_process');

function loadJsConst(file, constNames) {
  // dashboard/*.js files are plain `const NAME = {...}` / `[...]` scripts meant for a
  // <script> tag — run them in a throwaway VM sandbox and pull the named consts back out.
  // `const X = ...` does not attach X as a property of the context object in Node's vm
  // module (only `var`/bare assignment do) — explicitly copy the bindings onto `this`
  // (== the context object for a non-strict top-level script) after the file's own code.
  const code = fs.readFileSync(file, 'utf8')
    + '\n;' + constNames.map(n => `if (typeof ${n} !== 'undefined') { this.${n} = ${n}; }`).join('\n');
  const sandbox = {};
  vm.createContext(sandbox);
  vm.runInContext(code, sandbox, { filename: file });
  const out = {};
  for (const name of constNames) out[name] = sandbox[name];
  return out;
}

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--dry-run') { out.dryRun = true; continue; }
    if (a.startsWith('--')) { out[a.slice(2)] = argv[i + 1]; i++; }
  }
  return out;
}

function actionsAdd(ledgerFile, { type, title, owner, ticker, due, evidence, defaultOnTimeout }, dryRun) {
  const scriptPath = path.join(__dirname, 'actions.js');
  const args = ['add', '--type', type, '--title', title, '--owner', owner, '--file', ledgerFile];
  if (ticker) args.push('--ticker', ticker);
  if (due) args.push('--due', due);
  if (evidence) args.push('--evidence', evidence);
  if (defaultOnTimeout) args.push('--default-on-timeout', defaultOnTimeout);
  if (dryRun) args.push('--dry-run');
  const result = execFileSync('node', [scriptPath, ...args], { encoding: 'utf8' });
  return result.trim();
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const root = path.join(__dirname, '..');
  const portfolioFile = args.portfolio || path.join(root, 'dashboard', 'portfolio.js');
  const macroFile = args.macro || path.join(root, 'dashboard', 'macroRegime.js');
  const ledgerFile = args.ledger || path.join(root, 'portfolio', 'actions.json');
  const dryRun = !!args.dryRun;

  let PORTFOLIO, MACRO_REGIME_HISTORY;
  try {
    ({ PORTFOLIO } = loadJsConst(portfolioFile, ['PORTFOLIO']));
    ({ MACRO_REGIME_HISTORY } = loadJsConst(macroFile, ['MACRO_REGIME_HISTORY']));
  } catch (e) {
    console.error(`ERROR: ไม่สามารถอ่าน/parse ไฟล์ข้อมูลได้: ${e.message}`);
    process.exit(1);
  }
  if (!PORTFOLIO || !Array.isArray(PORTFOLIO.positions)) {
    console.error('ERROR: ไม่พบ PORTFOLIO.positions');
    process.exit(1);
  }
  if (!Array.isArray(MACRO_REGIME_HISTORY) || MACRO_REGIME_HISTORY.length === 0) {
    console.error('ERROR: ไม่พบ MACRO_REGIME_HISTORY');
    process.exit(1);
  }

  let ledger;
  try {
    ledger = JSON.parse(fs.readFileSync(ledgerFile, 'utf8'));
  } catch (e) {
    console.error(`ERROR: ไม่สามารถอ่าน ledger ได้: ${e.message}`);
    process.exit(1);
  }
  const openItems = ledger.items.filter(i => i.status === 'open');

  const actions = [];

  // --- Check 1: stop-loss breach on any OPEN position ---
  for (const p of PORTFOLIO.positions) {
    if (!p.status || !String(p.status).startsWith('OPEN')) continue;
    if (typeof p.stopDistancePct !== 'number') continue;
    if (p.stopDistancePct <= 0) {
      const already = openItems.some(i => i.type === 'stop_loss' && i.ticker === p.ticker);
      if (already) {
        console.log(`[skip] ${p.ticker} stop-loss breach — ledger item เปิดอยู่แล้ว`);
        continue;
      }
      const title = `${p.ticker} stop-loss breach (stopDist ${p.stopDistancePct.toFixed(2)}%, priceUpdated ${p.priceUpdated || '?'}) — ต้องมี decision record`;
      const out = actionsAdd(ledgerFile, {
        type: 'stop_loss', title, owner: 'Max', ticker: p.ticker,
        evidence: `dashboard/portfolio.js positions[ticker=${p.ticker}] stopDistancePct=${p.stopDistancePct}, currentPrice=${p.currentPrice}, stopLoss=${p.stopLoss}`,
        defaultOnTimeout: 'escalate อย่างเดียว ไม่บังคับเทรด (CIO decision 2026-11-24)',
      }, dryRun);
      console.log(`[fire] stop-loss: ${p.ticker} — ${out}`);
      actions.push({ type: 'stop_loss', ticker: p.ticker });
    }
  }

  // --- Check 2: VIX regime tier change vs last ledger-recorded tier ---
  const latestRegime = MACRO_REGIME_HISTORY[MACRO_REGIME_HISTORY.length - 1];
  const vixIndicator = latestRegime && latestRegime.indicators && latestRegime.indicators.vix;
  const vixClass = vixIndicator && vixIndicator.classification;
  if (vixClass) {
    // Use a note on the most recent OPEN regime_recall-type item (if any) as the "last known
    // tier" marker; if none exists or the tier differs, that itself is the new-condition signal
    // this check exists to catch (a fresh Atlas re-call becoming due because the VIX band moved).
    const lastVixNote = ledger.items
      .filter(i => i.type === 'regime_recall')
      .flatMap(i => i.history || [])
      .filter(h => h.detail && h.detail.startsWith('vix_tier:'))
      .sort((a, b) => (a.date < b.date ? -1 : 1))
      .pop();
    const lastTier = lastVixNote ? lastVixNote.detail.replace('vix_tier:', '') : null;
    if (lastTier !== vixClass) {
      const already = openItems.some(i => i.type === 'regime_recall' && i.title.includes('VIX tier เปลี่ยน'));
      if (already) {
        console.log(`[skip] VIX tier เปลี่ยนเป็น ${vixClass} — ledger item regime_recall เปิดอยู่แล้ว`);
      } else {
        const title = `VIX tier เปลี่ยนเป็น ${vixClass} (vix=${vixIndicator.value}, record ${latestRegime.date || '?'}) — Atlas ต้อง re-call regime`;
        const out = actionsAdd(ledgerFile, {
          type: 'regime_recall', title, owner: 'Atlas',
          evidence: `dashboard/macroRegime.js MACRO_REGIME_HISTORY[-1].indicators.vix = ${JSON.stringify(vixIndicator)}`,
        }, dryRun);
        console.log(`[fire] vix_tier_change: ${vixClass} — ${out}`);
        if (!dryRun) {
          // record the tier we just reacted to so this doesn't re-fire every run
          const addedId = /เพิ่ม (ACT-\d+)/.exec(out);
          if (addedId) {
            execFileSync('node', [path.join(__dirname, 'actions.js'), 'note', '--id', addedId[1], '--note', `vix_tier:${vixClass}`, '--file', ledgerFile], { encoding: 'utf8' });
          }
        }
        actions.push({ type: 'regime_recall', vix: vixClass });
      }
    } else {
      console.log(`[ok] VIX tier ${vixClass} ไม่เปลี่ยนจากครั้งก่อน — ไม่ fire`);
    }
  } else {
    console.log('[warn] ไม่พบ vix.classification ใน MACRO_REGIME_HISTORY entry ล่าสุด — ข้าม check VIX');
  }

  console.log(`\n=== check-triggers.js เสร็จ — fired ${actions.length} เรื่องใหม่ ===`);
}

main();
