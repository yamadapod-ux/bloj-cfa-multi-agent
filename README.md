# บลจ. CFA — Multi-Agent Investment Research System

A 9-agent orchestrated research & simulated portfolio management system built on Claude Code, applying a CFA-grounded framework to US equities (NYSE/NASDAQ) with a live dashboard tracking performance against the S&P 500.

**🔗 Live dashboard:** see repo settings for the current Pages URL

## What this is

Every stock analysis runs through a fixed pipeline of specialized agents, each with its own system prompt, responsibilities, and house rules — not a single model doing everything, but a small research desk:

| Agent | Role |
|-------|------|
| **Charlie** | Orchestrator — plans the pipeline, delegates, writes the final report |
| **Atlas** | Macro analyst — regime calls (RISK-ON / TRANSITIONAL-CAUTIOUS / RISK-OFF) + verified data package before anyone else touches a ticker |
| **Emma** | Equity analyst — DCF/DDM valuation, moat analysis, business fundamentals |
| **Quinn** | Quant analyst — statistical rigor, probability-weighted EV, sensitivity matrices |
| **Bear** | Devil's advocate — required to challenge every thesis; has an anti-convergence protocol that fires when the team agrees *too* easily |
| **Morgan** | QA — hard gate before anything gets published; verifies sourcing, math, and rule compliance (PASS / FAIL / CONDITIONAL) |
| **Leo** | Learning log — captures what worked, what didn't, and calibrates future behavior |
| **Vera** | Performance tracker — alpha vs S&P 500, analyst scorecards, conviction calibration |
| **Max** | Portfolio manager — owns the simulated $10K portfolio, sizing, stop losses, and trade execution |

## Why it's structured this way

- **Hard rule: no training-knowledge financial data.** Every price, revenue figure, and macro indicator must come from a live web search with a URL attached in the same session — a past incident where a stale training price was off by 300%+ made this non-negotiable.
- **Bucket-specific valuation gates.** Value names need DCF + margin-of-safety ≥ 15%; growth names need a reverse-DCF sanity check instead, since multiple compression is the bigger risk than an earnings miss.
- **Pre-commitment rules.** Return-side rules (position sizing, conviction gates, deployment logic) are locked and can't be changed on a bad quarter — only a confirmed *rolling 8-quarter* negative alpha trend triggers a process review. This exists specifically to prevent rationalizing rule changes after a string of losses.
- **Everything is logged.** Every recommendation, trade, regime call, and QA rejection is written to disk (`reports/`, `agent_notes/`, `session_logs/`, `portfolio/decisions.md`) — the point is an auditable trail, not just a chat transcript.

## Repo layout

```
dashboard/        Static dashboard (HTML/JS) — portfolio, reports, news feed
reports/          Full equity research reports per ticker
agent_notes/      Per-agent working notes for every session
portfolio/        Simulated $10K portfolio state, trade log, watchlist
performance/      Weekly/quarterly performance vs S&P 500
session_logs/     Full session logs + monthly lessons-learned
.claude/agents/   System prompts for each of the 9 agents
.claude/commands/ Slash-command workflows (news scan, portfolio update, etc.)
CLAUDE.md         The house rules every agent operates under
```

## Status

Simulated portfolio, paper trading only — not investment advice. Built as an exploration of multi-agent orchestration, rule-based guardrails, and auditability in an LLM-driven research workflow.
