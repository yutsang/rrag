---
title: "IEDA 2540: Engineering Statistics"
full_name: "IEDA 2540 Engineering Statistics (formerly IELM 2510)"
type: source
tags: [courses, ieda, undergraduate, statistics, hypothesis-testing, regression, ieda2540, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA2540"
confidence: high
author: "Zhang, J."
date_published: "2016-02-01"
---

## 概述

IEDA 2540「工程統計」（歷史上曾以 IELM 2510 開設）是 IEDA 2520 的直接續課，由張繼恒教授講授，前置要求為 IEDA 2520 的概率基礎。課程採用 Sheldon M. Ross 所著《Introduction to Probability and Statistics for Engineers and Scientists》（Academic Press，第 4 版）為參考教材，將概率理論延伸至統計推斷，涵蓋矩估計法（MOM）與最大概似估計（MLE）、信賴區間構造（z 分佈及 t 分佈）、假設檢定（z 檢定、單樣本 t 檢定、雙樣本 t 檢定、配對 t 檢定、卡方檢定）以及簡單線性迴歸（OLS、R²、迴歸係數的統計推斷）。課程設有 3–4 人小組專案，要求學生選定真實統計問題、蒐集數據、應用課程方法並撰寫含圖表分析的一頁報告，模擬 OR 研究與業界數據分析的完整流程。IEDA 2540 是 IEDA 3010（運籌學 I）、IEDA 3230（應用迴歸）、IEDA 4100（隨機模型）及一切涉及數據分析的 IEDA 課程的必備前置知識。

## Course Overview

**IEDA 2540: Engineering Statistics** (historically offered as IELM 2510 "Engineering Probability and Statistics") is the statistical inference sequel to [[wiki/sources/courses/ieda-probability-for-engineers|IEDA 2520]]. Taught by Prof. Jiheng Zhang, it extends probability foundations into applied statistics: moving from describing distributions to making inferences about population parameters from sample data.

- **Textbook**: Sheldon M. Ross, *Introduction to Probability and Statistics for Engineers and Scientists*, Academic Press, 4th Edition (optional)

## Course Outline

### Module 1: Elements of Probability (Review)
Recap of IEDA 2520: sample spaces, conditional probability, Bayes' rule, key distributions. Provides the foundation for sampling distributions.

### Module 2: Random Variables (Review)
Discrete and continuous distributions, joint distributions, covariance. Introduction to **moment generating functions (MGFs)** as a tool for deriving properties of sums of random variables.

### Module 3: Limiting Theorems (Review)
LLN and CLT revisited — now used to justify normal approximations in statistical inference.

### Module 4: Descriptive Statistics
- Frequency tables, histograms, measures of center and spread
- Chebyshev's inequality
- Sample mean and variance as estimators of population parameters

### Module 5: Parameter Estimation
- **Point estimation**: method of moments, **maximum likelihood estimation (MLE)**
  - MLE finds the parameter value θ̂ that maximizes the likelihood function L(θ|data)
  - Properties: consistency, asymptotic efficiency, invariance
- **Interval estimation**: constructing **confidence intervals (CIs)**
  - 95% CI: if we repeated sampling, 95% of constructed intervals contain the true parameter
  - CI for mean (known σ): x̄ ± z_{α/2} · σ/√n
  - CI for mean (unknown σ): x̄ ± t_{α/2,n-1} · s/√n (t-distribution)
  - CI for proportion: p̂ ± z_{α/2} · √(p̂(1-p̂)/n)

### Module 6: Hypothesis Testing
See [[wiki/concepts/hypothesis-testing|Hypothesis Testing]] for full treatment. Key tests covered:
- **z-test**: large samples, known σ; test statistic Z = (x̄ - μ₀)/(σ/√n)
- **One-sample t-test**: unknown σ; test statistic T = (x̄ - μ₀)/(s/√n)
- **Two-sample t-test**: comparing two population means
- **Paired t-test**: matched pairs (before/after, A/B)
- **Chi-square test**: goodness-of-fit, test of independence
- Significance level α, p-value, Type I error (false positive), Type II error (false negative), power

### Module 7: Regression Analysis
- **Simple linear regression**: Y = β₀ + β₁X + ε
- **Ordinary least squares (OLS)**: minimizes Σ(yᵢ - ŷᵢ)²
- Confidence intervals and hypothesis tests for regression coefficients
- Coefficient of determination R²: proportion of variance explained
- **Statistical inference on regression**: t-test for slope, F-test for overall fit
- Connects to [[wiki/concepts/linear-regression|Linear Regression]] for extensions (multiple regression, diagnostics)

## Relationship to Other Courses

IEDA 2540 is a prerequisite or assumed background for:
- **IEDA 3010** (Operations Research): uses statistical models to evaluate simulation output
- **IEDA 3230** (Applied Regression): extends to multiple regression, diagnostics, model selection
- **IEDA 4100** (Stochastic Models): relies on probability distributions and limiting theorems
- Any IEDA course involving data analysis or experimental design

## Related Concepts

- [[wiki/concepts/hypothesis-testing|Hypothesis Testing]]
- [[wiki/concepts/linear-regression|Linear Regression]]
- [[wiki/concepts/ab-testing|A/B Testing]]
- [[probability-theory]]
- [[wiki/concepts/logistic-regression|Logistic Regression]]
- [[wiki/concepts/arma-models|ARMA Models]]
- [[wiki/concepts/clustering|Clustering]]
- [[wiki/sources/courses/ieda-probability-for-engineers|IEDA 2520: Probability for Engineers]]

## Source Materials

- raw/courses/IEDA/IEDA2540/IEDA2510(IEDA2520-2540)/ESU_Source/Syllabus.pdf
- raw/courses/IEDA/IEDA2540/IEDA2510(IEDA2520-2540)/ESU_Source/Module Notes/
