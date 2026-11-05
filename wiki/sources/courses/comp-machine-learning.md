---
title: "Machine Learning"
full_name: "COMP4211 Machine Learning"
type: source
tags: [courses, comp, undergraduate, machine-learning, comp4211, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP4211"
confidence: medium
---

## 概述

COMP4211 機器學習為計算機科學四年級學生提供機器學習算法的嚴格數學基礎訓練，先修要求為 COMP2012 資料結構、MATH2111 線性代數及 MATH2411 概率統計，是 COMP3211 人工智能基礎的深化延伸課程。課程參考教材包括 Bishop《模式識別與機器學習》（PRML）及 Murphy《機器學習：概率視角》，相較於應用導向的 IEDA3560，更強調統計學習理論（PAC 學習、VC 維、偏差-方差分解）與算法的數學推導。核心內容涵蓋支援向量機（SVM）的二次規劃對偶推導與核技巧（RBF、多項式核）、集成方法（隨機森林的 bagging 與 AdaBoost 的指數損失加權更新）、期望最大化（EM）算法用於高斯混合模型，以及多層感知機的反向傳播與卷積神經網絡架構概覽。學生完成課程後能夠從頭推導主要算法、分析其計算複雜度、選擇適當的超參數調整策略，並理解正則化技術（L1/L2、dropout、批次正規化）的統計動機。SVM 的對偶問題直接連結線性規劃對偶理論，EM 算法的結構呼應運籌學隨機模型中的期望步驟，使本課程對 OR 研究者亦具有重要的方法論價值。

## Course Overview

COMP4211 Machine Learning provides a rigorous, mathematically grounded treatment of machine learning algorithms — beyond the applied focus of courses like IEDA3560. The course emphasizes the theoretical foundations: statistical learning theory, kernel methods, and the bias-variance trade-off.

**Prerequisites**: COMP2011/2012, MATH2111 (linear algebra), MATH2411 (probability)

## Key Topics

### Statistical Learning Framework
- **PAC learning**, sample complexity, VC dimension
- **Bias-variance decomposition**: total error = bias² + variance + noise
- Empirical Risk Minimization (ERM), overfitting, regularization

### Supervised Learning — Beyond Basics
- **Support Vector Machines (SVMs)**: maximum-margin hyperplane, hard/soft margin, dual formulation (quadratic programming), kernel trick
- **Kernel methods**: polynomial kernel, RBF/Gaussian kernel, kernel SVM, kernel ridge regression
- **Ensemble methods**: random forests (bagging + feature randomness), gradient boosting, AdaBoost (weight update, exponential loss)

### Neural Networks and Deep Learning
- **Perceptron** and multi-layer perceptron (MLP), universal approximation theorem
- **Backpropagation**: chain rule applied to computation graphs, gradient flow
- **Convolutional neural networks** (CNNs): convolution operation, pooling, LeNet/AlexNet architecture overview
- **Optimization**: SGD, momentum, Adam; learning rate schedules; vanishing/exploding gradients
- **Regularization**: dropout, batch normalization, early stopping, L1/L2 weight decay

### Unsupervised Learning
- **K-means revisited**: Lloyd's algorithm convergence, k-means++ initialization
- **Expectation-Maximization (EM)**: Gaussian mixture models, soft assignments
- **Dimensionality reduction**: PCA (mathematical derivation), autoencoders, t-SNE

### Model Assessment and Selection
- Cross-validation (k-fold, LOOCV), train/val/test splits
- Hyperparameter tuning: grid search, random search, Bayesian optimization
- Evaluation metrics: accuracy, precision/recall/F1, ROC-AUC, confusion matrix

## Connections to OR

- SVM dual problem is a **quadratic program** — directly uses [[linear-programming]] duality theory
- EM algorithm generalizes the expectation step seen in stochastic OR models
- Neural network training = non-convex [[optimization]]; understanding local minima matters
- Ensemble methods (random forests, XGBoost) are the practical go-to for tabular data in OR applications

## Related Concepts

- [[machine-learning-advanced]]
- [[linear-regression]]
- [[logistic-regression]]
- [[decision-trees]]
- [[clustering]]
- [[pca]]
- [[optimization]]
- [[linear-algebra]]
