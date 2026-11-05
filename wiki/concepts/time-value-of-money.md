---
title: "Time Value of Money"
full_name: "Time Value of Money (TVM)"
type: concept
tags: [finance, engineering-economics, tvm, discounting, compounding]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/engineering-economics.md"
confidence: high
---

## 概述

貨幣時間價值（Time Value of Money, TVM）是工程經濟學與財務分析的基石概念，核心命題是今天持有的一元比未來相同金額更有價值，因為現有資金可立即投資獲取回報。驅動此原則的三大力量為：資金的獲利潛力、通貨膨脹侵蝕購買力，以及未來現金流的不確定性風險。在技術層面，TVM 透過六種標準折算因子（單筆複利、現值、均勻系列沉沒基金、資本回收、複利總和、現值總和）以及算術漸變序列因子 $(P/G, i, N)$ 和幾何漸變序列因子，系統地實現不同時間點現金流之間的等價轉換。名義利率與實際有效利率的換算 $i_\text{eff} = (1 + r/M)^M - 1$（連續複利為 $e^r - 1$）在貸款攤銷、債券估值及年金定價中不可或缺，是後續 [[npv|NPV]]、[[irr|IRR]] 及 [[depreciation|折舊]]稅盾計算的共同輸入。在運籌學與金融工程研究中，TVM 框架進一步延伸至隨機折現因子（stochastic discount factor）與動態規劃，是跨期最優化與期權定價模型的數學前身。EEMT5510 課程以加拿大按揭半年複利慣例的買房／租房案例，示範了現實中複利頻率誤判如何顯著改變決策結論。

## Core Mechanism

The **time value of money (TVM)** states that a sum of money available now is worth more than the same sum in the future, because the present sum can be invested to earn a return. This is the foundational principle underlying all engineering economy evaluation methods — [[npv|NPV]], [[irr|IRR]], annual worth, and capitalized worth all depend on TVM calculations.

### Why Money Has Time Value

Three factors drive TVM:

1. **Earning potential**: Money can be invested to generate returns. Even risk-free instruments (e.g., government bonds) offer positive yields.
2. **Inflation**: The purchasing power of money generally declines over time. A fixed sum buys fewer goods in the future than today.
3. **Risk and uncertainty**: Future cash flows are uncertain. A bird in the hand is worth two in the bush — present money eliminates the risk of non-receipt.

### Simple vs. Compound Interest

**Simple interest** calculates interest only on the original principal:

$$I = P \times N \times i$$

where $P$ is the principal, $N$ is the number of periods, and $i$ is the interest rate per period. Total amount: $F = P(1 + Ni)$.

**Compound interest** calculates interest on the principal plus any accumulated interest:

$$F = P(1 + i)^N$$

Compounding is the standard assumption in engineering economy. The difference between simple and compound interest grows dramatically with longer time horizons — this is the power of compounding.

### Equivalence

Two cash flows are **equivalent** at a given interest rate if they have the same value when converted to the same point in time. Equivalence is the central concept enabling comparison of alternatives with different cash flow patterns. For example, receiving \$1,000 today is equivalent to receiving \$1,610.51 in five years at 10% annual interest, because $1000 \times (1.10)^5 = 1610.51$.

Equivalence depends on the interest rate — two cash flows equivalent at 10% are generally not equivalent at 8%.

### Worked Example: Annuity Due

Twenty annual deposits of \$1,000 made at the **beginning** of each year into a 2.5% savings account (HW1 Problem 3). Standard $F/A$ assumes end-of-period payments, so multiply by $(F/P, 2.5\%, 1)$ to shift the series forward one year:

$$F = 1{,}000 \cdot (F/A, 2.5\%, 20) \cdot (F/P, 2.5\%, 1) = 1{,}000 \cdot 25.545 \cdot 1.025 = \$26{,}183.27$$

### Worked Example: Sinking Fund Return (HW1 Problem 4b)

As a companion to the "bragging-rights" lump-sum return (10.53% over 23 years from \$10K to \$100K), HW1 P4b asks: if instead \$500 per year is deposited over 23 years at the start of each year to reach \$100,000, what return is implied? Using the beginning-of-period convention ($F/A$ factor on 24 periods, subtract the final un-invested dollar):

$$100{,}000 = 500 \cdot (F/A, i', 24) - 500 \;\Longrightarrow\; (F/A, i', 24) = 201 \;\Longrightarrow\; i' = 15.58\%$$

Interpretation: **regular disciplined contributions can earn a higher implied return** than an inferred single-point rate over the same horizon, because the sinking-fund factor absorbs the compounding differently. The juxtaposition drives home why Principle 3 (consistent viewpoint) matters for performance-claim communication.

### Factor Identity

An intuitive identity from HW1 Problem 6: $(A/F, i\%, N) = (A/P, i\%, N) - i$. Algebraically, $A/P$ differs from $A/F$ by one extra compound period ($(1+i)^N$ in the numerator vs. $1$), which accounts for exactly $i$ of difference. Geometrically, $A/P$ includes the interest cost of the initial principal while $A/F$ does not.

## Key Formulas

### Six Standard Factors

Engineering economy uses six conversion factors, each with a standard notation:

| Factor Name | Converts | Formula | Notation |
|-------------|----------|---------|----------|
| Single-payment compound amount | P to F | $F = P(1+i)^N$ | $(F/P, i\%, N)$ |
| Single-payment present worth | F to P | $P = F(1+i)^{-N}$ | $(P/F, i\%, N)$ |
| Uniform series sinking fund | F to A | $A = F \frac{i}{(1+i)^N - 1}$ | $(A/F, i\%, N)$ |
| Uniform series capital recovery | P to A | $A = P \frac{i(1+i)^N}{(1+i)^N - 1}$ | $(A/P, i\%, N)$ |
| Uniform series compound amount | A to F | $F = A \frac{(1+i)^N - 1}{i}$ | $(F/A, i\%, N)$ |
| Uniform series present worth | A to P | $P = A \frac{(1+i)^N - 1}{i(1+i)^N}$ | $(P/A, i\%, N)$ |

Where $P$ = present value, $F$ = future value, $A$ = uniform annual amount, $i$ = interest rate per period, and $N$ = number of periods.

### Gradient Series

For cash flows that increase by a constant amount $G$ each period (arithmetic gradient):

$$P = G \frac{(1+i)^N - iN - 1}{i^2(1+i)^N}$$

The gradient present worth factor is denoted $(P/G, i\%, N)$.

For cash flows growing at a constant rate $g$ per period (geometric gradient):

$$P = A_1 \frac{1 - (1+g)^N(1+i)^{-N}}{i - g} \quad \text{for } i \neq g$$

### Nominal vs. Effective Interest Rates

When compounding occurs more frequently than annually:

- **Nominal rate** $r$: Stated annual rate without considering sub-period compounding.
- **Effective rate** $i_{\text{eff}}$: Actual annual rate accounting for compounding frequency.

$$i_{\text{eff}} = \left(1 + \frac{r}{M}\right)^M - 1$$

where $M$ = number of compounding periods per year. For continuous compounding: $i_{\text{eff}} = e^r - 1$.

**Worked examples (HW2 Problem 3)**:
- Given $i_{\text{eff}} = 12\%$, find the nominal rate compounded quarterly: $0.12 = (1 + r/4)^4 - 1 \Rightarrow r = 11.49\%$.
- Given $r = 8\%$ compounded monthly: $i_{\text{eff}} = (1 + 0.08/12)^{12} - 1 = 8.30\%$.
- To triple principal at 3% effective annual: $3 = (1.03)^N \Rightarrow N = \ln 3 / \ln 1.03 = 37.2$ years.

### Geometric Gradient

When cash flows grow at a geometric rate $g$ per period, the closed-form present worth is:

$$P = A_1 \cdot \frac{1 - (1 + g)^N (1 + i)^{-N}}{i - g}, \quad i \neq g$$

When $i = g$, $P = N A_1 / (1 + i)$. This factor is essential for inflation-adjusted analyses.

**Worked example (HW2 Problem 2 — Natural Gas Heating)**: A firm pays \$20,000/year for natural gas escalating at 10%, plus \$800/year furnace maintenance escalating at 15%. Horizon = 10 years, $i = 18\%$. Using geometric gradient:

$$P_{\text{gas}} = 22{,}000 \cdot \frac{1 - (F/P, 10\%, 10)(P/F, 18\%, 10)}{0.18 - 0.10} = \$138{,}717$$

$$P_{\text{maint}} = 800(1.15) \cdot \frac{1 - (F/P, 15\%, 10)(P/F, 18\%, 10)}{0.18 - 0.15} = \$6{,}962$$

Annualized: $AW = (138{,}717 + 6{,}962)(A/P, 18\%, 10) = \$32{,}416$/year.

## Cash Flow Diagrams

A **cash flow diagram** is the standard visual tool for TVM problems:

- Horizontal line represents the time axis, divided into equal periods.
- **Upward arrows** represent cash inflows (receipts).
- **Downward arrows** represent cash outflows (disbursements).
- Arrow length is roughly proportional to magnitude.
- Time 0 is the present; time $N$ is the end of the study period.

Convention: Draw from a consistent viewpoint (borrower or lender, buyer or seller). Mixing viewpoints within one diagram creates errors.

## Practical Applications

### Loan Amortization

A loan of $P$ at rate $i$ per period for $N$ periods requires equal payments of:

$$A = P(A/P, i\%, N)$$

Each payment splits into interest (on remaining balance) and principal repayment. Early payments are interest-heavy; later payments are principal-heavy.

### Deferred Annuities

When a uniform series starts $J$ periods after time 0, first find the present value at the start of the annuity, then discount back:

$$P_0 = A(P/A, i\%, N)(P/F, i\%, J)$$

### Comparing Alternatives

TVM enables apples-to-apples comparison of alternatives with different timing. Convert all cash flows to a common time point (usually present or annual) and compare using equivalent worth methods.

### Buy vs. Rent Decision (Ivey W14403 Case)

The EEMT5510 "Buy vs. Rent" case applies TVM to a personal real-estate decision. Key steps:

1. Compute the monthly mortgage payment using $A = P(A/P, i_m, 300)$ where $i_m$ is the monthly effective rate derived from the 4% Canadian quoted rate (**semi-annual compounding** convention: $i_m = (1 + r/2)^{2/12} - 1$, not $r/12$ as in US mortgages).
2. The **opportunity cost** of the down payment is the foregone monthly return at the same rate, since the money would otherwise have been earning $i_m$.
3. Compute outstanding mortgage principal at future horizons (2, 5, 10 years) via $P_k = A \cdot (P/A, i_m, 300 - 12k)$.
4. Compare total equivalent rent cash flows against total buy cash flows (mortgage + condo fees + taxes + maintenance + closing costs) plus potential capital gain or loss on sale under four price scenarios.

This case illustrates why monthly-to-effective-rate conversion, mortgage amortization, and opportunity-cost reasoning must all be applied correctly to reach a defensible conclusion.

## Common Pitfalls

- **Mismatching periods and rates**: The interest rate period must match the cash flow period. If cash flows are monthly, use a monthly rate.
- **Forgetting the timing convention**: End-of-period convention is standard. Payments at the beginning of a period require adjustment (multiply by $(1+i)$).
- **Ignoring inflation**: Nominal cash flows should be discounted at nominal rates; real cash flows at real rates. Mixing them produces errors.
- **Double-counting**: Do not apply both an inflation adjustment and a nominal discount rate that already incorporates inflation.

## Related Concepts

- [[npv|NPV]] — Uses TVM to evaluate project worth at time zero
- [[irr|IRR]] — The discount rate that makes the present worth of all cash flows zero
- [[depreciation|Depreciation]] — Book cost allocation over asset life; interacts with tax-adjusted cash flows
- [[cvp-analysis|CVP Analysis]] — Breakeven analysis; TVM extends static CVP to multi-period settings
- [[financial-ratios|Financial Ratios]] — Financial performance metrics; some incorporate discounted cash flows
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Financial Engineering and Capital Budgeting)

## Source Materials

- L4 - Time Value of Money
- L5 - Evaluating a Single Project
- [[wiki/sources/courses/engineering-economics.md|EEMT5510 Engineering Economics and Cost Management]]
