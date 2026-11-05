---
title: "Managerial Accounting"
full_name: "Managerial Accounting and Cost Management"
type: concept
tags: [accounting, cost-management, managerial-accounting]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/acct-managerial-accounting"
confidence: medium
---

## 概述

管理會計（Managerial Accounting）為企業內部決策者提供以成本分析為核心的量化框架，與對外報告的財務會計的根本差異在於其前瞻性、細顆粒度（可按產品線、部門或訂單分解）且不受 GAAP/IFRS 約束。成本按行為分類（固定、變動、混合、階梯固定）是 [[cvp-analysis|CVP 分析]] 與損益平衡計算的基礎；按可追溯性分類（直接成本 vs. 間接費用）則決定了產品成本的分攤邏輯。傳統作業成本法以單一費率分攤製造費用，在產品組合複雜時系統性地扭曲成本；作業基礎成本法（ABC）通過兩階段分攤（費用→作業池→產品）還原各產品對資源的真實消耗，揭示高量簡單產品長期補貼低量複雜產品的隱性問題，為正確定價與產品組合決策提供依據。標準成本制度通過將實際成本與預定標準對比，系統分解材料（價格差異 + 數量差異）、人工（工資率差異 + 效率差異）及製造費用差異，是製造業績效控制的主要工具，也是 [[balanced-scorecard|平衡計分卡]] 財務績效視角的數據來源。在約束資源下的決策中，「每單位稀缺資源貢獻毛利最大化」原則等同於 [[linear-programming|線性規劃]] 的對偶問題——影子價格正是放寬約束一單位所增加的邊際利潤，形成管理會計與 OR 優化之間的概念橋樑。預算編製（主預算、彈性預算）提供業績比較基準；零基預算與 Kaizen 預算（持續改善目標嵌入預算）則代表了從靜態控制到動態改善導向的演進。對於 OR 研究者而言，管理會計的相關成本概念（沉沒成本無關、機會成本必须計入）與成本估算技術（高低點法、迴歸分析估算成本函數）是構建現實決策模型的重要實踐語言。

## What It Is

**Managerial accounting** provides financial information for internal decision-making — unlike financial accounting (which reports to external stakeholders under GAAP/IFRS). Managerial accounting is forward-looking, detailed by product/division, and not constrained by external reporting rules.

## Cost Classification

**By behavior**:
- **Fixed costs**: don't change with output (rent, salaried managers). Fixed per-unit cost declines with volume.
- **Variable costs**: change proportionally with output (raw materials, direct labor paid per piece)
- **Mixed (semi-variable)**: fixed component + variable component (utility bills)
- **Step-fixed**: fixed within a range, then jump (supervisors: one per 10 workers)

**By traceability**:
- **Direct costs**: traceable to a specific cost object (product, department)
- **Indirect (overhead) costs**: shared across multiple cost objects; must be allocated

**By relevance**:
- **Relevant costs**: future costs that differ between alternatives (for decisions)
- **Sunk costs**: already incurred, irrelevant to future decisions
- **Opportunity costs**: foregone benefit of the next best alternative

## Cost-Volume-Profit (CVP) Analysis

See [[cvp-analysis]] for full treatment. Key relationships:
- **Contribution margin** = Revenue − Variable costs
- **Break-even point**: Fixed costs / Contribution margin per unit
- **Operating leverage**: % change in profit / % change in revenue = higher leverage → more risk/reward

## Product Costing Systems

### Job Order Costing
Track costs per individual job/batch. Direct materials + direct labor = **prime costs**. Manufacturing overhead allocated using **predetermined overhead rate**: $\text{POHR} = \text{Estimated overhead} / \text{Estimated activity base}$ (direct labor hours, machine hours).

Used for: custom manufacturing, construction, printing, professional services.

### Process Costing
Costs averaged over homogeneous units in a continuous process. **Equivalent units** = whole units that could have been completed with the effort spent on WIP.

Used for: chemicals, food processing, oil refining.

### Activity-Based Costing (ABC)

Traditional overhead allocation (one rate) distorts product costs when products use overhead resources differently. **ABC** assigns overhead in two stages:
1. Assign costs to **activity cost pools** (setup, material handling, inspection)
2. Assign activity costs to products using **activity rates** (cost per setup, cost per material move)

**ABC reveals**: high-volume simple products often cross-subsidize low-volume complex products under traditional costing. Can lead to correct product pricing decisions.

## Standard Costing and Variance Analysis

**Standard costs**: predetermined per-unit costs for direct materials, direct labor, overhead.

**Variances** decompose actual vs. standard cost:

**Direct materials**:
- Price variance = (Actual price − Standard price) × Actual qty
- Quantity variance = (Actual qty − Standard qty) × Standard price

**Direct labor**:
- Rate variance = (Actual rate − Standard rate) × Actual hours
- Efficiency variance = (Actual hours − Standard hours) × Standard rate

**Manufacturing overhead**:
- Spending variance (fixed + variable components)
- Volume variance (fixed overhead: actual vs. budgeted volume)

Variance analysis pinpoints where performance deviated — useful for [[balanced-scorecard]] and operations control.

## Budgeting

**Master budget**: comprehensive financial plan linking operating budgets (sales, production, COGS, SG&A) to financial budgets (pro forma income statement, balance sheet, cash flow).

**Flexible budget**: adjusts for actual activity level — separates volume variance from efficiency/spending variances.

**Zero-based budgeting**: every expenditure must be re-justified (vs. incremental "last year + X%").

**Kaizen budgeting**: builds continuous improvement targets into the budget — each period's budget assumes a cost reduction vs. prior period.

## Relevant Costs for Decisions

**Make-or-buy**: compare incremental manufacturing cost to purchase price + opportunity cost of freed capacity.

**Special orders**: accept if price > variable cost (provided no capacity constraint and no impact on regular sales).

**Product mix / constrained resource**: when a single resource is scarce, maximize contribution margin per unit of constrained resource (closely related to LP shadow prices — see [[linear-programming]]).

**Drop a segment**: only relevant costs matter. Fixed costs that won't be eliminated are irrelevant to the drop decision.

## Assumptions and Limitations

- **Linearity of cost functions**: standard CVP and variance analysis assume linear cost behavior within the relevant range. Economies of scale, learning curves, and batch-level costs violate linearity; piecewise-linear or nonlinear cost functions are needed for broader ranges.
- **ABC requires accurate activity driver measurement**: identifying cost drivers and measuring activity volumes is resource-intensive. Inaccurate driver rates can produce ABC costs as misleading as traditional allocation. Time-driven ABC (Kaplan & Anderson 2004) reduces the data burden by using time as the universal driver.
- **Standard costs become outdated quickly**: in fast-changing environments (rapid material cost inflation, frequent product redesigns), standards need continuous revision or the variance signal loses meaning.
- **Sunk cost irrelevance is counterintuitive**: managers often commit the sunk cost fallacy — continuing a failing project to "recover" past investment. Managerial accounting training is partly about building the discipline to ignore sunk costs, connecting directly to [[behavioral-economics|behavioral economics]] research on escalation of commitment.
- **Transfer pricing complexity**: when divisions trade internally, the transfer price affects divisional performance measures but not consolidated profit. Optimal transfer pricing (marginal cost rule vs. market price vs. negotiated price) is a principal-agent problem that cannot be solved by accounting rules alone.

## Related Concepts

- [[cvp-analysis|CVP Analysis]] — Core analytical tool; contribution margin, breakeven, operating leverage
- [[financial-statements|Financial Statements]] — Managerial accounting feeds internal reports; product costs flow to income statement via COGS
- [[financial-ratios|Financial Ratios]] — ROI, residual income, and EVA are managerial extensions of financial ratio analysis to divisional performance
- [[balanced-scorecard|Balanced Scorecard]] — Integrates financial (variance, ROI) and non-financial (quality, customer, learning) performance metrics
- [[capacity-planning|Capacity Planning]] — Bottleneck identification and throughput accounting (Theory of Constraints) extend managerial accounting to operations
- [[linear-programming|Linear Programming]] — Product mix under constrained resources; shadow price = contribution margin per unit of scarce resource
- [[depreciation|Depreciation]] — Book depreciation vs. tax depreciation (MACRS); affects product cost and reported profit differently
- [[behavioral-economics|Behavioral Economics]] — Sunk cost fallacy, escalation of commitment, budgetary slack; behavioral dimensions of standard-setting and performance evaluation
- [[wiki/mocs/operations-research|Operations Research MOC]]

## Source Materials

- [[wiki/sources/courses/acct-managerial-accounting|ACCT2200 Managerial Accounting]]
- [[wiki/sources/courses/accounting|SBMT5010 Accounting for Managers]]
- [[wiki/sources/courses/engineering-economics|EEMT5510 Engineering Economics and Cost Management]]
