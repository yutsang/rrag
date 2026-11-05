---
title: "Financial Derivatives"
full_name: "IEDA3330 Financial Derivatives"
type: source
tags: [courses, ieda, undergraduate, finance, derivatives, ieda3330, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3330"
confidence: medium
---

## 概述

IEDA 3330「金融衍生工具」是香港科技大學 IEDA 學系三年級本科生的選修課，在工業工程課程中屬於較不尋常的金融工程取向科目，充分利用學生已具備的微積分與概率基礎。課程系統涵蓋遠期合約（無套利定價、持有成本模型）、期貨（逐日結算、基差、套期保值）、利率互換（固定換浮動、以債券組合估值）及期權（買賣期權到期收益、買賣平價 Put-Call Parity）。定價方法方面，重點介紹二項式期權定價樹（風險中性概率 q、CRR 參數化 u = e^{σ√Δt}、美式期權回溯歸納）及 Black-Scholes 模型（GBM 假設、歐式期權公式、Greeks：Delta/Gamma/Theta/Vega/Rho、Delta 對沖、隱含波動率與波動率微笑）。課程揭示 OR 的動態規劃後向歸納與二項式定價樹在數學結構上完全一致，為學生展示 OR 方法在金融工程中的普適性。修讀本課為後續 IEDA 4331（進階衍生品 OR 專題）及 IEDA 4510（系統風險管理）提供必要的衍生品理論基礎，亦是財務工程研究方向的重要入門。

## Course Overview

IEDA3330 is an unusual course for an IEDA program — it brings financial derivatives into the IE curriculum, reflecting the HKUST IEDA department's quantitative finance track. The course uses IEDA students' strong calculus and probability background to cover derivatives rigorously.

## Key Topics

### Derivatives Overview
- Forward contracts: long/short payoffs, forward price = $S_0 e^{rT}$, cost of carry
- Futures contracts: marking-to-market, basis, convergence, hedging with futures
- Swaps: interest rate swaps (fixed-for-floating), currency swaps, valuation as bond portfolio

### Options
- Call and put payoffs; moneyness (in/at/out of the money)
- Put-call parity: $C - P = S_0 - Ke^{-rT}$
- Bounds on option prices: intrinsic value, time value
- Early exercise: American call on non-dividend stock never optimal; puts may be

### Binomial Option Pricing
- One-period model: risk-neutral probabilities $q = (e^{r\Delta t} - d)/(u - d)$
- Risk-neutral valuation: price = discounted expected payoff under $q$
- Multi-period trees: backward induction
- American options on trees: compare hold vs. exercise at each node
- CRR parameterization: $u = e^{\sigma\sqrt{\Delta t}}$

### Black-Scholes Model
- GBM stock price assumption: $dS = \mu S dt + \sigma S dW_t$
- Black-Scholes formula for European calls and puts
- Greeks: delta, gamma, theta, vega, rho
- Delta hedging: maintaining delta-neutral portfolio
- Implied volatility; volatility smile/skew

### Applications
- Hedging with options: protective put, covered call, collar strategies
- Financial crisis case: how derivatives contributed to systemic risk (ABCP, CDOs)
- Real options thinking: investment decisions as options (option to delay, expand, abandon)

## Connections to IEDA Curriculum

This course connects IEDA's OR methods (dynamic programming in binomial trees) with financial engineering. The same DP backward induction used in IEDA3010 appears in option pricing — reinforcing the universality of OR methodology.

## Related Concepts

- [[options-pricing]]
- [[stochastic-calculus]]
- [[time-value-of-money]]
- [[garch]]
- [[corporate-finance]]
- [[portfolio-theory]]
