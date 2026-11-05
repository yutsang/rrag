---
title: "Investments"
full_name: "FINA3103 Investments"
type: source
tags: [courses, fina, undergraduate, investments, portfolio-management, asset-pricing, fina3103, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/FINA/FINA3103"
confidence: medium
---

## 概述

FINA3103 投資學為金融學專業三年級學生提供資產定價理論與投資組合管理的系統訓練，以 Bodie、Kane 與 Marcus《投資學》（Investments，McGraw-Hill 標準教材）為主要教材，先修要求為 FINA2203 企業財務及 ISOM2500/MATH2411 統計學。課程以 Markowitz 均值-方差框架為理論核心，嚴格推導有效前沿、最小方差組合及切線組合（最大 Sharpe 比率組合），並在此基礎上建立 CAPM 的均衡定價邏輯（安全市場線、β 估計）、Ross 的套利定價理論（APT）及 Fama-French 三因子、Carhart 四因子模型。固定收益分析章節深入存續期間（Macaulay、Modified）、凸性與債券免疫策略；衍生品章節介紹保護性看跌期權、備兌看漲期權等投資組合保護策略。學生完成課程後能夠構建最優化多資產組合、估算個股 α 與 β、解讀投資績效歸因（Brinson-Hood-Beebower 框架）、評估市場效率的實證異象（規模效應、動量效應），以及利用 Sharpe、Treynor 及 Jensen α 等指標評估基金管理績效，是量化投資研究與 CFA 考試備考的重要學術基礎。

## Course Overview

**Textbook**: Bodie, Kane & Marcus, *Investments* (standard FINA upper-level text)

Covers asset pricing theory, portfolio construction, and the practical mechanics of equity, fixed income, and derivative analysis.

## Key Topics

### Portfolio Theory
- Mean-variance framework: $E[R_p] = \sum w_i E[R_i]$; $\sigma^2_p = \mathbf{w}^T \Sigma \mathbf{w}$
- Efficient frontier; minimum variance portfolio; tangency portfolio
- Two-fund separation theorem; role of the risk-free asset
- Capital Market Line (CML); Sharpe ratio maximization
- See [[portfolio-theory]]

### Asset Pricing Models
- **CAPM**: $E[R_i] = R_f + \beta_i(E[R_m]-R_f)$; security market line (SML)
- Beta estimation: OLS regression of excess returns on market; Blume adjustment
- **APT** (Ross 1976): $E[R_i] = R_f + \sum_k \beta_{ik} \lambda_k$; absence of arbitrage pricing
- **Fama-French 3-Factor**: market, SMB (size), HML (value)
- **Carhart 4-Factor**: adds momentum (WML — winners minus losers)

### Equity Analysis
- Intrinsic value models: Gordon Growth Model (DDM), FCFE discount
- Relative valuation: P/E, P/B, EV/EBITDA multiples — see [[financial-ratios]]
- Fundamental analysis: analyzing financial statements for investment signals
- Technical analysis: price momentum, moving averages, RSI (efficient market critique)

### Fixed Income Analysis
- Bond pricing: YTM, current yield; price-yield relationship
- Duration (Macaulay, Modified): $D_{mod} = \frac{D_{Mac}}{1+y}$; convexity
- Bond immunization: duration matching to hedge interest rate risk
- Yield curve: theories (expectations, liquidity premium, segmented markets)
- Spread analysis: credit spread, OAS (option-adjusted spread) — see [[fixed-income]]

### Market Efficiency
- EMH: weak, semi-strong, strong forms
- Anomalies: size effect, value effect, momentum, low-volatility; behavioral explanations
- Limits to arbitrage: fundamental risk, noise trader risk, holding costs
- Behavioral finance: overconfidence, anchoring, mental accounting — see [[behavioral-economics]]

### Derivatives in Portfolio Management
- Protective put; covered call (collar); synthetic positions
- Index futures: hedging beta; adjusting portfolio duration
- Options-based strategies: straddles, spreads — see [[options-pricing]]

### Performance Evaluation
- Risk-adjusted returns: Sharpe ratio, Treynor ratio, Jensen's alpha, Information ratio
- Attribution analysis: Brinson-Hood-Beebower framework (asset allocation vs. security selection)
- Style analysis: returns-based style boxes (Sharpe's approach)

## Related Concepts

- [[portfolio-theory]]
- [[fixed-income]]
- [[options-pricing]]
- [[financial-ratios]]
- [[behavioral-economics]]

## Source Materials

- FINA3103 Course Materials
