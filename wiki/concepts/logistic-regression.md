---
title: "Logistic Regression"
full_name: "Logistic Regression (Binary Classification)"
type: concept
tags: [statistics, classification, machine-learning, supervised-learning, healthcare-analytics]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/applied-statistics"
confidence: high
---

## 概述

邏輯回歸是一種將線性模型延伸至二元分類問題的統計方法，透過 Sigmoid 函數將線性組合映射至0到1之間的概率值，並以對數概似估計法（MLE）取代 OLS 進行參數估計，因而不存在封閉式解析解。其輸出的勝算比（odds ratio）具有直觀的可解釋性，使其成為醫療、金融與保險等受監管領域的首選分類模型。EEMT5500 課程以 Framingham 心臟研究為案例，展示如何使用15個臨床特徵（年齡、性別、血壓、膽固醇、血糖等）預測10年冠心病風險，並通過混淆矩陣和 ROCR 曲線示範不同分類閾值對靈敏度與特異度的權衡。模型評估的核心議題在於類別不平衡（只有約15%的受試者患病），此時單純依賴準確率指標會嚴重誤導決策，AUC-ROC 和精確率-召回率曲線才是更可靠的評估工具。在運籌學與機器學習研究中，邏輯回歸亦作為強基準模型（baseline classifier），用於與決策樹、隨機森林及梯度提升等非參數方法進行比較，其正則化版本（L1/L2 懲罰）則能有效處理高維稀疏特徵空間。

## Core Mechanism

**Logistic regression** models the probability of a binary outcome (0 or 1) using the **sigmoid (logistic) function**:

$$P(y = 1 \mid x) = \frac{1}{1 + e^{-z}}$$

where $z = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p$ is a linear combination of predictors, identical in form to [[linear-regression|Linear Regression]]. The sigmoid function maps any real-valued z to a probability between 0 and 1, creating an S-shaped curve.

### The Logit Transformation

The **logit** is the inverse of the sigmoid — it transforms a probability into a linear scale:

$$\text{logit}(p) = \ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p$$

The term $\frac{p}{1-p}$ is called the **odds** (e.g., if P = 0.75, the odds are 3:1). The logit is the natural logarithm of the odds, hence logistic regression is sometimes called **log-odds regression**.

### Odds Ratios

The exponentiated coefficient $e^{\beta_j}$ gives the **odds ratio** for predictor $x_j$: the multiplicative change in odds for a one-unit increase in $x_j$, holding other predictors constant.

- Odds ratio > 1: Increasing x_j increases the probability of y = 1
- Odds ratio = 1: No effect
- Odds ratio < 1: Increasing x_j decreases the probability of y = 1

For example, if the coefficient for smoking is 0.47, then $e^{0.47} = 1.60$, meaning smokers have **1.6 times the odds** of the outcome compared to non-smokers, all else equal.

### Estimation

Unlike OLS in linear regression, logistic regression uses **Maximum Likelihood Estimation (MLE)**. The likelihood function represents the probability of observing the actual outcomes given the model parameters, and MLE finds the parameters that maximize this probability. There is no closed-form solution — iterative numerical methods (e.g., Newton-Raphson, IRLS) are used.

## Case Study: Framingham Heart Study (Lecture 4)

The **Framingham Heart Study** is one of the most important longitudinal studies in medical history. Begun in 1948, it enrolled **5,209 adult subjects** (ages 30-62) from Framingham, Massachusetts, with the goal of identifying risk factors for cardiovascular disease.

**Predictor variables** used in the EEMT5500 logistic regression model:

| Variable | Type | Description |
|----------|------|-------------|
| Age | Continuous | Age in years |
| Sex | Binary | Male (1) or Female (0) |
| SysBP | Continuous | Systolic blood pressure (mmHg) |
| TotChol | Continuous | Total cholesterol (mg/dL) |
| CigDay | Continuous | Cigarettes smoked per day |
| BMI | Continuous | Body mass index |
| Diabetes | Binary | Diabetic status |
| Glucose | Continuous | Blood glucose level (mg/dL) |

**Outcome variable**: 10-year risk of coronary heart disease (CHD) — binary (yes/no).

### Model Results and Interpretation

Starting from 3,658 complete-case observations and a 65/35 stratified split (`set.seed(1000)` in `caTools::sample.split`), the full 15-variable `glm(TenYearCHD ~ ., family = binomial)` on 2,378 training cases identified `male`, `age`, `education`, `cigsPerDay`, `totChol`, `sysBP`, and `glucose` as significant at $\alpha = 0.05$. Notably `sysBP` and `diaBP` correlate at 0.78, and `currentSmoker` with `cigsPerDay` at 0.77 — classic multicollinearity that causes `diaBP` and `currentSmoker` to lose significance once their correlated partners are in the model.

Re-fitting with only the significant predictors (Model 2):

$$\text{Logit} = -9.02 + 0.58 \cdot \text{male} + 0.070 \cdot \text{age} - 0.125 \cdot \text{education} + 0.020 \cdot \text{cigsPerDay} + 0.0033 \cdot \text{totChol} + 0.0145 \cdot \text{sysBP} + 0.0079 \cdot \text{glucose}$$

### Interpreting Coefficients via Odds Ratios

- Each additional year of age: $e^{0.070} = 1.072$, so odds of CHD rise 7.2% per year.
- Being male vs. female: $e^{0.58} = 1.79$, almost double the odds.
- Smoking one additional cigarette per day: $e^{0.020} = 1.020$, a 2% increase per cigarette (dose-response).
- Education (four levels): each level up reduces CHD odds by $1 - e^{-0.125} = 11.8\%$, though this is confounded with lifestyle.

### Threshold Tuning on the Test Set

Because only ~15% of subjects develop CHD, accuracy is not the right metric. Test-set confusion matrices at three thresholds:

| Threshold | TN | FP | FN | TP | Accuracy | FPR | FNR |
|-----------|-----|-----|-----|-----|----------|-----|-----|
| 0.5 | 1078 | 7 | 177 | 18 | 85.63% | 0.65% | 90.77% |
| 0.2 | 837 | 248 | 96 | 99 | 73.13% | 22.86% | 49.23% |
| 0.1 | 495 | 590 | 33 | 162 | 51.33% | 54.38% | 16.92% |
| Baseline (predict 0) | 1085 | 0 | 195 | 0 | 84.77% | 0% | 100% |

At $t = 0.5$ the model barely beats the "always healthy" baseline on accuracy but misses 90% of real CHD cases. Moving to $t = 0.2$ catches roughly half the at-risk patients at the cost of 23% false alarms — a reasonable trade-off when the downstream intervention is cheap (lifestyle counseling) and missing a case is costly (heart attack). The **ROCR package** draws the full FPR-FNR curve across all thresholds:

```r
library(ROCR)
ROCRpred = prediction(predictTrain, Train$TenYearCHD)
ROCRperf = performance(ROCRpred, "fnr", "fpr")
plot(ROCRperf, colorize = TRUE, print.cutoffs.at = c(0.1, 0.2, 0.3, 0.4, 0.5, 0.6))
```

### Clinical Decision Making

The Framingham model illustrates a key advantage of logistic regression over black-box classifiers: **interpretability**. Clinicians can explain to patients exactly which factors contribute to their risk and by how much. The odds ratios provide actionable insights:
- "Quitting smoking would reduce your CHD odds by X%"
- "Reducing your blood pressure by 10 points would decrease your risk by Y%"

This interpretability makes logistic regression the **preferred model in regulated domains** (healthcare, finance, insurance) where decisions must be explainable.

## Model Evaluation

Logistic regression models are evaluated differently from linear regression:

| Metric | Description |
|--------|-------------|
| **Accuracy** | (TP + TN) / Total — overall correct classification rate |
| **Sensitivity (Recall)** | TP / (TP + FN) — proportion of actual positives correctly identified |
| **Specificity** | TN / (TN + FP) — proportion of actual negatives correctly identified |
| **AUC-ROC** | Area under the Receiver Operating Characteristic curve — threshold-independent measure |
| **Confusion Matrix** | 2x2 table of TP, TN, FP, FN counts |

The **classification threshold** is a critical choice. In medical applications, a lower threshold (e.g., 0.05) increases sensitivity at the cost of specificity — it is better to over-flag potential heart disease cases than to miss them.

## Comparison with Other Classifiers

| Criterion | Logistic Regression | [[decision-trees|Decision Trees]] | Random Forest |
|-----------|--------------------|--------------------|---------------|
| Interpretability | High (coefficients, odds ratios) | Medium (tree visualization) | Low |
| Non-linear relationships | Requires manual feature engineering | Captures automatically | Captures automatically |
| Overfitting risk | Low (fewer parameters) | Medium (pruning needed) | Low (ensemble averaging) |
| Speed | Fast | Fast | Slower |
| Best for | Interpretable risk scoring | Rule-based classification | Maximum accuracy |

## Practical Considerations

- **Class imbalance**: When the outcome is rare (e.g., 5% CHD rate), accuracy is misleading. A model predicting "no CHD" for everyone achieves 95% accuracy. Use AUC-ROC, precision-recall curves, or class-weighted models.
- **Multicollinearity**: Correlated predictors inflate standard errors and make individual coefficients unreliable. Check VIF values.
- **Linearity in log-odds**: Logistic regression assumes each predictor has a linear relationship with the log-odds of the outcome. Non-linear effects require polynomial terms or splines.
- **Sample size**: Rule of thumb — at least 10-20 events per predictor variable (Events Per Variable, EPV).

## Worked Example: LendingClub Loan Default (HW2)

HW2 applies logistic regression to `Loans.csv`, 9,578 three-year loans funded through LendingClub.com between May 2007 and February 2010, predicting the binary `NotFullyPaid` outcome from 17 borrower features (credit policy, loan purpose dummies, IntRate, Installment, LogAnnualInc, DTI, FICO, days with credit line, revolving balance/utilization, inquiries, delinquencies, public records). A 70/30 stratified split leaves ~6,700 training rows; the simple "predict fully paid" baseline already achieves **84.0%** accuracy because only ~16% of loans default.

The full `glm(NotFullyPaid ~ ., family="binomial")` identifies **CreditPolicy, Purpose.CC, Purpose.DC, Purpose.SB, Installment, LogAnnualInc, FICO, RevolBal, InqLast6mths, and PubRec** as significant at $\alpha = 0.05$, but at a 0.5 threshold it predicts "default" for only 23 of 2,873 test loans, barely edging the baseline to **84.0%**. A worked piece of coefficient arithmetic: the FICO coefficient is $-0.00734$, so two otherwise identical applicants differing only by 10 FICO points have a logit gap of $(-0.00734)(-10) = 0.0734$ — i.e., the 700 applicant has $e^{0.0734} \approx 1.076$ times the odds of default relative to the 710 applicant, a small but monotone effect.

Part (b) refits the model on **`IntRate` alone**. IntRate is highly significant by itself ($\hat{\beta} = 17.1$) yet was *insignificant* in the full model — a clean multicollinearity signal, since LendingClub's own underwriting already bakes risk features into the rate. Using just IntRate, the maximum predicted default probability on the test set is only **0.452**, so at threshold 0.5 the model never predicts default at all: a "smart baseline" for ranking but useless as a classifier without threshold tuning. The takeaway parallels Framingham's: in imbalanced lending data, threshold choice and rank-ordering (AUC) matter far more than headline accuracy.

## Worked Example: Parole Violator Prediction (Midterm)

The midterm exam applies logistic regression to `Parole.csv` — parolees in 2004 who served ≤ 6 months with maximum sentences ≤ 18 months. Features include `Male`, `RaceWhite`, `Age`, `State` (Kentucky / Louisiana / Virginia / Other), `TimeServed`, `MaxSentence`, `MultipleOffences`, and `Crime` (Larceny / Drugs / Driving / Other); the target is `Violator`. The exam walks through (i) reading coefficients, (ii) scoring a specific applicant by hand, (iii) computing test-set FPR / FNR at threshold 0.5, (iv) comparing to the "everyone non-violator" baseline, and (v) arguing about *which* error a real parole board would care about more. The parole board cares about **false negatives** — releasing someone who re-offends — so the correct move is to **lower** the threshold from 0.5, accepting more false positives (deny parole to a non-violator) to reduce the rarer but costlier false negative. This is the same logic as clinical CHD screening in Framingham, but with the asymmetry running in the opposite direction across the confusion matrix.

## External Validation of the Framingham Model

Internal train/test splits measure in-population generalization; external validation measures cross-population generalization. The Framingham model was re-tested on four diverse cohorts:

| Cohort | Population | Result |
|--------|-----------|--------|
| ARIC | White and Black Americans | Accurate for Black men (n = 1,428) despite higher diabetes |
| HHP (Honolulu) | Japanese American men (n = 2,755) | Systematically **overpredicts** CHD |
| PR | Hispanic Americans | Mixed calibration |
| SHS | Native Americans | Mixed calibration |

The lesson: a model trained on white, middle-class Framingham residents will miscalibrate on populations with different lifestyle, genetic, and dietary profiles. This motivated subsequent cohort expansions (second generation 1971, third 2002, more diverse groups 1994 and 2003) and genome-wide association studies.

## Public Health Impact

The Framingham study gave **Ed Freis** the evidence needed to argue for the VA Trial of the diuretic chlorothiazide (a randomized double-blind clinical trial), which reduced CHD risk significantly — now a $1B+ global diuretics market. Later, Framingham data supported the statin trials: a study of 4,444 CHD patients showed statins cut second heart attack risk by 37%, and a study of 6,595 men with high cholesterol showed a 32% reduction in cardiovascular death. Statins are now a $20B+ global market. More than 2,400 studies use Framingham data, and the study is listed among the top 10 cardiology advances of the 20th century.

## Related Concepts

- [[linear-regression|Linear Regression]] — the continuous-outcome counterpart; logistic regression adapts the same linear framework
- [[decision-trees|Decision Trees]] — alternative classifier that captures non-linear patterns automatically
- [[nlp-basics|NLP Basics]] — text classification tasks often use logistic regression as a baseline
- [[benfords-law|Benford's Law]] — another probability-based detection framework
- [[ab-testing|A/B Testing]] — uses similar statistical testing for binary outcome experiments
- [[clustering|Clustering]] — unsupervised alternative when labels are unavailable
- [[wiki/entities/hkust|HKUST]] — course home institution
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Statistical Learning for OR)

## Source Materials

- Lecture 4: Framingham Heart Study (Logistic Regression)
- [[wiki/sources/courses/applied-statistics|EEMT5500 Applied Probability, Statistics and Data Analytics]]
