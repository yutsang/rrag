---
title: "Applied Probability, Statistics and Data Analytics"
full_name: "Applied Probability, Statistics and Data Analytics (EEMT5500)"
type: source
tags: [course, statistics, machine-learning, data-analytics, regression, classification, clustering, nlp, optimization, eemt5500, level-5]
created: "2026-04-09"
updated: "2026-04-14"
source: "raw/courses/EEMT5500 Applied Probability, Statistics and Data Analytics/"
confidence: high
author: "Xiaowei Zhang (HKUST)"
date_published: "2023"
---

## 概述

EEMT5500「應用概率、統計與資料分析」是香港科技大學工程管理碩士（MSc EEMT）課程的核心必修科，由張曉薇教授主講，以 R 語言為全程實作工具。課程共 12 講，依序涵蓋 Benford's Law（詐欺偵測）、線性迴歸（Bordeaux 葡萄酒定價、Moneyball 棒球分析）、邏輯迴歸（Framingham 心臟病預測）、決策樹 CART 與 Random Forest（美國最高法院判決預測）、文字分析與 NLP（Apple 推文情感分析）、聚類分析與推薦系統（Netflix Prize、MovieLens）及收益管理線性規劃（美國航空 JFK-DFW 容量分配）。課程面向具備一定工程或技術背景但無深厚統計基礎的碩士生，強調「資料驅動的決策模型始終優於專家判斷」的核心洞見，以真實商業案例（Enron 會計詐欺、Madoff 龐氏騙局、Supreme Court 預測）貫穿每個方法的動機與應用邊界。R 軟件包括 `caTools`、`rpart`、`caret`、`tm`、`randomForest`、`lpSolve` 等，三次作業與期中考試覆蓋從迴歸到最佳化的完整工具鏈，小組項目要求學生對自選數據集進行端對端分析。課程與 EEMT5540（IT for E-Commerce）中的機器學習模塊形成緊密的方法呼應，是修讀 EEMT5560（整合商業解決方案）及進行任何數據密集型工程管理研究的重要分析基礎。

## Course Overview

EEMT5500 is taught by Prof. **Xiaowei Zhang** at [[wiki/entities/hkust|HKUST]] within the MSc in Engineering Enterprise Management curriculum. The course spans a Lecture 0 syllabus session plus 12 topical notes that progress from descriptive statistical tests through supervised and unsupervised machine learning, text analytics, optimization, and finance. Every lecture is anchored by a real-world case study and accompanied by reproducible R code using packages `caTools`, `rpart`, `caret`, `tm`, `SnowballC`, `randomForest`, and `lpSolve`.

| Lec | Topic | Case Study | Method Family |
|-----|-------|------------|---------------|
| 1 | [[benfords-law\|Benford's Law]] | Chargeback fraud, Enron, Madoff | Goodness-of-fit |
| 2 | [[linear-regression\|Linear Regression]] | Bordeaux wine (Ashenfelter) | OLS |
| 3 | [[linear-regression\|Linear Regression]] | Moneyball (Oakland A's) | OLS, multicollinearity |
| 4 | [[logistic-regression\|Logistic Regression]] | Framingham Heart Study | MLE, threshold tuning |
| 5 | [[decision-trees\|Decision Trees]] | US Supreme Court (Justice Stevens) | CART, k-fold CV |
| 6 | [[nlp-basics\|NLP Basics]] | Apple tweet sentiment | Bag-of-Words, CART, Random Forest |
| 7 | [[clustering\|Clustering]] and [[recommendation-systems\|Recommendation Systems]] | Netflix Prize, MovieLens | K-means, hierarchical clustering |
| 8 | [[revenue-management\|Revenue Management]] | American Airlines (Crandall) | Linear programming |
| 9 | Google AdWords | Keyword auctions | Second-price auctions |
| 10 | Sports Scheduling | MLB / NBA tournament design | Integer programming |
| 11 | Portfolio Management | Markowitz mean-variance | Quadratic programming |
| 12 | Multi-factor Asset Pricing | Fama-French, CAPM | Regression in finance |

Lectures 9-12 extend optimization and regression into auctions, scheduling, and finance but sit outside the core analytics track that this wiki summarizes. The remainder of this page walks through Lectures 1-8 in depth.

## Software Stack

The course uses R as its primary language, introduced in a dedicated "Intro to R" module. Key packages and their roles:

| Package | Purpose |
|---------|---------|
| `caTools` | `sample.split()` for stratified train/test splits |
| `rpart`, `rpart.plot` | CART trees and visualization |
| `caret` | `train()` with `trainControl` for cross-validation |
| `tm`, `SnowballC` | Text corpus, Porter stemming |
| `randomForest` | Bagged ensemble classifier |
| `ROCR` | ROC / FPR-FNR curves |
| `lpSolve`, `lpSolveAPI` | Linear programming |
| `GGally` | `ggpairs()` correlation matrix plots |

## Lecture 1: Benford's Law

**[[benfords-law|Benford's Law]]** describes the non-uniform distribution of leading digits in naturally occurring datasets:

$$P(d) = \log_{10}\left(1 + \frac{1}{d}\right), \quad d \in \{1, 2, \ldots, 9\}$$

The digit 1 appears as the leading digit approximately 30.1% of the time, while 9 appears only 4.6%. The law's theoretical foundation rests on **scale invariance** — if a dataset spans multiple orders of magnitude, multiplying by any constant preserves the logarithmic first-digit distribution, so the currency unit is irrelevant.

The course demonstrates fraud detection with the **Mean Absolute Deviation (MAD)** statistic against an 11,127-row credit-card chargeback dataset (`trans.csv`):

```r
data = read.csv("trans.csv")
data$FD = as.numeric(substr(data$Amount, 1, 1))
df = data.frame(Digit = 1:9,
                Amount = as.vector(table(data$FD)) / nrow(data),
                Benford = log10(1 + 1/seq(1, 9)))
df$AD = abs(df$Amount - df$Benford)
mean(df$AD)  # MAD = 0.0278
```

The observed distribution (39.6% starting with 1 vs. Benford's 30.1%) yields **MAD = 0.0278**, far above the 0.015 nonconformity threshold — closer investigation is warranted. The course discusses three real cases: the **Enron scandal** (publicized Oct 2001, bankrupt Dec 2001), **Bernie Madoff's** multi-billion-dollar Ponzi scheme, and an anonymous NYSE-listed Chinese mining company flagged by Absaroka Capital Management in 2011 for quarterly reports (March 2008 - September 2010) that did not follow Benford's Law, where the excess of 8s could be explained by the "Lucky Number" theory. The 2009 Iranian election and 2020 U.S. presidential election (Allegheny, PA) are presented as cautionary cases where Benford's Law is unreliable for small-sample, narrow-range data like precinct vote counts.

## Lecture 2-3: Linear Regression

**[[linear-regression|Linear Regression]]** is introduced through the model $y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$, estimated via **Ordinary Least Squares (OLS)** minimizing $\text{SSE} = \sum_i (y_i - \hat{y}_i)^2$. Key metrics covered:

$$\text{RMSE} = \sqrt{\frac{\text{SSE}}{n}}, \quad R^2 = 1 - \frac{\text{SSE}}{\text{SST}}, \quad \text{SST} = \sum_i (y_i - \bar{y})^2$$

**Wine case (Lecture 2)**: Princeton economist **Orley Ashenfelter** built a model predicting Bordeaux wine prices from weather variables (winter rainfall, average growing-season temperature, harvest rainfall, age) on 25 vintages from 1952-1978. Progressive model fit:

| Model | Variables | In-sample $R^2$ | Out-of-sample $R^2$ |
|-------|-----------|-----------------|---------------------|
| 1 | AGST | 0.44 | 0.79 |
| 2 | + HarvestRain | 0.71 | -0.08 |
| 3 | + Age | 0.79 | 0.53 |
| 4 | + WinterRain | 0.83 | 0.79 |
| 5 | + FrancePop | 0.83 | 0.76 |

Model 4 (dropping FrancePop because of near-perfect correlation with Age, $r = -0.994$) yields:

$$\text{Price} = -3.43 + 0.607 \cdot \text{AGST} - 0.00397 \cdot \text{HarvestRain} + 0.00108 \cdot \text{WinterRain} + 0.0239 \cdot \text{Age}$$

Ashenfelter famously predicted 1989 would be "the wine of the century" and 1990 even better, infuriating critic **Robert M. Parker Jr.** who called him "an absolute total sham" — but 1989 sold for more than twice the price of 1986 at auction and 1990 sold for more still.

**Moneyball case (Lecture 3)**: Oakland Athletics GM **Billy Beane** and his Harvard-educated assistant **Paul DePodesta** used regression on 902 team-seasons (1962-2001) to identify undervalued metrics. Three nested models:

1. $\text{Wins} = 80.88 + 0.1058 \cdot \text{RunDiff}$, $R^2 = 0.881$ — solving for Wins $\geq 95$ gives RunDiff $\geq 133.4$
2. $\text{RunsScored} = -804.63 + 2737.77 \cdot \text{OBP} + 1584.91 \cdot \text{SLG}$, $R^2 = 0.930$
3. $\text{RunsAllowed} = -837.38 + 2913.60 \cdot \text{OOBP} + 1514.29 \cdot \text{OSLG}$, $R^2 = 0.907$

Adding batting average to model 2 produced a statistically negative coefficient ($\hat{\beta}_{BA} = -369$) due to multicollinearity with OBP ($r = 0.854$). Using 2001 player-level statistics as inputs, the models predicted 805 runs scored, 622 runs allowed, and 100 wins for the 2002 A's — actual: 800, 653, and 103. The A's set a league record with 20 consecutive wins on a ~$40M payroll while facing Yankees teams spending $120M+. The chapter closes with the insight that playoff outcomes are essentially unpredictable: correlation between regular season wins and World Series titles (1996-2011) is just 0.03.

## Lecture 4: Logistic Regression

**[[logistic-regression|Logistic Regression]]** extends regression to binary classification using the sigmoid function:

$$P(y=1 \mid \mathbf{x}) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k)}}, \quad \log\left(\frac{P(y=1)}{P(y=0)}\right) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k$$

The logit is the natural log of the odds, and coefficients are estimated via **Maximum Likelihood Estimation (MLE)** using iterative methods since there is no closed form.

**Framingham Heart Study**: Launched in 1948 with 5,209 adults aged 30-59 from Framingham, Massachusetts, motivated by President **FDR's** death: his blood pressure reached 300/190 the day he died, yet his physician deemed his arteriosclerosis "no more than normal for a man of his age." The course uses an anonymized cohort of 3,658 complete observations split 65/35 into training (2,378) and test (1,280) sets. Using `glm(TenYearCHD ~ ., family = binomial)`, a reduced model with significant predictors is:

$$\text{Logit} = -9.02 + 0.58 \cdot \text{male} + 0.070 \cdot \text{age} - 0.125 \cdot \text{education} + 0.020 \cdot \text{cigsPerDay} + 0.0033 \cdot \text{totChol} + 0.0145 \cdot \text{sysBP} + 0.0079 \cdot \text{glucose}$$

Because only ~15% of subjects develop CHD, threshold tuning is essential. Test-set confusion matrices:

| Threshold | Accuracy | FPR | FNR |
|-----------|----------|-----|-----|
| 0.5 | 85.63% | 0.65% | 90.77% |
| 0.2 | 73.13% | 22.86% | 49.23% |
| 0.1 | 51.33% | 54.38% | 16.92% |
| Baseline (always 0) | 84.77% | 0% | 100% |

The ROCR package draws an FPR-FNR curve across all thresholds. External validation across diverse cohorts (ARIC for Black subjects, HHP for Japanese Americans, PR for Hispanic, SHS for Native American) showed the model calibrates well for Black men but systematically overpredicts CHD for Japanese Americans, illustrating the limits of models trained on the predominantly white, middle-class Framingham cohort. The study motivated the diuretic chlorothiazide trials and later the statins, now $1B and $20B markets respectively.

## Lecture 5: Decision Trees (CART)

**[[decision-trees|Decision Trees]]** are introduced through the **CART (Classification and Regression Trees)** algorithm. Logistic regression coefficients like "2nd circuit: +1.66, 4th circuit: +2.82, lower court liberal: -1.22" are offered as a counter-example of poor interpretability, motivating the tree approach.

The course uses the `stevens.csv` dataset (566 cases from 1994-2001 when the same nine justices presided, the longest such period in 180+ years), focusing on predicting whether **Justice Stevens** votes to reverse the lower court. Variables: Circuit, Issue, Petitioner, Respondent, LowerCourt, Unconst. A 70/30 stratified split via `sample.split()` gives 396 training / 170 test cases.

```r
library(rpart); library(rpart.plot); library(caret)
# Initial model with minbucket=25
StevensTree = rpart(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst,
                    data = TrainingSet, method = "class", minbucket = 25)
# 10-fold CV over cp grid
numFolds = trainControl(method = "cv", number = 10)
cpGrid = expand.grid(cp = seq(0.1, 0.3, 0.05))
train(Reverse ~ ., data = TrainingSet, method = "rpart",
      trControl = numFolds, tuneGrid = cpGrid)
```

10-fold cross-validation selects **cp = 0.15** (accuracy 0.6444, Kappa 0.2829 across folds). Rebuilding the tree with cp = 0.15 yields a test-set confusion matrix of (59, 18; 29, 64) and out-of-sample accuracy of **(59+64)/170 = 72.35%** — a substantial improvement over the initial minbucket=25 model's 65.88%.

**Martin's full study** used 628 SCOTUS cases (1994-2001) to predict 68 cases from October Term 2002, before the term began. A two-stage CART approach first tried to predict unanimous liberal or conservative decisions, then fell back to individual-justice trees with majority aggregation. Martin recruited **83 legal experts** (71 academics, 12 attorneys, 38 former clerks, 33 chaired professors). Results:

| Method | Overall Case Accuracy | Individual Justice Accuracy |
|--------|----------------------|------------------------------|
| CART model | **75%** | 67% |
| Legal experts | 59% | 68% |

The takeaway is striking: a simple tree built from high-level case features outperforms experts at predicting full-court decisions, though experts hold their own on individual-justice votes where case-specific nuance matters.

## Lecture 6: Text Analytics / NLP

**[[nlp-basics|NLP Basics]]** opens with the **2013 AP Twitter hack** — a fake tweet that the White House had been bombed caused the S&P 500 to drop 1% within seconds. Motivation: Twitter processes ~500 million tweets per day, impossible to triage by hand. The course covers the full preprocessing pipeline (lowercase, punctuation, stop words, **Porter Stemmer** from 1980) before the **Bag-of-Words** model is fitted.

The Apple tweet dataset contains 1,181 tweets scored -2 to +2 by five **Amazon Mechanical Turk** workers each (averaged); the target variable `Harsh` is TRUE if average $\leq -1$ (182 harsh vs. 999 non-harsh). The full pipeline:

```r
library(tm); library(SnowballC)
corpus = VCorpus(VectorSource(tweets$Tweet))
corpus = tm_map(corpus, content_transformer(tolower))
corpus = tm_map(corpus, removePunctuation)
corpus = tm_map(corpus, removeWords, c("apple", stopwords("english")))
corpus = tm_map(corpus, stemDocument)
frequencies = DocumentTermMatrix(corpus)     # 1181 x 3289
sparse = removeSparseTerms(frequencies, 0.995) # 1181 x 309
```

Example stemmed output: "I have to say, Apple has by far the best customer care service I have ever received" becomes "far best custom care servic ever receiv". A 70/30 split yields 826 training / 355 test tweets. Model comparison on the test set:

| Model | cp | Accuracy | FPR | FNR |
|-------|-----|----------|-----|-----|
| Baseline (always FALSE) | — | 84.51% | 0% | 100% |
| CART 1 | 0.2 | 87.89% | 0.33% | 76.64% |
| CART 2 | 0.001 | 87.61% | 2.67% | 65.45% |
| CART 3 (CV optimal) | 0.034 | **88.45%** | 1.00% | 69.09% |
| Random Forest | — | **88.73%** | 2.33% | 60.00% |

CART 1 is a single split on the stemmed token **"freak"** — confirming that even crude features carry real signal. Cross-validated cp = 0.034 (from a grid `seq(0.001, 0.2, 0.001)` over 10 folds) gives a two-split tree on "freak" and "hate". [[decision-trees|Random Forest]] achieves the best accuracy and lowest false negative rate at the cost of interpretability.

## Lecture 7: Clustering and Recommendation Systems

**[[clustering|Clustering]]** is motivated by the **Netflix Prize** (2006-2009, $1M, won by **BellKor's Pragmatic Chaos** with 10.05% RMSE improvement over Cinematch on September 2009). The course covers Euclidean distance and two algorithms:

$$d_{ij} = \sqrt{\sum_{k=1}^{p}(x_{ik} - x_{jk})^2}$$

**K-means** — specify K, randomly assign points, compute centroids, re-assign to nearest centroid, repeat until convergence. **Hierarchical (agglomerative)** — start with each point as its own cluster, merge closest pair until one cluster remains, then cut the dendrogram at chosen height.

| Criterion | K-means | Hierarchical |
|-----------|---------|--------------|
| Speed | $O(nKT)$ | $O(n^2)$ or worse |
| K selection | Must specify in advance | Cut dendrogram after |
| Outlier sensitivity | High (skews centroids) | Lower |
| Reproducibility | Depends on `nstart` | Deterministic |

**MovieLens case**: 9,707 movies represented as 18-dimensional binary genre vectors (columns 4-21 of `movies.csv`). Distance example from the lectures: *Toy Story* (animation, comedy, children) vs. *Batman Forever* (action, adventure, comedy, crime) gives $d = \sqrt{5}$.

```r
km.out = kmeans(movies[4:21], 10, nstart = 25)
distances = dist(movies[4:21])
hc.out = hclust(distances, method = "ward.D")
hc.clusters = cutree(hc.out, k = 10)
tapply(movies$Action, km.out$cluster, mean)  # Action proportion per cluster
```

K-means with K = 10 assigned *Avengers: Age of Ultron* to cluster 4 (74.1% Action), alongside *Cutthroat Island*, *Mortal Kombat*, *Batman Forever*, *Star Wars: Episode IV*. Hierarchical (Ward's method, cut at 10) placed it in cluster 5 (72.4% Action) near *Heat*, *GoldenEye*, *Batman Forever* — different but equally valid partitions.

**[[recommendation-systems|Recommendation Systems]]**: The lecture introduces three approaches via a toy user-movie rating matrix (Amy, Bob, Carl, Dan rating *Avengers: Age of Ultron*, *Apollo 13*, *Top Gun*, *Terminator*): **collaborative filtering** (suggest *Avengers* to Carl because Amy liked it and their tastes align), **content-based filtering** (suggest Joss Whedon's *Serenity* because Amy liked the director's *Avengers*), and **hybrid systems** that combine both. Netflix's actual system is hybrid: collaborative filtering identifies similar users, then content filtering surfaces unseen items from shared favorite genres.

## Lecture 8: Revenue Management and Linear Optimization

Revenue management is framed as a **linear programming (LP)** problem. The course covers LP formulation, feasible regions, corner-point solutions, and **shadow prices** (sensitivity analysis).

**American Airlines case**: A single-route JFK-DFW problem with two fare classes (Regular $617, Discount $238). The LP formulation maximizes revenue subject to capacity and demand constraints. Key findings:
- Shadow price for discount seats = $0 (not binding)
- Shadow price for regular seats = $379 (= $617 - $238, the opportunity cost)
- Original aircraft profit: $5,006
- Boeing 757-200 alternative: $3,198
- Boeing 767-300 alternative: $2,442

The model extends to a multi-route network (JFK-DFW-LAX) with 6 decision variables covering nonstop and connecting itineraries.

Revenue management generated **$1.4 billion in incremental revenue** for American Airlines over three years (Robert Crandall, CEO). The Sabre Holdings system built for AA grew to serve 400 airlines, 90,000 hotels, and 30 car-rental companies. Delta Airlines increased annual revenue by $300M and Marriott hotels by $100M through similar systems.

## Key Findings

- **Data-driven models consistently outperform expert judgment**: Wine pricing (regression vs. sommeliers), Supreme Court prediction (CART 75% vs. experts 59%), and revenue management (optimization vs. heuristic allocation).
- **Model complexity trade-offs are central**: Simpler models (single-split CART) are interpretable but miss patterns; complex models (Random Forest) gain accuracy but lose explainability.
- **Cross-validation is essential**: Both the Supreme Court (cp=0.15) and tweet sentiment (cp=0.034) cases show that cross-validated parameter tuning produces the best out-of-sample performance.
- **Unsupervised methods require domain judgment**: Choosing K in clustering has no definitive method — trial, error, and interpretation are necessary.
- **Linear optimization has massive real-world impact**: Revenue management transformed the airline industry, with quantifiable billion-dollar impacts.

## Case Studies / Projects

| Project | Dataset | Methods | Key Finding |
|---|---|---|---|
| Insurance anti-fraud classifier | 1,000-row auto-insurance claims dataset, 38 variables including policy details, incident characteristics, claim amounts, and a binary `fraud` label | Logistic regression, [[decision-trees\|CART]], [[decision-trees\|Random Forest]], Gradient Boosting, SVM, KNN, Neural Network, all tuned via cross-validated grid search in R and Python; confusion-matrix evaluation with asymmetric cost of false positives | **Decision Tree (CV = 0.827)** and **Gradient Boosting (CV = 0.821)** after tuning were the best classifiers on a small (n≈700 training) fraud dataset. Top predictors: `incident_severity = Major Damage`, `insured_hobbies = chess`, `vehicle_claim`, `policy_annual_premium`, `incident_date`. The "chess hobby" importance is a cautionary pattern-recognition artefact — feature importances on a small dataset will surface spurious correlates alongside genuine signals, which project teams must interrogate before deploying the model. |

## Key Findings

- **Data-driven models consistently outperform expert judgment**: wine pricing (regression vs. sommeliers), Supreme Court prediction (CART 75% vs. experts 59%), revenue management (optimization vs. heuristic allocation), Ashenfelter's 1989/1990 Bordeaux predictions outranking Parker.
- **Cross-validation is essential**: Supreme Court (cp = 0.15) and tweet sentiment (cp = 0.034) both show that CV-tuned parameters deliver the best out-of-sample performance, and the Wine model demonstrates that more variables sometimes *hurt* out-of-sample $R^2$ (adding HarvestRain alone dropped it to -0.08).
- **Class imbalance dominates threshold choice**: Framingham's ~15% CHD rate forces the clinician to trade off false positive rate against false negative rate by moving the threshold, not by retraining.
- **Multicollinearity requires deliberate variable selection**: Moneyball drops BA because it correlates with OBP at $r = 0.854$; Wine drops FrancePop because it correlates with Age at $r = -0.994$; HW1 climate drops CFC-11/N2O after diagnosing the correlation structure.
- **Interpretability vs. accuracy is explicit**: single CART trees beat Random Forest on explainability, but Random Forest is 0.3-0.5 percentage points more accurate. [[logistic-regression|Logistic regression]] beats both on interpretability in regulated domains like healthcare.
- **External validation matters**: Framingham model calibrates for Black men but overpredicts Japanese American men, showing that internal CV is not a substitute for cross-population testing.

## Related Concepts

- [[benfords-law|Benford's Law]]
- [[linear-regression|Linear Regression]]
- [[logistic-regression|Logistic Regression]]
- [[decision-trees|Decision Trees]]
- [[nlp-basics|NLP Basics]]
- [[clustering|Clustering]]
- [[recommendation-systems|Recommendation Systems]]
- [[pca|PCA]]
- [[ab-testing|A/B Testing]]
- [[revenue-management|Revenue Management]]
- [[wiki/entities/hkust|HKUST]]

## Source Materials

- Lecture 1: Benford's Law
- Lecture 2: Wine Steward (Linear Regression)
- Lecture 3: Moneyball (Linear Regression)
- Lecture 4: Framingham Heart Study (Logistic Regression)
- Lecture 5: Supreme Court (Decision Trees)
- Lecture 6: Text Analytics (NLP)
- Lecture 7: Netflix (Clustering & Recommendation Systems)
- Lecture 8: Airline Revenue Management
