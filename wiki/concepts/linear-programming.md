---
title: "Linear Programming"
full_name: "Linear Programming (LP)"
type: concept
tags: [optimization, operations-research, linear-programming]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/ieda-operations-research-i"
confidence: high
---

## 概述

線性規劃（Linear Programming, LP）是在線性等式與不等式約束下最大化或最小化線性目標函數的數學優化框架，標準形式為 min cᵀx s.t. Ax ≤ b, x ≥ 0，其中可行域為凸多面體，最優解必然出現在頂點（極點）之上。Dantzig 於 1947 年提出的單純形法（Simplex Method）透過逐步移動頂點尋找最優，實際效率極高，雖然最壞情況為指數時間，但內點法（Interior Point Methods）可在多項式時間內求解。LP 的對偶理論是其核心：每個原始問題對應一個對偶問題，強對偶定理保證兩者最優值相等（在可行且有界時），對偶變數即為約束的影子價格（shadow price），量化每單位右端鬆動帶來的目標改善。靈敏度分析（Sensitivity Analysis）進一步回答成本係數與右端向量在多大範圍內可變動而不改變最優基。LP 是整數規劃的鬆弛基礎、網絡流的通用框架（全么模矩陣保證自動整數解）、隨機規劃的場景子問題，以及機器學習中支持向量機的底層優化結構，是運籌學與管理科學研究者必須掌握的核心工具。

## What It Is

**Linear programming (LP)** is the problem of optimizing a linear objective function subject to linear equality and inequality constraints. It is the foundational model of mathematical optimization:

$$\min_{x} \; c^T x \quad \text{s.t.} \quad Ax \leq b, \; x \geq 0$$

where $x \in \mathbb{R}^n$ are the decision variables, $c$ is the cost vector, $A$ is the constraint matrix, and $b$ is the right-hand-side vector. Maximization problems are converted by negating $c$.

## Why It Matters

LP is practically important for several reasons:
- **Polynomial solvability**: LP can be solved in polynomial time (interior point methods), and the simplex method is fast in practice despite exponential worst-case complexity
- **Duality theory**: every LP has a dual whose solution gives shadow prices — the marginal value of relaxing each constraint
- **Foundation for harder problems**: integer programming relaxes integrality; network flow is a special LP; stochastic programming adds scenarios; dynamic programming has LP reformulations
- **Ubiquity**: production planning, diet problems, airline crew scheduling, portfolio optimization, and LP relaxations of NP-hard combinatorial problems

## How It Works

### Feasible Region and Geometry
The feasible region $\{x : Ax \leq b, x \geq 0\}$ is a **convex polyhedron** (or empty). If an optimal solution exists, it occurs at a **vertex** (extreme point) of this polyhedron — this is why the simplex method, which traverses vertices, works.

### Simplex Method
Developed by Dantzig (1947). Algorithm:
1. Find an initial basic feasible solution (BFS) — a vertex
2. Compute reduced costs for non-basic variables; if all ≥ 0 (for minimization), current BFS is optimal
3. Select entering variable (most negative reduced cost — Bland's rule avoids cycling)
4. Perform a pivot: one variable enters the basis, one leaves (ratio test prevents infeasibility)
5. Repeat until optimality or unboundedness detected

Complexity: exponential worst-case (Klee-Minty example) but typically $O(m)$ pivots for $m$ constraints in practice.

### LP Duality
Every LP (primal) has an associated **dual LP**:

| Primal | Dual |
|---|---|
| $\min c^T x$ | $\max b^T y$ |
| $Ax \geq b$ | $A^T y \leq c$ |
| $x \geq 0$ | $y \geq 0$ |

**Weak duality**: $c^T x \geq b^T y$ for all feasible primal $x$ and dual $y$.
**Strong duality**: if primal is feasible and bounded, optimal values are equal: $c^T x^* = b^T y^*$.

**Economic interpretation**: dual variables $y_i$ are **shadow prices** — the increase in optimal cost per unit increase in $b_i$. If a production constraint has shadow price \$5, relaxing it by 1 unit saves \$5.

### Sensitivity Analysis
After solving, sensitivity analysis asks: how much can coefficients change before the optimal basis changes?
- **RHS ranging**: how much can $b_i$ change while shadow prices remain valid?
- **Objective ranging**: how much can $c_j$ change before the optimal solution changes?
- **100% rule**: multiple simultaneous changes can be evaluated by combining individual ranges

## Practical Applications

**Production planning**: $x_j$ = units of product $j$ to produce; constraints on machine hours, materials; objective minimizes cost or maximizes profit.

**Transportation problem**: LP special case. $x_{ij}$ = flow from supply node $i$ to demand node $j$. Total supply/demand constraints are the rows. Solved more efficiently as a network flow.

**Diet problem**: minimize cost of food while meeting nutritional requirements. Classic Stigler (1945) problem — first computationally solved LP.

**Portfolio allocation** (linear): maximize expected return subject to budget and linear risk constraints (Markowitz mean-variance is a QP, not LP, but linear versions exist).

## Comparison with Alternatives

| Method | When to Use |
|---|---|
| LP | Continuous variables, linear objective and constraints |
| Integer programming | Require integer or binary decisions |
| Quadratic programming | Quadratic objective (portfolio optimization) |
| Dynamic programming | Sequential decisions, optimal substructure |
| Network simplex | LP with network structure — much faster than general simplex |

## Solvers

Commercial: **Gurobi**, **CPLEX**, **Xpress** (industry standard, milliseconds for problems with millions of variables).
Open-source: **GLPK**, **CBC**, **HiGHS** (competitive for moderate-size problems).
Python interfaces: `gurobipy`, `scipy.optimize.linprog`, `PuLP`, `cvxpy`.

## Limitations and Caveats

1. **Linearity assumption**: real objective and constraint functions are often nonlinear (economies of scale, quadratic risk, integer quantities). LP is an approximation in such cases; nonlinear programming or MIP may be required.
2. **Continuous variables**: LP requires continuous decision variables. When decisions are inherently discrete (open a facility or not, assign a worker or not), the LP relaxation may have fractional solutions that are not directly actionable — use [[integer-programming]] instead.
3. **Degeneracy and cycling**: when multiple constraints are tight at a vertex (degenerate BFS), the simplex method can cycle without progress. Bland's rule or perturbation prevents cycling but may slow convergence.
4. **Sensitivity analysis validity range**: shadow prices and ranging results are only valid locally — they assume the optimal basis does not change. Large simultaneous changes invalidate the 100% rule.
5. **Solver numerical precision**: commercial solvers use floating-point arithmetic; near-zero reduced costs may be misclassified. For ill-conditioned problems, interior-point methods are more numerically stable than simplex.

## Related Concepts

- [[integer-programming]]
- [[network-flows]]
- [[optimization]]
- [[newsvendor-problem]]
- [[revenue-management]]
- [[supply-chain-management]]
- [[portfolio-theory]]
- [[facility-location]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
