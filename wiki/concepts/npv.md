---
title: "Net Present Value"
full_name: "Net Present Value (NPV)"
type: concept
tags: [finance, engineering-economics, npv, project-evaluation, discounting]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/engineering-economics.md"
confidence: high
---

## 概述

淨現值（Net Present Value, NPV），在工程經濟學中稱為現值（Present Worth, PW），是資本預算中最核心的項目評估準則，其公式為 $NPV = \sum_{k=0}^{N} F_k (1+i)^{-k}$，將所有未來現金流按最低可接受回報率（MARR）折現至時間零點以衡量投資所創造的淨財富。NPV 與價值最大化原則完全一致，並具備可加總性——項目組合的 NPV 等於各子項目 NPV 之和，使其成為在資本配給約束下進行整數規劃優化的天然目標函數。作為等值換算工具，NPV 衍生出年值（AW）、終值（FW）及資本化成本（CW，適用於永久設施），三者在接受或拒絕決策上始終一致。在不等壽命方案比較中，AW 法隱含「重複假設」，能在無需計算最小公倍數的情況下自動達成等值比較。在互斥方案之間，NPV 準確計入規模差異，避免 [[irr|IRR]] 直接比較法的陷阱。實務上，NPV 的折現率來自企業的加權平均資本成本（WACC），連結至 [[corporate-finance|公司財務]]；而 WACC 的估計本身依賴 CAPM（見 [[portfolio-theory|投資組合理論]]），形成從微觀項目到宏觀市場均衡的完整定價鏈。EEMT5510 課程以青島城市綜合體、Cathay Pacific 貨運站（NPV ≈ HK\$2.67B）及 WeeWork 等案例，示範了敏感性分析與決策樹與 NPV 框架的結合應用。

## Core Mechanism

**Net Present Value (NPV)**, referred to as **Present Worth (PW)** in engineering economy, converts all cash flows of a project to their equivalent value at time zero using a specified discount rate. The discount rate used is the **Minimum Attractive Rate of Return (MARR)**, which represents the organization's opportunity cost of capital.

### Formula

$$NPV = PW(i) = \sum_{k=0}^{N} F_k (1+i)^{-k} = \sum_{k=0}^{N} F_k (P/F, i\%, k)$$

where:
- $F_k$ = net cash flow at end of period $k$ (positive for inflows, negative for outflows)
- $i$ = discount rate (MARR)
- $N$ = project life (number of periods)
- $(P/F, i\%, k)$ = single-payment present worth factor

### Decision Rule

| Condition | Decision |
|-----------|----------|
| $NPV \geq 0$ | Accept the project. It earns at least the MARR. |
| $NPV < 0$ | Reject the project. It does not meet the MARR threshold. |

When $NPV = 0$, the project earns exactly the MARR — it is marginally acceptable.

### Relationship to MARR

The **MARR** is the minimum return an organization requires to justify an investment. It is set considering:

- **Cost of capital**: Weighted average of debt and equity costs.
- **Opportunity cost**: Return available from the best alternative investment of similar risk.
- **Risk premium**: Additional return to compensate for project-specific uncertainty.

A higher MARR produces lower NPV values, making projects harder to justify. The MARR is a policy decision, not calculated from the project itself.

## Equivalent Worth Methods

NPV is one of three equivalent worth methods, all yielding consistent accept/reject decisions:

### Future Worth (FW)

$$FW(i) = PW(i) \times (F/P, i\%, N) = \sum_{k=0}^{N} F_k (F/P, i\%, N-k)$$

Accept if $FW(\text{MARR}) \geq 0$. FW and PW always agree because $(F/P, i\%, N) > 0$.

### Annual Worth (AW)

$$AW(i) = PW(i) \times (A/P, i\%, N)$$

Converts all cash flows to an equivalent uniform annual series. Particularly useful for comparing alternatives with different lives, because AW is the same for any number of complete life cycles (assuming repeatability).

**Capital Recovery (CR)** is a key component:

$$CR = I \cdot (A/P, i\%, N) - S \cdot (A/F, i\%, N)$$

where $I$ = initial investment and $S$ = salvage value. Then $AW = R - E - CR$ where $R$ and $E$ are annual equivalent revenues and expenses.

### Capitalized Worth (CW)

For projects with infinite life (perpetuities):

$$CW = \frac{A}{i}$$

where $A$ is the annual equivalent cost. Used for infrastructure projects, endowments, and permanent installations.

## Comparing Mutually Exclusive Alternatives

When selecting among mutually exclusive alternatives:

### Investment Alternatives (Revenue Projects)

These generate positive revenues. Select the alternative with the **highest NPV** (provided it is non-negative). Do not simply pick the one with the highest rate of return — NPV correctly accounts for scale.

### Cost Alternatives (Service Projects)

All alternatives serve a required function; revenues are absent or identical. Select the alternative with the **lowest present worth of costs** (i.e., least negative PW, or equivalently, highest PW).

### Unequal Lives

When alternatives have different useful lives:

1. **Repeatability assumption**: If the project can be repeated with identical cash flows, use AW — it naturally handles unequal lives.
2. **Co-terminated assumption**: Define a common study period. Truncate longer-lived alternatives (assign salvage values) and extend shorter-lived alternatives (assume replacement or leasing costs).
3. **Least Common Multiple (LCM)**: Repeat each alternative over the LCM of their lives and compare total PW. This is equivalent to AW comparison.

### Incremental Analysis

For investment alternatives, rank by increasing initial investment. Starting from the base alternative (do-nothing or lowest cost), evaluate each increment. An increment is justified if its incremental NPV > 0 (or equivalently, incremental [[irr|IRR]] > MARR).

## Bond Valuation as NPV Application

Bond pricing is a direct NPV application. The price of a bond equals the present value of its future cash flows:

$$P = C(P/F, i\%, N) + rZ(P/A, i\%, N)$$

where:
- $C$ = face (par) value
- $r$ = coupon rate per period
- $Z$ = face value (bond denomination)
- $i$ = required yield per period
- $N$ = number of remaining periods

When $i > r$, the bond trades at a **discount**; when $i < r$, at a **premium**; when $i = r$, at **par**.

## Advantages and Limitations

### Advantages

- **Consistent with value maximization**: NPV directly measures wealth creation in monetary terms.
- **Additive**: The NPV of a portfolio equals the sum of individual NPVs — enables modular analysis.
- **Handles varying cash flows**: No assumption of uniform payments required.
- **Unambiguous**: Always yields a single value (unlike [[irr|IRR]] which can have multiple solutions).

### Limitations

- **Requires MARR specification**: The result depends critically on the chosen discount rate.
- **Scale-dependent**: A \$10M project with NPV = \$1M may be preferred over a \$1M project with NPV = \$500K, even though the latter has higher returns. This is a feature (maximizes value) but can conflict with capital rationing.
- **Assumes reinvestment at MARR**: All intermediate cash flows are implicitly reinvested at the MARR. This is generally considered more realistic than IRR's assumption.
- **Difficult to communicate**: Non-financial stakeholders often find percentage returns (IRR) more intuitive than absolute dollar values.

## Practical Example

A machine costs \$50,000, generates \$15,000/year net revenue for 5 years, and has \$5,000 salvage value. At MARR = 10%:

$$NPV = -50{,}000 + 15{,}000(P/A, 10\%, 5) + 5{,}000(P/F, 10\%, 5)$$
$$= -50{,}000 + 15{,}000(3.7908) + 5{,}000(0.6209)$$
$$= -50{,}000 + 56{,}862 + 3{,}105 = 9{,}967$$

Since $NPV = \$9{,}967 > 0$, the investment is acceptable.

### HW2 Problem 5 — Commercial Building Breakeven Revenue

A \$200M commercial building with \$30M annual operating cost, \$50M salvage, 10-year life, and MARR = 25% must break even at time zero. Setting $NPV = 0$:

$$0 = -200{,}000{,}000 + (A - 30{,}000{,}000)(P/A, 25\%, 10) + 50{,}000{,}000(P/F, 25\%, 10)$$

Solving: $A = \$84.51M$/year minimum revenue. This is an **inverse NPV** — solving for the revenue that makes the project just acceptable. The same technique underlies breakeven sensitivity analysis.

### HW3 Problem 3 — Capital-Budgeting with Contingent Proposals

Four proposals (A, B, C, D) are evaluated at MARR = 15%; A and C are mutually exclusive, B and D are mutually exclusive and each contingent on A or C being selected, and total budget ≤ \$18,000. Computing each PW: $PW_A = \$5{,}466$, $PW_B = \$896$, $PW_C = -\$4{,}565$, $PW_D = -\$4{,}728$. The integer linear program:

$$\max \; 5466 X_A + 896 X_B - 4565 X_C - 4728 X_D$$
$$\text{s.t. } X_A + X_C \leq 1, \; X_B + X_D \leq X_A + X_C, \; 100000 X_A + 20000 X_B + 120000 X_C + 30000 X_D \leq 18{,}000$$

This illustrates that NPV is additive — total portfolio NPV equals the sum of individual NPVs — which makes it ideal for binary optimization under capital rationing.

### Annual Worth for Unequal Lives

When alternatives differ in life, AW implicitly repeats each to infinity and so compares them on equal footing without requiring a common study period. For the WeeWork example (HW3 Problem 5), the \$10M building over 12 years with \$3.3M furnishings refreshed every 4 years gives $AW(10\%) = \$238{,}221 > 0$ without needing to extend to a common multiple.

### HW4 Problem 4 — Build vs. Rent Decision Tree

A firm must choose between building a new facility (cost \$10.5M now + \$17M salvage at year 10, with a 5-year option to add or rent extra space) and renting through 10 years (\$900K/yr at 55% vs. \$700K/yr at 45%, MARR = 10%). Folding back the decision tree at stage 2 shows the additional-space sub-problem resolves to **rent** ($PW_{RA} = -\$4.12M$ vs. $PW_{BA} = -\$5.11M$). Rolling this back into the top-level comparison:

$$PW_{\text{Build}} = -5{,}378{,}970 \quad\text{vs.}\quad PW_{\text{Rent}} = -5{,}002{,}099$$

so **rent** is recommended. This example shows how NPV combines with folded-back decision trees: each branch is evaluated at the decision node, the max/min PW is substituted back up the tree, and the top-level NPV compares the best-strategy cash flows — NPV is additive and can absorb the optionality from downstream decisions without losing consistency.

### Cross-course case: Cathay Pacific Cargo Terminal (EEMT5520)

The [[service-ops|EEMT5520]] Cathay Pacific Cargo Terminal case is a long-horizon NPV problem dressed as a capacity decision. HACTL's SuperTerminal 1 was capped at 2.6M tonnes (Cathay held 60% of throughput) and a captive Cathay terminal would cost HK\$4.8–5.5B with a 20-year concession. The worksheet builds a WACC of **12.09%** from cost-of-equity (CAPM) and after-tax cost-of-debt, then discounts projected cargo-revenue deltas net of opex and the salvage value at year 20. Result: $NPV \approx \$2.67\text{B}$, decisive but highly sensitive to the assumed demand share the captive terminal captures from third parties. This is the same pattern as the Qingdao City Complex case above — a single-shot capital decision where the NPV verdict depends on a handful of load-bearing assumptions that deserve explicit sensitivity analysis. See [[capacity-planning|Capacity Planning]] for the operational-side framing.

## Related Concepts

- [[time-value-of-money|TVM]] — Theoretical foundation for discounting
- [[irr|IRR]] — Alternative evaluation method; the rate where NPV = 0
- [[depreciation|Depreciation]] — Affects after-tax cash flows used in NPV calculations
- [[cvp-analysis|CVP Analysis]] — Breakeven analysis; NPV extends it to multi-period settings
- [[financial-ratios|Financial Ratios]] — Profitability and return metrics complement NPV analysis
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Financial Engineering and Capital Budgeting)

## Source Materials

- L5 - Evaluating a Single Project
- L6 - Project Comparison and Selection
- [[wiki/sources/courses/engineering-economics.md|EEMT5510 Engineering Economics and Cost Management]]
