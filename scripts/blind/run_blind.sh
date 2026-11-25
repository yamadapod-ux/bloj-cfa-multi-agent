#!/usr/bin/env bash
# VS2 1.7 blind re-derivation — รัน claude -p แยก process นอก repo (ไม่เห็น CLAUDE.md / memory / tool ใดๆ)
# usage: bash scripts/blind/run_blind.sh <prompt_file> <out_file> [model]
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PROMPT="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
OUT="$(cd "$(dirname "$2")" && pwd -W)/$(basename "$2")"
MODEL="${3:-}"
WORK="$(mktemp -d)"
case "$WORK" in "$REPO"*) echo "ABORT: work dir อยู่ใน repo" >&2; exit 1;; esac
WORK_NATIVE="$(cd "$WORK" && pwd -W)"
cp "$PROMPT" "$WORK/prompt.md"
cp "$REPO/scripts/blind/emma_blind_system.md" "$WORK/system.md"
SHA="$(sha256sum "$PROMPT" | cut -d' ' -f1)"
( cd "$WORK" && claude -p --tools "" --strict-mcp-config \
    --system-prompt-file system.md ${MODEL:+--model "$MODEL"} \
    --output-format json < prompt.md > result.json )
# Windows/MSYS temp mount can lag a beat before the write is visible to the next process — wait for it.
for i in $(seq 1 60); do [ -s "$WORK/result.json" ] && break; sleep 1; done
if [ ! -s "$WORK/result.json" ]; then echo "ABORT: result.json ไม่ปรากฏหลังรอ 60s ($WORK)" >&2; ls -la "$WORK" >&2; exit 1; fi
# python here is native Windows python.exe — it cannot resolve /tmp/... MSYS paths, needs C:/... form
python -I - "$WORK_NATIVE/result.json" "$OUT" "$SHA" "$WORK_NATIVE" "${MODEL:-default}" "$REPO" <<'PY'
import json, sys, datetime, csv, os
res, out, sha, work, model, repo = sys.argv[1:7]
d = json.load(open(res, encoding="utf-8"))
hdr = (f"<!-- blind-run: date={datetime.date.today()} prompt_sha256={sha} "
       f"cwd={work} model={model} tools=none num_turns={d.get('num_turns')} "
       f"is_error={d.get('is_error')} -->\n\n")
open(out, "w", encoding="utf-8").write(hdr + d.get("result", ""))
# T0: log token usage (CLAUDE.md T0 convention) -- best-effort, never fails the run
try:
    usage = d.get("usage", {}) or {}
    log_path = os.path.join(repo, "performance", "token_log.csv")
    is_new = not os.path.exists(log_path)
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["date", "task", "agent", "model", "input_tokens", "output_tokens", "cost_usd"])
        w.writerow([
            datetime.date.today().isoformat(), "blind_rederivation", "emma_blind", model,
            usage.get("input_tokens", ""), usage.get("output_tokens", ""),
            d.get("total_cost_usd", ""),
        ])
except Exception as e:
    print(f"token_log warning: {e}", file=sys.stderr)
PY
echo "saved: $OUT (prompt sha256 $SHA)"
