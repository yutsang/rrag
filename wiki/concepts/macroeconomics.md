---
title: "Macroeconomics"
full_name: "Macroeconomics"
type: concept
tags: [economics, macroeconomics, finance]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/econ-macroeconomics"
confidence: medium
---

## 概述

宏觀經濟學（Macroeconomics）研究整體經濟的運作規律，核心變量包括 GDP（支出法：$Y = C + I + G + NX$）、通貨膨脹率、失業率及利率，分析財政政策與貨幣政策如何影響總需求與總供給的均衡。IS-LM 模型在商品市場（IS 曲線：$Y = C(Y-T) + I(r) + G$，利率降低刺激投資）與貨幣市場（LM 曲線：貨幣供需均衡）的共同均衡下描述短期經濟動態，並揭示財政政策的「擠出效應」（higher $r$ 抑制私人投資）與貨幣政策的傳導機制。Phillips 曲線 $\pi = \pi^e - \alpha(u - u^*)$ 描述通脹與失業的短期權衡，長期垂直於自然失業率，而泰勒規則 $r = r^* + \phi_\pi(\pi - \pi^*) + \phi_y(Y - Y^*)$ 則提供了中央銀行利率決策的標準化框架。倒掛殖利率曲線（長期利率低於短期利率）是歷史上最可靠的衰退領先指標，直接連結宏觀預測至 [[fixed-income|固定收益]] 分析與 [[portfolio-theory|投資組合理論]] 中的系統性風險計量。在運籌學與商業分析的應用中，GDP 增速、利率水平與消費者信心是需求預測模型（[[arma-models|ARMA]]/[[cointegration|VAR]] 含外生宏觀變量）的關鍵外生輸入，影響 [[supply-chain-management|供應鏈]] 的生產計劃與庫存緩衝設計；匯率與貿易政策則決定全球採購與製造選址的成本結構。宏觀環境同時也是 [[npv|NPV]] 分析中貼現率估計（WACC 的無風險利率成分）的外部錨點，其系統性風險溢酬通過 [[portfolio-theory|CAPM]] 反映在股權資本成本中，形成從宏觀利率環境到微觀項目評估的完整定價鏈。

## National Income Accounting

**GDP (Gross Domestic Product)**: total market value of all final goods and services produced in a country in a period.

**Expenditure approach**: $GDP = C + I + G + NX$
- $C$: Household consumption
- $I$: Business investment (fixed + inventory)
- $G$: Government spending (not transfers)
- $NX = X - M$: Net exports (exports minus imports)

**Income approach**: GDP = wages + profits + rents + interest

**Real vs. nominal GDP**: nominal deflated by price level (GDP deflator). Real GDP growth = economic growth.

## Business Cycles

Output fluctuates around a long-run trend: **expansions** (GDP above trend) and **recessions** (two consecutive quarters of negative real GDP growth).

**Leading indicators**: stock prices, business confidence, yield curve slope (inverted yield curve predicts recession)
**Coincident indicators**: GDP, employment, industrial production
**Lagging indicators**: unemployment rate, bank loans

**Okun's law**: 1% increase in unemployment ↔ ~2% decrease in real GDP.

Cyclicality matters for demand forecasting and [[supply-chain-management]] planning horizons.

## IS-LM Model (Short Run)

**IS curve** (goods market): $Y = C(Y-T) + I(r) + G$. Downward sloping: lower interest rate $r$ → higher investment → higher output $Y$.

**LM curve** (money market): $M/P = L(Y, r)$. Upward sloping: higher $Y$ → higher money demand → higher $r$ to clear money market.

**Equilibrium**: intersection of IS and LM. 

**Fiscal policy** (shift IS): increase $G$ or cut $T$ → IS shifts right → $Y$ and $r$ both rise. **Crowding out**: higher $r$ reduces private investment, partially offsetting fiscal stimulus.

**Monetary policy** (shift LM): central bank increases money supply → LM shifts right → $Y$ rises, $r$ falls. More effective when IS is steep (interest-elastic investment).

## Inflation and the Phillips Curve

**CPI (Consumer Price Index)**: measures cost of a basket of goods. $\pi = (CPI_t - CPI_{t-1})/CPI_{t-1}$.

**Phillips curve**: short-run trade-off between inflation $\pi$ and unemployment $u$: $\pi = \pi^e - \alpha(u - u^*)$

- $\pi^e$: expected inflation
- $u^*$: natural rate of unemployment (NAIRU)
- Short-run: can reduce unemployment by accepting higher inflation
- Long-run: vertical at $u^*$ — no permanent trade-off

**Stagflation** (1970s): high inflation + high unemployment. Caused by supply shocks (oil prices); violated simple Phillips curve.

## Monetary Policy

**Central bank tools**: policy interest rate (Fed Funds rate, HIBOR), reserve requirements, quantitative easing (QE).

**Taylor rule**: $r = r^* + \phi_\pi(\pi - \pi^*) + \phi_y(Y - Y^*)$ — prescribes how much to raise rates in response to inflation and output gaps.

**Transmission mechanism**: policy rate → bank lending rates → investment, housing, consumption → aggregate demand → inflation.

**Zero lower bound**: nominal rates cannot go below zero (or slightly negative). QE (asset purchases) is the alternative when rates are at zero.

## Open Economy

**Exchange rate**: price of one currency in terms of another. Real exchange rate: $q = e \cdot P^*/P$ (competitiveness).

**Purchasing power parity (PPP)**: in the long run, exchange rates adjust so that identical goods cost the same across countries. Used for international GDP comparisons.

**Balance of payments**: current account (trade in goods/services) + capital account (financial flows). Surplus CA = net foreign asset accumulation.

**Mundell-Fleming**: IS-LM extended to open economy. Fixed exchange rate: monetary policy ineffective; flexible: monetary policy very effective.

## Relevance to OR and Business Analytics

- **Demand forecasting**: GDP growth, interest rates, consumer confidence are key exogenous variables in demand models. [[arma-models]] and [[cointegration]] applied to macro time series.
- **Supply chain resilience**: trade policy, exchange rates affect sourcing decisions
- **Interest rates**: discount rate for [[npv]] analysis depends on macroeconomic interest rate environment
- **Financial analytics**: macro factors appear as systematic risk factors in asset pricing models ([[portfolio-theory]])

## Assumptions and Limitations

- **IS-LM is a short-run, closed-economy simplification**: ignores expectations formation (Ricardian equivalence in fiscal policy), capital mobility (Mundell-Fleming for open economies), and supply-side dynamics. New Keynesian DSGE models with rational expectations and price stickiness are the modern replacement for policy analysis.
- **Phillips curve instability**: the short-run trade-off between inflation and unemployment shifted in the 1970s stagflation and again post-2008 when the curve appeared to flatten. Expectations-augmented and non-linear specifications (e.g., kinked Phillips curve) are active research areas.
- **Taylor rule as a description, not a law**: central banks deviate from the rule during crises (ZLB episodes, QE, forward guidance), and the equilibrium real rate $r^*$ is unobserved and time-varying.
- **Aggregate demand models abstract from distributional effects**: GDP growth may coexist with rising inequality; sectoral heterogeneity matters for supply-chain planning even when macro aggregates look stable.

## Related Concepts

- [[microeconomics|Microeconomics]] — Macro aggregates built from micro foundations (consumer optimization, firm production)
- [[arma-models|ARMA Models]] — Macro time series (GDP, CPI, unemployment) modeled as ARIMA; exogenous macro variables feed demand forecasting models
- [[cointegration|Cointegration]] — Long-run macro relationships (PPP, interest rate parity, money-income nexus) tested via Johansen/VECM
- [[garch|GARCH Models]] — Macro uncertainty and financial volatility; conditional variance of macro series used in risk models
- [[time-value-of-money|Time Value of Money]] — Risk-free rate $r_f$ is anchored to the central bank policy rate and macro inflation expectations
- [[financial-ratios|Financial Ratios]] — Firm-level ratios are sensitive to macro cycle; interest coverage deteriorates in recessions
- [[behavioral-economics|Behavioral Economics]] — Animal spirits, consumer confidence, and fiscal multiplier magnitude depend on behavioral responses to policy
- [[fixed-income|Fixed Income]] — Yield curve shape driven by monetary policy expectations; macro forecasting is core to fixed income strategy
- [[portfolio-theory|Portfolio Theory]] — Macro factors (GDP growth, inflation, credit spreads) appear as systematic risk premia in multi-factor asset pricing models
- [[supply-chain-management|Supply Chain Management]] — Trade policy, exchange rates, and business cycle affect sourcing decisions and safety-stock requirements
- [[wiki/mocs/operations-research|Operations Research MOC]]

## Source Materials

- [[wiki/sources/courses/econ-macroeconomics|ECON2123 Macroeconomic Theory]]
- [[wiki/sources/courses/econ-introductory-economics|ECON2103 Introductory Economics]]
- [[wiki/sources/courses/financial-time-series|MSBD5006 Quantitative Analysis of Financial Time Series]]
