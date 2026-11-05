---
title: "A/B Testing"
full_name: "A/B Testing (Randomized Controlled Experiments)"
type: concept
tags: [statistics, experimentation, hypothesis-testing, product-analytics, causal-inference]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/applied-statistics"
confidence: medium
---

## 概述

A/B 測試（隨機對照實驗）是建立因果關係最可靠的方法論，透過將受試單元隨機分配至對照組（A）和實驗組（B），以頻率主義假設檢驗框架（虛無假設、p 值、顯著性水準 α）或貝葉斯框架量化兩種方案的效果差異，從而做出有統計保障的數據驅動決策。樣本量計算是實驗設計的核心：在 α=0.05、80% 統計功效下，檢測1個百分點的轉化率提升需每組約16,558個用戶，最小可檢測效應量（MDE）的選擇直接決定實驗成本。Google 每年在搜尋引擎上運行逾一萬次 A/B 實驗，Netflix、Amazon 等科技公司同時並行數千個實驗，體現了實驗文化作為競爭優勢的戰略地位。常見的實驗陷阱包括：偷看問題（早期停止膨脹假陽性率）、多重比較問題（需 Bonferroni 校正）、新奇效應與首要效應、以及辛普森悖論（整體結果與分層結果相反）。A/B 測試的統計機制（z 檢定、t 檢定、卡方檢定）與[[hypothesis-testing|假設檢驗]]直接相通，其結果分析亦可用[[linear-regression|線性回歸]]（連續結果）或[[logistic-regression|邏輯回歸]]（二元結果）加入協變量控制以提高統計功效；在運籌學中，A/B 測試是評估新決策策略（如定價算法、排程規則）的黃金標準。

## Core Mechanism

**A/B testing** (also called **split testing** or **randomized controlled experiment**) is a method for comparing two versions of a product, feature, or intervention to determine which performs better on a specified metric. It is the gold standard for establishing **causal** relationships between changes and outcomes.

### Experimental Design

1. **Define the hypothesis**: Specify what you expect the change to achieve (e.g., "A new button color will increase click-through rate")
2. **Choose the metric**: Select a primary success metric (conversion rate, revenue per user, engagement time)
3. **Randomize**: Randomly assign users to the **control group** (A — existing version) and **treatment group** (B — new version)
4. **Run the experiment**: Expose each group to their respective version for a sufficient duration
5. **Analyze results**: Use statistical tests to determine if the difference is significant
6. **Decide**: Ship the winner, iterate, or declare no significant difference

### Why Randomization Matters

Randomization ensures that the only systematic difference between groups is the treatment itself. Without randomization, observed differences could be caused by **confounding variables** — pre-existing differences between the groups rather than the treatment effect. This is the same principle underlying clinical trials like the [[logistic-regression|Framingham Heart Study]], though Framingham was observational rather than experimental.

## Statistical Framework

### Hypothesis Testing

A/B testing uses the **frequentist hypothesis testing** framework:

- **Null hypothesis (H0)**: There is no difference between A and B (the treatment has no effect)
- **Alternative hypothesis (H1)**: There is a difference (the treatment has an effect)
- **p-value**: The probability of observing a difference as large as (or larger than) the one measured, assuming H0 is true
- **Significance level ($\alpha$)**: The threshold below which $p$ is considered significant (typically $\alpha = 0.05$)

### Key Statistical Concepts

| Concept | Definition | Typical Target |
|---------|------------|----------------|
| **Statistical significance** | p-value $< \alpha$ | $\alpha = 0.05$ (5%) |
| **Statistical power** | Probability of detecting a true effect | 80% or higher |
| **Type I error** | False positive — declaring an effect when none exists | Controlled by $\alpha$ |
| **Type II error** | False negative — missing a real effect | Controlled by power |
| **Minimum Detectable Effect (MDE)** | Smallest effect size the test can reliably detect | Depends on sample size |
| **Confidence interval** | Range of plausible values for the true effect | 95% CI |

### Sample Size Calculation

Before running an A/B test, calculate the required sample size:

$$n = \frac{(Z_{\alpha/2} + Z_{\beta})^2 \cdot 2p(1-p)}{\delta^2}$$

where:
- $Z_{\alpha/2}$: Z-score for significance level (1.96 for $\alpha = 0.05$)
- $Z_{\beta}$: Z-score for power (0.84 for 80% power)
- $p$: Baseline conversion rate
- $\delta$: Minimum detectable effect (absolute difference)

Underpowered tests (insufficient sample size) frequently fail to detect real effects, leading to incorrect conclusions.

### Worked Example: Checkout Button Color

Suppose a baseline checkout conversion rate is $p = 0.12$ and we want to detect a minimum lift of $\delta = 0.01$ (from 12% to 13%) at $\alpha = 0.05$ and 80% power:

$$n = \frac{(1.96 + 0.84)^2 \cdot 2 \cdot 0.12 \cdot 0.88}{0.01^2} = \frac{7.84 \cdot 0.2112}{0.0001} \approx 16{,}558 \text{ users per arm}$$

A 1-percentage-point lift therefore requires ~33,000 users total. Halving the MDE to 0.5pp quadruples the required sample to ~132,000 per arm — a reminder that detecting small effects is expensive. This calculation is the same Z-score arithmetic behind the confidence intervals reported in the Framingham [[logistic-regression|Logistic Regression]] coefficients.

## Connection to EEMT5500 Concepts

While A/B testing is not a standalone lecture in EEMT5500, the course builds the statistical foundation essential for understanding and conducting A/B tests:

### Cross-Validation (Lecture 5)

**K-fold cross-validation** in [[decision-trees|Decision Trees]] is conceptually related to A/B testing — both involve splitting data into groups and comparing performance metrics. Cross-validation tests model performance; A/B testing tests intervention effectiveness. Both guard against overfitting to a single sample.

### Confusion Matrix Metrics (Lectures 5-6)

The accuracy, false positive rate, and false negative rate metrics used to evaluate [[decision-trees|Decision Trees]] and [[nlp-basics|NLP Basics]] models are directly analogous to A/B testing metrics:
- **False positive rate** = Type I error rate
- **False negative rate** = 1 - Power (Type II error rate)
- The trade-off between sensitivity and specificity mirrors the trade-off between detection power and false alarm rate in experiments

### Regression for Analysis (Lectures 2-4)

A/B test results are often analyzed using [[linear-regression|Linear Regression]] (for continuous outcomes) or [[logistic-regression|Logistic Regression]] (for binary outcomes), with the treatment indicator as a predictor variable. Regression allows controlling for covariates and estimating treatment effects with confidence intervals.

## Practical Implementation

### Common Testing Scenarios

| Domain | Control (A) | Treatment (B) | Metric |
|--------|-------------|---------------|--------|
| **E-commerce** | Current product page | New layout/design | Conversion rate |
| **Email marketing** | Subject line A | Subject line B | Open rate, click rate |
| **Pricing** | Current price | Discounted price | Revenue per user |
| **UX design** | Blue button | Green button | Click-through rate |
| **Recommendation** | Algorithm v1 | Algorithm v2 | Engagement, retention |

### Common Pitfalls

1. **Peeking**: Checking results before the experiment reaches its planned sample size inflates false positive rates. Use sequential testing methods if early stopping is needed.

2. **Multiple comparisons**: Testing many variants simultaneously (A/B/C/D...) without correction inflates Type I error. Apply Bonferroni correction or control the False Discovery Rate.

3. **Novelty/primacy effects**: Users may initially engage more (or less) with a new experience simply because it is different. Allow sufficient time for effects to stabilize.

4. **Simpson's paradox**: Overall results may differ from segment-level results. Always check key segments (new vs. returning users, mobile vs. desktop).

5. **Metric gaming**: Optimizing a single metric may harm other important metrics. Track guardrail metrics alongside the primary metric.

6. **Survivorship bias**: If the treatment causes some users to drop out, comparing only remaining users is biased. Use intent-to-treat analysis.

## Bayesian A/B Testing

An alternative to the frequentist approach is **Bayesian A/B testing**, which:
- Produces a **probability that B is better than A** (more intuitive than p-values)
- Incorporates **prior beliefs** about likely effect sizes
- Enables **continuous monitoring** without the peeking problem
- Provides **credible intervals** rather than confidence intervals

Many modern experimentation platforms (Optimizely, VWO, Google Optimize) offer both frequentist and Bayesian analysis.

## Industry Scale

Major technology companies run thousands of A/B tests simultaneously:
- **Google**: Runs over 10,000 experiments per year on search alone
- **Netflix**: Tests every aspect of the UI, from artwork to recommendation algorithms
- **Amazon**: Continuous experimentation on pricing, layout, and features
- **Microsoft (Bing)**: The experimentation platform processes billions of data points daily

A/B testing culture is considered a key competitive advantage in technology companies, enabling rapid, evidence-based iteration.

## Connection to Course Case Studies

Although EEMT5500 does not run an end-to-end A/B test, each of its case studies touches a piece of the machinery:

- **Moneyball (Lecture 3)**: The Oakland A's effectively ran a natural experiment — replacing Giambi/Damon/Isringhausen with cheaper OBP/SLG-matched players — and measured the Wins residual against the predicted 95 wins. A proper A/B test would randomize rosters, which is impossible in sport, so [[linear-regression|Linear Regression]] with a treatment dummy serves as the observational substitute.
- **Framingham (Lecture 4)**: The original cohort is observational, but the downstream public-health response (ALLHAT for diuretics, statin trials) used randomized A/B testing to validate Framingham's [[logistic-regression|Logistic Regression]] risk-factor findings before drugs were approved.
- **Supreme Court (Lecture 5)**: Martin's head-to-head CART-vs-experts competition is structurally an A/B test with n=68 cases, accuracy as the metric, and a 16-point gap (75% vs 59%) that is statistically significant even at this small sample size.
- **Apple tweets (Lecture 6)**: Comparing CART cp=0.034 (88.45%) against Random Forest (88.73%) on the same 355-tweet test set is an A/B comparison of classifiers; the 0.28-point gap on n=355 is within noise, showing why sample size matters.
- **Netflix Prize (Lecture 7)**: Netflix ran continuous online A/B tests against Cinematch throughout the competition before adopting any submitted algorithm — offline RMSE gains did not guarantee online engagement gains.

## Related Concepts

- [[wiki/concepts/hypothesis-testing|Hypothesis Testing]] — the statistical engine underlying A/B tests (t-tests, z-tests, p-values, power)
- [[linear-regression|Linear Regression]] — used to analyze A/B test results with continuous outcomes
- [[logistic-regression|Logistic Regression]] — used to analyze A/B test results with binary outcomes
- [[decision-trees|Decision Trees]] — cross-validation shares conceptual parallels with experimental design
- [[nlp-basics|NLP Basics]] — A/B testing different messaging or content variants
- [[recommendation-systems|Recommendation Systems]] — A/B testing is essential for evaluating recommendation algorithm changes
- [[benfords-law|Benford's Law]] — both rely on comparing observed distributions against expected distributions
- [[clustering|Clustering]] — cluster-then-test enables heterogeneous treatment effect estimation across segments
- [[pca|PCA]] — dimensionality reduction can collapse correlated guardrail metrics into interpretable composite scores
- [[wiki/entities/hkust|HKUST]] — course home institution
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Statistical Learning for OR)

## Source Materials

- [[wiki/sources/courses/applied-statistics|EEMT5500 Applied Probability, Statistics and Data Analytics]]
