---
title: "Probability Theory"
full_name: "Probability Theory"
type: concept
tags: [mathematics, probability, statistics, foundations]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/hkust-probability-statistics"
confidence: high
---

## 概述

概率論是量化不確定性的數學語言，以 Kolmogorov 三公理（非負性、規範性、可列可加性）為基礎，嚴格定義了概率空間 $(\Omega, \mathcal{F}, P)$，並由此推導出條件概率、貝葉斯定理、隨機變量及其分佈等核心概念。離散分佈（Bernoulli、Binomial、Poisson、幾何分佈）和連續分佈（常態、指數、Gamma、Beta、對數正態）各有其在運籌學中的典型應用：Poisson 分佈描述到達過程，指數分佈刻畫無記憶服務時間，對數正態分佈擬合需求量與資產價格。大數定律（樣本均值依概率收斂至期望值）與中心極限定理（標準化樣本均值趨近標準正態）是統計推斷與[[hypothesis-testing|假設檢驗]]的理論基石，也是[[ab-testing|A/B 測試]]樣本量計算的數學依據。全期望定律 $E[X] = E[E[X|Y]]$ 和全方差定律是複雜隨機模型（如分階段需求、混合泊松）的強力計算工具，廣泛應用於[[newsvendor-problem|報童問題]]和[[queueing-theory|排隊理論]]的解析推導。機率論在機器學習中扮演雙重角色：線性回歸的 OLS 等價於高斯誤差下的最大似然估計，邏輯回歸直接最大化伯努利似然，而貝葉斯推斷通過先驗與後驗整合不確定性，是貝葉斯優化和主動學習的基礎。

## Foundations: Kolmogorov Axioms

A **probability space** $(\Omega, \mathcal{F}, P)$ consists of:
- **Sample space** $\Omega$: set of all possible outcomes
- **$\sigma$-algebra** $\mathcal{F}$: collection of "events" (subsets of $\Omega$) closed under complement and countable union
- **Probability measure** $P: \mathcal{F} \to [0,1]$ satisfying: $P(\Omega) = 1$, and countable additivity: $P(\bigcup_i A_i) = \sum_i P(A_i)$ for disjoint $A_i$

**Derived rules**: $P(\emptyset) = 0$; $P(A^c) = 1 - P(A)$; $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

## Conditional Probability and Independence

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \quad (P(B) > 0)$$

**Bayes' theorem**: $P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}$ — the foundation of Bayesian inference and [[nlp-basics]] text classification.

**Total probability**: $P(B) = \sum_i P(B \mid A_i) P(A_i)$ for a partition $\{A_i\}$.

**Independence**: $A \perp B \iff P(A \cap B) = P(A)P(B)$. Mutual independence of $n$ events requires $\binom{n}{k}$ conditions for each $k \geq 2$ — pairwise independence is not sufficient.

## Random Variables

A **random variable** $X: \Omega \to \mathbb{R}$ is a measurable function. Characterized by its distribution.

### Discrete Distributions

| Distribution | PMF $P(X=k)$ | Mean | Variance | OR Use |
|---|---|---|---|---|
| Bernoulli($p$) | $p^k(1-p)^{1-k}$ | $p$ | $p(1-p)$ | Binary outcomes |
| Binomial($n,p$) | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | Defect counts |
| Poisson($\lambda$) | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ | Arrival counts |
| Geometric($p$) | $(1-p)^{k-1}p$ | $1/p$ | $(1-p)/p^2$ | Time to first success |
| Negative Binomial | – | $r/p$ | $r(1-p)/p^2$ | Overdispersed counts |

### Continuous Distributions

| Distribution | PDF | Mean | Variance | OR Use |
|---|---|---|---|---|
| Uniform($a,b$) | $1/(b-a)$ | $(a+b)/2$ | $(b-a)^2/12$ | Prior beliefs |
| Normal($\mu, \sigma^2$) | $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ | Demand, errors |
| Exponential($\lambda$) | $\lambda e^{-\lambda x}$ | $1/\lambda$ | $1/\lambda^2$ | Service times, inter-arrivals |
| Gamma($\alpha, \beta$) | — | $\alpha/\beta$ | $\alpha/\beta^2$ | Erlang service |
| Beta($\alpha, \beta$) | — | $\alpha/(\alpha+\beta)$ | – | Bayesian prior for $p$ |
| Lognormal($\mu, \sigma^2$) | — | $e^{\mu+\sigma^2/2}$ | — | Asset prices, demand |

## Expectation and Moments

$$E[X] = \sum_k k \cdot P(X=k) \quad \text{(discrete)}, \quad E[X] = \int_{-\infty}^{\infty} x f(x) \, dx \quad \text{(continuous)}$$

**Variance**: $\text{Var}(X) = E[X^2] - (E[X])^2 = E[(X - \mu)^2]$

**Linearity**: $E[aX + bY] = aE[X] + bE[Y]$ (always, even if $X, Y$ dependent).

**Covariance**: $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$; if independent, $\text{Cov} = 0$ (not conversely).

**Law of total expectation**: $E[X] = E[E[X|Y]]$ — powerful for computing expectations by conditioning.

**Law of total variance**: $\text{Var}(X) = E[\text{Var}(X|Y)] + \text{Var}(E[X|Y])$.

## Limit Theorems

**Law of Large Numbers (LLN)**: if $X_1, X_2, \ldots$ are iid with mean $\mu$, then $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu$. Strong LLN: convergence almost surely.

**Central Limit Theorem (CLT)**: if $X_i$ iid with mean $\mu$ and variance $\sigma^2 < \infty$, then:
$$\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \xrightarrow{d} \mathcal{N}(0, 1)$$

CLT justifies the Normal approximation for sums of many small effects — underpins confidence intervals and hypothesis tests.

**Chebyshev's inequality**: $P(|X - \mu| \geq k\sigma) \leq 1/k^2$ — weak but distribution-free bound.

## OR Relevance

**Inventory/newsvendor**: demand $D$ is random; optimal order quantity $Q^* = F^{-1}(c_u/(c_u + c_o))$ where $F$ is the demand CDF. See [[newsvendor-problem]].

**Queueing**: Poisson arrivals + exponential service = M/M/1 queue. Steady-state analysis requires understanding distributions and limits. See [[queueing-theory]], [[stochastic-processes]].

**A/B testing**: CLT enables normal approximation for test statistics; Type I/II error analysis. See [[ab-testing]].

**Machine learning**: probabilistic interpretation of linear regression (MLE = OLS under Gaussian errors); logistic regression = log-odds model; Naive Bayes classifier. See [[linear-regression]], [[logistic-regression]].

## Related Concepts

- [[stochastic-processes]]
- [[hypothesis-testing]]
- [[ab-testing]]
- [[queueing-theory]]
- [[newsvendor-problem]]
- [[arma-models]]
- [[linear-algebra]]
- [[optimization]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
