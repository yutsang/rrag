---
title: "PCA"
full_name: "Principal Component Analysis (PCA)"
type: concept
tags: [machine-learning, dimensionality-reduction, unsupervised-learning, statistics, feature-engineering]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/applied-statistics"
confidence: medium
---

## 概述

主成分分析（PCA）是一種無監督的線性降維技術，透過求解樣本協方差矩陣的特徵分解（等價於對中心化數據矩陣做奇異值分解 SVD），將高維數據投影到保留最大變異量的正交低維空間中，所得各主成分互不相關且按解釋方差量遞減排列。PCA 的核心公式為 $\Sigma v_j = \lambda_j v_j$，其中 $\lambda_j$ 為第 $j$ 個特徵值，對應第 $j$ 個主成分所解釋的方差量；選取保留多少個主成分通常依據累積解釋方差比例（如90%）、Scree 圖肘點或 Kaiser 準則（特徵值 > 1）決定。在推薦系統領域，PCA 與 SVD 密切相關——Netflix Prize 中取得突破的矩陣分解法本質上是對用戶-物品評分矩陣做截斷 SVD，提取潛在因子空間；自然語言處理中的潛在語義分析（LSA）也採用相同原理對文件-詞項矩陣降維。PCA 的主要侷限在於只能捕捉線性結構，對非線性流形數據（如螺旋形）效果有限，此時需使用 t-SNE、UMAP 等非線性降維方法；另一侷限是主成分為原始特徵的線性組合，往往缺乏直觀可解釋性，在需要模型可解釋性的運籌學情境中需謹慎使用。在多重共線性嚴重的迴歸問題中，主成分迴歸（PCR）能有效解決係數符號翻轉的問題（如 EEMT5500 氣候變化作業中 N2O 係數為負的案例）。

## Core Mechanism

**Principal Component Analysis (PCA)** is a dimensionality reduction technique that transforms a dataset of potentially correlated variables into a set of linearly uncorrelated variables called **principal components**. Each principal component captures the maximum remaining variance in the data, subject to being orthogonal (perpendicular) to all preceding components.

### Mathematical Foundation

Given a centered data matrix $X \in \mathbb{R}^{n \times p}$, PCA solves the eigendecomposition of the sample covariance matrix $\Sigma = \frac{1}{n-1} X^\top X$:

$$\Sigma v_j = \lambda_j v_j, \quad j = 1, \ldots, p$$

Equivalently, the first principal component direction is the unit vector $v_1$ that maximizes the variance of the projected data:

$$v_1 = \arg\max_{\|v\| = 1} v^\top \Sigma v$$

The procedure:

1. **Center** the data by subtracting the mean of each feature: $\tilde{x}_{ij} = x_{ij} - \bar{x}_j$
2. **Compute** the covariance matrix $\Sigma$ ($p \times p$)
3. **Eigendecompose** $\Sigma$ to find eigenvectors $v_1, \ldots, v_p$ and eigenvalues $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p \geq 0$
4. **Project** the centered data onto the top $k$ eigenvectors: $Z = \tilde{X} V_{1:k}$

The first principal component (PC1) is the direction in feature space along which the data varies most. PC2 is the direction of maximum remaining variance orthogonal to PC1, and so on. Because PCA is equivalent to the **Singular Value Decomposition (SVD)** of the centered data matrix ($\tilde{X} = U D V^\top$, with $\lambda_j = d_j^2 / (n-1)$), numerically stable implementations prefer SVD over direct eigendecomposition of $\Sigma$.

### Variance Explained

Each eigenvalue represents the amount of variance captured by its corresponding principal component. The **proportion of variance explained** by component j is:

$$PVE(j) = \frac{\lambda_j}{\sum_k \lambda_k}$$

The **cumulative proportion of variance explained** indicates how many components are needed to capture a target percentage (e.g., 90% or 95%) of total variance.

## How to Choose the Number of Components

Several heuristics guide the choice of k (number of components to retain):

| Method | Rule |
|--------|------|
| **Scree plot** | Plot eigenvalues vs. component number; look for an "elbow" |
| **Kaiser criterion** | Retain components with eigenvalue > 1 (for standardized data) |
| **Cumulative variance** | Retain enough components to explain 90-95% of variance |
| **Cross-validation** | Use downstream task performance to select k |

## When to Use PCA

PCA is most valuable when:
- **Multicollinearity** exists among features (common in real-world datasets)
- **Dimensionality is high** relative to sample size (p >> n or p comparable to n)
- **Visualization** of high-dimensional data is needed (project to 2D or 3D)
- **Noise reduction** is desired (small principal components often capture noise)
- **Pre-processing** before [[clustering|Clustering]] or other algorithms that suffer from the curse of dimensionality

### Connection to Clustering

PCA is frequently applied as a preprocessing step before [[clustering|Clustering]]. In high-dimensional spaces:
- Euclidean distance becomes less meaningful (curse of dimensionality)
- Many features may be noisy or redundant
- PCA projects data into a lower-dimensional space where clustering algorithms work more effectively

For the MovieLens dataset in EEMT5500 (18 genre features), PCA could reduce the 18 binary dimensions to, say, 5-6 principal components capturing the dominant genre patterns (e.g., "action vs. drama", "children vs. adult") before applying K-means or hierarchical clustering.

### Connection to Recommendation Systems

PCA is closely related to **Singular Value Decomposition (SVD)**, which was the most successful technique in the Netflix Prize. SVD factorizes the user-item rating matrix into lower-dimensional latent factors that capture hidden patterns:
- **User factors**: Represent each user's affinity for latent dimensions (e.g., preference for action, tolerance for subtitles)
- **Item factors**: Represent each item's loading on those same dimensions

This is essentially PCA applied to the rating matrix, and it powers the matrix factorization approach to [[recommendation-systems|Recommendation Systems]].

## Practical Implementation

### In R

```r
# Standardize the data (mean=0, sd=1)
data_scaled = scale(data)

# Run PCA
pca_result = prcomp(data_scaled, center = TRUE, scale. = TRUE)

# View variance explained
summary(pca_result)

# Scree plot
plot(pca_result, type = "l")

# Access principal components
pc_scores = pca_result$x[, 1:k]  # First k components
```

### In Python

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

pca = PCA(n_components=0.95)  # Retain 95% variance
pc_scores = pca.fit_transform(data_scaled)
```

## Strengths and Limitations

### Strengths
- **Reduces dimensionality** while preserving maximum variance
- **Removes multicollinearity** — principal components are orthogonal by construction
- **Noise reduction** — discarding small components filters out noise
- **Unsupervised** — requires no labels
- **Computationally efficient** — eigendecomposition is well-optimized

### Limitations
- **Linear only**: PCA captures only linear relationships. Non-linear dimensionality reduction (t-SNE, UMAP) may be better for complex data
- **Interpretability**: Principal components are linear combinations of original features and may lack intuitive meaning
- **Sensitive to scaling**: Features must be standardized before PCA; otherwise, features with larger scales dominate
- **Variance ≠ Importance**: The direction of maximum variance may not be the most informative for a downstream task (consider supervised alternatives like LDA)

## Concrete Application to EEMT5500 Datasets

Although EEMT5500 does not lecture PCA directly, several of its datasets are natural candidates:

- **MovieLens (Lecture 7)**: 9,707 movies x 18 binary genre features. Running `prcomp(movies[, 4:21])` would typically compress to ~5 components capturing dominant genre contrasts (e.g., "serious drama vs. action blockbuster", "kids/animation vs. adult", "horror/thriller vs. comedy"). Clustering on the top PCs reduces noise and often produces cleaner genre partitions than raw binary vectors.
- **Moneyball (Lecture 3)**: batting features (BA, OBP, SLG, OPS, doubles, triples, walks, strikeouts) are highly correlated. PCA would reveal that a single "overall offense" component explains most variance, and a second "power vs. contact" component separates sluggers from high-average hitters. This is one justification for using OBP + SLG rather than the full batting stat menu.
- **Climate change HW1**: CO2, CH4, N2O, CFC-11, CFC-12 all trend together over time ($r > 0.9$). A principal-components regression (PCR) on the first two PCs would sidestep the sign-flip multicollinearity problem that motivates the reduced model in the homework solution.

## Related Concepts

- [[clustering|Clustering]] — PCA is commonly used as a preprocessing step before clustering
- [[recommendation-systems|Recommendation Systems]] — SVD/matrix factorization is PCA applied to user-item matrices
- [[linear-regression|Linear Regression]] — PCA can address multicollinearity among regression predictors (PCR)
- [[nlp-basics|NLP Basics]] — Latent Semantic Analysis (LSA) applies SVD to document-term matrices
- [[decision-trees|Decision Trees]] — tree-based methods handle high dimensionality without PCA
- [[logistic-regression|Logistic Regression]] — principal components can serve as reduced-dimensionality predictors
- [[wiki/entities/hkust|HKUST]] — course home institution
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Statistical Learning for OR)

## Source Materials

- [[wiki/sources/courses/applied-statistics|EEMT5500 Applied Probability, Statistics and Data Analytics]]
