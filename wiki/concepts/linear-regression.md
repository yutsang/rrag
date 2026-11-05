---
title: "Linear Regression"
full_name: "Linear Regression (OLS)"
type: concept
tags: [statistics, regression, machine-learning, prediction, supervised-learning]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/applied-statistics"
confidence: high
---

## 概述

線性回歸是統計學與機器學習中最基本的監督式學習模型，透過最小化殘差平方和（OLS）來擬合因變量與一個或多個自變量之間的線性關係，並在 Gauss-Markov 假設成立時產生最佳線性無偏估計量（BLUE）。其核心評估指標包括 $R^2$、調整後 $R^2$、RMSE 以及 AIC/BIC，而多重共線性診斷（VIF）、殘差分析與交叉驗證則是確保模型品質的關鍵工具。EEMT5500 課程以紅酒定價（Ashenfelter 模型）和 Moneyball 棒球分析為案例，具體展示線性回歸如何透過量化隱性市場效率——從天氣變數預測葡萄酒年份品質、用 OBP 和 SLG 替代傳統球探判斷——在實際商業決策中系統性地超越領域專家。線性回歸在運籌學研究中扮演雙重角色：它既是統計預測的起點，也是理解廣義最小二乘法、嶺迴歸、主成分迴歸（PCR）及 LASSO 等進階方法的理論基礎。模型的重要侷限在於它僅能捕捉線性關聯，且對異方差、多重共線性及離群值敏感，超出訓練樣本範圍外的預測可能嚴重失準。

## Core Mechanism

**Linear regression** models the relationship between a dependent variable y and one or more independent variables x as a linear equation:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_p x_p + \varepsilon$$

where:
- $\beta_0$ is the intercept ($y$ value when all predictors are 0)
- $\beta_1 \ldots \beta_p$ are the regression coefficients (slope of each predictor)
- $\varepsilon$ is the error term (assumed normally distributed with mean 0)

### Ordinary Least Squares (OLS) Estimation

The **OLS** method estimates coefficients by minimizing the **Sum of Squared Errors (SSE)**:

$$SSE = \sum_i (y_i - \hat{y}_i)^2$$

This produces the best linear unbiased estimates (BLUE) under the Gauss-Markov assumptions: linearity, independence, homoscedasticity (constant variance of errors), normality of errors, and no perfect multicollinearity.

### Model Evaluation Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **SSE** | $\sum_i (y_i - \hat{y}_i)^2$ | Total squared prediction error; lower is better |
| **SST** | $\sum_i (y_i - \bar{y})^2$ | Total variance in the data |
| **$R^2$** | $1 - SSE/SST$ | Proportion of variance explained; 0 to 1 |
| **RMSE** | $\sqrt{SSE/n}$ | Average prediction error in original units |
| **Adjusted $R^2$** | $1 - (1-R^2)\frac{n-1}{n-p-1}$ | $R^2$ penalized for number of predictors |

**R-squared** is the most commonly discussed metric: an $R^2$ of 0.80 means the model explains 80% of the variance in the dependent variable. However, $R^2$ always increases with additional predictors, so **adjusted $R^2$** is preferred for model comparison.

## Case Study: Wine Quality Prediction (Lecture 2)

Princeton economist **Orley Ashenfelter** developed a regression model predicting Bordeaux wine prices based on weather variables, using 25 vintages from 1952-1978 (`wine.csv` in the course materials). His work challenged the expert-based system dominated by critics like **Robert M. Parker Jr.**, who called Ashenfelter "an absolute total sham" and compared him to "a movie critic who never goes to see the movie but tells you how good it is based on the actors and the director."

**Model variables**:

| Variable | Description | Expected Sign |
|----------|-------------|---------------|
| AGST | Average Growing Season Temperature (April-September, °C) | Positive |
| HarvestRain | Rainfall during August-September (mm) | Negative |
| WinterRain | Rainfall during October-March (mm) | Positive |
| Age | Age of wine in 1990 (years) | Positive |
| FrancePop | Population of France (correlates with time) | Ambiguous |

### Incremental Model Fit

Progressive $R^2$ as variables are added:

| Variables | In-sample $R^2$ | Out-of-sample $R^2$ |
|-----------|-----------------|---------------------|
| AGST | 0.44 | 0.79 |
| + HarvestRain | 0.71 | **-0.08** |
| + Age | 0.79 | 0.53 |
| + WinterRain | 0.83 | 0.79 |
| + FrancePop | 0.83 | 0.76 |

The negative out-of-sample $R^2$ after adding HarvestRain is a striking warning: a better in-sample fit can be *worse* on new data, and $R^2$ is unbounded below on held-out data. FrancePop was dropped from the final model because it correlated with Age at $r = -0.9944$ (a textbook case of multicollinearity).

### Final Wine Model (R output)

```r
model4 = lm(Price ~ AGST + HarvestRain + WinterRain + Age, data = wine)
```

$$\text{Price} = -3.43 + 0.607 \cdot \text{AGST} - 0.00397 \cdot \text{HarvestRain} + 0.00108 \cdot \text{WinterRain} + 0.0239 \cdot \text{Age}$$

- AGST: $\hat{\beta} = 0.607$, $p = 5.2 \times 10^{-6}$
- HarvestRain: $\hat{\beta} = -0.00397$, $p = 0.00015$
- Age: $\hat{\beta} = 0.0239$, $p = 0.0078$
- $R^2 = 0.8286$, Adjusted $R^2 = 0.7943$

Ashenfelter's 1989 prediction ("wine of the century") and 1990 prediction (better still) were confirmed by auction prices: the 1989 vintage sold for more than twice the price of 1986, and 1990 sold for even more. Parker himself later conceded that "2000 is the greatest vintage Bordeaux has ever produced" — consistent with Ashenfelter's earlier forecast.

## Case Study: Moneyball (Lecture 3)

**Billy Beane**, General Manager of the Oakland Athletics, used regression analysis on 902 team-seasons (1962-2001) to identify undervalued baseball players, as documented in Michael Lewis's book *Moneyball* (2003). Beane hired Harvard graduate **Paul DePodesta** as his assistant specifically for this analytical work.

**The Problem**: The A's had a payroll of ~$40 million, competing against teams like the New York Yankees at $120M+. Traditional scouting valued batting average (BA), stolen bases, and subjective "tools" assessments. DePodesta framed the problem as: how many regular-season wins are needed for a playoff spot? Answer: **95**.

### Step 1: Wins from Run Differential

```r
WinsReg = lm(W ~ RD, data = moneyball)
```

$$\text{Wins} = 80.8814 + 0.1058 \cdot \text{RunDiff}, \quad R^2 = 0.8808$$

Solving $80.8814 + 0.1058 \cdot \text{RD} \geq 95$ gives $\text{RD} \geq 133.4$, closely matching the A's internal estimate of 135.

### Step 2: Runs Scored from Batting Statistics

The first attempt included BA, OBP, SLG:

$$\hat{RS} = -788.46 + 2917.42 \cdot \text{OBP} + 1637.93 \cdot \text{SLG} - 368.97 \cdot \text{BA}$$

The BA coefficient is *negative* and significant ($p = 0.005$), a tell-tale multicollinearity symptom: $\text{cor}(\text{BA}, \text{OBP}) = 0.8541$. Dropping BA gives the clean model:

$$\hat{RS} = -804.63 + 2737.77 \cdot \text{OBP} + 1584.91 \cdot \text{SLG}, \quad R^2 = 0.9296$$

### Step 3: Runs Allowed from Opponent Statistics

$$\hat{RA} = -837.38 + 2913.60 \cdot \text{OOBP} + 1514.29 \cdot \text{OSLG}, \quad R^2 = 0.9073$$

### Predicting the 2002 Season

Using 2001 player-level statistics (24 batters, 17 pitchers on the A's 2002 roster): team OBP = 0.339, SLG = 0.430, OOBP = 0.307, OSLG = 0.373.

| Metric | Our Prediction | DePodesta Prediction | Actual |
|--------|---------------|---------------------|--------|
| Runs Scored | 805 | 800-820 | 800 |
| Runs Allowed | 622 | 650-670 | 653 |
| Wins | 100 | 93-97 | **103** |

The 2002 A's set an American League record with **20 consecutive wins**. Their success was "20 more wins than teams with equivalent payrolls" in 2002; by 2020, with other teams adopting similar analytics, the A's advantage has shrunk to ~10 wins.

### Playoffs Are Still Luck

Regression on 1996-2011 data shows the correlation between regular-season wins and winning the World Series is only **0.03**. Beane's mantra: build to reach the playoffs; once there, "anything can happen." This is the analytical justification for not trying to model the World Series itself.

### Why This Matters for Business

The Moneyball case demonstrates **market inefficiency exploitation through analytics**. In any domain where human judgment creates systematic biases in valuation, regression can identify underpriced assets. This principle applies to:
- Talent acquisition (hiring undervalued employees)
- Investment (identifying mispriced securities)
- Marketing (finding undervalued customer segments)

## Assumptions and Diagnostics

Linear regression requires several assumptions that should be checked:

1. **Linearity**: Plot residuals vs. fitted values — should show no pattern
2. **Independence**: Observations should not be correlated (especially important in time series)
3. **Homoscedasticity**: Residual variance should be constant across fitted values
4. **Normality**: Residuals should be approximately normally distributed (Q-Q plot)
5. **No multicollinearity**: Predictors should not be highly correlated with each other (check VIF)

Violations can be addressed through transformations (log, polynomial), weighted least squares, or switching to alternative models like [[logistic-regression|Logistic Regression]] for binary outcomes or [[decision-trees|Decision Trees]] for non-linear relationships.

## Practical Considerations

- **Overfitting**: Adding too many predictors improves training $R^2$ but degrades out-of-sample performance. Use adjusted R², AIC/BIC, or cross-validation for model selection.
- **Outliers**: Influential observations can dramatically affect coefficients. Use Cook's distance or leverage plots to identify them.
- **Interpretation**: Each coefficient represents the change in y for a one-unit change in x, **holding all other variables constant** (ceteris paribus).
- **Causation vs. Correlation**: Regression identifies associations, not causal relationships. The wine model shows that weather predicts price, but weather does not "cause" price in a direct interventional sense.

## Climate Change Application (HW1)

HW1 applies linear regression to `ClimateChange.csv` (monthly data 1983-2008, split at 2006 for train/test). The eight-variable OLS fit achieves in-sample $R^2 = 0.7509$ but produces significant *negative* coefficients on **N2O and CFC-11** — contradicting the known greenhouse effect of both. The diagnosis: N2O correlates with CO2 at $r = 0.981$, CH4 at 0.894, CFC.12 at 0.839, and CFC-11 with CFC.12 at 0.831, so the multivariate regression cannot disentangle their effects. A reduced model with only MEI, TSI, Aerosols, N2O recovers a positive N2O coefficient ($+0.0253$ vs. $-0.0165$) with in-sample $R^2 = 0.7261$ and test-set $R^2 \approx 0.50$. This is a canonical teaching example of multicollinearity flipping coefficient signs, and the subsequent test-set degradation shows why out-of-sample validation is the final arbiter even when training $R^2$ is healthy.

## Worked Example: State Life Expectancy (HW2)

HW2 uses `StateData.csv` (50 US states, 1970s census) to predict `LifeExp` from Population, Murder, Frost, Income, Illiteracy, Area, HighSchoolGrad with a 70/30 split. The seven-variable OLS fit gives a training $R^2 = 0.7703$ but only $R^2 \approx 0.55$ on the held-out states. Dropping Income, Illiteracy, and Area (none of which were significant) yields a simpler four-variable model:

$$\text{LifeExp} = 70.62 + 4.6 \times 10^{-5}\, \text{Population} - 0.262\, \text{Murder} - 0.00103\, \text{Frost} + 0.0395\, \text{HighSchoolGrad}$$

with training $R^2 = 0.7596$ and **test $R^2 = 0.6033$** — lower on training, higher on test. This is the central lesson: removing insignificant predictors can *improve* out-of-sample performance because it eliminates noise that the larger model was memorizing. HW2 then compares this linear model against a CART regression tree (`minbucket=5`) and a [[decision-trees|Random Forest]] (`nodesize=5`) on the same problem — the simpler linear model wins on out-of-sample $R^2$ against both, a reminder that tree ensembles are not automatically better on small, noisy, approximately-linear datasets (n=35 training rows).

## Related Concepts

- [[logistic-regression|Logistic Regression]] — extends regression to binary classification via the sigmoid function
- [[decision-trees|Decision Trees]] — non-parametric alternative that captures non-linear relationships
- [[benfords-law|Benford's Law]] — another statistical tool for detecting patterns in numerical data
- [[clustering|Clustering]] — unsupervised counterpart to supervised regression
- [[pca|PCA]] — dimensionality reduction technique often used before regression
- [[ab-testing|A/B Testing]] — uses regression-like statistical testing for experimental comparisons
- [[financial-ratios|Financial Ratios]] — quantitative measures that can serve as regression predictors
- [[wiki/entities/hkust|HKUST]] — course home institution
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Financial Time Series and Econometrics / Statistical Learning for OR)

## Source Materials

- Lecture 2: Wine Steward (Linear Regression)
- Lecture 3: Moneyball (Linear Regression)
- [[wiki/sources/courses/applied-statistics|EEMT5500 Applied Probability, Statistics and Data Analytics]]
