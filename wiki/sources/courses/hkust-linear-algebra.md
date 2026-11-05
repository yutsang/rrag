---
title: "HKUST Linear Algebra"
full_name: "HKUST Linear Algebra (MATH2111/2131)"
type: source
tags: [courses, math, undergraduate, linear-algebra, math2111, math2131, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH/MATH2111"
confidence: medium
---

## 概述

MATH2111 及 MATH2131 構成香港科技大學線性代數課程序列，系統介紹向量空間、矩陣運算、特徵分解及內積空間理論，是理工科二年級的核心數學必修課。標準版 MATH2111 以 Leon《線性代數及其應用》或 Lay《線性代數》為教材，側重矩陣計算的應用；榮譽版 MATH2131 則採用更理論化的處理，涵蓋抽象向量空間公理與嚴格的證明訓練。先修要求為大學一年級微積分（MATH1012/1013），提供對 $\mathbb{R}^n$ 的基本幾何直覺。課程使學生掌握高斯消元法、LU 分解、特徵值分解（$A = PDP^{-1}$）、Gram-Schmidt 正交化及奇異值分解（SVD）等核心工具，能夠求解線性方程組、建立最小二乘模型及分析線性變換的結構性質。線性代數是機器學習（PCA、線性迴歸的正則方程）、運籌學（單純形法的基矩陣）、統計學（多元回歸）及數值計算的共同數學語言，在研究與工業實踐中均不可或缺。

## Course Structure

| Course | Content |
|---|---|
| MATH2111 | Matrix algebra and applications |
| MATH2131 | Honors linear algebra (more theoretical) |

## Key Topics

### Systems of Linear Equations
- Gaussian elimination; row echelon form; reduced row echelon form
- Solution sets: unique, none, or infinitely many; rank-nullity theorem
- LU decomposition; $PA = LU$ with partial pivoting

### Vector Spaces
- Definition (8 axioms); subspaces; span; linear independence
- Basis and dimension; coordinates relative to a basis
- Column space, null space, row space; rank and nullity
- Change of basis matrix

### Linear Transformations
- Matrix representation of a linear map $T: V \to W$
- Composition = matrix product; inverse = matrix inverse
- Kernel and image; rank-nullity theorem revisited

### Eigenvalues and Eigenvectors
- Characteristic polynomial $\det(A - \lambda I) = 0$
- Geometric vs. algebraic multiplicity
- Diagonalization: $A = PDP^{-1}$ when $n$ linearly independent eigenvectors exist
- Symmetric matrices: real eigenvalues, orthogonal eigenvectors ($A = Q\Lambda Q^T$)

### Inner Products and Orthogonality
- Dot product, Euclidean norm, angle between vectors
- Gram-Schmidt orthogonalization
- Orthogonal complement; orthogonal projection $\text{proj}_U v$
- Least squares: normal equations $A^TAx = A^Tb$; overdetermined systems

### Singular Value Decomposition (SVD)
- $A = U\Sigma V^T$; singular values $\sigma_1 \geq \sigma_2 \geq \cdots$
- Truncated SVD as best rank-$k$ approximation
- Applications: PCA, low-rank matrix approximation, pseudoinverse

## Applications Emphasised

- **Least squares** regression: OLS = $\hat{\beta} = (X^TX)^{-1}X^Ty$ — see [[linear-regression]]
- **PCA**: eigenvectors of covariance matrix / right singular vectors of data matrix — see [[pca]]
- **Markov chains**: steady state = left eigenvector for eigenvalue 1 — see [[stochastic-processes]]
- **LP simplex**: basis matrices and their inverses are linear algebra at heart — see [[linear-programming]]

## Related Concepts

- [[linear-algebra]]
- [[pca]]
- [[linear-regression]]
- [[optimization]]
- [[linear-programming]]
