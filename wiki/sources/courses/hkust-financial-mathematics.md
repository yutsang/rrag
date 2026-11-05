---
title: "HKUST Financial Mathematics"
full_name: "HKUST Financial Mathematics (MATH4424/4514)"
type: source
tags: [courses, math, undergraduate, financial-math, derivatives, stochastic-calculus, math4424, math4514, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH/MATH4424"
confidence: medium
---

## 概述

MATH4424 金融數學與 MATH4514 金融計算為香港科技大學數學系四年級學生提供量化金融的完整訓練，涵蓋無套利定價理論、隨機微積分及數值定價方法，先修要求為 MATH4432 隨機過程及 MATH2351 常微分方程。MATH4424 以 Shreve《隨機微積分與金融》或 Hull《期權、期貨及其他衍生品》為參考教材，從二項式模型出發建立風險中性定價的直覺，繼而以 Itô 公式、Girsanov 定理及 Feynman-Kac 定理嚴格推導 Black-Scholes 方程；MATH4514 側重數值方法，教授 CRR 二叉樹、有限差分格式（顯式、隱式、Crank-Nicolson）及 Monte Carlo 模擬等計算技術。學生完成課程後能夠推導 Black-Scholes 公式及其 Greeks、建立利率短期模型（Vasicek、CIR）、對奇異期權進行定價，並在 Python 或 MATLAB 中實現數值定價演算法。本課程是量化分析師（Quant）的核心技術培訓，亦與運籌學中的隨機最優控制（Hamilton-Jacobi-Bellman 方程）及金融風險管理實踐緊密相連。

## Course Structure

| Course | Content |
|---|---|
| MATH4424 | Financial Mathematics (analytic methods) |
| MATH4514 | Financial Computation (numerical methods) |

## Key Topics

### MATH4424: Financial Mathematics

**No-Arbitrage Foundations**:
- One-period binomial model; replicating portfolios; risk-neutral pricing
- Fundamental theorems of asset pricing:
  1. No arbitrage ↔ existence of risk-neutral measure $\mathbb{Q}$
  2. Completeness ↔ uniqueness of $\mathbb{Q}$
- Change of measure: Radon-Nikodym derivative; Girsanov's theorem

**Continuous-Time Stochastic Calculus**:
- Brownian motion $W_t$; filtrations; adapted processes
- Itô's formula: $df(W_t) = f'(W_t)\,dW_t + \frac{1}{2}f''(W_t)\,dt$
- Stochastic differential equations (SDEs): existence, uniqueness, Euler-Maruyama scheme
- Feynman-Kac theorem: connects PDEs to expectations of diffusion processes

**Black-Scholes Framework**:
- GBM model: $dS = \mu S\,dt + \sigma S\,dW$
- Black-Scholes PDE derivation via delta hedging and Itô's lemma
- Black-Scholes formula: $C = S_0 N(d_1) - Ke^{-rT}N(d_2)$
- Greeks: $\Delta, \Gamma, \Theta, \mathcal{V}, \rho$ — see [[options-pricing]]
- Put-call parity; dividends; American options (early exercise boundary)

**Interest Rate Models**:
- Short-rate models: Vasicek, CIR, Hull-White; affine term structure
- HJM framework: forward rate dynamics
- Bond pricing PDE; zero-coupon bond formula in Vasicek model — see [[fixed-income]]

**Exotic Options and Derivatives**:
- Barrier options: knock-in/knock-out, reflection principle pricing
- Asian options: arithmetic/geometric average
- Lookback options; digital/binary options
- Variance swaps; volatility surface; local volatility (Dupire's equation)

### MATH4514: Financial Computation

**Numerical Methods for Option Pricing**:
- Binomial trees: CRR (Cox-Ross-Rubinstein) parameterization; convergence to BS
- Finite-difference methods: explicit, implicit, Crank-Nicolson schemes for BS PDE
- Monte Carlo simulation: GBM path simulation; variance reduction (antithetic, control variates)
- Quasi-Monte Carlo: low-discrepancy sequences (Sobol, Halton)

**Calibration and Estimation**:
- Implied volatility: Newton-Raphson root finding; volatility smile/skew
- Maximum likelihood for SDEs; discrete-time approximations
- GARCH estimation — see [[garch]]

## Connections Across Wiki

- Black-Scholes derivation uses [[stochastic-calculus]] (Itô's lemma) and [[differential-equations]] (parabolic PDE)
- Risk-neutral pricing unifies [[options-pricing]] concept page
- Numerical methods connect to [[algorithms-and-data-structures]] (numerical linear algebra)
- Fixed income models connect to [[fixed-income]] concept page

## Related Concepts

- [[stochastic-calculus]]
- [[options-pricing]]
- [[fixed-income]]
- [[portfolio-theory]]

## Source Materials

- MATH4424 Course Materials
