---
title: "IEDA 3560 Data Analytics for Business"
full_name: "IEDA 3560: Predictive Analytics"
type: source
tags: [courses, ieda, undergraduate, machine-learning, analytics, ieda3560, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3560/IEDA3560 Syllabus.pdf"
confidence: high
author: "Guillermo Gallego"
date_published: "2022-02-04"
---

## 概述

IEDA 3560「商業數據分析」（又稱 Predictive Analytics）是香港科技大學 IEDA 學系三年級本科生的選修課，由 Guillermo Gallego 教授於 2022 年春季主講，前置要求為 IEDA 2520（概率）及 IEDA 2540（統計）。課程不設指定教材（參考 Zhi-Hua Zhou 的《Machine Learning》），以 Python 貫穿全程，系統涵蓋機器學習與資料探勘的核心方法：線性迴歸（OLS、Ridge/Lasso/Elastic Net 正則化）、交叉驗證與自助法（Bootstrap）、分類（邏輯迴歸、LDA/QDA）、樹模型（CART、Bagging、隨機森林、Boosting/AdaBoost/梯度提升）、支持向量機（SVM 核技巧、最大間隔超平面）、聚類分析（k-Means、層次聚類）及降維（PCA、偏最小二乘 PLS）。應用場景橫跨廣告、電商、金融、醫療、市場行銷及收益管理，課程作業包括電動車分類（EV Data）、銷售預測及推薦分析等 10 個 Python 作業，並以小組項目（25%）對真實數據集完成端對端分析。本課是 IEDA 4180（服務工程）與 IEDA 4410（數據驅動供應鏈管理）的重要方法基礎，亦為有意從事數據科學或 OR 研究的學生提供完整的預測分析工具鏈。

## Course Overview

**IEDA 3560 Predictive Analytics** (Spring 2022, Prof. Guillermo Gallego) trains students to identify, evaluate, and capture decision-analytic opportunities by deploying machine learning and data mining techniques. The course emphasizes *practical discipline*: mastery of both methodology and domain-specific applications across advertising, e-commerce, finance, healthcare, marketing, and revenue management.

**Prerequisites**: IEDA 2520 (Probability), IEDA 2540 (Statistics).  
**Programming**: Python throughout; no required textbook (reference: *Machine Learning* by Zhi-Hua Zhou, Springer).

## Course Outline

| Module | Topics |
|--------|--------|
| 1 | Introduction to decision analytics |
| 2 | Linear models and regression |
| 3 | Quality of predictions / financial analytics |
| 4 | Resampling: cross-validation and bootstrap |
| 5 | Subset selection, Ridge and Lasso regressions |
| 6 | Logistic regression and linear discriminant analysis |
| 7 | Predicting outcomes / recommendation analytics |
| 8 | k-Nearest Neighbors and tree-based methods |
| 9 | Support Vector Machines |
| 10 | Clustering |
| 11 | PCA and partial least squares |

## Key Topics

### Linear Models and Regression (Module 2)

The course begins with **ordinary least squares (OLS)** regression as the foundation for all predictive modeling. Topics include matrix formulation (β̂ = (XᵀX)⁻¹Xᵀy), residual analysis, R², adjusted R², and the bias-variance tradeoff. Financial analytics applications are introduced early — stock return prediction using the advertising dataset (AAPL.csv, Advertising.csv appear in course materials). See [[wiki/concepts/linear-regression|Linear Regression]].

### Model Selection and Regularization (Modules 4–5)

**Cross-validation** (k-fold) replaces train/test splits for reliable generalization estimates. The **bootstrap** produces confidence intervals for model statistics without distributional assumptions.

**Subset selection** (best-subset, forward/backward stepwise) and regularization:
- **Ridge regression**: L2 penalty λ‖β‖². Shrinks coefficients toward zero, handles multicollinearity.
- **Lasso regression**: L1 penalty λ‖β‖₁. Performs variable selection by zeroing coefficients; better for sparse true models.
- **Elastic net**: combines L1 and L2 penalties.

### Classification (Module 6)

**Logistic regression** models P(Y=1|X) = σ(Xβ) where σ is the sigmoid function. Estimated by maximum likelihood. See [[wiki/concepts/logistic-regression|Logistic Regression]].

**Linear Discriminant Analysis (LDA)** assumes Gaussian class-conditional distributions with shared covariance. The decision boundary is linear; QDA allows class-specific covariances for a quadratic boundary.

### Tree-Based Methods and Ensembles (Module 8)

**Decision trees** (CART): recursive binary splitting on features; pruned by cost-complexity criterion. Interpretable but high variance.

**Bagging**: bootstrap aggregate of many trees to reduce variance.

**Random forests**: bagging with random feature subsets at each split — reduces correlation between trees, improving over pure bagging.

**Boosting** (AdaBoost, gradient boosting): sequentially fit models to residuals; very competitive in practice. Course materials include `Bagging_Boosting.pdf` and `decision_trees.pdf`. See [[wiki/concepts/decision-trees|Decision Trees]].

### Support Vector Machines (Module 9)

**SVM** finds the maximum-margin hyperplane separating classes. The **kernel trick** maps inputs to high-dimensional feature spaces implicitly, enabling non-linear boundaries with linear SVM. Common kernels: polynomial, RBF (Gaussian). Course covers support vectors, slack variables (soft-margin SVM), and the dual optimization formulation.

### Clustering (Module 10)

**k-Means**: iterative assignment of n points to k centroids minimizing within-cluster sum of squares. Sensitive to initialization (k-means++ remedy) and choice of k (elbow method, silhouette). See [[wiki/concepts/clustering|Clustering]].

**Hierarchical clustering**: agglomerative bottom-up (single, complete, average linkage). Produces dendrogram — no need to pre-specify k.

### Dimensionality Reduction (Module 11)

**Principal Component Analysis (PCA)**: eigendecomposition of the covariance matrix; projects data onto directions of maximum variance. Used for visualization, noise reduction, and as preprocessing before supervised learning. See [[wiki/concepts/pca|PCA]].

**Partial Least Squares (PLS)**: supervised dimensionality reduction that maximizes covariance between projections of X and Y — more relevant than PCA when the goal is prediction.

### Recommendation Analytics (Module 7)

Covers collaborative filtering, matrix factorization, and content-based methods. Real-world examples: Netflix, Amazon, Pandora. Course homework includes `Classification_eCarData.ipynb` (EV classification) and `Regression - Sales.ipynb`.

## Practical Gotchas

- **Bias-variance tradeoff**: models that overfit training data generalize poorly. Cross-validation is the standard remedy; regularization directly controls complexity.
- **Class imbalance**: logistic regression and trees can fail when classes are severely imbalanced; remedies include oversampling (SMOTE), undersampling, and adjusted thresholds.
- **Feature scaling**: Ridge/Lasso/SVM/kNN all require standardized features; tree-based methods are scale-invariant.
- **Interpretability vs. accuracy**: linear models and shallow trees are interpretable; ensembles and SVMs are black boxes.

## Related Concepts

- [[wiki/concepts/linear-regression|Linear Regression]] — OLS, regularization
- [[wiki/concepts/logistic-regression|Logistic Regression]] — binary and multi-class classification
- [[wiki/concepts/decision-trees|Decision Trees]] — CART, bagging, random forests, boosting
- [[wiki/concepts/clustering|Clustering]] — k-means, hierarchical
- [[wiki/concepts/pca|PCA]] — dimensionality reduction
- [[wiki/concepts/ab-testing|A/B Testing]] — statistical hypothesis testing for analytics

## Source Materials

- raw/courses/IEDA/IEDA3560/IEDA3560 Syllabus.pdf
- raw/courses/IEDA/IEDA3560/Bagging_Boosting.pdf
- raw/courses/IEDA/IEDA3560/decision_trees.pdf
- raw/courses/IEDA/IEDA3560/Logistic_Regression.pdf
