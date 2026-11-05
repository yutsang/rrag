---
title: "Optimization"
full_name: "Mathematical Optimization"
type: concept
tags: [mathematics, optimization, operations-research, machine-learning]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/hkust-linear-algebra"
confidence: high
---

## 概述

數學優化是在可行域 X 中尋找目標函數 f(x) 的最小值（或最大值）的科學，一般形式為 min f(x) s.t. gi(x) ≤ 0, hj(x) = 0，是運籌學、機器學習與工程設計的統一方法論基礎。問題結構決定可解性與演算法選擇：線性規劃（LP）在多項式時間可解且擁有完整對偶理論；凸優化（Convex Optimization）保證局部最優即全局最優，涵蓋 LP、二次規劃（QP）、二階錐規劃（SOCP）及半正定規劃（SDP）等層次，各有對應的高效內點法求解器。KKT（Karush-Kuhn-Tucker）條件是約束優化的必要最優性條件，在凸問題下亦充分，其中對偶變數（拉格朗日乘子）λi 即約束 i 的影子價格，量化鬆動約束的邊際價值。非凸問題（整數規劃、神經網路訓練、組合優化）是實際中最重要但最難的類別，分支定界提供精確解，隨機梯度下降（SGD）及其變體（Adam）為深度學習的標準訓練算法，元啟發式（模擬退火、遺傳算法）在無法精確求解時提供近似解。多目標優化（Pareto Frontier）、隨機規劃（Stochastic Programming）與魯棒優化（Robust Optimization）是運籌學研究中最活躍的延伸方向，分別對應多準則決策、不確定性下期望成本最小化及最壞情境下的抗擾性設計。

## What It Is

An **optimization problem** has the general form:
$$\min_{x \in \mathcal{X}} f(x) \quad \text{s.t.} \quad g_i(x) \leq 0, \; h_j(x) = 0$$

where $f: \mathbb{R}^n \to \mathbb{R}$ is the objective, $g_i$ are inequality constraints, $h_j$ are equality constraints, and $\mathcal{X}$ is the domain.

## Unconstrained Optimization

### First and Second Order Conditions
- **Gradient** $\nabla f(x) = 0$: necessary for a local minimum (for differentiable $f$)
- **Hessian** $\nabla^2 f(x) \succ 0$ (positive definite): sufficient for a strict local minimum
- **Convexity** makes local = global: if $f$ is convex, any local minimum is global

### Gradient-Based Methods

**Gradient descent** (steepest descent):
$$x_{k+1} = x_k - \alpha_k \nabla f(x_k)$$
Step size $\alpha_k$ chosen by line search (Armijo/Wolfe conditions) or fixed. Convergence rate: $O(1/k)$ for convex $f$ with Lipschitz gradient.

**Newton's method**: uses second-order information — $x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k)$. Quadratic convergence near optimum, but requires Hessian inversion ($O(n^3)$).

**Quasi-Newton (L-BFGS)**: approximate inverse Hessian using gradient history. Near-Newton convergence, O(n) memory. Standard for training logistic regression and other smooth ML models.

**Stochastic Gradient Descent (SGD)**: estimate gradient from a minibatch. Noisy but scalable to massive datasets. With learning rate decay, converges to neighborhood of optimum. Used for neural network training.

**Adam**: adaptive moment estimation — maintains per-parameter learning rates. Dominant optimizer for deep learning.

## Constrained Optimization

### Lagrangian and KKT Conditions

For $\min f(x)$ s.t. $g_i(x) \leq 0$, $h_j(x) = 0$, the **Lagrangian** is:
$$\mathcal{L}(x, \lambda, \nu) = f(x) + \sum_i \lambda_i g_i(x) + \sum_j \nu_j h_j(x)$$

**KKT (Karush-Kuhn-Tucker) conditions** are necessary for optimality (under constraint qualifications):
1. **Stationarity**: $\nabla_x \mathcal{L} = 0$
2. **Primal feasibility**: $g_i(x^*) \leq 0$, $h_j(x^*) = 0$
3. **Dual feasibility**: $\lambda_i \geq 0$
4. **Complementary slackness**: $\lambda_i g_i(x^*) = 0$

Economic interpretation: $\lambda_i$ is the shadow price of constraint $i$ (increase in objective per unit tightening).

For **convex** problems (convex $f$, convex $g_i$, affine $h_j$), KKT conditions are also sufficient.

## Convex Optimization

A function $f$ is **convex** if $f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta) f(y)$ for all $\theta \in [0,1]$.

**Convex optimization** problems have:
- Unique global optimum (if strictly convex)
- Polynomial-time algorithms
- Strong duality (under Slater's condition): primal and dual optimal values equal

**Important convex problem classes**:

| Class | Form | Examples |
|---|---|---|
| Linear program (LP) | Linear $f$, linear constraints | See [[linear-programming]] |
| Quadratic program (QP) | Quadratic $f$, linear constraints | Portfolio optimization (Markowitz) |
| Second-order cone program (SOCP) | Linear $f$, quadratic constraints | Robust optimization |
| Semidefinite program (SDP) | Trace objective, PSD constraints | Relaxations of combinatorial problems |
| Geometric program (GP) | Posynomial objective | Circuit design, supply chain |

**CVX/CVXPY**: modeling language that automatically identifies and solves convex problems.

## Non-Convex Optimization

Most real problems (neural networks, integer programs, combinatorial problems) are non-convex. Strategies:
- **Local search**: gradient descent, simulated annealing, find local optima
- **Branch and bound**: exact for MIP (see [[integer-programming]])
- **Metaheuristics**: genetic algorithms, tabu search, particle swarm — no guarantees but practical
- **Convex relaxations**: solve relaxed convex problem; round to feasible solution

## Multi-Objective Optimization

Multiple conflicting objectives: $\min (f_1(x), f_2(x), \ldots)$. No single optimal solution — instead find the **Pareto frontier**: solutions where no objective can be improved without worsening another.

Methods: weighted sum scalarization, $\epsilon$-constraint method, NSGA-II (evolutionary). Relevant to [[ahp]] and [[balanced-scorecard]] settings.

## OR/ML Connection Points

- **LP/IP**: exact optimization with linear structure; see [[linear-programming]]
- **ML training**: empirical risk minimization = optimization problem; see [[linear-regression]], [[logistic-regression]]
- **Newsvendor**: critical fractile is a first-order condition; see [[newsvendor-problem]]
- **Revenue management**: dynamic programming as sequential optimization; see [[revenue-management]]
- **Portfolio**: QP (mean-variance); see [[portfolio-theory]]

## Related Concepts

- [[linear-programming]]
- [[integer-programming]]
- [[linear-algebra]]
- [[linear-regression]]
- [[logistic-regression]]
- [[newsvendor-problem]]
- [[portfolio-theory]]
- [[stochastic-processes]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
