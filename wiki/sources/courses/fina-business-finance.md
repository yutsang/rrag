---
title: "Business Finance"
full_name: "FINA2203 Business Finance"
type: source
tags: [courses, fina, undergraduate, corporate-finance, capital-budgeting, fina2203, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/FINA/FINA2203"
confidence: medium
---

## 概述

FINA2203 企業財務為金融學專業二年級學生提供公司財務決策的核心理論框架，以 Brealey、Myers 及 Allen《公司財務原則》（Principles of Corporate Finance，McGraw-Hill 標準教材）為主要教材，先修要求為 ACCT2010 會計學原理及 ECON2103 經濟學概論。課程圍繞企業財務的三大核心決策組織：投資決策（NPV 法則與 IRR 的衝突分析、自由現金流估算）、融資決策（Modigliani-Miller 無稅命題與含稅資本結構最優化、WACC 計算）及股利決策（MM 股利無關命題與信號理論）。學生完成課程後能夠建構資本預算模型（含沉沒成本、機會成本及側面效應的識別）、估算加權平均資本成本（WACC）、分析槓桿對股東回報的放大效應，以及運用情境分析與 Monte Carlo 模擬評估項目風險。課程的實物期權框架（擴張、放棄、延遲選擇權）將金融期權定價思維引入資本預算，是量化風險管理研究的重要橋梁；運營資金管理章節中的 Baumol 現金餘額模型亦直接連結運籌學的庫存優化理論。

## Course Overview

**Textbook**: Brealey, Myers & Allen, *Principles of Corporate Finance* (standard edition)

Core corporate finance course covering the three key financial decisions:
1. **Investment decision**: capital budgeting — which projects to take?
2. **Financing decision**: capital structure — debt vs. equity mix?
3. **Dividend decision**: payout policy — cash dividends vs. buybacks?

## Key Topics

### Time Value of Money (Applications)
- NPV rule: invest when NPV > 0; see [[npv]]
- IRR and conflicts with NPV; see [[irr]]
- Annuities, perpetuities; EAC (equivalent annual cost) for unequal lives

### Capital Budgeting
- Free cash flow (FCF) estimation: incremental after-tax cash flows
- Sunk costs vs. opportunity costs; cannibalization effects
- Sensitivity analysis; scenario analysis; Monte Carlo simulation
- Real options: option to expand, abandon, delay — see [[options-pricing]]

### Risk and Return
- Portfolio diversification: systematic vs. unsystematic risk
- Beta: measure of market sensitivity; estimation from regression
- CAPM: $E[R] = R_f + \beta(E[R_m] - R_f)$; see [[portfolio-theory]]
- Fama-French 3-factor model: market, size (SMB), value (HML)

### Cost of Capital
- WACC: $r_{WACC} = \frac{E}{E+D}r_E + \frac{D}{E+D}r_D(1-\tau)$
- Cost of equity: CAPM; dividend growth model
- Adjusting beta for leverage: Hamada equation

### Capital Structure
- Modigliani-Miller propositions I and II (without taxes): capital structure irrelevance
- With corporate taxes: tax shield value = $\tau D$; optimal leverage
- Costs of financial distress; trade-off theory
- Pecking order theory: asymmetric information and adverse selection
- See [[corporate-finance]]

### Dividend Policy
- MM dividend irrelevance proposition
- Signaling theory: dividends signal cash flow quality
- Share repurchases: tax efficiency vs. dividends; buyback mechanics
- Lintner's model: smoothing dividend adjustments

### Working Capital Management
- Cash conversion cycle: DIO + DSO − DPO
- Optimal cash balance: Baumol model, Miller-Orr model
- Accounts receivable management; trade credit
- Inventory management basics — see [[newsvendor-problem]]

## Related Concepts

- [[npv]]
- [[irr]]
- [[portfolio-theory]]
- [[corporate-finance]]
- [[options-pricing]]

## Source Materials

- FINA2203 Course Materials
