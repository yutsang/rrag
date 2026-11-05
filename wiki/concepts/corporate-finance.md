---
title: "Corporate Finance"
full_name: "Corporate Finance"
type: concept
tags: [finance, corporate-finance, capital-structure]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/fina-financial-management"
confidence: high
---

## 概述

企業財務（Corporate Finance）研究公司面臨的三大核心決策：投資決策（應接受哪些資本預算項目）、融資決策（如何搭配債務與股權以最低成本籌集資金）及股息政策（盈餘應保留再投資還是分配給股東）。Modigliani-Miller（MM）定理以無套利為公理，在完美資本市場下證明資本結構不影響企業總價值（MM I），並推導出財務槓桿如何提高股東的必要回報率（MM II：$r_E = r_0 + (r_0 - r_D)(D/E)$）；引入公司稅後，利息稅盾使負債企業價值等於全股本價值加上稅盾現值（$V_L = V_U + \tau_c D$），但財務困境成本與代理問題形成抗衡力量，催生了最優資本結構的權衡理論。加權平均資本成本 $WACC = \frac{E}{V}r_E + \frac{D}{V}r_D(1-\tau_c)$ 是聯繫資本結構決策與項目評估的關鍵橋樑：它既是 [[npv|NPV]] 分析的折現率，也是 [[irr|IRR]] 與之比較的門檻利率，且通過 CAPM 將 $r_E = R_f + \beta_E(R_M - R_f)$ 連結至 [[portfolio-theory|系統性風險]] 定價。自由現金流定義 $FCF = EBIT(1-\tau) + D\&A - \Delta NWC - CapEx$ 是 DCF 估值模型的核心輸入，終值（以永續增長公式或退出乘數估算）通常佔企業總估值的 60–80%，因此對長期增長率假設高度敏感。代理問題（自由現金流浪費、債務懸空、風險轉移）是公司治理設計的根本動機，股票期權補償、債務契約與獨立董事會監督是三種主要的機制補救方案。在運籌學研究的延伸中，實物期權框架（[[options-pricing|Real Options]]）將 [[stochastic-calculus|隨機微積分]] 的最優停時理論應用於資本預算，為 NPV 靜態分析無法量化的管理彈性（等待、擴張、放棄）提供了定量估值依據。

## What It Is

**Corporate finance** deals with three fundamental decisions firms make:
1. **Investment decision**: which projects to undertake (capital budgeting)
2. **Financing decision**: how to fund those projects (debt vs. equity)
3. **Dividend decision**: how to distribute profits

## Capital Budgeting (Investment Decision)

Tools already covered in engineering economics context:
- **NPV**: invest if $NPV > 0$; sum of discounted cash flows. See [[npv]]
- **IRR**: internal rate of return; invest if $IRR > r_{hurdle}$. See [[irr]]
- **Payback period**: years to recover initial investment — ignores time value, but used for liquidity assessment

**Free Cash Flow (FCF)**: cash available to investors after all investment and working capital needs:
$$FCF = EBIT(1-\tau) + D\&A - \Delta NWC - CapEx$$

**Terminal value**: growing perpetuity $TV = FCF_T(1+g)/(r-g)$ or exit multiple. Dominates DCF value for long-lived projects.

## Capital Structure (Financing Decision)

How should a firm finance its assets — debt (bonds, loans) or equity (shares)?

### Modigliani-Miller (MM) Theorems

**MM Proposition I (no taxes)**: capital structure is irrelevant. The value of the firm is determined by its real assets, not how they are financed. Any combination of debt and equity gives the same total firm value.

*Intuition*: investors can create any desired leverage by borrowing/lending personally ("homemade leverage"). No value created by capital structure.

**MM Proposition II (no taxes)**: cost of equity increases with leverage. $r_E = r_0 + (r_0 - r_D)(D/E)$. Higher leverage → higher financial risk → higher required return on equity.

**With corporate taxes (MM with taxes)**: interest payments are tax-deductible, creating a **tax shield**. Value of levered firm = value of unlevered firm + PV(tax shield).

*Tax shield = $\tau_c \times D$* for permanent debt. This argues for 100% debt — but firms don't do this because of:

### Trade-off Theory

Optimal leverage balances:
- **Benefits**: interest tax shield reduces tax burden
- **Costs**: financial distress costs (direct: bankruptcy legal fees; indirect: lost sales, customer confidence, underinvestment)

**Target leverage**: each firm has an optimal $D/E$ ratio. Utilities (stable cash flows, many tangible assets) carry more debt than tech firms.

### Pecking Order Theory

Firms prefer internal funds → debt → equity (in that order). Information asymmetry: equity issuance signals overvaluation, so managers prefer debt.

## WACC (Weighted Average Cost of Capital)

$$WACC = \frac{E}{V} r_E + \frac{D}{V} r_D (1 - \tau_c)$$

where $V = E + D$, $r_E$ is cost of equity (from CAPM: $r_E = R_f + \beta_E (R_M - R_f)$), $r_D$ is cost of debt (yield to maturity), $\tau_c$ is corporate tax rate.

WACC is the discount rate for **all-equity financed** projects with the same risk as the firm. Used in DCF valuation of the entire firm.

**Engineering connection**: WACC is the hurdle rate used in NPV analysis for corporate capital budgeting — the $r$ in the Cathay Pacific case from EEMT5520.

## Dividend Policy

**MM dividend irrelevance**: with perfect markets, dividend policy doesn't affect firm value (investors can replicate any dividend stream by buying/selling shares).

**In practice**: dividends signal management confidence (signaling theory); sticky dividends — cuts are negative signals; share buybacks more tax-efficient than dividends in many jurisdictions.

## Agency Problems

**Principal-agent problem**: managers (agents) may not act in shareholders' (principals) interests.
- **Free cash flow problem**: managers empire-build with excess cash rather than returning it
- **Debt overhang**: highly levered firms underinvest (gains go to debt holders, losses borne by equity)
- **Risk shifting**: equity holders benefit from upside; debt holders bear downside → moral hazard

**Solutions**: performance-based compensation (stock options), monitoring (board, auditors), debt covenants.

## Connections to OR and Engineering

- WACC = discount rate for [[npv]] and [[irr]] calculations in engineering projects
- Capital structure affects the hurdle rate for investment decisions
- Real options (see [[options-pricing]]) apply derivatives framework to capital budgeting
- [[depreciation]] affects after-tax cash flows and hence project NPV

## Assumptions and Limitations

- **MM theorems require perfect markets**: no taxes, no bankruptcy costs, symmetric information, no agency conflicts. Relaxing each assumption generates a distinct theory (trade-off, pecking order, signaling).
- **WACC as a constant discount rate**: assumes constant capital structure (leverage ratio stays fixed). If leverage changes over the project life, adjusted present value (APV = unlevered NPV + PV of tax shield) is more appropriate.
- **Terminal value dominance**: in DCF, terminal value typically accounts for 60–80% of firm value under a perpetuity assumption; small changes in growth rate $g$ or discount rate $r$ cause large valuation swings.
- **FCF definition sensitivity**: differences in treatment of operating leases (post-IFRS 16), capitalized R&D, and working capital definitions can materially alter FCF and thus DCF value — making cross-firm comparisons unreliable without normalization.

## Related Concepts

- [[npv|Net Present Value]] — Primary capital budgeting criterion; WACC is the discount rate
- [[irr|Internal Rate of Return]] — Compared to WACC as the hurdle rate; same caveats apply (multiple IRRs, scale)
- [[depreciation|Depreciation]] — Affects after-tax FCF via tax shield; MACRS choice matters for project NPV
- [[financial-ratios|Financial Ratios]] — Leverage ratios (D/E, interest coverage) feed into WACC estimation; DuPont links ROE to capital structure
- [[portfolio-theory|Portfolio Theory]] — CAPM provides $r_E = R_f + \beta(R_M - R_f)$; beta estimation from comparable firms
- [[options-pricing|Options Pricing]] — Real options framework; equity as a call option on firm assets (Merton 1974 structural model)
- [[fixed-income|Fixed Income]] — Cost of debt $r_D$ = YTM of firm's bonds; credit spread reflects default risk
- [[cvp-analysis|CVP Analysis]] — Operating leverage (fixed vs. variable cost structure) interacts with financial leverage in total risk assessment
- [[stochastic-calculus|Stochastic Calculus]] — Real options and continuous-time investment timing solved via HJB/optimal stopping
- [[wiki/mocs/operations-research|Operations Research MOC]]
- [[wiki/mocs/financial-engineering|Financial Engineering MOC]]

## Source Materials

- [[wiki/sources/courses/fina-financial-management|FINA2303 Financial Management]]
- [[wiki/sources/courses/fina-business-finance|FINA2203 Business Finance]]
- [[wiki/sources/courses/engineering-economics|EEMT5510 Engineering Economics and Cost Management]]
