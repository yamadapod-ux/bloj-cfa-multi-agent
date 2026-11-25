// =================================================================
// dashboard/planProgress.js — Improvement Plan Progress (WP-DB1)
// สถานะ WP/Checkpoint ของ "แผนปรับปรุงระบบ" (คุยกับ hermes - แผนปรับปรุง.md)
// Hand-maintained static list — อัปเดต status ตอนที่ทำแต่ละ WP เสร็จ (ดู improvement_log.md
// เป็น source of truth ที่แท้จริง, ไฟล์นี้คือ snapshot ไว้โชว์บน Overview เท่านั้น)
// status: 'done' | 'in_progress' | 'pending'
// =================================================================

const PLAN_PROGRESS_LAST_UPDATED = "2026-11-26";

const PLAN_PROGRESS = [
  { id: "WP-D1",     label: "D1 decision (ข) ลงกฎ",                         status: "done",        note: "เสร็จ 2026-11-24" },
  { id: "WP-D1-fix",  label: "แก้ไฟล์ตามที่ Opus ตรวจเจอ",                    status: "done",        note: "เสร็จ 2026-11-24" },
  { id: "WP1",        label: "Action Ledger + CLI",                          status: "done",        note: "เสร็จ 2026-11-24" },
  { id: "WP2",        label: "ใส่งานค้างจริงลง ledger",                      status: "done",        note: "เสร็จ 2026-11-24" },
  { id: "งานด่วน",    label: "งานด่วนจากไฟล์แผน (CIO 2026-11-24)",           status: "done",        note: "เสร็จ 2026-11-25" },
  { id: "WP-DB1",     label: "หน้าแรกแบบศูนย์สั่งการ (Dashboard Overview)",   status: "in_progress", note: "กำลังทำอยู่ตอนนี้" },
  { id: "WP-E",       label: "E-series (scorecard ฯลฯ)",                     status: "pending" },
  { id: "WP3",        label: "ต่อ ledger เข้ากับ cron เดิม + ตั้ง cron Vera", status: "pending" },
  { id: "WP-T1",       label: "WP-T1",                                      status: "pending" },
  { id: "WP-T2",       label: "WP-T2",                                      status: "pending" },
  { id: "WP4",        label: "Digest ของ CIO + Open Decision มีวันตัดสิน",   status: "pending" },
  { id: "WP-DB2",     label: "WP-DB2 (dashboard เพิ่มเติม)",                 status: "pending" },
  { id: "WP5",        label: "validate.js กันข้อมูลค้าง",                   status: "pending" },
  { id: "WP6",        label: "LAST_UPDATED คำนวณเอง",                       status: "pending" },
  { id: "WP7",        label: "Pipeline แบบมี checkpoint กันชน usage limit", status: "pending" },
  { id: "WP-T3",       label: "WP-T3",                                      status: "pending" },
  { id: "WP8",        label: "วัดต้นทุนของการไม่ลงมือ",                     status: "pending" },
  { id: "WP9",        label: "WP9",                                         status: "pending" },
  { id: "Checkpoint A", label: "Checkpoint A",                              status: "pending" },
  { id: "Checkpoint B", label: "Checkpoint B",                              status: "pending" },
  { id: "Checkpoint D", label: "Checkpoint D",                              status: "pending" },
  { id: "Checkpoint E", label: "Checkpoint E",                              status: "pending" },
  { id: "Checkpoint C", label: "Checkpoint C",                              status: "pending" },
];
