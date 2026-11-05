---
title: "Depreciation"
full_name: "Depreciation"
type: concept
tags: [finance, engineering-economics, depreciation, accounting, tax]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/engineering-economics.md"
confidence: high
---

## 概述

折舊（Depreciation）是將有形資產取得成本在其使用年限內系統性分攤的會計方法。折舊本身不產生現金流出，而是一項帳面成本（book cost），但通過減少應稅所得創造實質的稅盾效益（$\text{稅盾}_k = d_k \times t$）。工程經濟學常用四種折舊方法：直線法（SL）、餘額遞減法（DB，含雙倍加速 DDB）、年數總和法（SYD）及美國稅務強制使用的 MACRS（採用 200% DB 切換 SL 加半年慣例）。各方法分攤同等總量，差異僅在時間分佈——加速法在早年提列較大折舊，其稅盾現值更高，因此在後稅 NPV 分析中更具優勢，這正是貨幣時間價值原則（[[time-value-of-money|TVM]]）的直接應用。稅後現金流公式為 $\text{ATCF}_k = (\text{Revenue}_k - \text{Expense}_k)(1-t) + t \cdot d_k$，折舊方法的選擇直接決定各期 ATCF，並影響項目的後稅 [[irr|IRR]]。特別需要注意的是，邊際稅率（而非平均稅率）才是決定折舊增量稅盾價值的關鍵：在累進稅制下（如香港薪俸稅），若企業未來稅率預期上升，直線法在某些情境下可能優於加速法，此邊際稅率效應是企業資本支出決策中常被忽略的細節。在固定資產財務報表（[[financial-statements|財務報表]]）中，折舊累計額影響資產帳面價值、資產報酬率（ROA）與資產週轉率等 [[financial-ratios|財務比率]]。EEMT5510 L7 以 \$25,000（8 年）與 \$160,000（6 年）設備的詳細稅後現金流表為例，驗證了各折舊方法對後稅 NPV 的影響差異。

## Core Mechanism

**Depreciation** is the systematic allocation of the cost of a tangible asset over its useful life. It is a **book cost** (non-cash charge) that reduces taxable income, thereby creating a **tax shield** — the real cash benefit of depreciation.

### Key Terms

| Term | Definition |
|------|-----------|
| **Cost basis ($B$)** | Total capitalized cost of the asset including purchase price, delivery, installation |
| **Useful life ($N$)** | Estimated service life in years (or units of production) |
| **Salvage value ($SV_N$)** | Estimated value at end of useful life |
| **Book value ($BV_k$)** | Remaining undepreciated value at end of year $k$: $BV_k = B - \sum_{j=1}^{k} d_j$ |
| **Depreciation charge ($d_k$)** | Amount depreciated in year $k$ |
| **Depreciable amount** | $B - SV_N$ (total amount to be depreciated) |

### Property Types

- **Tangible property**: Physical assets (buildings, equipment, vehicles). Depreciable.
  - **Real property**: Land and structures. Land itself is not depreciable.
  - **Personal property**: All tangible property that is not real property.
- **Intangible property**: Non-physical assets (patents, copyrights, goodwill). Subject to **amortization**, not depreciation.

### Eligibility Rules (L7 Ex. 7.1)

An asset qualifies for depreciation only if it: (1) is used for business purposes, (2) has a determinable useful life longer than 1 year, (3) decays, wears out, or loses value over time, and (4) is not inventory or an investment asset. For example, in a pizza business: a baking oven is depreciable; pizza dough and toppings are not (useful life < 1 year); a **leased** delivery van is not (only the owner can claim depreciation); a car used solely for the owner's personal travel is not (not business purpose).

## Depreciation Methods

### Straight-Line (SL) Method

The simplest method — equal annual depreciation charges:

$$d_k = \frac{B - SV_N}{N}$$

$$BV_k = B - k \cdot d_k = B - k \left(\frac{B - SV_N}{N}\right)$$

**Characteristics**: Uniform expense recognition. Easy to compute. Understates early-year economic consumption for assets that lose value quickly.

**Depreciation rate**: $R_{SL} = 1/N$.

### Declining Balance (DB) Method

Applies a constant depreciation rate $R$ to the **current book value** (not the original cost basis):

$$d_k = R \cdot BV_{k-1} = B(1-R)^{k-1} \cdot R$$

$$BV_k = B(1-R)^k$$

Common variants:
- **Double Declining Balance (DDB)**: $R = 2/N$ (200% of straight-line rate)
- **150% Declining Balance**: $R = 1.5/N$

**Characteristics**: Accelerated — larger deductions in early years, smaller later. Never fully depreciates to zero (asymptotic). Often switched to straight-line in later years to fully recover the depreciable amount.

**Switch to SL**: At some year $k^*$, the SL depreciation on the remaining book value exceeds the DB charge. Switch at that point:

$$d_k^{SL} = \frac{BV_{k-1} - SV_N}{N - k + 1}$$

Switch when $d_k^{SL} > d_k^{DB}$.

### Sum-of-Years-Digits (SYD) Method

An accelerated method using a decreasing fraction each year:

$$d_k = \frac{N - k + 1}{\text{SYD}} \times (B - SV_N)$$

where $\text{SYD} = \frac{N(N+1)}{2}$.

$$BV_k = B - \frac{k(2N - k + 1)}{N(N+1)} \times (B - SV_N)$$

**Characteristics**: Accelerated like DB but reaches exactly $SV_N$ at end of life. The depreciation rate decreases linearly: in year 1, the fraction is $N/\text{SYD}$; in year $N$, it is $1/\text{SYD}$.

### L7 Ex. 7.2 — SL Schedule

For $B = \$25{,}000$, $SV_N = \$2{,}000$, $N = 8$ years: $d_k = (25{,}000 - 2{,}000)/8 = \$2{,}875$/year. Book values descend linearly: \$25,000 → \$22,125 → \$19,250 → \$16,375 → \$13,500 → \$10,625 → \$7,750 → \$4,875 → \$2,000.

### L7 Ex. 7.3 — 200% DB Schedule

For $B = \$4{,}000$, $N = 10$, $SV = 0$: $R = 2/10 = 0.2$. Year 1: $d_1 = 4000(0.2) = \$800$, $BV_1 = 3{,}200$. Year 6: $d_6 = 4000(0.8)^5(0.2) = 262.14$, $BV_6 = 4000(0.8)^6 = 1{,}048.58$. By year 10, $BV_{10} = 4000(0.8)^{10} = 429.50$ — the asymptotic tail never reaches zero, motivating a mandatory switch to SL at the optimal year.

### Comparison of Methods

For an asset with $B = \$10{,}000$, $SV_N = \$2{,}000$, $N = 5$ years:

| Year | SL | DDB | SYD |
|------|-----|------|------|
| 1 | \$1,600 | \$4,000 | \$2,667 |
| 2 | \$1,600 | \$2,400 | \$2,133 |
| 3 | \$1,600 | \$1,440 | \$1,600 |
| 4 | \$1,600 | \$160* | \$1,067 |
| 5 | \$1,600 | \$0* | \$533 |
| **Total** | **\$8,000** | **\$8,000** | **\$8,000** |

*DDB switches to SL or stops when BV reaches SV.

All methods depreciate the same total amount ($B - SV_N = \$8{,}000$). Accelerated methods front-load the deductions, producing larger early-year tax shields and higher [[npv|NPV]] of tax savings.

## MACRS (Modified Accelerated Cost Recovery System)

**MACRS** is the US tax depreciation system mandated by the IRS. Key features:

- **Property classes**: 3, 5, 7, 10, 15, 20 years for personal property; 27.5 and 39 years for real property.
- **Half-year convention**: Assets are assumed placed in service at the midpoint of the first year, creating $N+1$ years of deductions for an $N$-year class.
- **GDS (General Depreciation System)**: Uses 200% DB switching to SL for most personal property.
- **ADS (Alternative Depreciation System)**: Uses SL over a longer recovery period.
- **Salvage value**: Always assumed to be zero under MACRS.

Common MACRS property classes:
| Class | Example Assets |
|-------|---------------|
| 3-year | Special manufacturing tools, tractors |
| 5-year | Computers, vehicles, office equipment |
| 7-year | Office furniture, most manufacturing equipment |
| 10-year | Water transportation equipment, petroleum refining |
| 15-year | Land improvements, municipal wastewater |
| 27.5-year | Residential rental property |
| 39-year | Nonresidential real property |

MACRS rates for 5-year property: 20%, 32%, 19.2%, 11.52%, 11.52%, 5.76% (across 6 years due to half-year convention).

## Tax Shield Effect

The real economic benefit of depreciation is the **tax shield**:

$$\text{Tax savings}_k = d_k \times t$$

where $t$ is the marginal tax rate. Accelerated methods produce larger early-year tax shields, which have higher present value. The NPV of tax savings is:

$$NPV_{\text{tax shield}} = t \sum_{k=1}^{N} d_k (P/F, i\%, k)$$

Since the total depreciation is the same regardless of method, the difference lies entirely in timing — and [[time-value-of-money|TVM]] makes earlier deductions more valuable.

## Relationship to Engineering Economy

Depreciation enters engineering economy through **after-tax analysis**:

$$\text{ATCF}_k = (\text{Revenue}_k - \text{Expense}_k)(1-t) + t \cdot d_k$$

where ATCF = After-Tax Cash Flow. The term $t \cdot d_k$ is the tax shield. After-tax NPV is:

$$NPV_{\text{after-tax}} = \sum_{k=0}^{N} \text{ATCF}_k (P/F, i_{\text{after-tax}}\%, k)$$

The choice of depreciation method directly impacts the timing of tax shields and therefore the after-tax NPV and [[irr|IRR]] of a project.

## Worked Example — HW3 Problem 4

A capital asset costs \$120,000 + \$40,000 installation (basis $B = \$160,000$), depreciated straight-line over 6 years to $SV = \$10,000$, so $d_k = (160 - 10)/6 = \$25,000$/year. It generates \$35,000/year revenue with O&M starting at \$8,000 and rising \$1,000/year. After-tax MARR = 12%, effective tax rate $t = 30\%$. At EOY 6 the asset is sold for \$50,000.

| EOY | Before-tax CF | Depreciation | Taxable Income | Tax | ATCF |
|---|---|---|---|---|---|
| 0 | -\$160,000 | — | — | — | -\$160,000 |
| 1 | \$27,000 | \$25,000 | \$2,000 | -\$600 | \$26,400 |
| 2 | \$26,000 | \$25,000 | \$1,000 | -\$300 | \$25,700 |
| 3 | \$25,000 | \$25,000 | 0 | 0 | \$25,000 |
| 4 | \$24,000 | \$25,000 | -\$1,000 | +\$300 | \$24,300 |
| 5 | \$23,000 | \$25,000 | -\$2,000 | +\$600 | \$23,600 |
| 6 | \$72,000 | \$35,000 | \$37,000 | -\$11,100 | \$60,900 |

EOY 6 combines \$22,000 operating cash + \$50,000 salvage; depreciation includes \$10,000 remaining book. Discounted at 12%: $PW = -\$38{,}459$ → **reject**. Notice how the **uniform gradient** pattern on pre-tax cash flows interacts with constant depreciation to produce a symmetric tax pattern.

**No-negative-tax convention**: EEMT5510 solutions impose the rule that **if taxable income is negative, no tax refund is granted** (the tax entry becomes zero, not a positive credit). This is a simplification vs. real-world rules that allow loss carry-forwards or immediate refunds. It flips the sign convention only when TI < 0 and matters most for accelerated methods (DDB, SYD) that may drive TI below zero in early years. The Trionym case (Case Study #2) calls this out explicitly — Trionym "did not recognize negative taxes in their accounting practices" — so students must audit their NPV worksheets against this rule whenever depreciation exceeds the before-tax operating cash flow.

## Tax Shield and Marginal Rates

The marginal tax rate, not the effective rate, drives the incremental value of an extra dollar of depreciation. HK salary tax uses progressive brackets (2%/6%/10%/14%/17% on successive \$50K slices), and income tax on businesses is similarly tiered — so the benefit of an accelerated method depends on whether the firm is in a high or low bracket in the year the deduction is taken. When the marginal rate rises over time (e.g., a growing business), front-loading depreciation may **reduce** total tax savings, creating an edge case where straight-line can beat DDB in after-tax NPV.

## Related Concepts

- [[npv|NPV]] — After-tax NPV depends on depreciation-generated tax shields
- [[irr|IRR]] — After-tax IRR affected by depreciation method choice
- [[time-value-of-money|TVM]] — Why accelerated depreciation is preferred (earlier tax shields)
- [[cvp-analysis|CVP Analysis]] — Depreciation as a fixed cost in breakeven calculations
- [[financial-ratios|Financial Ratios]] — Depreciation affects book value, ROA, and asset turnover
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Financial Engineering and Capital Budgeting)

## Source Materials

- L7 - Depreciation and Income Taxes
- [[wiki/sources/courses/engineering-economics.md|EEMT5510 Engineering Economics and Cost Management]]
