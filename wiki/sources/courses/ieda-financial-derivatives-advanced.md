---
title: "IEDA 4331 Advanced Topics in OR: Financial Derivatives"
full_name: "IEDA 4331: Advanced Topics in Operations Research — Financial Derivatives"
type: source
tags: [courses, ieda, undergraduate, finance, derivatives, options, stochastic, ieda4331, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA4331/2019-2020 Fall/"
confidence: medium
author: "Wei Jiang"
date_published: "2019-09-01"
---

## 概述

IEDA 4331「作業研究進階專題：金融衍生品」是香港科技大學 IEDA 學系四年級本科生的進階選修課，由江威教授於 2019–2020 年秋季主講，以 IEDA 3330（金融衍生工具）為前置。課程以運籌學方法深入金融工程，涵蓋無套利遠期定價（含儲存成本與便利收益）、利率互換（固定端現值匹配定價）、Black-Scholes 模型（GBM 假設、歐式期權公式、Greeks：Delta/Gamma/Vega 的計算與對沖應用、平值期權近似公式推導）、二項樹（風險中性概率、CRR 參數化 u = e^{σ√Δt}、美式期權回溯歸納）及三項樹（對障礙期權的精度優勢）。課程以 Python 實作 Black-Scholes 公式、二項樹與三項樹定價，並實作有限差分法（顯式與 Crank-Nicolson 隱式格式）求解 Black-Scholes PDE。期末大型專案要求學生以港交所即時數據（匯豐 00005.HK 期權鏈、HV30 歷史波動率、香港一年期國債收益率）對比三種定價方法，體現 OR 數值方法在真實金融市場的應用。課程亦介紹 VaR（在險價值）及 Delta-Gamma-Vega 中性投資組合構建，與 IEDA 4510（系統風險管理）形成緊密銜接。

## Course Overview

**IEDA 4331 Advanced Topics in OR** (2019–2020 Fall, Instructor: Wei Jiang) focuses on financial derivatives pricing as an application of Operations Research methods. The course demonstrates how no-arbitrage arguments, stochastic processes, and numerical methods from OR intersect in financial engineering.

No dedicated syllabus was found; course content is reconstructed from homework sets (HW 1–5), the final project, and project binomial/PDE materials.

## Key Topics

### Forward Contracts and No-Arbitrage Pricing (HW 1)

**Forward price** for a commodity with storage cost c(j) and convenience yield y(j):

$$F = \frac{S}{d(0,M)} + \sum_{j=0}^{M-1} \frac{c(j) - y(j)}{d(j,M)}$$

where d(j,M) is the discount factor from period j to M. This is derived by no-arbitrage: any deviation allows a riskless profit.

**Put option lower bound**: by no-arbitrage, p ≥ (Ke^{−rT} − S₀)⁺. Proof uses the put-call parity framework.

**Interest rate swaps**: in a plain-vanilla swap, firm A pays fixed leg NX and receives floating leg Nr_{t−1}. Given discount factors d(0,1), d(0,2), d(0,3), the fair fixed rate X is determined by equating present values of fixed and floating legs.

### Option Pricing: Black-Scholes Model

The **Black-Scholes formula** prices European options under the assumption that the underlying stock follows geometric Brownian motion dS = μS dt + σS dW:

- Call: C = S₀N(d₁) − Ke^{−rT}N(d₂)
- Put: P = Ke^{−rT}N(−d₂) − S₀N(−d₁)

where d₁ = [ln(S₀/K) + (r + σ²/2)T] / (σ√T) and d₂ = d₁ − σ√T.

**At-the-money approximation** (HW final project): when S_t = K and r = 0, T − t small:

$$c_t \approx \sigma S_t \sqrt{\frac{T-t}{2\pi}}$$

Derived by Taylor-expanding N(d₁) around zero since d₁ ≈ 0 when at-the-money and e^{−x²/2} ≈ 1 for small x.

**Greeks**: sensitivities of option price to model parameters:
- **Delta** (Δ = ∂C/∂S): rate of change with stock price; used for delta-hedging.
- **Gamma** (Γ = ∂²C/∂S²): rate of change of delta; measures convexity of option payoff.
- **Vega** (ν = ∂C/∂σ): sensitivity to volatility.

**Delta-Gamma-Vega neutral portfolio**: given a portfolio of options with known (Δ, Γ, ν), use traded options and futures to make all three Greeks simultaneously zero. This requires solving a system of linear equations.

### Binomial Tree Method (Project)

The **binomial tree** discretizes the stock price process into up (u) and down (d) moves per period. Under **risk-neutral pricing**, the up-move probability is:

$$p^Q = \frac{e^{r\Delta t} - d}{u - d}$$

where u and d are matched to the historical volatility: u = e^{σ√Δt}, d = 1/u.

Option price = discounted expectation under Q: V_t = e^{−rΔt}[p^Q V_{t+1,u} + (1−p^Q)V_{t+1,d}].

American options are handled by comparing continuation value with early exercise value at each node.

Convergence: as N → ∞ (more periods), binomial price → Black-Scholes price.

### Trinomial Tree Method (Project)

The **trinomial tree** adds a middle (unchanged) node to each period:
- Stock moves up (×u), unchanged (×1), or down (×d).
- The parameter λ controls the width of the tree.
- Three risk-neutral probabilities (p_u, p_m, p_d) are matched to mean and variance of the log-price process.

Advantages over binomial: faster convergence for a given number of time steps; better suited for barrier options (the middle node can align with the barrier level).

**Barrier options**: options that activate (knock-in) or expire (knock-out) when the stock price crosses a barrier H. The trinomial tree's extra node allows aligning a tree level with H, dramatically improving accuracy.

### Numerical PDE Methods

Black-Scholes PDE: ∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S − rV = 0.

**Finite difference methods**:
- **Explicit scheme**: solve forward in time; conditionally stable.
- **Implicit scheme** (Crank-Nicolson): solve backward; unconditionally stable; second-order accurate.

Students implement these methods in Python and compare with Black-Scholes analytical results and binomial/trinomial tree prices.

### Risk Management Applications

**Portfolio delta-neutralization with futures**: a futures contract on the stock has delta e^{−r(T-t)} (not 1) due to marking-to-market. The number of futures contracts needed to delta-hedge a portfolio of options is computed accordingly.

**VaR (Value at Risk)**: probability-based risk measure — the loss not exceeded with probability 1−α over a holding period. Connects to the IEDA 4510 (System Risk Management) course material.

## Project: Pricing HSBC Exchange-Traded Options

Students price real HSBC (00005.HK) options using:
1. Live data from HKEX (stock price, option chain, HV30 volatility).
2. Hong Kong 1-year bond yield as the risk-free rate.
3. Three methods: Black-Scholes formula, binomial tree (N=10, 50, 100), trinomial tree.
4. Compare results and discuss differences.

This integrates Python implementation, financial data retrieval, and model validation.

## Related Concepts

- [[wiki/concepts/arma-models|ARMA Models]] — time series models for volatility estimation
- [[wiki/concepts/garch|GARCH]] — volatility modeling relevant to option pricing
- [[wiki/concepts/financial-ratios|Financial Ratios]] — fundamental analysis context
- [[wiki/concepts/time-value-of-money|Time Value of Money]] — discounting and present value foundations

## Source Materials

- raw/courses/IEDA/IEDA4331/2019-2020 Fall/HW/HW 1.pdf
- raw/courses/IEDA/IEDA4331/2019-2020 Fall/Project/Final_project.pdf
- raw/courses/IEDA/IEDA4331/2019-2020 Fall/Project/project_binomial.pdf
- raw/courses/IEDA/IEDA4331/2019-2020 Fall/Project/project_bs_pde.pdf
