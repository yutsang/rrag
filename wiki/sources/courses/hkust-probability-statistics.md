---
title: "HKUST Probability and Statistics"
full_name: "HKUST Probability and Statistics (MATH2411/2511)"
type: source
tags: [courses, math, undergraduate, probability, statistics, math2411, math2511, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH/MATH2411"
confidence: medium
---

## 概述

MATH2411 概率論及 MATH2511 統計學構成香港科技大學數學系的機率統計序列，為理工科學生提供嚴格的概率公理化基礎、統計推斷理論及回歸分析方法。MATH2411 面向工程及應用科學學生，以 Walpole、Myers 等《工程統計》或 Montgomery《應用統計》系列為教材，強調與工程實踐相關的應用場景；MATH2511 則採用更嚴格的測度論視角，適合數學專業學生。先修要求為 MATH1013/1014 微積分，使學生具備連續型隨機變數積分推導的能力。課程覆蓋範圍從概率公理（Kolmogorov 體系）、常見離散與連續分佈、聯合分佈與條件期望，到最大概似估計（MLE）、信賴區間、假設檢定（z-test、t-test、ANOVA）及線性回歸分析。相較於 ISOM2500 的商業統計導向，本課程更注重數學嚴謹性，為後續隨機過程、GARCH 模型、貝葉斯統計及機器學習的理論基礎提供必要準備，亦是運籌學博士班研究的統計工具基礎。

## Course Structure

| Course | Content |
|---|---|
| MATH2411 | Applied statistics (engineering focus) |
| MATH2511 | Foundations of probability theory (more rigorous) |

## Key Topics

### MATH2411: Applied Statistics
**Probability foundations**:
- Sample spaces, events, axioms; combinatorial probability
- Conditional probability, Bayes' theorem, independence
- Random variables: PMF, PDF, CDF; expectation, variance, moments

**Key distributions**: Binomial, Geometric, Negative Binomial, Poisson, Uniform, Normal, Exponential, Gamma, Beta, Chi-square, t, F

**Joint distributions**: joint PMF/PDF, marginal distributions, covariance, correlation; conditional distributions; conditional expectation

**Limit theorems**: Markov inequality, Chebyshev inequality, LLN, CLT, delta method

**Statistical inference**:
- Point estimation: MLE (method of maximum likelihood), method of moments
- Properties: unbiasedness, consistency, efficiency, Cramér-Rao bound
- Confidence intervals: mean (known/unknown $\sigma$), proportion, difference of means
- Hypothesis testing: z-test, t-test, p-value, power, sample size determination
- Nonparametric tests: sign test, Wilcoxon rank-sum, Kruskal-Wallis

**Regression analysis**:
- Simple linear regression: OLS, $R^2$, residual analysis
- Multiple regression: matrix form $\hat{\beta} = (X^TX)^{-1}X^Ty$, F-test, $t$-tests
- Model diagnostics: normality, homoscedasticity, outliers

### MATH2511: Probability Theory (Honors)
More rigorous treatment including:
- Measure-theoretic foundations (intro level)
- Generating functions: PGF, MGF, characteristic functions
- Convergence in probability, a.s., in $L^p$, in distribution
- Borel-Cantelli lemmas; strong LLN proof
- CLT proof via characteristic functions

## Connections to Wiki

Provides rigorous mathematical foundations for:
- [[probability-theory]] concept page
- [[hypothesis-testing]] methods
- [[arma-models]] and [[garch]] statistical foundations
- [[stochastic-processes]] (CTMC, Poisson process)

## Related Concepts

- [[probability-theory]]
- [[hypothesis-testing]]
- [[linear-regression]]
- [[ab-testing]]
- [[stochastic-processes]]
