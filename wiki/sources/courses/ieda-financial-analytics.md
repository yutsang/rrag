---
title: "IEDA 4510 System Risk Management"
full_name: "IEDA 4510: System Risk Management"
type: source
tags: [courses, ieda, undergraduate, finance, risk-management, quantitative, ieda4510, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA4510/IEDA_4510_syllabus_2022.pdf"
confidence: high
author: "Shuoguang Yang"
date_published: "2022-01-01"
---

## 概述

IEDA 4510「系統風險管理」是香港科技大學 IEDA 學系四年級本科生的選修課，由楊碩光教授於 2022 年春季主講，前置要求為基礎財務與概率知識，採用 Hull 的《Risk Management and Financial Institutions》（第 5 版，Wiley）為主要教材，評核方式為作業（20%）、期中（30%）及期末考試（50%）。課程聚焦於金融機構的風險量化與控制，系統涵蓋金融機構類型（商業銀行、投資銀行、保險公司、對沖基金）與交易帳簿 vs. 銀行帳簿的監管區別；市場風險度量（VaR 的歷史模擬法、方差-協方差參數法及蒙地卡羅法、預期短缺 ES/CVaR 的一致性優勢、GARCH(1,1) 波動率模型與 EWMA RiskMetrics、回溯測試 Basel 交通燈系統）；監管框架（Basel I/II/III 資本充足率、三大支柱、CET1 要求、FRTB 以 ES 取代 VaR）；以及信用風險（違約概率 PD、違約損失率 LGD、違約敞口 EAD、Merton 結構模型、CDS 信用違約互換、CDO 分層結構產品）。課程亦介紹對手方信用風險（CVA）及波動率聚集現象對 GARCH 建模的理論依據，與 IEDA 3330/4331（金融衍生品）及 MSBD5006（金融時間序列）形成緊密的知識鏈，是量化金融與風險研究方向的重要本科選修。

## Course Overview

**IEDA 4510 System Risk Management** (Spring 2022, Prof. Shuoguang Yang) covers the basic concepts of financial risk and provides analytical approaches to quantify and control various types of risk in finance, with a focus on risks within financial institutions. Risk management has drawn tremendous attention across industries following major crises (2008 financial crisis, LTCM collapse, etc.).

**Prerequisites**: Basic understanding of finance and probability.  
**Textbook**: Hull, J.C., *Risk Management and Financial Institutes*, 5th Ed., Wiley.

## Topics Covered

| Topic | Description |
|-------|-------------|
| Financial institutions and trading | Bank types, trading books, market makers |
| Market risk | VaR, ES, volatility models |
| Regulation | Basel I/II/III, capital requirements |
| Credit risk | Default models, credit derivatives |

## Key Topics

### Financial Institutions and Trading

**Types of financial institutions**:
- **Commercial banks**: take deposits, make loans; regulated by central banks and deposit insurance schemes.
- **Investment banks**: underwriting, M&A advisory, proprietary trading, market making.
- **Insurance companies**: underwrite risks; investment portfolios must match liability duration.
- **Hedge funds**: leveraged strategies; less regulated; performance fee structure.

**Trading book vs. banking book**: the trading book contains positions marked to market daily (derivatives, securities); the banking book contains loans held to maturity. Capital requirements differ substantially between the two.

**Market making**: dealers post bid and ask prices; profit from the bid-ask spread while managing inventory risk. Delta-hedging (see IEDA 4331) is the primary tool.

### Market Risk

**Value at Risk (VaR)**: the loss not exceeded with probability 1−α over a horizon Δt. VaR_{α}(ΔP) = −inf{x : P(ΔP ≤ x) ≥ α}.

Three approaches:
1. **Historical simulation**: sort past P&L scenarios; take the α-quantile. Non-parametric; captures fat tails and correlations automatically.
2. **Variance-covariance (parametric)**: assume ΔP ~ N(μ, σ²); VaR = μ − z_α σ. Fast; fails for non-normal returns.
3. **Monte Carlo simulation**: simulate future price paths from a model; compute P&L distribution.

**Expected Shortfall (ES / CVaR)**: ES_α = E[−ΔP | ΔP < −VaR_α]. ES is coherent (satisfies subadditivity); VaR is not. Basel III shifted from VaR to ES for trading book capital.

**Volatility modeling**: financial returns exhibit **volatility clustering** — large moves follow large moves. The [[wiki/concepts/garch|GARCH]] model (Bollerslev, 1986) captures this: σ²_t = ω + α ε²_{t-1} + β σ²_{t-1}. EWMA (RiskMetrics) is a special case with ω=0, α+β=1.

**Backtesting**: test whether VaR exceptions (actual losses exceeding VaR) occur at the nominal frequency. Basel traffic-light system: green (0–4 exceptions/year), yellow (5–9), red (10+). Kupiec test and Christoffersen test for independence of exceptions.

### Regulation: Basel Framework

**Basel I** (1988): minimum capital ratio = 8% of risk-weighted assets (RWA). Simple risk weights by asset class.

**Basel II** (2004): three pillars:
1. Minimum capital requirements (more risk-sensitive; internal models allowed).
2. Supervisory review.
3. Market discipline (disclosure).

**Basel III** (2010, post-GFC): strengthened capital (higher quality Tier 1 capital, higher ratios), introduced liquidity requirements (LCR, NSFR), and leverage ratio. Fundamental Review of the Trading Book (FRTB) replaced VaR with ES and tightened internal model approval.

**Capital adequacy**: Total capital / RWA ≥ 8%. Capital quality hierarchy: Common Equity Tier 1 (CET1) → Additional Tier 1 → Tier 2. CET1 must be ≥ 4.5% of RWA under Basel III.

### Credit Risk

**Default risk**: the risk that a counterparty fails to meet its obligations. Key metrics:
- **Probability of Default (PD)**: estimated from historical default rates (rating agencies) or structural models (Merton).
- **Loss Given Default (LGD)**: 1 − recovery rate.
- **Exposure at Default (EAD)**: outstanding balance at time of default.
- Expected loss: EL = PD × LGD × EAD.

**Merton model** (structural approach): firm defaults when asset value V_A falls below debt face value D at maturity. Equity = call option on firm assets: E = V_A N(d₁) − De^{−rT} N(d₂). Firm asset volatility σ_A estimated from equity volatility using Black-Scholes relationships.

**Credit derivatives**:
- **Credit Default Swap (CDS)**: protection buyer pays periodic fee; receives face value minus recovery upon default. CDS spread reflects market-implied PD.
- **Collateralized Debt Obligations (CDOs)**: tranche structured products on pools of loans. Senior tranches have low PD but suffered in 2008 due to correlation underestimation.

**Counterparty credit risk (CCR)**: for derivatives, EAD is stochastic (depends on future market prices). CVA (Credit Valuation Adjustment) = present value of expected credit losses on a derivatives portfolio.

### Connections to Time Series Methods

Volatility estimation and forecasting connects to [[wiki/concepts/garch|GARCH]] and [[wiki/concepts/arma-models|ARMA Models]]:
- GARCH(1,1) is standard for daily VaR volatility.
- Long-memory GARCH (FIGARCH) for persistence.
- **Cointegration** in multi-asset portfolios: cointegrated asset pairs have stable long-run relationships; pairs trading strategies exploit deviations. See [[wiki/concepts/cointegration|Cointegration]].

### Connections to Financial Ratios

Regulatory ratios are a form of [[wiki/concepts/financial-ratios|Financial Ratios]]:
- **Capital adequacy ratio (CAR)**: Total Capital / RWA.
- **Leverage ratio**: Tier 1 Capital / Total Exposure.
- **Liquidity Coverage Ratio (LCR)**: High-Quality Liquid Assets / Net Cash Outflows over 30 days ≥ 100%.

## Related Concepts

- [[wiki/concepts/garch|GARCH]] — volatility modeling for market risk
- [[wiki/concepts/arma-models|ARMA Models]] — time series foundations for risk models
- [[wiki/concepts/cointegration|Cointegration]] — long-run relationships in financial markets
- [[wiki/concepts/financial-ratios|Financial Ratios]] — regulatory capital ratios
- [[wiki/concepts/linear-regression|Linear Regression]] — factor models for market risk

## Source Materials

- raw/courses/IEDA/IEDA4510/IEDA_4510_syllabus_2022.pdf
