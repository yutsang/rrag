---
title: "Options Pricing"
full_name: "Options Pricing and Financial Derivatives"
type: concept
tags: [finance, derivatives, options-pricing, stochastic-calculus]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/fina-investments"
confidence: high
---

## 概述

期權定價理論（Options Pricing）建立在無套利原則與 [[stochastic-calculus|隨機微積分]] 的基礎上，以 Black-Scholes-Merton（1973）模型為核心成就。Black-Scholes 公式 $C = S_0 N(d_1) - Ke^{-rT}N(d_2)$ 的推導路徑是：假設標的資產遵循幾何布朗運動 $dS = \mu S\,dt + \sigma S\,dW_t$，對期權價格 $C(t, S_t)$ 應用伊藤引理，構建 Delta 中性對沖組合消去隨機項，再由無套利條件——無風險組合只能賺取無風險利率——導出 BS 偏微分方程，其解析解即為上述公式。二項式樹模型（Cox-Ross-Rubinstein, 1979）提供等價的離散時間框架，風險中性概率 $q = (e^{r\Delta t} - d)/(u - d)$ 的推導與 BS 一致，並自然處理美式期權的提前行使（於每節點比較持有價值與行使價值取最大值）。希臘字母（Delta、Gamma、Vega、Theta、Rho）量化期權價格對各輸入變量的偏導數，是交易員動態對沖（Delta-Gamma hedging）的操作語言；隱含波動率則是從市場價格反推的 $\sigma$，其隨執行價格的波動微笑/偏斜結構反映了 BS 固定波動率假設的局限。在運籌學中，期權定價與最優停時問題（Optimal Stopping）等價：美式期權行使問題是求解最優停時 $\tau^* = \inf\{t : V(t, S_t) = (S_t - K)^+\}$ 的隨機控制問題，由 Hamilton-Jacobi-Bellman 方程描述；實物期權分析（Real Options）將相同框架用於資本預算，「等待投資的期權」、「擴張期權」與「放棄期權」為 [[npv|NPV]] 靜態分析無法捕捉的管理彈性提供了定量估值方法，是工程項目評估的重要補充。此外，[[garch|GARCH]] 族的隨機波動率模型（Heston、SABR）克服了 BS 的固定波動率假設，是定價帶微笑結構的衍生品的現代替代方案。

## What It Is

An **option** is a financial contract giving the holder the right (but not obligation) to buy (**call**) or sell (**put**) an underlying asset $S$ at a **strike price** $K$ by an **expiry date** $T$.

**Call payoff at expiry**: $\max(S_T - K, 0)$
**Put payoff at expiry**: $\max(K - S_T, 0)$

American options can be exercised any time before $T$; European options only at $T$.

## Put-Call Parity

For European options on a non-dividend-paying stock:
$$C - P = S_0 - K e^{-rT}$$

Violation implies arbitrage. Fundamental identity linking calls and puts.

## Binomial Tree Model

**Cox-Ross-Rubinstein (1979)**: discretize time into $n$ steps of length $\Delta t$. At each node, stock moves up by factor $u$ or down by $d$:
- $u = e^{\sigma\sqrt{\Delta t}}$, $d = 1/u$
- **Risk-neutral probability**: $q = (e^{r\Delta t} - d)/(u - d)$

**Risk-neutral pricing**: price option by discounting expected payoff under $q$, not the real-world probability. No-arbitrage forces this.

**American option**: at each node, compare hold value vs. exercise value; take the maximum. Binomial tree naturally handles early exercise.

As $n \to \infty$ and $\Delta t \to 0$, the binomial model converges to Black-Scholes.

## Black-Scholes Model

**Assumptions**: stock follows geometric Brownian motion $dS = \mu S \, dt + \sigma S \, dW_t$; continuous trading; no dividends; constant risk-free rate $r$ and volatility $\sigma$.

**Black-Scholes formula** (European call):
$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$
$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$

where $N(\cdot)$ is the standard normal CDF.

**Derivation**: form a delta-hedged portfolio ($\Delta = N(d_1)$ shares per call), apply Ito's lemma, invoke no-arbitrage — the hedge eliminates risk, so the portfolio earns the risk-free rate. Results in the BS PDE: $\frac{\partial C}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} + rS \frac{\partial C}{\partial S} - rC = 0$.

## Greeks

The Greeks measure sensitivity of option price to model inputs:

| Greek | Formula | Interpretation |
|---|---|---|
| **Delta** ($\Delta$) | $\partial C/\partial S = N(d_1)$ | Shares to hold for delta-neutral hedge |
| **Gamma** ($\Gamma$) | $\partial^2 C/\partial S^2$ | Rate of change of delta; convexity |
| **Vega** ($\nu$) | $\partial C/\partial \sigma$ | Sensitivity to volatility |
| **Theta** ($\Theta$) | $\partial C/\partial t$ | Time decay (usually negative for long options) |
| **Rho** ($\rho$) | $\partial C/\partial r$ | Sensitivity to interest rate |

**Delta hedging**: maintain a portfolio with $\Delta = 0$ by continuously rebalancing. Cost of hedging = gamma × realized variance.

## Implied Volatility

BS formula can be inverted: given market price, back out $\sigma$ — this is **implied volatility (IV)**. 

- IV is the market's expectation of future volatility
- **Volatility smile/skew**: IV varies with strike $K$ (violating constant-$\sigma$ BS assumption) — deep out-of-the-money puts have higher IV (crash risk premium)
- **VIX**: market volatility index derived from S&P 500 options IV

## Extensions and Limitations

**BS limitations**: constant volatility (stochastic vol models: Heston, SABR), no jumps (Merton jump-diffusion), no transaction costs, continuous hedging.

**American options**: no closed form. Numerical methods: binomial tree, finite differences, Monte Carlo with Longstaff-Schwartz.

**Exotic options**: barrier, Asian, lookback — require Monte Carlo or PDE methods.

**Real options**: apply option framework to capital investment decisions — "option to expand," "option to abandon." Bridges financial derivatives to NPV analysis. See [[npv]].

## Assumptions and Limitations

**Black-Scholes assumptions**:
1. Underlying follows geometric Brownian motion with **constant** $\mu$ and $\sigma$ — violated by volatility clustering ([[garch|GARCH]] effects) and jumps.
2. **Continuous trading** and frictionless markets — no transaction costs, bid-ask spreads, or market impact.
3. **No dividends** on the underlying during the option's life (adjustable via $S_0 e^{-qT}$ for continuous dividend yield $q$).
4. **Constant risk-free rate** $r$ over the option's life.
5. **European exercise** only — American options require numerical methods.

**Key limitations**:
- **Volatility smile/skew**: implied volatility $\sigma_{IV}(K, T)$ varies with strike and maturity, violating the flat-$\sigma$ assumption. Deep OTM puts carry higher IV due to crash risk premium (left-tail fear).
- **Stochastic volatility**: Heston (1993) model adds a mean-reverting variance process $d\nu_t = \kappa(\theta - \nu_t)dt + \xi\sqrt{\nu_t}dW_t^\nu$ (correlated with $dW_t^S$), reproducing the skew and allowing semi-closed-form pricing.
- **Jump risk**: Merton (1976) jump-diffusion adds a Poisson jump process; jumps are unhedgeable with the underlying alone.
- **Model risk**: all parametric models misspecify reality to some degree; wrong model $\sigma$ leads to systematic delta-hedging errors.

## Connections to OR

- **Optimal stopping**: American option exercise = optimal stopping problem $\tau^* = \inf\{t: V(t,S_t) = (S_t-K)^+\}$; solved by the free-boundary HJB PDE — see [[stochastic-calculus|Stochastic Calculus]].
- **Stochastic inventory**: the newsvendor has a "call option" structure on demand — the critical ratio $CR = (p-c)/(p-s)$ is the option's delta; see [[newsvendor-problem|Newsvendor Problem]].
- **Revenue management**: capacity selling with uncertain demand has option-like payoff structure; see [[revenue-management|Revenue Management]].
- **Real options in capital budgeting**: option to expand (call), option to abandon (put), option to defer (call on NPV) — see [[npv|NPV]] and [[corporate-finance|Corporate Finance]].

## Related Concepts

- [[stochastic-calculus|Stochastic Calculus]] — Mathematical foundation: Itô's lemma, GBM, BS PDE derivation
- [[portfolio-theory|Portfolio Theory]] — Options extend portfolios to nonlinear payoffs; put-call parity links to no-arbitrage pricing
- [[garch|GARCH Models]] — Stochastic volatility models (Heston, SABR) generalize GARCH to continuous time
- [[time-value-of-money|Time Value of Money]] — Option price = discounted expected payoff under risk-neutral measure
- [[npv|Net Present Value]] — Real options analysis extends NPV to capture managerial flexibility
- [[behavioral-economics|Behavioral Economics]] — Volatility smile partly reflects behavioral demand for crash insurance (loss aversion)
- [[revenue-management|Revenue Management]] — Capacity control has option-like payoff structure
- [[fixed-income|Fixed Income]] — Interest rate options (caps, floors, swaptions) priced via short-rate models (Vasicek, CIR, HJM)
- [[corporate-finance|Corporate Finance]] — Real options; equity as a call option on firm assets (Merton 1974 structural credit model)
- [[wiki/mocs/operations-research|Operations Research MOC]]
- [[wiki/mocs/financial-engineering|Financial Engineering MOC]]

## Source Materials

- [[wiki/sources/courses/fina-investments|FINA3103 Investments]]
- [[wiki/sources/courses/ieda-financial-derivatives|IEDA3330 Financial Derivatives]]
- [[wiki/sources/courses/ieda-financial-derivatives-advanced|IEDA4331 Financial Derivatives (Advanced)]]
- [[wiki/sources/courses/hkust-financial-mathematics|MATH4424/4514 Financial Mathematics]]
