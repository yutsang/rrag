---
title: "Simulation"
full_name: "Monte Carlo and Discrete-Event Simulation"
type: concept
tags: [operations-research, simulation, monte-carlo, stochastic, methods]
created: "2026-04-14"
updated: "2026-04-14"
source: "https://www.sciencedirect.com/book/9780124158252/simulation"
confidence: high
---

## 概述

模擬（Simulation）是透過對隨機系統建模並反覆抽樣來估計感興趣量（均值、分位數、機率）的計算方法，分為蒙地卡羅模擬（Monte Carlo Simulation，靜態問題）與離散事件模擬（Discrete-Event Simulation, DES，動態時間演化系統）兩大範疇。蒙地卡羅的核心估計量 μ̂ₙ = (1/n) Σ g(Xᵢ) 由大數法則保證收斂，標準誤差以 σ/√n 下降，收斂速率與維度無關，使其成為高維積分的唯一實用工具。離散事件模擬以未來事件表（Future Event List）驅動時鐘跳進，處理排隊網絡、製造系統及供應鏈中無解析解的複雜動態。方差縮減技術（控制變量法、對偶變量法、重要性採樣、分層抽樣）是提升模擬效率的關鍵，可在不增加採樣數量的情況下大幅降低估計誤差。模擬的主要限制是近似性（而非精確解）及輸出自相關（需批均值或再生方法構造有效置信區間）；穩態模擬還需處理初始化偏差（warm-up period）。在運籌學中，模擬廣泛補充了 M/M/1 等解析模型無法處理的 G/G/s 排隊、多期庫存策略評估、金融期權的蒙地卡羅定價及系統可靠性分析，是模擬優化（Simulation-Optimization）研究的核心計算工具。

## What It Is

**Simulation** is the process of building a model of a stochastic system and running experiments on that model to estimate quantities of interest — means, variances, quantiles, probabilities. Unlike analytical methods that yield exact formulas, simulation is approximate but universally applicable: if you can describe a system's random behavior, you can simulate it.

Two major paradigms:
- **Monte Carlo simulation**: static; generate many independent samples to estimate an expectation or integral.
- **Discrete-event simulation (DES)**: dynamic; model a system that evolves over time through a sequence of events.

## Why It Matters

Simulation fills the gap left by analytical tractability:
- Queueing networks beyond M/M/1 have no closed-form solutions for arbitrary service distributions — simulation handles them directly.
- Financial options with path-dependent payoffs (Asian, barrier, American) have no general Black-Scholes formula — Monte Carlo simulation is standard.
- Supply chain models with correlated demand, multiple products, and complex policies cannot be solved analytically — simulation evaluates them.
- Engineering reliability: system failure probability under complex component interactions is estimated by simulation.

## Monte Carlo Simulation

### Core Idea

To estimate E[g(X)] for a random variable X: generate n i.i.d. samples X₁, ..., Xₙ from the distribution of X, then use the estimator:

$$\hat{\mu}_n = \frac{1}{n} \sum_{i=1}^n g(X_i)$$

By the Strong Law of Large Numbers, $\hat{\mu}_n \to E[g(X)]$ almost surely. By the Central Limit Theorem, $\sqrt{n}(\hat{\mu}_n - \mu) \xrightarrow{d} N(0, \sigma^2)$, giving a 95% confidence interval $\hat{\mu}_n \pm 1.96\sigma/\sqrt{n}$.

**Convergence rate**: standard error = σ/√n. Halving the error requires 4× as many samples. This 1/√n rate is dimension-independent, making Monte Carlo the only viable method in high dimensions (>10).

### Generating Random Variables

All generation builds on U ~ Uniform[0,1]:

**Inverse CDF method**: if U ~ Uniform[0,1], then X = F⁻¹(U) has CDF F. Works whenever F⁻¹ has a closed form:
- Exponential(λ): X = −ln(U)/λ
- Weibull(α,β): X = β(−ln U)^{1/α}
- Discrete: find j such that F(j−1) < U ≤ F(j)

**Acceptance-rejection**: to sample from density f using envelope cg (where c·g(x) ≥ f(x) everywhere):
1. Generate X ~ g and U ~ Uniform[0,1].
2. Accept X if U ≤ f(X)/(c·g(X)); else reject and repeat.
Acceptance probability = 1/c. Efficient when f is close in shape to g.

**Box-Muller transform**: generate Normal(0,1) from two uniforms: Z = √(−2 ln U₁) cos(2π U₂).

### Variance Reduction Techniques

Reduce standard error without increasing sample size:

**Control variates**: if C has known mean μ_C and is correlated with estimator Y, use:
$$\tilde{Y} = Y - b(C - \mu_C), \quad b^* = \frac{\text{Cov}(Y,C)}{\text{Var}(C)}$$
Variance reduction factor: $1 - \rho^2_{Y,C}$. If ρ = 0.9, variance drops to 19% of original — effective when a good control exists.

**Antithetic variates**: use paired samples (U, 1−U) instead of two independent uniforms. Estimator: $\tilde{Y} = [g(U) + g(1-U)]/2$. If g is monotone, g(U) and g(1−U) are negatively correlated, reducing variance.

**Stratified sampling**: divide [0,1] into k strata; take n/k samples from each. Eliminates sampling variance within strata. Systematic stratification (Latin hypercube) extends this to multiple dimensions.

**Importance sampling**: sample from a modified distribution h that overweights the region of interest; correct with likelihood ratio weights w(X) = f(X)/h(X). Can dramatically reduce variance for rare event estimation (VaR tail probabilities).

**Conditional Monte Carlo**: exploit $\text{Var}(E[Y|Z]) \leq \text{Var}(Y)$; replace Y with the conditional expectation E[Y|Z=z] when it can be computed analytically.

## Discrete-Event Simulation

### Event-Driven Paradigm

A DES model consists of:
- **State variables**: describe the system at any point in time (queue lengths, server status, inventories).
- **Events**: instantaneous occurrences that change state (arrival, departure, failure, replenishment).
- **Future Event List (FEL)**: priority queue of scheduled events, sorted by event time.

**Simulation loop**:
1. Remove the earliest event from FEL.
2. Advance simulation clock to that event time.
3. Update state variables.
4. Schedule any new events triggered by this event.
5. Collect statistics.
6. Repeat until stopping criterion.

This approach skips over idle periods — the clock jumps directly from event to event — making DES far faster than time-step simulation for sparse event streams.

### Queueing System Simulation

**M/M/1 queue simulation**:
- Arrival event: generate next inter-arrival ~ Exp(λ); if server busy, join queue; else start service.
- Departure event: generate service time ~ Exp(μ); if queue non-empty, start next customer.
- Collect: waiting time per customer, queue length at each event.

**Validation**: compare simulated mean waiting time against analytical M/M/1 formula W = 1/(μ−λ). See [[wiki/concepts/queueing-theory|Queueing Theory]].

**Output analysis**: simulation output is correlated (waiting times of successive customers are dependent). Use batch means or regenerative methods to construct valid confidence intervals.

### Steady-State vs. Terminating Simulations

**Terminating simulation**: finite horizon with a defined stopping condition (e.g., simulate one 8-hour shift). Output: statistics within the horizon.

**Steady-state simulation**: system runs indefinitely; interest is in long-run averages. Problem: **initialization bias** — early output reflects transient behavior, not steady state. Remedies: warm-up period (discard initial observations), or start in steady state if it can be identified.

## Applications

### Operations and Supply Chain

- **Inventory systems**: simulate demand, lead times, and ordering policies to estimate fill rates and costs for complex multi-product, multi-echelon systems beyond the analytical [[wiki/concepts/newsvendor-problem|Newsvendor Problem]].
- **Production systems**: simulate job shop dynamics, machine failures, and operator scheduling to estimate throughput and cycle time.
- **Supply chain disruptions**: simulate stochastic supply disruptions to estimate stockout probability and evaluate mitigation strategies.

### Financial Engineering

- **Option pricing**: for path-dependent options (Asian: payoff depends on average price; barrier: payoff depends on whether price crosses a threshold), Monte Carlo simulation is the standard approach.
- **Risk measurement**: Value at Risk (VaR) and Expected Shortfall (ES) are estimated by simulating P&L scenarios. See [[wiki/sources/courses/ieda-financial-analytics|IEDA 4510]].
- **Credit risk**: simulate correlated defaults across a portfolio to estimate loss distribution for CDO tranching.

### Reliability Engineering

- **System reliability**: when components fail independently with known failure rate distributions, system reliability (probability all critical paths survive) is estimated by simulation.
- **Maintenance optimization**: simulate failure and repair processes under different maintenance policies to minimize expected total cost.

## Practical Gotchas

- **Pseudo-random number generators**: linear congruential generators are fast but have short periods and correlations in high dimensions. Use Mersenne Twister (period 2¹⁹⁹³⁷−1) or PCG for serious simulation work.
- **Seed management**: set a fixed seed for reproducibility; use different seeds for independent replications.
- **Correlated samples within a replication**: batch means or spectral methods needed for valid CI; naive CI using n independent samples is only valid for i.i.d. output.
- **Variance reduction requires design**: control variates and antithetic variates must be planned before running the simulation; they cannot be applied post-hoc.

## Comparison with Analytical Methods

| Criterion | Analytical | Simulation |
|-----------|-----------|------------|
| Exactness | Exact (when tractable) | Approximate (SE ∝ 1/√n) |
| Scope | Limited to tractable models | Universal |
| Speed | Instantaneous | Minutes to hours |
| Insight | Closed-form reveals structure | Black-box unless analyzed |
| Optimization | Straightforward | Requires simulation-optimization |

Analytical and simulation methods are complementary: use analytics to understand structure and build intuition; use simulation to validate assumptions and estimate quantities for realistic models.

## Related Concepts

- [[wiki/concepts/queueing-theory|Queueing Theory]] — analytical models that simulation validates and extends
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — stochastic inventory model; simulation handles multi-period extensions
- [[wiki/concepts/arma-models|ARMA Models]] — time series processes that can be simulated
- [[wiki/concepts/garch|GARCH]] — volatility processes simulated for financial risk
- [[wiki/mocs/operations-research|Operations Research MOC]] — simulation within the OR toolkit

## Source Materials

- raw/courses/IEDA/IEDA4130/2022S/IEDA4130_syllabus_2022.pdf
