# -*- coding: utf-8 -*-
"""
dashboard/_patch_chym.py
Insert CHYM (Chime Financial, Inc.) analysis entry into dashboard/data.js
REPORTS array + update LAST_UPDATED.

Dashboard Write Safety: targeted script, never full-file Write on data.js
(precedent: _patch_meli.py, _patch_adi.py, _patch_tls.py).

Run:
    cd "C:\\Users\\user\\Desktop\\\u0e1a\u0e25\u0e08\\\u0e1a\u0e25\u0e08 CFA"
    python dashboard/_patch_chym.py
"""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DATA_JS_PATH = "dashboard/data.js"
REPORT_MD_PATH = "reports/CHYM_2026-08-31.md"
NEW_LAST_UPDATED = "2026-08-31"


def build_entry():
    with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
        report_md = f.read()
    escaped = report_md.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

    metadata = r'''  {
    ticker: "CHYM",
    company: "Chime Financial, Inc.",
    date: "2026-08-31",
    version: "v1 (Morgan QA CONDITIONAL PASS \u2014 Data Quality 8/10)",
    sector: "US Consumer Fintech / Neobank (interchange-fee-based digital banking for underbanked / paycheck-to-paycheck)",
    bucket: "GROWTH",
    price: 33.20,
    recommendation: "AVOID / HOLD-WAIT \u2014 NO DEPLOY",
    blendedFV: 22.30,
    esgAdjFV: 21.07,
    mos: "-32.8%",
    mosPct: -32.8,
    mosPctEsgAdj: -36.5,
    conviction: 4.83,
    convictionEmma: 4.0,
    convictionQuinn: 4.5,
    convictionBear: 6.0,
    convictionAvg: 4.83,
    targetBull: 38,
    targetBase: 22,
    stopLoss: 15.60,
    pwEV: 24.47,
    pwEvBear: 19.85,
    beta: 1.70,
    sharpe1Y: 0.15,
    forwardSharpe: 0.15,
    maxDrawdown: "-64.7% (since IPO; -53.5% ex IPO-day spike)",
    kelly: "Negative \u0e17\u0e38\u0e01 fraction (Full / Half / Quarter) \u2192 allocation 0%. E[3yr return] \u221226.3% (Quinn) = negative edge. Kelly \u0e1e\u0e25\u0e34\u0e01\u0e1a\u0e27\u0e01\u0e17\u0e35\u0e48\u0e23\u0e32\u0e04\u0e32 ~$24\u201325 \u0e2b\u0e23\u0e37\u0e2d\u0e15\u0e48\u0e33\u0e01\u0e27\u0e48\u0e32",
    moat: "NARROW (weak) \u2014 Emma NARROW ~7\u201310 \u0e1b\u0e35 / Bear NONE (\u0e22\u0e2d\u0e21 'weak Narrow') \u2192 reconciled NARROW-weak, durability ~5\u20137 \u0e1b\u0e35. \u0e41\u0e2b\u0e25\u0e48\u0e07\u0e2b\u0e25\u0e31\u0e01 = cost advantage (branchless serve underbanked) + brand \u2014 \u0e41\u0e15\u0e48 no pricing power \u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c\u0e41\u0e25\u0e49\u0e27 (ARPAM +6% \u0e02\u0e13\u0e30 revenue +27%), \u0e44\u0e21\u0e48\u0e21\u0e35 bank charter (ARPU ~1/3 SoFi), 64\u201370% \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e1a\u0e19 Durbin regulatory arbitrage \u0e17\u0e35\u0e48\u0e21\u0e35 pending adverse court case",
    esgRating: "Medium-High",
    esgScore: 5.0,
    macroRegime: "RISK-ON",
    morganQA: "CONDITIONAL PASS (Data Quality 8/10, 0 HIGH / 3 MEDIUM / 3 LOW, reject type SANITY_FAIL + soft RULE_VIOLATION). Price gate PASS ($33.20 Stockanalysis + $33.77 Yahoo + Morgan independent $33.36, \u0394 < 5%). Financial spot-check 5/5 PASS. Market cap sanity 378.6M \u00d7 $33.20 = $12,570M \u2713. Blended FV 40/30/30 canonical verified \u2014 report \u0e40\u0e1b\u0e34\u0e14\u0e42\u0e1b\u0e07 fabricated 'IPS 2026-05-15 \u2192 40/35/25' \u0e43\u0e19 Charlie base-prompt (Error #8/#9 prevention instance \u0e15\u0e48\u0e2d\u0e40\u0e19\u0e37\u0e48\u0e2d\u0e07). DCF Cash Flow Consistency Rule: SBC 11.5% > 10% \u2192 \u0e22\u0e34\u0e07; \u0e17\u0e31\u0e49\u0e07 3 NOPAT-based FCFF; Emma DCF base $21 vs Quinn base $26 gap +23.8% < 25% \u2192 reconciliation table \u0e44\u0e21\u0e48\u0e1a\u0e31\u0e07\u0e04\u0e31\u0e1a. 3 MEDIUM \u0e41\u0e01\u0e49\u0e01\u0e48\u0e2d\u0e19 Leo embed: (1) Emma esgBreakdown block raw (e8/s5/g4/5.5) \u2192 embed reconciled {e:8,s:4.5,g:3.5,overall:5.0}; (2) ESG table Bear column \u2192 Bear notes \u00a77 (E8/S4/G3); (3) Stop Loss $15.50 \u221220.5% \u2192 $15.60 \u221220.0% \u0e40\u0e1b\u0e4a\u0e30. \u0e44\u0e21\u0e48\u0e21\u0e35\u0e02\u0e49\u0e2d\u0e44\u0e2b\u0e19\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19 verdict.",
    sp500Reference: 7711.76,
    sp500ReferenceNote: "7,711.76 (2026-08-28 close \u2014 reuse agent_notes/atlas/2026-08-31_CHYM.md \u00a7A; \u0e44\u0e21\u0e48\u0e21\u0e35 trading session \u0e43\u0e2b\u0e21\u0e48\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07 2026-08-28 \u2192 2026-08-31)",
    revenueGrowthYoY: 26.4,
    entryZone: "$18\u201321 (mid $19.50) \u2014 \u0e15\u0e49\u0e2d\u0e07\u0e44\u0e14\u0e49 MOS \u2265 15% vs Blended FV $22.30 AND Bull Flip Trigger \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19 (Reg II resolution / GAAP-margin proof 2Q / member re-accel). \u0e08\u0e32\u0e01 entry mid $19.50 \u2192 Blended FV $22.30 = CAGR +4.6%/\u0e1b\u0e35 (modest \u2014 \u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35 bull-flip \u0e40\u0e2a\u0e23\u0e34\u0e21)",
    positionSize: "0% \u2014 FAIL Growth conviction gate (avg 4.83 < 6.5) + FAIL Growth MOS Gate 0/2 (Reverse DCF 1.24\u20131.42\u00d7 consensus > 1.2\u00d7; EV/Rev + Fwd P/E ~90th pctile > 70th). Value cross-check \u0e01\u0e47 FAIL \u0e17\u0e31\u0e49\u0e07 2 \u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19 (MOS \u221232.8% << 15%; Conviction < 7.0). Regime RISK-ON 3/4 (Fed-hawkish overlay), 1.0x, Force Deploy active \u0e41\u0e15\u0e48\u0e44\u0e21\u0e48\u0e21\u0e35 candidate \u0e1c\u0e48\u0e32\u0e19 gate \u2192 \u0e44\u0e21\u0e48 force",
    keyThesis: "CHYM = neobank consumer-facing \u0e23\u0e32\u0e22\u0e43\u0e2b\u0e0d\u0e48\u0e2a\u0e38\u0e14\u0e02\u0e2d\u0e07\u0e2a\u0e2b\u0e23\u0e31\u0e10\u0e2f \u0e17\u0e35\u0e48\u0e1e\u0e36\u0e48\u0e07 interchange fees (~64\u201370% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49) \u0e1c\u0e48\u0e32\u0e19 partner banks (Bancorp + Stride) \u0e1a\u0e19 Durbin exemption. Q2'26 = GAAP-profitable quarter \u0e41\u0e23\u0e01, FCF TTM +$312M, net cash +$980M, member +20% \u2014 \u0e18\u0e38\u0e23\u0e01\u0e34\u0e08\u0e08\u0e23\u0e34\u0e07. \u0e41\u0e15\u0e48\u0e17\u0e35\u0e48 $33.20 \u0e40\u0e17\u0e23\u0e14 ~50x forward P/E \u0e1a\u0e19 fundamental \u0e17\u0e35\u0e48\u0e41\u0e22\u0e48\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21 peer (revenue growth +26.4% \u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14 + operating margin 15.2% \u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14 vs SOFI/DAVE/NU/HOOD). Growth MOS Gate FAIL 0/2 + Conviction 4.83 < 6.5 + MOS \u221232.8% + Kelly 0%. Street mean 12M PT ~$33 \u2248 spot = upside ~0% \u0e41\u0e21\u0e49\u0e08\u0e32\u0e01 Street. Interchange \u0e41\u0e02\u0e27\u0e19\u0e1a\u0e19 Reg II 8th Circuit litigation \u0e17\u0e35\u0e48\u0e1c\u0e25\u0e25\u0e31\u0e1e\u0e18\u0e4c\u0e2a\u0e2d\u0e07\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07. 6th consecutive 'priced-for-perfection' NO-DEPLOY (MU/CRCL/ADI/MELI/GCT\u2192CHYM). \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48 hard AVOID \u2014 net cash + FCF+ + NOL shield = downside floor \u0e08\u0e23\u0e34\u0e07. Watchlist \u2014 Bull Flip \u0e17\u0e35\u0e48 \u2264$24 + regulatory/margin proof",
    topRisk: "Interchange regulatory binary (\u0e2a\u0e2d\u0e07\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07) \u2014 ~64\u201370% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 = debit interchange \u0e1a\u0e19 Durbin exemption. Reg II \u0e16\u0e39\u0e01 ND District Court vacated \u0e17\u0e31\u0e49\u0e07\u0e09\u0e1a\u0e31\u0e1a (\u0e2a.\u0e04. 2025, stay), 8th Circuit fully briefed \u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48 \u0e21\u0e35.\u0e04. 2026, \u0e23\u0e2d\u0e04\u0e33\u0e1e\u0e34\u0e1e\u0e32\u0e01\u0e29\u0e32 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48. \u0e16\u0e49\u0e32 affirm vacatur \u2192 \u0e18\u0e19\u0e32\u0e04\u0e32\u0e23\u0e43\u0e2b\u0e0d\u0e48\u0e40\u0e01\u0e47\u0e1a interchange \u0e44\u0e21\u0e48\u0e16\u0e39\u0e01 cap \u2192 gap compression \u2192 CHYM \u0e40\u0e2a\u0e35\u0e22 relative advantage \u0e1a\u0e19\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e2a\u0e48\u0e27\u0e19\u0e43\u0e2b\u0e0d\u0e48. Bear P-W EV $19.85 (MOS \u221240%). Sensitivity: 6/25 cells (24%) justify $33.20 \u2014 \u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23 Revenue CAGR \u2265 20% AND terminal op margin \u2265 30% \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19 (best-in-cohort \u2014 CHYM \u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19 worst-in-cohort \u0e17\u0e31\u0e49\u0e07\u0e2a\u0e2d\u0e07\u0e21\u0e34\u0e15\u0e34)",
    reportFile: "../reports/CHYM_2026-08-31.md",
    businessSummary: {
      oneLiner: "\u0e18\u0e19\u0e32\u0e04\u0e32\u0e23\u0e14\u0e34\u0e08\u0e34\u0e17\u0e31\u0e25\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2a\u0e32\u0e02\u0e32 \u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e04\u0e19 underbanked / \u0e2b\u0e32\u0e40\u0e0a\u0e49\u0e32\u0e01\u0e34\u0e19\u0e04\u0e48\u0e33 \u2014 \u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e2b\u0e25\u0e31\u0e01\u0e21\u0e32\u0e08\u0e32\u0e01\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21 interchange \u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e23\u0e39\u0e14\u0e1a\u0e31\u0e15\u0e23 debit",
      analogy: "\u0e40\u0e2b\u0e21\u0e37\u0e2d\u0e19\u0e41\u0e2d\u0e1e\u0e18\u0e19\u0e32\u0e04\u0e32\u0e23\u0e17\u0e35\u0e48\u0e44\u0e21\u0e48\u0e21\u0e35\u0e2a\u0e32\u0e02\u0e32 \u0e44\u0e21\u0e48\u0e04\u0e34\u0e14\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21 overdraft \u2014 \u0e41\u0e15\u0e48\u0e40\u0e07\u0e34\u0e19\u0e17\u0e35\u0e48\u0e44\u0e14\u0e49\u0e21\u0e32\u0e08\u0e23\u0e34\u0e07\u0e04\u0e37\u0e2d\u0e2a\u0e48\u0e27\u0e19\u0e41\u0e1a\u0e48\u0e07\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21\u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e23\u0e39\u0e14\u0e1a\u0e31\u0e15\u0e23 (interchange ~1.5% \u0e02\u0e2d\u0e07\u0e22\u0e2d\u0e14) \u0e41\u0e1a\u0e48\u0e07\u0e01\u0e31\u0e1a partner bank",
      moneyFlow: [
        "Interchange (~64\u201370% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49) \u2014 \u0e17\u0e38\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07 member \u0e23\u0e39\u0e14\u0e1a\u0e31\u0e15\u0e23 debit \u0e23\u0e49\u0e32\u0e19\u0e04\u0e49\u0e32\u0e08\u0e48\u0e32\u0e22 interchange fee \u2192 Chime \u0e41\u0e1a\u0e48\u0e07\u0e01\u0e31\u0e1a partner bank (Bancorp/Stride); partner bank <$10B assets \u2192 Durbin exemption \u2192 \u0e44\u0e21\u0e48\u0e16\u0e39\u0e01 Reg II cap",
        "SpotMe (fee-free overdraft \u0e16\u0e36\u0e07 ~$200) \u2014 \u0e02\u0e2d 'tip' \u0e41\u0e1a\u0e1a\u0e2a\u0e21\u0e31\u0e04\u0e23\u0e43\u0e08 (headline/regulatory tail risk)",
        "MyPay (earned-wage access), Credit Builder (secured card), ChimePlus (premium subscription)",
        "Platform / lending revenue (Instant Loans unsecured, +48% YoY) \u2014 ARPAM expansion vector \u0e41\u0e15\u0e48\u0e40\u0e1e\u0e34\u0e48\u0e21 credit risk",
        "\u0e40\u0e07\u0e34\u0e19\u0e2a\u0e14\u0e40\u0e2b\u0e25\u0e37\u0e2d ($1.16B liquid) \u0e40\u0e01\u0e47\u0e1a T-bills \u2192 other income \u0e40\u0e25\u0e47\u0e01\u0e19\u0e49\u0e2d\u0e22; \u0e44\u0e21\u0e48\u0e08\u0e48\u0e32\u0e22\u0e1b\u0e31\u0e19\u0e1c\u0e25"
      ],
      whyDifferent: "largest US consumer neobank member base (10.4M primary-account) + brand \u0e17\u0e35\u0e48\u0e41\u0e02\u0e47\u0e07\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21 underbanked/Gen-Z + branchless cost advantage \u2014 \u0e41\u0e15\u0e48 interchange-only model \u0e21\u0e35 hard ARPU ceiling \u0e17\u0e35\u0e48 SoFi/NU (\u0e21\u0e35 charter) \u0e44\u0e21\u0e48\u0e21\u0e35",
      simpleRisk: "64\u201370% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49\u0e41\u0e02\u0e27\u0e19\u0e1a\u0e19\u0e0a\u0e48\u0e2d\u0e07\u0e01\u0e0e\u0e2b\u0e21\u0e32\u0e22 (Durbin exemption) \u0e17\u0e35\u0e48\u0e21\u0e35\u0e04\u0e14\u0e35\u0e28\u0e32\u0e25\u0e04\u0e49\u0e32\u0e07\u0e2d\u0e22\u0e39\u0e48 (Reg II 8th Circuit) \u2014 \u0e16\u0e49\u0e32\u0e28\u0e32\u0e25\u0e15\u0e31\u0e14\u0e2a\u0e34\u0e19\u0e25\u0e1a Reg II \u0e17\u0e31\u0e49\u0e07\u0e09\u0e1a\u0e31\u0e1a \u0e18\u0e19\u0e32\u0e04\u0e32\u0e23\u0e43\u0e2b\u0e0d\u0e48\u0e01\u0e47\u0e40\u0e01\u0e47\u0e1a interchange \u0e44\u0e21\u0e48\u0e16\u0e39\u0e01 cap \u0e40\u0e0a\u0e48\u0e19\u0e01\u0e31\u0e19 \u2192 Chime \u0e40\u0e2a\u0e35\u0e22\u0e04\u0e27\u0e32\u0e21\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a; + \u0e44\u0e21\u0e48\u0e21\u0e35 pricing power (ARPAM +6% \u0e02\u0e13\u0e30 revenue +27%) + SBC 11.5% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 \u0e17\u0e33\u0e43\u0e2b\u0e49 GAAP net loss \u2212$18.2M + credit-loss line \u0e42\u0e15\u0e40\u0e23\u0e47\u0e27\u0e01\u0e27\u0e48\u0e32\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49"
    },
    thesisBullets: [
      { title: "Worst-in-cohort fundamentals @ premium multiple", why: "revenue growth +26.4% (\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14) + operating margin 15.2% (\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14) vs SOFI (+40.9%/17.3%), DAVE (+48.6%/36.0%), NU (+44.3%/52.0%), HOOD (+38.3%/46.0%) \u2014 \u0e41\u0e15\u0e48\u0e40\u0e17\u0e23\u0e14 forward P/E ~50x (\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14, ~2x peer median). \u0e15\u0e25\u0e32\u0e14\u0e44\u0e21\u0e48\u0e44\u0e14\u0e49 apply discount \u0e17\u0e35\u0e48 fundamental \u0e2a\u0e21\u0e04\u0e27\u0e23\u0e44\u0e14\u0e49" },
      { title: "Interchange concentration + regulatory binary \u0e2a\u0e2d\u0e07\u0e17\u0e34\u0e28\u0e17\u0e32\u0e07", why: "~64\u201370% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 = debit interchange \u0e1a\u0e19 Durbin exemption. Reg II vacated \u0e17\u0e31\u0e49\u0e07\u0e09\u0e1a\u0e31\u0e1a (\u0e2a.\u0e04. 2025, stay), 8th Circuit \u0e23\u0e2d\u0e04\u0e33\u0e1e\u0e34\u0e1e\u0e32\u0e01\u0e29\u0e32. affirm \u2192 gap exempt/non-exempt \u0e41\u0e04\u0e1a\u0e25\u0e07 \u2192 CHYM \u0e40\u0e2a\u0e35\u0e22 relative advantage. 'deregulation \u0e14\u0e35\u0e15\u0e48\u0e2d fintech' \u0e40\u0e1b\u0e47\u0e19\u0e2a\u0e31\u0e0d\u0e0a\u0e32\u0e15\u0e0d\u0e32\u0e13\u0e1c\u0e34\u0e14\u0e43\u0e19\u0e01\u0e23\u0e13\u0e35\u0e19\u0e35\u0e49" },
      { title: "\u0e44\u0e21\u0e48\u0e21\u0e35 pricing power + \u0e44\u0e21\u0e48\u0e21\u0e35 bank charter", why: "ARPAM +6% \u0e02\u0e13\u0e30 revenue +27% = growth \u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e21\u0e32\u0e08\u0e32\u0e01 member adds \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48 monetization. \u0e44\u0e21\u0e48\u0e21\u0e35 charter (\u0e15\u0e48\u0e32\u0e07\u0e08\u0e32\u0e01 SOFI) \u2192 ARPU ~1/3 SoFi, \u0e1e\u0e36\u0e48\u0e07 partner bank 2 \u0e23\u0e32\u0e22 (Bancorp + Stride ~46% \u0e02\u0e2d\u0e07 receivables)" },
      { title: "SBC wedge + credit-loss line \u0e42\u0e15\u0e40\u0e23\u0e47\u0e27", why: "SBC TTM $283.6M = 11.5% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 \u2192 GAAP net loss \u2212$18.2M \u0e17\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48 op margin +15%. Q2'26 transaction & risk losses $103.3M (+16% QoQ vs revenue +4% QoQ); mix shift \u2192 Instant Loans unsecured \u0e0a\u0e48\u0e27\u0e07 near-prime credit normalize" },
      { title: "\u0e23\u0e32\u0e04\u0e32 near-ATH, Street mean PT \u2248 spot", why: "+25% \u0e08\u0e32\u0e01 IPO, \u22122.8% \u0e08\u0e32\u0e01 52W high \u2014 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48 pullback. Street consensus 12M PT mean ~$33.15 \u2248 spot = Street \u0e40\u0e2d\u0e07\u0e01\u0e47\u0e40\u0e2b\u0e47\u0e19 upside ~0%; 'Buy' upgrades $38\u201345 = IPO-syndicate outliers (MS/Goldman = underwriters)" }
    ],
    esgBreakdown: { e: 8, s: 4.5, g: 3.5, overall: 5.0 },
    esgBreakdownNote: "Reconciled \u0e08\u0e32\u0e01 report \u00a7ESG (Emma / Bear \u2192 Reconciled): Environmental 8 / 8 \u2192 8.0 (digital-only, carbon footprint \u0e15\u0e48\u0e33, immaterial). Social 5 / 4 \u2192 4.5 (financial-inclusion positive \u0e41\u0e15\u0e48 monetize vulnerable paycheck-to-paycheck demographic; SpotMe tip + MyPay EWA fee criticism; CFPB $3.25M penalty + \u2265$1.3M redress \u0e1e.\u0e04. 2024; predatory-lending optics \u0e1a\u0e19 Instant Loans). Governance 4 / 3 \u2192 3.5 (dual-class \u2014 co-founders Britt/King \u0e04\u0e38\u0e21 voting power ~65\u201374% \u0e14\u0e49\u0e27\u0e22 economic stake \u0e40\u0e25\u0e47\u0e01\u0e01\u0e27\u0e48\u0e32; SBC $1,082M FY2025 spike; adjusted-metrics reliance; partner-bank concentration governance). Overall 5.5 / 5.0 \u2192 5.0/10 (MEDIUM\u2013HIGH RISK). Total ESG valuation impact reconciled \u2248 \u22125.5% (Emma \u22125% / Bear \u22126%) \u2192 ESG-adj Blended FV $21.07 \u2192 MOS \u221236.5%. Emma structured-data block \u0e22\u0e31\u0e07 stale (e8/s5/g4/overall5.5) \u2014 Leo embed \u0e08\u0e32\u0e01 reconciled report \u0e15\u0e32\u0e21 Morgan Issue #1 (ESG structured-block staleness \u0e0b\u0e49\u0e33\u0e15\u0e48\u0e2d\u0e08\u0e32\u0e01 TLS/CRCL/ADI/MELI/GCT)",
    customerConcentration: {
      note: "Members: \u0e44\u0e21\u0e48\u0e21\u0e35 member \u0e40\u0e14\u0e35\u0e22\u0e27 >1% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 \u2014 fragmented (10.4M primary-account members). Partner-bank concentration: The Bancorp + Stride Bank \u2248 46% \u0e02\u0e2d\u0e07 receivables (10-Q; ~27% / 19%) \u2014 single point of failure \u0e15\u0e48\u0e2d business model (\u0e44\u0e21\u0e48\u0e21\u0e35 charter \u0e2a\u0e33\u0e23\u0e2d\u0e07). \u26a0\ufe0f flag > 20%. Card networks: Visa/Mastercard \u2014 interchange schedule dependency"
    },
    geographyRevenue: {
      unitedStates: "~100% \u2014 domestic-only neobank",
      international: "~0%",
      china: "~0% \u2014 \u0e44\u0e21\u0e48\u0e21\u0e35 exposure. Geopolitical Risk LOW (domestic) \u2014 \u0e41\u0e15\u0e48 Regulatory Risk HIGH: 100% \u0e02\u0e2d\u0e07 business \u0e41\u0e02\u0e27\u0e19\u0e1a\u0e19 US interchange/consumer-finance regulation (Durbin exemption, Reg II, CFPB, EWA classification)"
    },
    revenueSegments: [
      { label: "Payments (debit interchange + MyPay / out-of-network ATM fees)", value: 64 },
      { label: "Platform / lending (Instant Loans, ChimePlus, other)", value: 36 }
    ],
    revenueSegmentsNote: "Q2'26 10-Q: Payments revenue $430.0M (64%) / Platform-related $239.7M (36%) / total $669.8M. Interchange \u0e08\u0e23\u0e34\u0e07 ~60\u201365% \u0e02\u0e2d\u0e07 total (payments revenue \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e40\u0e1b\u0e47\u0e19 interchange 100% \u2014 \u0e21\u0e35 MyPay fee, out-of-network ATM). Bear Data Integrity #2: Atlas '70% interchange' overstate \u0e40\u0e25\u0e47\u0e01\u0e19\u0e49\u0e2d\u0e22",
    competitorData: [
      { ticker: "CHYM", company: "Chime Financial (subject)", revenueGrowth: 26.4, operatingMargin: 15.2, marketCap: 12570 },
      { ticker: "SOFI", company: "SoFi Technologies", revenueGrowth: 40.9, operatingMargin: 17.3, marketCap: 23310, strengths: "\u0e21\u0e35 bank charter \u2192 ARPU ~3x CHYM, NIM capture, lending + investing + wealth cross-sell; growth +40.9% \u0e40\u0e23\u0e47\u0e27\u0e01\u0e27\u0e48\u0e32 CHYM; \u0e40\u0e1b\u0e47\u0e19 proof point \u0e27\u0e48\u0e32 charter model \u0e0a\u0e19\u0e30 interchange-only", weaknesses: "op margin 17.3% \u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e2a\u0e39\u0e07; beta ~2.17; rate-sensitive; \u0e41\u0e02\u0e48\u0e07\u0e15\u0e23\u0e07\u0e01\u0e31\u0e1a CHYM \u0e43\u0e19 underbanked segment", threatLevel: "HIGH" },
      { ticker: "DAVE", company: "Dave Inc.", revenueGrowth: 48.6, operatingMargin: 36.0, marketCap: 4260, strengths: "growth +48.6% \u0e40\u0e23\u0e47\u0e27\u0e2a\u0e38\u0e14\u0e43\u0e19\u0e01\u0e25\u0e38\u0e48\u0e21, op margin 36% \u0e2a\u0e39\u0e07\u0e01\u0e27\u0e48\u0e32 CHYM 2x; ExtraCash + fee model \u0e17\u0e35\u0e48\u0e21\u0e35 pricing power \u0e21\u0e32\u0e01\u0e01\u0e27\u0e48\u0e32; Fwd P/E ~15x \u0e16\u0e39\u0e01\u0e01\u0e27\u0e48\u0e32 CHYM 3x", weaknesses: "scale \u0e40\u0e25\u0e47\u0e01\u0e01\u0e27\u0e48\u0e32\u0e21\u0e32\u0e01 ($4.3B market cap); micro-float; ExtraCash tip model \u0e21\u0e35 regulatory tail \u0e40\u0e0a\u0e48\u0e19\u0e01\u0e31\u0e19", threatLevel: "MEDIUM" },
      { ticker: "NU", company: "Nu Holdings", revenueGrowth: 44.3, operatingMargin: 52.0, marketCap: 65500, strengths: "op margin 52% (best-in-cohort), bank charter, monopoly-ish Brazil position, 100M+ \u0e25\u0e39\u0e01\u0e04\u0e49\u0e32, credit underwriting \u0e0a\u0e31\u0e49\u0e19\u0e40\u0e22\u0e35\u0e48\u0e22\u0e21; proof \u0e27\u0e48\u0e32 neobank operating leverage \u0e40\u0e1b\u0e47\u0e19 non-linear (op margin ~0% 2021 \u2192 52% 2024)", weaknesses: "LatAm/EM concentration; \u0e44\u0e21\u0e48\u0e21\u0e35 e-commerce/logistics; credit-cycle exposure; \u0e44\u0e21\u0e48\u0e44\u0e14\u0e49\u0e41\u0e02\u0e48\u0e07\u0e43\u0e19 US", threatLevel: "LOW" },
      { ticker: "HOOD", company: "Robinhood Markets", revenueGrowth: 38.3, operatingMargin: 46.0, marketCap: 75300, strengths: "op margin 46%, growth +38.3%, crypto + options + Gold subscription monetization \u0e2b\u0e25\u0e32\u0e01\u0e2b\u0e25\u0e32\u0e22; brand \u0e41\u0e02\u0e47\u0e07\u0e43\u0e19 retail; net cash \u0e21\u0e32\u0e01", weaknesses: "revenue \u0e1c\u0e39\u0e01\u0e01\u0e31\u0e1a trading volume / crypto cycle; Fwd P/E ~40x+ \u0e01\u0e47\u0e41\u0e1e\u0e07; \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48 pure neobank (brokerage-first)", threatLevel: "MEDIUM" }
    ],
    bullFlipTriggers: [
      "\u0e23\u0e32\u0e04\u0e32 \u2264 $24 \u2014 MOS \u0e1a\u0e27\u0e01 vs Blended FV + Kelly \u0e01\u0e25\u0e31\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e1a\u0e27\u0e01",
      "GAAP profitability \u0e1e\u0e34\u0e2a\u0e39\u0e08\u0e19\u0e4c: 2 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e15\u0e34\u0e14\u0e01\u0e31\u0e19 GAAP operating margin > 12% AND GAAP net income \u0e1a\u0e27\u0e01 (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48\u0e41\u0e04\u0e48 adjusted)",
      "Platform revenue > 35% YoY 2 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e15\u0e34\u0e14 AND Instant Loans charge-off < 4% \u0e1c\u0e48\u0e32\u0e19\u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e17\u0e35\u0e48 unemployment \u0e02\u0e36\u0e49\u0e19",
      "Fed 2023 debit-cap proposal (\u221230%) finalized \u2192 gap exempt/non-exempt \u0e01\u0e27\u0e49\u0e32\u0e07\u0e02\u0e36\u0e49\u0e19 \u2192 interchange tailwind",
      "ARPAM growth re-accelerate > 12% YoY \u2014 proof \u0e27\u0e48\u0e32\u0e21\u0e35 monetization lever (\u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48 member-adds only)"
    ],
    bearFlipTriggers: [
      "8th Circuit affirms ND vacatur \u0e02\u0e2d\u0e07 Reg II \u2192 interchange take-rate compression \u221215% \u2192 FV ~$13\u201315",
      "Transaction & risk losses > 18% \u0e02\u0e2d\u0e07 revenue 2 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a\u0e15\u0e34\u0e14 (\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19 ~15%)",
      "Bancorp \u0e2b\u0e23\u0e37\u0e2d Stride \u0e44\u0e14\u0e49 BaaS consent order / exit / renegotiate adverse",
      "Active member growth < 12% YoY \u0e2b\u0e23\u0e37\u0e2d management \u0e2b\u0e31\u0e48\u0e19 guidance",
      "Purchase volume growth < 10% YoY \u0e2b\u0e23\u0e37\u0e2d guide take-rate \u0e25\u0e07\u0e2d\u0e35\u0e01"
    ],
    thesisInvalidation: "Bear \u0e1c\u0e34\u0e14\u0e16\u0e49\u0e32 \u0e20\u0e32\u0e22\u0e43\u0e19 4 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a: GAAP op margin > 20% AND revenue growth > 22% AND Platform > 45% \u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e44\u0e14\u0e49 (charge-offs contained) \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e01\u0e31\u0e19 \u2192 CHYM \u0e40\u0e1b\u0e47\u0e19 top-quartile \u0e17\u0e31\u0e49\u0e07 growth+margin \u2192 ~50x justified \u2192 FV > $35. Holder \u0e1c\u0e34\u0e14\u0e16\u0e49\u0e32: Durbin exemption \u0e16\u0e39\u0e01 legislate \u0e22\u0e01\u0e40\u0e25\u0e34\u0e01 / \u0e02\u0e22\u0e32\u0e22 cap \u0e2a\u0e39\u0e48 partner banks / partner-bank disruption / direct-deposit member count YoY \u0e15\u0e34\u0e14\u0e25\u0e1a 2 \u0e44\u0e15\u0e23\u0e21\u0e32\u0e2a. Data invalidation: credit-loss reserves \u0e44\u0e21\u0e48\u0e1e\u0e2d (allowance ~$70M vs receivables ~$115M = ~61% coverage) \u2192 restatement / surprise provisioning",
    unitEconomics: {
      ruleOf40: "~39% (Rev growth +26.4% + FCF margin 12.7%) \u2014 Borderline Fail (43% \u0e16\u0e49\u0e32\u0e43\u0e0a\u0e49 adj EBITDA margin)",
      nrr: "N/A \u2014 \u0e44\u0e21\u0e48 disclose (implied cohort ~120%+)",
      ltvCac: "~9.0x (Emma est., S-1/shareholder letter)",
      cacPayback: "15\u201318 \u0e40\u0e14\u0e37\u0e2d\u0e19",
      sbcPctRevenue: "11.5% (SBC TTM $283.6M) \u2014 HIGH, DCF Cash Flow Consistency Rule \u0e22\u0e34\u0e07; net dilution ~1.5%/yr post-IPO",
      note: "Active members 10.4M (+20% YoY); ARPAM $260 (+6% YoY) = ceiling \u0e15\u0e48\u0e33 ~1/3 charter peer; Gross Margin TTM 88.7%; Operating Margin GAAP 15.2% (worst-in-cohort vs peer median ~35%); Net Income TTM \u2212$18.2M (SBC wedge). \u0e04\u0e27\u0e32\u0e21\u0e40\u0e2a\u0e35\u0e48\u0e22\u0e07 = structural economics + regulatory binary + credit cycle \u2014 \u0e44\u0e21\u0e48\u0e43\u0e0a\u0e48 accounting fraud"
    },
    fvVerifiedDate: "2026-08-31",
    priceUpdated: "2026-08-31",
'''

    full_content_field = "    fullContent: `" + escaped + "`,\n"
    closing = "  },\n"
    return metadata + "\n" + full_content_field + closing


def main():
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if 'ticker: "CHYM"' in content:
        print("CHYM entry already exists in data.js \u2014 aborting to avoid duplicate.")
        sys.exit(1)

    entry = build_entry()

    content, n = re.subn(r'const LAST_UPDATED = "[\d-]+";',
                         f'const LAST_UPDATED = "{NEW_LAST_UPDATED}";', content, count=1)
    if n != 1:
        print("WARNING: LAST_UPDATED not replaced.")

    marker = "const REPORTS = ["
    idx = content.find(marker)
    if idx == -1:
        print("ERROR: REPORTS marker not found. Aborting.")
        sys.exit(1)
    insert_at = idx + len(marker) + 1
    new_content = content[:insert_at] + "\n" + entry + content[insert_at:]

    ob, cb = new_content.count("{"), new_content.count("}")
    obr, cbr = new_content.count("["), new_content.count("]")
    if ob != cb:
        print(f"ERROR: brace mismatch {ob} vs {cb} \u2014 aborting."); sys.exit(1)
    if obr != cbr:
        print(f"ERROR: bracket mismatch {obr} vs {cbr} \u2014 aborting."); sys.exit(1)
    if re.search(r'\[\s*,', new_content) or re.search(r',\s*,', new_content):
        print("ERROR: lone/double comma detected \u2014 aborting."); sys.exit(1)

    with open(DATA_JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("CHYM entry inserted. LAST_UPDATED =", NEW_LAST_UPDATED)


if __name__ == "__main__":
    main()
