---
title: "Stochastic Calculus"
full_name: "Stochastic Calculus (Itô Calculus)"
type: concept
tags: [mathematics, stochastic-calculus, finance, probability]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/hkust-financial-mathematics"
confidence: high
---

## 概述

隨機微積分（Stochastic Calculus，又稱伊藤微積分）將古典微積分延伸至路徑連續但處處不可微的隨機過程，由伊藤清（Kiyosi Itô）於 1940 年代奠基。其核心困難在於布朗運動路徑的二次變差非零——$\sum_i (W_{t_i} - W_{t_{i-1}})^2 \to t$，記作 $(dW_t)^2 = dt$——使得標準 Riemann-Stieltjes 積分失效，必須以左端點 Riemann 和的 $L^2$ 極限定義伊藤積分。伊藤引理是全框架的核心公式：對 $f(t, X_t)$ 展開時，二階偏導項 $\frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2} dt$ 是古典鏈式法則中沒有對應項的「伊藤修正」，正是這一修正項在幾何布朗運動 $dS = \mu S\,dt + \sigma S\,dW_t$ 的求解中引出了對數轉換後的漂移項修正 $-\sigma^2/2$，進而使 $S_t$ 服從對數正態分佈。Black-Scholes 方程的整個推導鏈依賴伊藤引理：期權價格 $C(t, S_t)$ 的 SDE → Delta 對沖消除隨機項 → 無風險組合賺取無風險利率 → BS PDE，這是 [[options-pricing|期權定價]] 的數學骨架。均值回歸的 Ornstein-Uhlenbeck 過程（用於利率 Vasicek 模型、波動率均值回歸）與確保正值的 CIR 過程（$dr = \kappa(\theta - r)dt + \sigma\sqrt{r}dW$，Feller 條件 $2\kappa\theta \geq \sigma^2$）是 [[fixed-income|固定收益]] 利率衍生品定價的標準連續時間工具。在運籌學的隨機控制分支中，Hamilton-Jacobi-Bellman（HJB）方程是伊藤引理在最優控制問題上的直接應用，是連續時間動態規劃的數學核心，涵蓋最優投資組合（Merton 問題）、連續時間庫存控制（$(s,S)$ 策略的最優性證明）及最優停時（美式期權行使）等 OR 核心問題。對 [[arma-models|ARMA]] 與 [[garch|GARCH]] 的時間序列分析者而言，隨機微積分提供了離散模型的連續時間對應物與嚴格極限理論基礎。

## What It Is

**Stochastic calculus** extends ordinary calculus to handle functions of stochastic processes — specifically, processes with a random component that is continuous but nowhere differentiable (like Brownian motion). Standard calculus fails because Brownian paths have **infinite variation** on any interval.

## Brownian Motion (Wiener Process)

A stochastic process $\{W_t\}_{t \geq 0}$ is a **standard Brownian motion** if:
1. $W_0 = 0$ almost surely
2. **Independent increments**: $W_t - W_s \perp W_s - W_u$ for $u < s < t$
3. **Stationary increments**: $W_t - W_s \sim \mathcal{N}(0, t-s)$
4. **Continuous paths**: $t \mapsto W_t$ is continuous a.s.

**Key properties**:
- $E[W_t] = 0$, $\text{Var}(W_t) = t$
- Nowhere differentiable: $\lim_{h \to 0} (W_{t+h} - W_t)/h$ does not exist
- Quadratic variation: $\sum_i (W_{t_i} - W_{t_{i-1}})^2 \to t$ as partition is refined — written $(dW_t)^2 = dt$

## Itô Integral

For a deterministic function $f$, $\int_0^T f(t) dW_t$ is a Gaussian random variable with mean 0 and variance $\int_0^T f(t)^2 dt$.

For a stochastic integrand $H_t$ (adapted to $W$), the **Itô integral** $\int_0^T H_t dW_t$ is defined as the $L^2$ limit of Riemann-Stieltjes sums evaluated at the **left endpoint** (unlike Stratonovich which uses midpoints).

**Itô isometry**: $E\left[\left(\int_0^T H_t dW_t\right)^2\right] = E\left[\int_0^T H_t^2 dt\right]$

## Itô's Lemma

The central result of stochastic calculus. For a function $f(t, X_t)$ where $X_t$ satisfies:
$$dX_t = \mu(t, X_t) dt + \sigma(t, X_t) dW_t$$

then:
$$df(t, X_t) = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial x} dX_t + \frac{1}{2} \frac{\partial^2 f}{\partial x^2} (dX_t)^2$$

Using $(dt)^2 = 0$, $dt \cdot dW_t = 0$, $(dW_t)^2 = dt$:

$$df = \left(\frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}\right) dt + \sigma \frac{\partial f}{\partial x} dW_t$$

The extra $\frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}$ term — the **Itô correction** — has no counterpart in ordinary calculus. It arises because Brownian paths have non-zero quadratic variation.

## Geometric Brownian Motion

The most important SDE in finance. Stock price model:
$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

**Solution** (apply Itô's lemma to $f = \ln S$):
$$S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]$$

$S_t$ is **lognormal**: $\ln S_t \sim \mathcal{N}(\ln S_0 + (\mu - \sigma^2/2)t, \; \sigma^2 t)$.

The $-\sigma^2/2$ term (Itô correction) causes the mean of $\ln S$ to be less than $\mu t$ — log-return mean ≠ arithmetic return mean.

## Black-Scholes via Itô's Lemma

Consider a call option $C(t, S_t)$. By Itô's lemma:
$$dC = \left(\frac{\partial C}{\partial t} + \mu S \frac{\partial C}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}\right)dt + \sigma S \frac{\partial C}{\partial S} dW_t$$

Form a delta-hedged portfolio $\Pi = C - \Delta S$ (choose $\Delta = \partial C/\partial S$). The $dW_t$ terms cancel:
$$d\Pi = \left(\frac{\partial C}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}\right)dt$$

No randomness → portfolio earns risk-free rate: $d\Pi = r\Pi \, dt$. This gives the **Black-Scholes PDE**:
$$\frac{\partial C}{\partial t} + rS\frac{\partial C}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} - rC = 0$$

See [[options-pricing]] for the closed-form solution.

## Stochastic Differential Equations (SDEs)

General SDE: $dX_t = b(t, X_t)dt + \sigma(t, X_t)dW_t$. Under Lipschitz conditions on $b$ and $\sigma$, a unique strong solution exists.

**Mean-reverting (Ornstein-Uhlenbeck) process**:
$$dX_t = \kappa(\theta - X_t)dt + \sigma dW_t$$
Used for interest rates (Vasicek model), volatility, commodity prices. Stationary distribution: $\mathcal{N}(\theta, \sigma^2/2\kappa)$.

**Cox-Ingersoll-Ross (CIR)**:
$$dr_t = \kappa(\theta - r_t)dt + \sigma\sqrt{r_t}dW_t$$
Interest rate model; ensures $r_t \geq 0$ when $2\kappa\theta \geq \sigma^2$ (Feller condition).

## Connections to OR

**Stochastic control**: maximize $E\left[\int_0^T r(X_t, u_t)dt + g(X_T)\right]$ over control $u_t$. The **Hamilton-Jacobi-Bellman (HJB) equation** is a nonlinear PDE derived via Itô's lemma — the continuous-time analogue of dynamic programming.

**Optimal stopping**: American options, secretary problem. The value function satisfies a variational inequality.

**Inventory control**: continuous-time inventory models with Brownian demand use SDE techniques; optimal $(s, S)$ policies in continuous time.

## Assumptions and Limitations

- **Continuous paths / continuous trading**: Brownian motion has continuous paths; real markets have discrete trading, bid-ask spreads, and overnight gaps. Delta hedging in discrete time incurs hedging error proportional to $\Gamma \sigma^2 S^2 \Delta t$.
- **Itô vs. Stratonovich convention**: the choice of integration convention matters for chain-rule application. Finance uses Itô (non-anticipating, martingale property preserved); physics often uses Stratonovich (ordinary chain rule holds). Results differ by the $\frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}$ correction term.
- **Strong vs. weak solutions**: existence and uniqueness of strong solutions requires Lipschitz and linear growth conditions on drift $b$ and diffusion $\sigma$ coefficients — violated by, e.g., the CIR process near zero (only weak solution guaranteed without Feller condition).
- **Curse of dimensionality in HJB**: the HJB PDE lives in the state space dimension; for high-dimensional control problems (large portfolio, many state variables), finite-difference methods become intractable and deep learning / neural-network PDEs solvers (e.g., deep BSDE method, Han et al. 2018) are the frontier approach.

## Related Concepts

- [[options-pricing|Options Pricing]] — BS PDE derived directly from Itô's lemma; Greeks are partial derivatives of the option price function
- [[probability-theory|Probability Theory]] — Brownian motion is defined on a probability space; measure-theoretic foundations underlie the change-of-measure (Girsanov) technique for risk-neutral pricing
- [[differential-equations|Differential Equations]] — BS PDE is a parabolic PDE solvable by heat-equation transformation; SDEs are the stochastic counterpart of ODEs
- [[stochastic-processes|Stochastic Processes]] — Brownian motion, martingales, Markov property, and Itô processes are special cases of the general stochastic process framework
- [[garch|GARCH Models]] — GARCH is the discrete-time analogue of stochastic volatility SDEs; GARCH(1,1) converges to a diffusion as $\Delta t \to 0$
- [[cointegration|Cointegration]] — VECM error-correction term is the discrete-time counterpart of an OU mean-reverting SDE
- [[arma-models|ARMA Models]] — ARMA(p,q) is the discrete-time analogue of linear SDEs; unit-root ARIMA corresponds to a random walk (driftless BM in continuous time)
- [[portfolio-theory|Portfolio Theory]] — Merton continuous-time portfolio problem solved via HJB; dynamic asset allocation is a stochastic control problem
- [[wiki/mocs/operations-research|Operations Research MOC]]
- [[wiki/mocs/financial-engineering|Financial Engineering MOC]]

## Source Materials

- [[wiki/sources/courses/hkust-financial-mathematics|MATH4424/4514 Financial Mathematics]]
- [[wiki/sources/courses/hkust-stochastic-modeling|MATH4432 Stochastic Modeling]]
- [[wiki/sources/courses/ieda-financial-derivatives-advanced|IEDA4331 Financial Derivatives (Advanced)]]
