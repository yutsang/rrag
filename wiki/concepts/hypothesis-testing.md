---
title: "Hypothesis Testing"
full_name: "Statistical Hypothesis Testing"
type: concept
tags: [statistics, inference, hypothesis-testing, engineering-statistics]
created: "2026-04-14"
updated: "2026-04-14"
source: "https://en.wikipedia.org/wiki/Statistical_hypothesis_test"
confidence: high
---

## 概述

假設檢定是統計推斷的核心程序，透過從樣本數據計算檢定統計量並與理論分佈比較，對總體參數在預設顯著性水準 α 下作出拒絕或不拒絕虛無假設的二元決策。主要檢定類型包括：z 檢定（大樣本已知 σ）、單樣本與雙樣本 t 檢定（小樣本未知 σ）、配對 t 檢定、F 檢定（方差比）、卡方拟合度檢定與獨立性檢定，以及比較三組或以上均值的 ANOVA；每種方法對應明確的適用條件與假設前提。第一類錯誤（假陽性，概率 = α）與第二類錯誤（假陰性，概率 = β）之間存在不可消除的權衡——提高統計功效（1-β）需要增加樣本量或放寬 α，而樣本量計算公式將顯著性水準、功效、效應量三者連結為可操作的設計參數。常見誤用包括：p 值濫用（p-hacking）、將統計顯著性等同於實際重要性（忽略效應量 Cohen's d、η²）、在大樣本下微小差異自動顯著，以及正態性假設違反時未轉用 Mann-Whitney U 等非參數替代方法。假設檢定廣泛應用於[[ab-testing|A/B 測試]]（雙樣本比例 z 檢定）、[[linear-regression|線性回歸]]係數顯著性（t 檢定）、[[benfords-law|Benford's Law]]偏差量化（卡方檢定），以及製造業品質管控與隨機模擬輸出的統計比較。

## What It Is

**Hypothesis testing** is a formal statistical procedure for deciding whether observed data are consistent with a specific claim (hypothesis) about a population. The procedure produces a binary decision: reject or fail to reject the **null hypothesis** H₀.

The process is inherently probabilistic — it does not prove that H₀ is true or false, only that the observed data are (un)likely under H₀.

## Why It Matters

Hypothesis testing underpins:
- **A/B testing** in product development and e-commerce (see [[wiki/concepts/ab-testing|A/B Testing]])
- **Quality control** in manufacturing (control charts, acceptance sampling)
- **Scientific inference** across medicine, engineering, and social science
- **Regression analysis** — testing whether coefficients are significantly different from zero (see [[wiki/concepts/linear-regression|Linear Regression]])
- **Operations research** — validating simulation output, comparing system configurations

## How It Works

### Step 1: State the Hypotheses

- **Null hypothesis H₀**: The default assumption; typically states "no effect," "no difference," or a specific parameter value (e.g., H₀: μ = μ₀).
- **Alternative hypothesis H₁ (Hₐ)**: The claim to be supported; states a departure from H₀.

**Directionality**:
- *Two-tailed*: H₁: μ ≠ μ₀ — tests for any difference
- *One-tailed (right)*: H₁: μ > μ₀ — tests for increase
- *One-tailed (left)*: H₁: μ < μ₀ — tests for decrease

### Step 2: Choose Significance Level α

**α** (alpha) is the probability of rejecting H₀ when it is actually true (**Type I error** / false positive). Common choices:
- α = 0.05 (5%): standard in social science and engineering
- α = 0.01 (1%): stricter, used in safety-critical applications
- α = 0.001 or lower: clinical trials, particle physics

The choice of α is made *before* seeing data, not after.

### Step 3: Compute the Test Statistic

The **test statistic** standardizes the observed data into a single number that measures how far the sample is from what H₀ predicts.

### Step 4: Determine the p-value or Critical Region

- **p-value**: Probability of observing a test statistic at least as extreme as the one computed, *assuming H₀ is true*.
  - p < α → reject H₀
  - p ≥ α → fail to reject H₀
- **Critical region**: Reject H₀ if the test statistic falls in the rejection region defined by the critical value z_{α/2} or t_{α/2,df}.

### Step 5: Make a Decision and Interpret

"Reject H₀" means the data provide sufficient evidence against H₀ at the chosen significance level. "Fail to reject H₀" does NOT mean H₀ is true — it means the data are not strong enough to reject it.

## Types of Errors

| | H₀ True | H₀ False |
|---|---|---|
| **Reject H₀** | Type I Error (α) | Correct (Power = 1−β) |
| **Fail to reject H₀** | Correct (1−α) | Type II Error (β) |

- **Type I Error (false positive)**: Rejecting a true H₀. Probability = α.
- **Type II Error (false negative)**: Failing to reject a false H₀. Probability = β.
- **Power (1−β)**: Probability of correctly rejecting a false H₀. Increases with larger sample size and larger true effect size.

The trade-off: reducing α (stricter standard) increases β (more missed detections). Power analysis determines the sample size needed to achieve both acceptable α and β.

## Key Tests

### z-Test
- **When to use**: Large samples (n ≥ 30) with known population standard deviation σ.
- **Test statistic**: Z = (x̄ − μ₀) / (σ / √n)
- **Distribution under H₀**: Standard normal N(0,1)
- **Critical values**: z_{0.025} = 1.96 for two-tailed α = 0.05

### One-Sample t-Test
- **When to use**: Small or moderate samples with unknown σ.
- **Test statistic**: T = (x̄ − μ₀) / (s / √n)
- **Distribution under H₀**: t-distribution with df = n−1
- As n increases, t-distribution → standard normal

### Two-Sample t-Test
- **When to use**: Comparing means of two independent groups.
- **H₀**: μ₁ = μ₂
- **Variants**: equal variances (pooled) vs. unequal variances (Welch's t-test)
- Core of [[wiki/concepts/ab-testing|A/B testing]] — compare treatment vs. control group outcomes

### Paired t-Test
- **When to use**: Two measurements on the same subjects (before/after, matched pairs).
- Compute differences dᵢ = x₁ᵢ − x₂ᵢ; test whether mean difference d̄ = 0.
- More powerful than two-sample t-test when pairing reduces variance.

### F-Test
- **When to use**: Comparing variances of two populations, or testing overall significance of a regression model.
- **Test statistic**: F = s₁²/s₂² (variance ratio) or MSR/MSE (regression)
- Distribution under H₀: F-distribution with (df₁, df₂) degrees of freedom

### Chi-Square Test
- **Goodness-of-fit**: Does observed frequency distribution match a theoretical distribution?
- **Test of independence**: Are two categorical variables independent?
- **Test statistic**: χ² = Σ (Observed − Expected)² / Expected
- Distribution under H₀: chi-square distribution with df = (rows−1)(cols−1)

## ANOVA (Analysis of Variance)

**ANOVA** extends the two-sample t-test to compare means across k ≥ 3 groups simultaneously, avoiding the inflated Type I error of multiple pairwise t-tests.

- **H₀**: All group means are equal (μ₁ = μ₂ = … = μₖ)
- **Test statistic**: F = MSB/MSW (between-group variance / within-group variance)
- Significant F → at least one group mean differs; post-hoc tests (Tukey, Bonferroni) identify which pairs differ
- **One-way ANOVA**: one factor; **Two-way ANOVA**: two factors, can test interaction effects

## Common Pitfalls

- **p-hacking**: Running many tests and only reporting those with p < α inflates Type I error. Pre-register hypotheses and use corrections (Bonferroni: α* = α/m for m tests).
- **Misinterpreting p-value**: p = 0.04 does NOT mean "96% probability that H₁ is true." It means "if H₀ were true, only 4% of samples would show this extreme a result."
- **Statistical vs. practical significance**: A very large sample can make a tiny, practically irrelevant difference statistically significant. Always report **effect size** (Cohen's d, η²) alongside p-values.
- **Assuming normality**: t-tests are robust to mild non-normality for large n (CLT), but small samples from skewed distributions require non-parametric alternatives (Mann-Whitney U, Wilcoxon).

## Practical Examples

### A/B Testing in E-commerce
An online retailer tests two checkout button colors. Control: blue (n=500, conversion rate 4.2%); Treatment: green (n=500, conversion rate 5.1%). Two-proportion z-test: is the difference statistically significant? If p < 0.05, deploy green. See [[wiki/concepts/ab-testing|A/B Testing]].

### Quality Control in Manufacturing
A factory targets bolt diameter μ = 10mm with σ = 0.05mm. A sample of n=25 yields x̄ = 10.03mm. One-sample z-test: Z = (10.03−10)/(0.05/5) = 3.0 > z_{0.025} = 1.96. Reject H₀ — the process is out of spec. Trigger investigation.

### Regression Significance
In a linear regression of sales on advertising spend, the slope coefficient β₁ has t-statistic = 3.8, p = 0.001. At α = 0.05, reject H₀: β₁ = 0 — advertising spend significantly predicts sales. See [[wiki/concepts/linear-regression|Linear Regression]].

## Related Concepts

- [[wiki/concepts/ab-testing|A/B Testing]]
- [[wiki/concepts/linear-regression|Linear Regression]]
- [[wiki/concepts/logistic-regression|Logistic Regression]]
- [[wiki/concepts/statistical-quality-control|Statistical Quality Control]]
- [[probability-theory]]
- [[wiki/sources/courses/ieda-engineering-statistics|IEDA 2540: Engineering Statistics]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
