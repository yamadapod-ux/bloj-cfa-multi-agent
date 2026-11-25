#!/usr/bin/env node
// scripts/actions.js — Action Ledger CLI (WP1 of แผนปรับปรุงระบบ, CIO-approved 2026-11-24)
// ห้ามแก้ portfolio/actions.json ด้วยมือ — ใช้ CLI นี้เท่านั้น
// Usage:
//   node scripts/actions.js add --type <type> --title "..." --owner <owner> [--ticker T] [--due YYYY-MM-DD] [--evidence "..."] [--default-on-timeout "..."] [--dry-run] [--file path]
//   node scripts/actions.js close --id ACT-0001 [--note "..."] [--dry-run] [--file path]
//   node scripts/actions.js note --id ACT-0001 --note "..." [--dry-run] [--file path]
//   node scripts/actions.js check [--owner X] [--json] [--file path]
//   node scripts/actions.js escalate [--dry-run] [--file path]

const fs = require('fs');
const path = require('path');

const VALID_TYPES = ['stop_loss', 'consultation', 'regime_recall', 'qa_reanalysis', 'fv_stale', 'open_decision', 'other'];
const VALID_STATUS = ['open', 'done', 'dropped'];

function parseArgs(argv) {
  const out = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      if (key === 'dry-run' || key === 'json') { out[key] = true; continue; }
      out[key] = argv[i + 1];
      i++;
    } else {
      out._.push(a);
    }
  }
  return out;
}

// ใช้เวลาไทย (Asia/Bangkok) เสมอ ไม่ใช้ toISOString() ตรงๆ (เป็น UTC — เที่ยงคืนถึง 7 โมงเช้าไทยจะได้วันที่ของเมื่อวาน)
function formatDateBangkok(date) {
  return new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Bangkok', year: 'numeric', month: '2-digit', day: '2-digit' }).format(date);
}

function todayStr() {
  return formatDateBangkok(new Date());
}

function daysBetween(a, b) {
  const da = new Date(a + 'T00:00:00Z');
  const db = new Date(b + 'T00:00:00Z');
  return Math.round((db - da) / 86400000);
}

function loadLedger(file) {
  const raw = fs.readFileSync(file, 'utf8');
  const data = JSON.parse(raw);
  validateSchema(data); // throws on invalid
  return data;
}

function validateSchema(data) {
  if (typeof data !== 'object' || data === null) throw new Error('SCHEMA: root must be object');
  if (data.schema_version !== 1) throw new Error('SCHEMA: schema_version must be 1');
  if (typeof data.sla_days !== 'object') throw new Error('SCHEMA: sla_days missing');
  if (typeof data.next_seq !== 'number') throw new Error('SCHEMA: next_seq must be number');
  if (!Array.isArray(data.items)) throw new Error('SCHEMA: items must be array');
  for (const it of data.items) {
    const req = ['id', 'type', 'title', 'owner', 'created', 'status', 'escalation_level', 'history'];
    for (const k of req) {
      if (!(k in it)) throw new Error(`SCHEMA: item ${it.id || '?'} missing field '${k}'`);
    }
    if (!VALID_TYPES.includes(it.type)) throw new Error(`SCHEMA: item ${it.id} invalid type '${it.type}'`);
    if (!VALID_STATUS.includes(it.status)) throw new Error(`SCHEMA: item ${it.id} invalid status '${it.status}'`);
    if (![0, 1, 2].includes(it.escalation_level)) throw new Error(`SCHEMA: item ${it.id} invalid escalation_level`);
    if (!Array.isArray(it.history)) throw new Error(`SCHEMA: item ${it.id} history must be array`);
  }
}

function saveLedger(file, data, dryRun) {
  validateSchema(data);
  const text = JSON.stringify(data, null, 2) + '\n';
  if (dryRun) {
    console.log(`[--dry-run] จะเขียนไฟล์ ${file} (${text.length} bytes) — ไม่ได้เขียนจริง`);
    return;
  }
  fs.writeFileSync(file, text, 'utf8');
}

// dashboard/actionsData.js — generated projection of the ledger for the file:// dashboard.
// WP-DB1: dashboard cannot use fetch() (opened via file://), so it needs a plain <script> data
// file in the same style as dashboard/portfolio.js, dashboard/news.js etc.
// Location is derived relative to the ledger file (../dashboard/actionsData.js from the
// ledger's parent dir) so tests can point --file at a throwaway fixture dir without touching
// the real dashboard/actionsData.js.
function dashboardOutputPath(file) {
  return path.join(path.dirname(file), '..', 'dashboard', 'actionsData.js');
}

function buildActionsData(data) {
  const today = todayStr();
  const items = data.items.map(it => {
    const due = effectiveDue(it, data.sla_days);
    const daysUntilDue = due ? daysBetween(today, due) : null; // negative = overdue
    return {
      id: it.id,
      type: it.type,
      ticker: it.ticker,
      title: it.title,
      owner: it.owner,
      created: it.created,
      due,
      daysUntilDue,
      status: it.status,
      escalation_level: it.escalation_level,
      default_on_timeout: it.default_on_timeout,
      evidence: it.evidence,
    };
  });
  return { generatedAt: new Date().toISOString(), items };
}

function writeActionsData(file, data) {
  const outPath = dashboardOutputPath(file);
  const outDir = path.dirname(outPath);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  const payload = buildActionsData(data);
  const text = '// =================================================================\n'
    + '// dashboard/actionsData.js — AUTO-GENERATED by scripts/actions.js (WP-DB1)\n'
    + '// Regenerated every time the Action Ledger changes (add/close/note/escalate, non-dry-run)\n'
    + '// and on every `check` — DO NOT EDIT BY HAND, your changes will be overwritten.\n'
    + '// Source of truth: portfolio/actions.json — see scripts/actions.js\n'
    + '// =================================================================\n\n'
    + `const ACTIONS_DATA = ${JSON.stringify(payload, null, 2)};\n`;
  fs.writeFileSync(outPath, text, 'utf8');
}

function effectiveDue(item, slaDays) {
  if (item.due) return item.due;
  const sla = slaDays[item.type] != null ? slaDays[item.type] : slaDays.other;
  const d = new Date(item.created + 'T00:00:00Z');
  d.setUTCDate(d.getUTCDate() + sla);
  return formatDateBangkok(d);
}

function cmdAdd(args, file) {
  if (!args.type || !args.title || !args.owner) {
    console.error('ERROR: add ต้องมี --type --title --owner');
    process.exit(2);
  }
  if (!VALID_TYPES.includes(args.type)) {
    console.error(`ERROR: type ต้องเป็นหนึ่งใน ${VALID_TYPES.join(', ')}`);
    process.exit(2);
  }
  const data = loadLedger(file);
  const id = `ACT-${String(data.next_seq).padStart(4, '0')}`;
  const created = args.created || todayStr();
  const item = {
    id,
    type: args.type,
    ticker: args.ticker || null,
    title: args.title,
    owner: args.owner,
    created,
    due: args.due || null,
    status: 'open',
    escalation_level: 0,
    default_on_timeout: args['default-on-timeout'] || null,
    evidence: args.evidence || null,
    history: [{ date: created, action: 'created', by: args.by || 'Hermes', detail: args.title }],
  };
  data.items.push(item);
  data.next_seq += 1;
  saveLedger(file, data, args['dry-run']);
  if (!args['dry-run']) writeActionsData(file, data);
  console.log(`${args['dry-run'] ? '[dry-run] ' : ''}เพิ่ม ${id} (${args.type}, owner=${args.owner}) due=${effectiveDue(item, data.sla_days)}`);
}

function cmdClose(args, file) {
  if (!args.id) { console.error('ERROR: close ต้องมี --id'); process.exit(2); }
  const data = loadLedger(file);
  const item = data.items.find(i => i.id === args.id);
  if (!item) { console.error(`ERROR: ไม่พบ ${args.id}`); process.exit(2); }
  item.status = args.status === 'dropped' ? 'dropped' : 'done';
  item.history.push({ date: todayStr(), action: item.status, by: args.by || 'Hermes', detail: args.note || '' });
  saveLedger(file, data, args['dry-run']);
  if (!args['dry-run']) writeActionsData(file, data);
  console.log(`${args['dry-run'] ? '[dry-run] ' : ''}ปิด ${args.id} -> ${item.status}`);
}

function cmdNote(args, file) {
  if (!args.id || !args.note) { console.error('ERROR: note ต้องมี --id --note'); process.exit(2); }
  const data = loadLedger(file);
  const item = data.items.find(i => i.id === args.id);
  if (!item) { console.error(`ERROR: ไม่พบ ${args.id}`); process.exit(2); }
  item.history.push({ date: todayStr(), action: 'note', by: args.by || 'Hermes', detail: args.note });
  saveLedger(file, data, args['dry-run']);
  if (!args['dry-run']) writeActionsData(file, data);
  console.log(`${args['dry-run'] ? '[dry-run] ' : ''}เพิ่ม note ให้ ${args.id}`);
}

function cmdCheck(args, file) {
  let data;
  try {
    data = loadLedger(file);
  } catch (e) {
    console.error('SCHEMA INVALID:', e.message);
    process.exit(1);
  }
  writeActionsData(file, data); // keep dashboard/actionsData.js in sync even on read-only check
  const today = todayStr();
  const open = data.items.filter(i => i.status === 'open');
  const rows = open.map(i => {
    const due = effectiveDue(i, data.sla_days);
    const overdueDays = daysBetween(due, today);
    return { ...i, due, overdueDays };
  });
  const overdue = rows.filter(r => r.overdueDays > 0).sort((a, b) => b.overdueDays - a.overdueDays);
  const dueToday = rows.filter(r => r.overdueDays === 0);
  const cioItems = rows.filter(r => r.owner === 'CIO');
  if (args.owner) {
    const filtered = rows.filter(r => r.owner === args.owner);
    if (args.json) { console.log(JSON.stringify(filtered, null, 2)); return; }
    console.log(`=== Owner: ${args.owner} (${filtered.length} เรื่อง) ===`);
    filtered.forEach(r => console.log(`  ${r.id} [L${r.escalation_level}] ${r.title} — due ${r.due}${r.overdueDays > 0 ? ` (เลยกำหนด ${r.overdueDays} วัน)` : ''}`));
    return;
  }
  if (args.json) {
    console.log(JSON.stringify({ overdue, dueToday, cioItems, totalOpen: open.length }, null, 2));
    return;
  }
  console.log(`=== Action Ledger check (${today}) — เปิดอยู่ ${open.length} เรื่อง ===`);
  console.log(`\n--- เลยกำหนด (${overdue.length}) ---`);
  overdue.forEach(r => console.log(`  ${r.id} [L${r.escalation_level}] owner=${r.owner} "${r.title}" — เลย ${r.overdueDays} วัน (due ${r.due})`));
  console.log(`\n--- ครบกำหนดวันนี้ (${dueToday.length}) ---`);
  dueToday.forEach(r => console.log(`  ${r.id} owner=${r.owner} "${r.title}"`));
  console.log(`\n--- ของ CIO (${cioItems.length}) ---`);
  cioItems.forEach(r => console.log(`  ${r.id} [L${r.escalation_level}] "${r.title}" — due ${r.due}`));
}

function cmdEscalate(args, file) {
  const data = loadLedger(file);
  const today = todayStr();
  let changed = 0;
  const log = [];
  for (const item of data.items) {
    if (item.status !== 'open') continue;
    const due = effectiveDue(item, data.sla_days);
    const overdueDays = daysBetween(due, today);
    let newLevel = item.escalation_level;
    if (overdueDays > 2 && item.escalation_level < 2) newLevel = 2;
    else if (overdueDays > 0 && item.escalation_level < 1) newLevel = 1;
    if (newLevel !== item.escalation_level) {
      log.push(`${item.id}: level ${item.escalation_level} -> ${newLevel} (เลยกำหนด ${overdueDays} วัน)`);
      item.escalation_level = newLevel;
      item.history.push({ date: today, action: 'escalated', by: 'escalate-cli', detail: `level -> ${newLevel}, overdue ${overdueDays}d` });
      changed++;
    }
  }
  if (changed === 0) {
    console.log('ไม่มี item ที่ต้อง escalate');
    return;
  }
  log.forEach(l => console.log((args['dry-run'] ? '[dry-run] ' : '') + l));
  saveLedger(file, data, args['dry-run']);
  if (!args['dry-run']) writeActionsData(file, data);
  console.log(`${args['dry-run'] ? '[dry-run] จะ' : ''}เลื่อนระดับ ${changed} เรื่อง`);
}

function main() {
  const argv = process.argv.slice(2);
  const cmd = argv[0];
  const args = parseArgs(argv.slice(1));
  const file = args.file || path.join(__dirname, '..', 'portfolio', 'actions.json');
  switch (cmd) {
    case 'add': return cmdAdd(args, file);
    case 'close': return cmdClose(args, file);
    case 'note': return cmdNote(args, file);
    case 'check': return cmdCheck(args, file);
    case 'escalate': return cmdEscalate(args, file);
    default:
      console.error('Usage: node scripts/actions.js <add|close|note|check|escalate> [options]');
      process.exit(2);
  }
}

main();
