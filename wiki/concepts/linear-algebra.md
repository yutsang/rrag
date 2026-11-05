---
title: "Linear Algebra"
full_name: "Linear Algebra"
type: concept
tags: [mathematics, linear-algebra, foundations]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/hkust-linear-algebra"
confidence: high
---

## 概述

線性代數是研究向量空間、線性映射與線性方程組 $Ax = b$ 的數學分支，是機器學習、統計學及運籌學的核心數學基礎——幾乎所有數值方法最終都歸結為矩陣運算。求解 $Ax = b$ 的高斯消元法時間複雜度為 $O(n^3)$，其解的存在性由秩條件 $\text{rank}(A) = \text{rank}([A|b])$ 決定，解空間結構（核空間、列空間）由秩-零化度定理 $\dim(\ker A) + \text{rank}(A) = n$ 刻畫。特徵值-特徵向量對（$Av = \lambda v$）是矩陣長期行為的指紋：對稱矩陣（協方差矩陣、圖 Laplacian）的特徵值均為實數且特徵向量正交，使得譜分解 $A = V\Lambda V^T$ 成立；正定矩陣（$x^TAx > 0$）對應凸二次型，是最優化中凸性的代數刻畫。奇異值分解 $A = U\Sigma V^T$ 是最通用的矩陣分解，將[[wiki/concepts/pca|主成分分析]]（協方差矩陣的特徵分解）、最小二乘迴歸（正規方程 $A^TAx = A^Tb$ 的解即 $x = V\Sigma^+ U^T b$）、[[wiki/concepts/recommendation-systems|推薦系統]]的矩陣分解（低秩近似 $A_k = U_k\Sigma_k V_k^T$ 最小化 Frobenius 範數誤差）統一在同一框架下；截斷 SVD 的最優低秩近似性（Eckart-Young定理）是維度縮減的理論基礎。在運籌學中，線性規劃的單純形法在線性代數的基可行解（Basic Feasible Solution）概念上運作，網絡流問題的全單模性（Total Unimodularity）保證 LP 松弛的整數解，馬可夫鏈的穩態分佈是轉移矩陣特徵值1對應的特徵向量。數值線性代數的核心挑戰——條件數（$\kappa(A) = \sigma_{\max}/\sigma_{\min}$）量化系統對輸入擾動的敏感性，高條件數矩陣使直接求解不穩定，須用迭代法（共軛梯度法）或正則化（嶺迴歸加 $\lambda I$ 改善條件數）代替。

## What It Is

Linear algebra studies **vector spaces** and **linear maps** between them. The central computational object is the **matrix** — a rectangular array representing a linear transformation, a system of equations, or a dataset.

## Vectors and Vector Spaces

A **vector space** over $\mathbb{R}$ is a set $V$ with addition and scalar multiplication satisfying the usual axioms. Key concepts:
- **Linear independence**: $\{v_1, \ldots, v_k\}$ independent if $\sum \alpha_i v_i = 0 \Rightarrow \alpha_i = 0$ for all $i$
- **Span**: set of all linear combinations of a collection of vectors
- **Basis**: a linearly independent spanning set; its size is the **dimension** of $V$
- **Inner product** (dot product): $\langle u, v \rangle = u^T v$; induces norm $\|v\| = \sqrt{v^T v}$; orthogonality: $u \perp v \iff u^T v = 0$

## Matrices and Systems of Equations

An $m \times n$ matrix $A$ represents a linear map from $\mathbb{R}^n$ to $\mathbb{R}^m$. Solving $Ax = b$:
- **Gaussian elimination** (row reduction): O(n³), produces row echelon form, identifies pivots
- **LU decomposition**: $A = LU$ where $L$ is lower triangular, $U$ upper. Efficient for solving multiple right-hand sides.
- **Rank**: number of linearly independent rows (= columns). $Ax = b$ has a solution iff $\text{rank}(A) = \text{rank}([A|b])$.
- **Null space (kernel)**: $\{x : Ax = 0\}$; dimension = $n - \text{rank}(A)$

## Eigenvalues and Eigenvectors

For square $A \in \mathbb{R}^{n \times n}$, a scalar $\lambda$ and non-zero $v$ satisfying $Av = \lambda v$ are an **eigenvalue** and **eigenvector** pair. Eigenvalues are roots of the characteristic polynomial $\det(A - \lambda I) = 0$.

**Diagonalization**: if $A$ has $n$ linearly independent eigenvectors, then $A = V \Lambda V^{-1}$ where $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_n)$. Enables fast computation of $A^k = V \Lambda^k V^{-1}$.

**Symmetric matrices** (common in statistics/ML): eigenvalues are real, eigenvectors are orthogonal ($V^{-1} = V^T$), so $A = V \Lambda V^T$ (spectral decomposition).

**Positive definite**: $A \succ 0$ iff all eigenvalues $> 0$ iff $x^T A x > 0$ for all $x \neq 0$. Covariance matrices are positive semidefinite ($\succeq 0$).

## Singular Value Decomposition (SVD)

For any $m \times n$ matrix $A$ (need not be square):
$$A = U \Sigma V^T$$
where $U \in \mathbb{R}^{m \times m}$ (left singular vectors), $\Sigma \in \mathbb{R}^{m \times n}$ (diagonal, singular values $\sigma_1 \geq \sigma_2 \geq \cdots \geq 0$), $V \in \mathbb{R}^{n \times n}$ (right singular vectors).

**Truncated SVD** (rank-$k$ approximation): $A \approx U_k \Sigma_k V_k^T$ minimizes $\|A - B\|_F$ over all rank-$k$ matrices $B$ (Eckart-Young theorem).

## Applications in ML and OR

**Least squares** ($Ax = b$ overdetermined): normal equations $A^T A x = A^T b$; solution $x = (A^T A)^{-1} A^T b = A^+ b$ where $A^+$ is the pseudoinverse. This is exactly OLS in [[linear-regression]].

**PCA**: find directions of maximum variance in data matrix $X$. The principal components are the right singular vectors of $X$ (or equivalently eigenvectors of the sample covariance). See [[pca]].

**Recommendation systems**: matrix factorization decomposes the user-item rating matrix as $R \approx U V^T$ via truncated SVD or alternating least squares. See [[recommendation-systems]].

**Linear programming**: the simplex method operates on the constraint matrix $A$ in basis form. The optimal basis $B$ satisfies $B^{-1}$ at each pivot — matrix inverse is central.

**Network flows**: the node-arc incidence matrix of a connected graph is totally unimodular — a key linear algebra property guaranteeing integer optimal solutions.

**Markov chains**: the steady-state distribution solves $\pi^T P = \pi^T$, i.e., $\pi$ is the left eigenvector of $P$ for eigenvalue 1.

## Numerical Considerations

- **Condition number** $\kappa(A) = \sigma_{\max}/\sigma_{\min}$: measures sensitivity to perturbations. High condition number → numerical instability.
- **Sparse matrices**: real-world LP/OR problems have sparse $A$; sparse direct solvers (CHOLMOD, SuperLU) exploit this for efficiency.
- **Iterative methods** (conjugate gradient, GMRES): preferred over direct solvers for very large, sparse, symmetric systems.

## Related Concepts

- [[pca]]
- [[linear-regression]]
- [[optimization]]
- [[linear-programming]]
- [[recommendation-systems]]
- [[stochastic-processes]]
- [[probability-theory]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
