#!/usr/bin/env node
// scripts/plan_smoke.js — pre-commit smoke test for every WP in the improvement plan
// รัน node --check กับทุกไฟล์ dashboard/*.js และ scripts/*.js + inline <script> ใน index.html
// + node scripts/actions.js check + node scripts/validate.js (ถ้ามีไฟล์แล้ว)
// Exit code != 0 ถ้ามีอันไหนไม่ผ่าน — ห้าม commit WP ใดถ้า exit code นี้ไม่ใช่ 0

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const ROOT = path.join(__dirname, '..');
let failures = [];

function run(label, fn) {
  try {
    fn();
    console.log(`OK   ${label}`);
  } catch (e) {
    console.log(`FAIL ${label}`);
    console.log('     ' + String(e.message || e).split('\n')[0]);
    failures.push(label);
  }
}

function checkNode(file) {
  execFileSync(process.execPath, ['--check', file], { stdio: 'pipe' });
}

function listFiles(dir, ext) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter(f => f.endsWith(ext)).map(f => path.join(dir, f));
}

// 1. dashboard/*.js
for (const f of listFiles(path.join(ROOT, 'dashboard'), '.js')) {
  run(`node --check ${path.relative(ROOT, f)}`, () => checkNode(f));
}

// 2. scripts/*.js (except this file itself, to avoid recursion weirdness in output)
for (const f of listFiles(path.join(ROOT, 'scripts'), '.js')) {
  run(`node --check ${path.relative(ROOT, f)}`, () => checkNode(f));
}

// 3. inline <script> blocks in dashboard/index.html
run('inline <script> syntax in dashboard/index.html', () => {
  const htmlPath = path.join(ROOT, 'dashboard', 'index.html');
  if (!fs.existsSync(htmlPath)) throw new Error('dashboard/index.html not found');
  const html = fs.readFileSync(htmlPath, 'utf8');
  const scriptRe = /<script(?:\s+[^>]*)?>([\s\S]*?)<\/script>/gi;
  let m;
  let count = 0;
  const tmp = path.join(require('os').tmpdir(), `plan_smoke_inline_${Date.now()}.js`);
  while ((m = scriptRe.exec(html))) {
    const srcAttr = /src\s*=/.test(m[0].split('>')[0]);
    if (srcAttr) continue; // external script tag, nothing inline to check
    const body = m[1].trim();
    if (!body) continue;
    count++;
    fs.writeFileSync(tmp, body, 'utf8');
    try {
      checkNode(tmp);
    } finally {
      // leave cleanup to the end
    }
  }
  if (fs.existsSync(tmp)) fs.unlinkSync(tmp);
  if (count === 0) throw new Error('no inline <script> blocks found (unexpected)');
});

// 4. node scripts/actions.js check
run('node scripts/actions.js check (schema valid)', () => {
  execFileSync(process.execPath, [path.join(ROOT, 'scripts', 'actions.js'), 'check'], { stdio: 'pipe', cwd: ROOT });
});

// 5. node scripts/validate.js (WP5) — only if it exists yet
const validatePath = path.join(ROOT, 'scripts', 'validate.js');
if (fs.existsSync(validatePath)) {
  run('node scripts/validate.js', () => {
    execFileSync(process.execPath, [validatePath], { stdio: 'pipe', cwd: ROOT });
  });
} else {
  console.log('SKIP node scripts/validate.js (ยังไม่มีไฟล์นี้ — มาจาก WP5)');
}

console.log('');
if (failures.length > 0) {
  console.log(`plan_smoke: FAIL (${failures.length} เรื่อง) — ห้าม commit จนกว่าจะแก้`);
  process.exit(1);
} else {
  console.log('plan_smoke: PASS ทั้งหมด');
  process.exit(0);
}
