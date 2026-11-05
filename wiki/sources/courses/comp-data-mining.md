---
title: "Data Mining"
full_name: "COMP4331 Data Mining"
type: source
tags: [courses, comp, undergraduate, data-mining, machine-learning, pattern-recognition, comp4331, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP4331"
confidence: medium
---

## 概述

COMP4331 數據挖掘為計算機科學四年級學生系統介紹從大規模數據集中發現知識（KDD）的核心方法，以 Han、Kamber 及 Pei《數據挖掘：概念與技術》（第三版）為標準教材，先修要求為 COMP3311 資料庫系統及 ISOM2500/MATH2411 統計學基礎。課程涵蓋數據預處理（缺失值填補、正規化、離散化）、頻繁模式挖掘（Apriori 算法的反單調性剪枝、FP-growth 的無候選集生成優化）、關聯規則評估（支持度、置信度、提升度）、多種分類器（決策樹 C4.5、朴素貝葉斯、SVM、集成方法）及聚類算法（k-means、DBSCAN 密度聚類、層次聚類的Ward 鏈接法）。異常檢測部分介紹局部異常因子（LOF）與孤立森林（Isolation Forest），並討論欺詐檢測與質量控制的實際應用。課程共設三份程式作業與期中考試，要求學生在真實數據集上實現算法原型，直接培養可擴展數據分析管線的設計能力。數據挖掘技術廣泛應用於商業智能儀表板、供應鏈需求預測、電商個性化推薦及金融風控模型，是數據驅動決策的核心工具集。

## Course Overview

**Textbook**: Han, Kamber & Pei, *Data Mining: Concepts and Techniques* (3rd ed.)

Data mining is the computational side of knowledge discovery in databases (KDD). Focuses on scalable algorithms and pattern discovery from structured data.

## Key Topics

### Data Preprocessing
- Data cleaning: handling missing values (imputation, deletion); noise (smoothing, binning); inconsistencies
- Data integration: entity resolution; schema mapping
- Data transformation: normalization (min-max, z-score); discretization; aggregation
- Dimensionality reduction: PCA for feature extraction; attribute subset selection — see [[pca]]
- Data warehouse: OLAP operations (roll-up, drill-down, slice, dice, pivot) — see [[database-systems]]

### Frequent Pattern Mining
- **Market basket analysis**: transaction database; support, confidence, lift
- **Apriori algorithm**: anti-monotone property; candidate generation and pruning; computational complexity
- **FP-growth**: FP-tree construction; pattern extraction without candidate generation; much faster than Apriori
- Association rules: $X \Rightarrow Y$; support threshold; confidence threshold; lift $> 1$ for positive correlation
- Sequential pattern mining: GSP algorithm; temporal ordering
- Constraint-based mining: push constraints into mining process

### Classification
- Decision trees: ID3, C4.5, CART; splitting criteria (information gain, Gini index, gain ratio)
- Overfitting and pruning: pre-pruning (early stopping), post-pruning (reduced error, cost-complexity)
- **Bayesian classification**: naïve Bayes; posterior probability; Laplace smoothing
- **Support Vector Machines**: hyperplane classification; margin maximization; kernel trick (RBF, polynomial) — see [[machine-learning-advanced]]
- **Ensemble methods**: bagging (random forests), boosting (AdaBoost, Gradient Boosting)
- Lazy learners: k-nearest neighbors; distance functions; curse of dimensionality
- Model evaluation: confusion matrix; accuracy, precision, recall, F1; ROC curves; cross-validation

### Clustering
- **k-means**: centroid-based; sensitivity to initialization (k-means++); elbow method for k selection
- **DBSCAN**: density-based; handles arbitrary shapes; identifies noise; core/border/noise points
- **Hierarchical clustering**: agglomerative (bottom-up); linkage methods (single, complete, average, Ward)
- Cluster validity: internal (silhouette score, Davies-Bouldin) vs. external (Rand index, NMI)
- See [[clustering]]

### Anomaly Detection
- Statistical approaches: z-score, modified z-score; Grubbs' test
- Distance-based: LOF (Local Outlier Factor); isolation forest
- Density-based methods; applications: fraud detection, intrusion detection, quality control

### Text and Web Mining (selected topics)
- TF-IDF for document representation
- Latent Semantic Analysis (LSA): SVD of term-document matrix
- PageRank algorithm: random surfer model; link analysis — see [[recommendation-systems]]

## Related Concepts

- [[machine-learning-advanced]]
- [[clustering]]
- [[pca]]
- [[recommendation-systems]]
- [[database-systems]]

## Source Materials

- COMP4331 Course Materials
