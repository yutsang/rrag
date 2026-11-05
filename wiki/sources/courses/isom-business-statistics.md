---
title: "Business Statistics"
full_name: "ISOM2500 Business Statistics"
type: source
tags: [courses, isom, undergraduate, statistics, business-analytics, isom2500, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/ISOM/ISOM2500"
confidence: medium
---

## 概述

ISOM2500 商業統計為工商管理學院二年級學生提供完整的統計推斷訓練，以 Berenson、Levine 及 Krehbiel《商業統計基礎》（Basic Business Statistics，Pearson 標準教材）為主要教材，先修要求為 ISOM1500 或同等數學基礎，是商學院所有數據分析及預測建模高年級課程（ISOM3360 預測分析、ISOM3540 商業智能）的核心統計先修科目。課程相較於 ISOM1500 提供更嚴格的統計推斷處理，涵蓋多種概率分佈（Bernoulli、二項、Poisson、正態、指數）及其參數估計、單樣本與雙樣本假設檢定（含配對 t 檢定）、單因子與雙因子 ANOVA（含交互作用效應）、卡方獨立性檢定，以及從簡單線性迴歸延伸至多元線性迴歸（VIF 多共線性診斷、AIC/BIC 模型選擇準則）的完整迴歸分析框架。學生完成課程後能夠設計統計實驗、計算及解讀信賴區間與 p 值、建立多元迴歸預測模型並進行殘差診斷，以及理解統計顯著性與實際意義的差別。本課程所培養的統計推斷能力是 A/B 測試設計（電商優化）、市場研究、財務建模及供應鏈需求預測的共同定量語言。

## Course Overview

**Textbook**: Berenson, Levine & Krehbiel, *Basic Business Statistics* (or equivalent)

More comprehensive than ISOM1500 — covers statistical inference with greater rigor and adds ANOVA, chi-square, and multiple regression in depth.

## Key Topics

### Descriptive Statistics and EDA
- Frequency distributions; stem-and-leaf plots; box-and-whisker plots
- Measures of location: arithmetic mean, geometric mean, harmonic mean
- Measures of shape: skewness coefficient, kurtosis
- Covariance and correlation: $r_{xy} = \frac{\sum(x-\bar{x})(y-\bar{y})}{(n-1)s_xs_y}$

### Probability Theory
- Classical, relative frequency, and subjective probability
- Bayes' theorem: posterior probability; applications in screening tests (sensitivity/specificity)
- Expected value and variance of a random variable

### Probability Distributions
- Discrete: Bernoulli, Binomial, Poisson; expectation and variance formulas
- Continuous: Uniform, Normal, Exponential; standardization
- Sampling distributions: $\bar{X} \sim N(\mu, \sigma^2/n)$ by CLT

### Statistical Inference
- Point estimation: unbiasedness; efficiency
- Confidence intervals: means (known/unknown σ), proportions, differences of means
- **Hypothesis testing**: formulation; Type I (α) and Type II (β) errors; power; p-value interpretation
- One-sample and two-sample tests (z and t); paired t-test
- See [[hypothesis-testing]]

### ANOVA and Multiple Comparisons
- One-way ANOVA: partitioning of variance (SST = SSB + SSW); F-test
- Multiple comparisons: Tukey's HSD; Bonferroni correction
- Two-way ANOVA: interaction effects

### Chi-Square Tests
- Goodness of fit: observed vs. expected frequencies; $\chi^2 = \sum \frac{(O-E)^2}{E}$
- Test of independence for contingency tables
- Test of variance (one-sample $\chi^2$)

### Regression Analysis
- Simple linear regression: OLS derivation; ANOVA table for regression
- Residual analysis: normality, homoscedasticity, independence; influence statistics
- Multiple linear regression: coefficient interpretation (ceteris paribus); adjusted $R^2$; multicollinearity (VIF)
- Model selection: forward, backward, stepwise; information criteria (AIC, BIC)
- See [[linear-regression]]

## Related Concepts

- [[hypothesis-testing]]
- [[linear-regression]]
- [[probability-theory]]

## Source Materials

- ISOM2500 Course Materials
