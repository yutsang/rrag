---
title: "Integrated Business Solutions"
full_name: "EEMT5560 Integrated Business Solutions"
type: source
tags: [course, hkust, ahp, dea, scor-model, business-simulation, supply-chain, eemt5560, level-5]
created: "2026-04-10"
updated: "2026-04-14"
source: "raw/courses/EEMT5560 Integrated Business Solutions"
confidence: high
author: "Ronald S. Lau, Ph.D."
date_published: "2025-01-01"
---

## 概述

EEMT5560「整合商業解決方案」是香港科技大學工程管理碩士（MSc EEMT）課程中的整合性必修科，由 Ronald S. Lau 博士（ISOM 系）主講，以「整合計劃與執行（IPX）」為核心主軸，強調跨職能協調是取得持續競爭優勢的唯一途徑。課程圍繞三大支柱展開：量化決策工具（AHP 層次分析法用於多準則供應商選擇與 KPI 加權，使用 Saaty 1–9 配對比較矩陣與一致性比率 CR ≤ 0.10；DEA 數據包絡分析應用於 82 間香港聖安娜餅屋分店的效率標竿比較，CCR 模型輸入管控與不可控變數分離）、Marco Business Simulation（MBS）商業模擬（四個遞增複雜度模型：Model 1–4，涵蓋定價、生產排程、行銷預算、R&D 投資、設備折舊、多市場策略及銀行借貸優化，以累積 NPV 為最終績效準則，SIREN 五維 KPI 儀表板對應平衡計分卡）及供應鏈個案研究（中草藥需求預測 Holt-Winters vs. 指數平滑 MAD 比較、供應鏈績效六大 KPI：完美訂單率、填充率、現金周轉周期等）。課程以 Cathay Pacific、Huawei、Walmart、Li & Fung、SF Express 及 Temu/PDD 為小組展示個案，並整合 Porter 五力、平衡計分卡、SCOR 模型等策略框架，是修畢 EEMT5500/5510/5360/5540 後的知識整合頂點課程，直接對接業界的供應鏈規劃與財務決策場景。

## Course Overview

**EEMT5560 Integrated Business Solutions** is a capstone-style course in the [[wiki/entities/hkust|HKUST]] Engineering Management program taught by Ronald S. Lau (ISOM Department). It integrates quantitative decision-making tools with hands-on business simulation to develop cross-functional management competencies. The course is structured around three major pillars:

1. **Quantitative decision frameworks** -- [[ahp|Analytic Hierarchy Process (AHP)]] for multi-criteria decision making and [[Data Envelopment Analysis (DEA)|Data Envelopment Analysis (DEA)]] for operational benchmarking.
2. **Business simulation** -- Progressive Marco Business Simulation (MBS) games of increasing complexity (Models 1 through 4).
3. **Supply chain and operations case studies** -- Real-world applications including demand forecasting, inventory management, and performance dashboards.

The course builds on strategic frameworks like [[porters-five-forces|Porter's Five Forces]], the [[balanced-scorecard|Balanced Scorecard]], and the [[scor-model|SCOR Model]] to frame MBS decisions in a broader management context. The unifying thread is **Integrated Planning and Execution (IPX)** -- the idea that cross-functional alignment (planning, purchasing, production, marketing, finance) is the only path to sustainable competitive advantage. Notable IPX software applications covered include SAP Integrated Business Planning and Blue Yonder advanced SCM.

## Analytical Tools

### Analytic Hierarchy Process (AHP)

The course introduces [[ahp|AHP]] as a structured approach to multi-criteria decision making. Key topics include:

- **Pairwise comparison matrices** using Saaty's 1-9 scale to express relative importance of criteria. For $n$ criteria, $\frac{n(n-1)}{2}$ comparisons are required.
- **Eigenvalue method** for deriving priority weights, with a geometric-mean approximation method as a spreadsheet-friendly shortcut.
- **Consistency Ratio**: $CR = \frac{CI}{RI}$ where $CI = \frac{\lambda_{\max} - n}{n-1}$. CR must be below 0.10 for the judgments to be considered acceptable.
- A worked example with 5 KPIs (Net profit, Retail sales, ROA, Utilization, Cash on hand) yielding eigenvector weights of 0.361, 0.062, 0.109, 0.211, 0.257 -- nearly identical to the approximation method (0.355, 0.064, 0.113, 0.211, 0.258).
- BPMSG AHP Calculator (bpmsg.com/ahp/ahp-calc.php) used for in-class exercises.
- Practical applications to vendor selection, project prioritization, and KPI weighting for composite business scoring.

### Data Envelopment Analysis (DEA)

[[Data Envelopment Analysis (DEA)|DEA]] is taught as a non-parametric method for benchmarking operational efficiency. Course coverage includes:

- **CCR model** (Charnes-Cooper-Rhodes, 1978) assuming constant returns to scale.
- Transformation from fractional programming $E_0 = \frac{\sum_r u_r y_{r0}}{\sum_i v_i x_{i0}}$ to standard LP by fixing $\sum_i v_i x_{i0} = 1$.
- **Efficient frontier** identification and peer analysis for underperforming units. Each DMU is allowed to pick its own most favorable weights.
- **Saint Honore case study**: DEA applied to 82 cake shop branches using **Frontier Analyst** software, with controlled inputs (staff count, SKU variety, spoilage rate, operating expenses), uncontrolled inputs (floor area, rent), and outputs (transaction count, total sales revenue). Example improvement target for branch H25 (efficiency 80.35%, peers C76 and Y13): -26.5% area, -23.8% expense, -29.7% SKU, -39.3% spoilage, -19.7% staff, +13.6% transactions.
- **Efficiency-profitability matrix** (2x2) classifies stores as stars, sleepers, problems, or divestment candidates. Saint Honore data shows Pearson $r = 0.62$ between efficiency and profitability -- moderate correlation that creates strategic segmentation opportunities.
- **Bank branch LP example** with 6 branches, 1 input (staff), 2 outputs (personal and business transactions), illustrating how to formulate and solve the LP in Excel Solver.

## Marco Business Simulation (MBS)

The MBS platform is the central experiential learning tool, progressing through four models of increasing complexity:

| Model | Decisions | Key Additions |
|-------|-----------|---------------|
| Model 1 | 4 | Purchasing, production quantity, retail pricing, marketing expenses |
| Model 2 | 8 | Equipment/maintenance, R&D, dividends added |
| Model 3 | 14 | Multi-market pricing (4 markets), production allocation across markets, competitive strategy |
| Model 4 | 18 | Bank loans, urgent purchasing, financial leverage optimization |

### Key Business Concepts in MBS

- **Cost structure analysis**: Variable costs (materials, labor, maintenance) vs. fixed costs (R&D, admin, depreciation, holding costs). Students analyze unit cost breakdowns across markets.
- **Breakeven analysis**: $TC = FC + VC \times Q$; breakeven point $Q = \frac{FC}{SP - VC}$. The simulation tracks breakeven points across rounds with what-if sensitivity analysis.
- **Production capacity planning**: Production volume determined by equipment capacity, shift scheduling (1-3 shifts with overtime at 1.5x cost), and raw material availability. Material conversion rates affect actual output.
- **S&OP (Sales and Operations Planning)**: Coordinating demand forecasts with production capacity and inventory to minimize stockouts and overproduction.
- **DuPont analysis**: $ROE = \text{Net Margin} \times \text{Asset Turnover} \times \text{Financial Leverage}$. Used to decompose performance and identify improvement levers. Apple's 2021 annual report used as illustration (5% sales increase yields +7% net profit vs. 5% COGS reduction yields +10.8% net profit).
- **NPV optimization**: Primary performance criterion across simulation rounds; teams optimize cumulative NPV through pricing, investment, and dividend decisions.
- **Departmental performance evaluation**: Internal transfer pricing used to assess planning, marketing, production, purchasing, and financial departments independently.

### Investment Decisions in MBS

Three key investment categories with three impact levels (high, moderate, low):

- **Marketing campaigns** -- Impact potential demand in individual markets. Approximately 30% of the investment effect persists into the next round.
- **R&D expenses** -- Impact product quality and subsequently overall potential demand. About 60% of R&D effect carries over to subsequent rounds, and R&D also improves the material conversion factor.
- **Maintenance** -- Impact production efficiency through the material conversion factor (default 0.775). Maintenance effect is single-round only.

### MBS Game Mechanics

The MBS user manual (v3.4, 2023) specifies the mechanisms that translate decisions into outcomes. These details anchor the course's "simulation is not guessing" thesis:

- **SIREN dashboard** -- Five monitored KPIs: **S**hare (sales / all-company sales), **I**nventory rate (FG / sales), **R**evenue, **E**xpense ratio (marketing + admin / revenue), **N**et profit. SIREN is the game's equivalent of a [[balanced-scorecard|Balanced Scorecard]].
- **Potential demand drivers** -- Current and prior-round price, marketing, R&D, previous market share, deferred market potential, economy index, seasonality, and price elasticity. Market share has "deferred effect" (high/moderate/low), meaning today's share buys residual demand tomorrow.
- **Unfilled demand penalty** -- When potential demand exceeds maximum available supply, **30% of unfilled demand is lost** and **70% is captured by competitors** -- a stockout directly funds rivals.
- **Equipment depreciation** -- Production capacity depreciates 2.5% per round (10% per year). New investment converts to capacity at $20 per unit adjusted by the price index. Teams that skip equipment reinvestment silently lose capacity each quarter.
- **Shift escalation (Model 3/4)** -- Production volume needed > 1.35 normal capacity triggers 2 shifts; > 2.5 normal capacity triggers 3 shifts. Overtime carries a 1.5x labor cost penalty.
- **Urgent purchasing (Model 4 only)** -- Raw materials purchased in the current round become available in the *same* round at a premium, enabling teams to rescue a stockout but destroying gross margin.
- **Product lifecycle** -- Each market has a lifecycle indicator that starts at 1 and rises to 2 (peak demand doubled). High-growth markets peak in ~5 rounds, moderate in ~8, low in ~15. After peak, demand wanes, which makes early-market selection a strategic commitment.

### Worked Example: Model 3 Supply-Demand Balancing

A four-round trace (Lecture 13A) illustrates how decisions cascade:

| Round | Production request | Actual production | RM inventory | Potential demand | Actual sales | FG inventory end |
|-------|--------------------|-------------------|--------------|------------------|--------------|-----------------|
| 1 | 500,000 | 500,000 | 1,180,617 | 651,667 | 521,182 | 2 |
| 2 | 1,000,000 | 939,092 | 1,285,617 | 761,354 | 761,354 | 177,740 |
| 3 | 946,458 | 372,023 | 500,000 | 766,749 | 549,761 | 2 |
| 4 | 647,000 | 647,000 | 1,000,001 | 968,954 | 647,000 | 2 |

Round 3 shows the classic trap: requested production collapsed from 946K to 372K because raw material inventory was only 500K after previous draw-down -- the team under-purchased material in round 2. Sales for round 3 were capped at 549,761 against demand of 766,749, leaking roughly 65,000 units to competitors via the 70/30 loss rule. The lesson drilled into students: **control the supply side first (raw material pipeline + capacity + shift planning), then chase the demand side**.

## Supply Chain Case Studies

### Chinese Pharmaceuticals (Notoginseng Products)

A demand forecasting and inventory management case from Yunan province covering:

- **Exponential smoothing methods** compared:
  - Simple (alpha = 0.4): MAD = 825
  - Optimized simple (alpha = 1.0): MAD = 479
  - Adaptive smoothing: MAD = 1,014
  - **Holt-Winters** (trend + seasonality): MAD = 325 (best performer)
- **Inventory management**: Distinction between inventory level (physical stock) and inventory position (level + on-order). Forecast-driven replenishment with 2-month lead time.

### Supply Chain Performance Dashboards

Based on the Benchmarking Success article, the course covers six essential supply chain KPIs:

1. **Perfect Order** -- Composite metric of on-time delivery, in-full delivery, damage-free delivery, and accurate documentation. Calculated as product of all four percentages.
2. **Fill Rate** -- Order fill, line fill, and unit fill tracking first-attempt delivery success
3. **Cash-to-Cash Cycle Time** -- Days inventory on hand + days sales outstanding - days payables outstanding
4. **Inventory Days of Supply** -- Inventory on hand divided by average daily consumption
5. **Customer Order Cycle Time** -- Days from purchase order receipt to delivery completion
6. **Total Supply Chain Management Cost as % of Sales** -- Primary financial KPI for supply chain operations

Key principle: Keep dashboards simple with 5-6 top-level KPIs, supported by lower-tier functional KPIs that are actionable and relevant to specific departments.

## Case Studies & Projects

The course assigns two major case studies, one reading on supply chain KPIs, and a capstone group presentation. Students choose one company from a curated list or perform an MBS Game Analysis instead.

| Artifact | Type | Focus Area | Key Tools / Analysis | Takeaway |
|----------|------|------------|----------------------|----------|
| **Saint Honore (ST115)** | HKUST case | Retail benchmarking of 82 Hong Kong cake-shop branches of a bakery founded 1972 (parent: CRA / Fung Group) | [[Data Envelopment Analysis (DEA)\|DEA]] on controllable (staff, SKU, spoilage, opex) vs. uncontrollable (floor area, rent) inputs; efficiency-profitability 2x2 matrix | Traditional single-ratio KPIs (sales/staff, profit margin) correlate only $r=0.7546$ between themselves and $r=0.62$ with DEA efficiency -- multi-input/output benchmarking exposes hidden star and sleeper stores that rankings miss. |
| **Chinese Pharmaceuticals / Noto37 (ST5)** | HKUST case | Demand forecasting for a Hong Kong herbal medicine supplier (Notoginseng from Yunnan -> HK contract manufacturer -> Mannings/Watson's retail, 90-100 day lead time) | Simple ES ($\alpha=0.4$), Solver-optimized $\alpha=1.0$, adaptive smoothing, [[arma-models\|Holt-Winters]] trend+seasonality; inventory position vs. level | Holt-Winters cut MAD from 825 -> 325 (~61% improvement) vs. default ES. A 50% winter/spring seasonal swing plus 1.5-2 month reorder lead time means naive forecasting guarantees stockouts at Mannings. |
| **Supply Chain Performance Dashboards (Benchmarking Success, 2019)** | Reading | Top-6 cross-functional supply chain KPIs; "multi-function display" airliner metaphor; paralysis-by-analysis warning | Perfect Order composite ($0.98 \times 0.93 \times 0.99 \times 0.96 = 86.61\%$), Fill Rate, C2C cycle time, Inventory DOS, Customer Order Cycle Time, TSCMC%S | Multiplicative composition of Perfect Order punishes mediocrity -- four "very good" metrics still compound to a disappointing top-line, which is precisely why it is useful as a headline KPI. |
| **MBS Model 3 Supply/Demand Trace (Lecture 13A)** | In-class worked example | Four-round production/purchasing trace demonstrating the raw-material inventory trap and the 70/30 stockout leakage | Sales volume = min(potential demand, max available); FG inventory rollover; capacity vs. RM constraints | A single round of under-purchasing raw materials in Round 2 collapsed Round 3 production from 946K requested to 372K actual, leaking ~65K units in sales to competitors. "Control the supply side first." |
| **Marco Business Simulation (Models 1-4)** | Multi-round project | Progressive 4-model capstone simulation run over the semester with friendly match + graded competition rounds | SIREN dashboard, DuPont decomposition, CVP breakeven, NPV optimization, departmental transfer pricing, [[ahp\|AHP]]-weighted composite judge score | Teams are graded on cumulative NPV; the simulation directly mirrors [[scor-model\|SCOR]] Plan/Source/Make/Deliver and [[balanced-scorecard\|BSC]] perspectives. Models 1-2 are practice (1 market); Models 3-4 introduce 4-market competition and Model 4 unlocks bank loans + urgent material purchases. |
| **Group Presentation: Cathay Pacific** | Capstone group case | Long-run competitive decline of a legacy full-service airline; pandemic shock; premium positioning vs. budget rivals | [[porters-five-forces\|Porter's Five Forces]] (rivalry, substitutes from HSR + Greater Bay Area carriers), strategy evolution analysis | Illustrates the "why most companies fail in the long run if they don't change" thesis -- industry structure shifts can strand strategies that were once textbook correct. |
| **Group Presentation: Huawei** | Capstone group case | Consumer electronics competitive strategy under US sanctions; smartphone share recovery against Apple; expansion into EV ecosystem | Competitive strategy, vertical integration, R&D investment ratio, cost leadership + differentiation | Huawei bucked a 22% Q1 China smartphone market decline and posted the only growth -- a concrete example of how R&D-driven differentiation compensates for constrained supply chains. |
| **Group Presentation: Wal-Mart** | Capstone group case | Cost-leadership operational excellence; EDLP; global sourcing and cross-docking | Supply chain cost leadership, [[scor-model\|SCOR]] Source and Deliver processes | Canonical operational excellence benchmark for MBS teams pursuing a low-price, high-volume strategy. |
| **Group Presentation: Li & Fung** | Capstone group case | "Borderless manufacturing" trading / supply chain orchestration across thousands of Asian suppliers | Supply chain design, buyer power, intermediary business model erosion in the direct-to-factory era | Case highlights what happens when platform e-commerce removes the middleman -- Li & Fung's decline frames the buyer-power lesson in [[porters-five-forces\|Porter's Five Forces]]. |
| **Group Presentation: SF Express** | Capstone group case | Courier/express competition in mainland China; premium-speed positioning against JD Logistics, YTO, STO | Operational model, network economics, price vs. reliability trade-off | Contrasts premium-service differentiation with Wal-Mart cost leadership -- students see both Porter generic strategies side by side in the same semester. |
| **Group Presentation: Temu / PDD** | Capstone group case | Cross-border e-commerce expansion from China to the US; social-commerce customer acquisition; comparison with Shein | Customer segmentation by disposable income (~$2.6K CN rural vs. ~$39K US mid-eastern states), [[stp-marketing\|STP]], price elasticity, content-creator marketing | The 2024 presentations documented Temu's attempt to port the PDD group-buying playbook to the US and whether it can "out-Shein Shein" in fast fashion. Connects directly to [[ecommerce-models\|E-Commerce Models]]. |
| **MBS Game Analysis (alternative capstone)** | Reflective project | Teams that choose this option analyze their own MBS rounds instead of a real company | Round-by-round decision review; what-if sensitivity on pricing/production; lesson extraction | Forces teams to treat their simulation data as a case study, applying DuPont, CVP, and [[ahp\|AHP]] to their own performance retrospectively. |

## Key Findings

- **Quantitative tools complement simulation learning**: AHP and DEA provide structured frameworks that students apply within the competitive MBS environment.
- **Cost reduction often outperforms revenue growth**: The DuPont analysis demonstrates that a 5% COGS reduction yields greater ROA improvement (+3.4 percentage points) than a 5% sales increase (+2.2 percentage points) for the same base business.
- **Financial leverage amplifies returns but distorts comparisons**: Company X with 90% debt achieves 30% ROE vs. Company Y with 0% debt at 8.4% ROE, despite identical EBIT -- illustrating how capital structure choices affect performance metrics.
- **Holt-Winters forecasting significantly outperforms simpler methods** when data exhibits both trend and seasonal patterns (MAD of 325 vs. 479-1,014 for alternatives).
- **The [[balanced-scorecard|Balanced Scorecard]] framework** links all four perspectives (financial, customer, internal process, learning & growth) and is directly reflected in MBS performance metrics across financial, marketing, operations, and investment categories.

## Related Concepts

- [[ahp|Analytic Hierarchy Process]] -- Multi-criteria decision making tool central to KPI weighting in the course
- [[Data Envelopment Analysis (DEA)|Data Envelopment Analysis]] -- Efficiency benchmarking method with LP formulation; applied to 82 Saint Honore shops
- [[scor-model|SCOR Model]] -- Supply chain performance framework structuring MBS decisions
- [[balanced-scorecard|Balanced Scorecard]] -- Strategy execution and performance measurement framework linking MBS departments to strategic objectives
- [[porters-five-forces|Porter's Five Forces]] -- Industry structure analysis for MBS competitive strategy
- [[supply-chain-management|Supply Chain Management]] -- The broader discipline that MBS exercises
- [[cvp-analysis|CVP Analysis]] -- Breakeven quantity $Q_{BE} = FC / (SP - VC)$ used for MBS pricing decisions
- [[npv|NPV]] -- Primary performance criterion across MBS rounds
- [[financial-statements|Financial Statements]] -- Generated each round for performance analysis
- [[financial-ratios|Financial Ratios]] -- DuPont decomposition and ROE analysis
- [[capacity-planning|Capacity Planning]] -- Shift scheduling and equipment investment decisions
- [[newsvendor-problem|Newsvendor Problem]] -- Related to single-period inventory decisions in MBS
- [[marketing-mix|Marketing Mix]] -- Marketing expense decisions across four markets
- [[stp-marketing|STP Marketing]] -- Market-specific positioning strategies
- [[arma-models|ARMA Models]] -- Advanced time-series alternatives to Holt-Winters for demand forecasting
- [[linear-regression|Linear Regression]] -- Baseline forecasting method contrasted with exponential smoothing
- [[erp|ERP]] -- SAP IBP and Blue Yonder mentioned as IPX software examples

## Source Materials

- Lecture 01: IPX Introduction
- Lecture 02: AHP
- Lecture 02: MBS Model 1
- Lecture 02: MBS Model 2
- Lecture 03: DEA
- Lecture 04: Saint Honore DEA Case
- Lecture 05: Chinese Pharmaceuticals
- Lecture 13: MBS Model 3
- Lecture 13A: Model 3 Supply/Demand Worked Example
- Lecture 14: MBS Model 4
- Reading: Supply Chain Performance Dashboards
- Case Study ST115: Saint Honore
- Case Study ST5: Chinese Pharmaceuticals
- MBS User Manual v3.4 (HKUST)
- MBS Pre-Game Planning Worksheet
- MBS Simulated Business Management Competition 2024
- Group Presentation Selection Form
- Temu Group Presentation Script
