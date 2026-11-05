---
title: "Integer Programming"
full_name: "Integer Programming (IP / MIP)"
type: concept
tags: [optimization, operations-research, integer-programming, combinatorial-optimization]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/ieda-operations-research-i"
confidence: high
---

## 概述

整數規劃（Integer Programming, IP / MIP）是要求部分或全部決策變量取整數值的優化問題，混合整數規劃（MIP）則同時包含連續與整數變量，二元整數規劃（0-1 IP）是最常見的子類別，用二元變量編碼是否開設設施、分配任務或選擇路線等決策。整數規劃屬於 NP 難問題類別，LP 鬆弛（去除整數約束）與整數最優之間的「整數間隙（integrality gap）」可能很大，因此直接四捨五入 LP 解往往不可行甚至不最優。現代求解器的核心演算法是分支定界法（Branch-and-Bound）：遞迴地在分數值變量上分叉建立子問題，以 LP 鬆弛的下界剪枝；結合割平面法（Cutting Planes，如 Gomory 切割、覆蓋不等式）構成分支割平面法（Branch-and-Cut），是 Gurobi、CPLEX 等商業求解器的基礎架構。對超大規模問題（如車輛路線問題），分支定價法（Branch-and-Price）透過列生成按需生成可行路線作為決策變量，將百萬變量問題化為可解結構。大 M 法、邏輯蘊含約束及固定成本建模是 IP 建模的標準技巧，廣泛應用於設施選址、排程、背包問題及旅行商問題（TSP）等運籌學核心問題。

## What It Is

An **integer program (IP)** requires some or all decision variables to take integer values:
$$\min_{x} \; c^T x \quad \text{s.t.} \quad Ax \leq b, \; x \geq 0, \; x_j \in \mathbb{Z} \; \forall j \in \mathcal{I}$$

**Mixed-integer program (MIP)**: some variables continuous, some integer.
**Binary IP (0-1 IP)**: all integer variables are $\{0, 1\}$ — most common in practice.

## Why Integer Constraints Matter

The LP relaxation (drop integrality) may have non-integer optimal solutions that are infeasible for the IP. Example: LP says "build 0.7 factories" — rounding is not always optimal or feasible. The **integrality gap** between LP relaxation and IP optimal can be large for hard instances.

## Modeling with Binary Variables

Binary variables $x_j \in \{0, 1\}$ encode yes/no decisions:

**Assignment**: $x_{ij} = 1$ if worker $i$ assigned to job $j$. Constraint: $\sum_j x_{ij} = 1$ (each worker gets one job).

**Facility location**: $y_j = 1$ if facility $j$ is opened. $x_{ij} = 1$ if customer $i$ served from $j$. Constraints link assignment to opening decisions.

**Disjunctive constraints** (either/or): $(Ax \leq b) \text{ OR } (Cx \leq d)$ modeled as: add binary $z$, impose $Ax \leq b + M(1-z)$ and $Cx \leq d + Mz$ (Big-M formulation).

**Logical implications**: $x_1 = 1 \Rightarrow x_2 = 1$ becomes $x_1 \leq x_2$.

**Fixed costs**: cost $f_j$ incurred if $x_j > 0$: minimize $\sum_j (c_j x_j + f_j y_j)$ where $y_j \geq x_j/M$.

## Algorithms

### Branch-and-Bound (B&B)

The workhorse of MIP solvers. Algorithm:
1. Solve LP relaxation. If solution is integral, done (optimal for IP).
2. Select a fractional variable $x_j = \bar{x}$ (branching). Create two subproblems: $x_j \leq \lfloor \bar{x} \rfloor$ and $x_j \geq \lceil \bar{x} \rceil$.
3. Recursively solve each; prune if LP lower bound ≥ current best integer solution (upper bound).
4. Best feasible solution found is optimal.

**Node selection**: best-first (minimize lower bound, explores wider tree), depth-first (finds integer solutions faster, less memory).
**Variable selection**: most fractional, strong branching (solve children LP before committing).
**Primal heuristics**: at each node, try to round or fix a feasible integer solution ("diving").

### Cutting Planes

Add linear constraints (cuts) that are valid for all integer solutions but violated by the current LP relaxation. Tighten the relaxation without branching.

**Gomory cuts**: mechanically derived from the simplex tableau; guaranteed to cut off any fractional solution.

**Problem-specific cuts**: exploit problem structure.
- **Cover inequalities** for knapsack: if $\sum_{j \in C} w_j > b$ (cover $C$ exceeds capacity), then $\sum_{j \in C} x_j \leq |C| - 1$
- **Subtour elimination** for TSP
- **Benders cuts** for structured two-stage problems

### Branch-and-Cut

Modern solvers combine B&B with automatic cut generation (Gomory, lift-and-project, flow covers, etc.) at each node. Gurobi's B&C can solve MIPs with millions of variables.

### Branch-and-Price

For large-scale IPs with too many variables: column generation within B&B. Pricing subproblem generates new columns (routes, schedules) on demand. Essential for [[vehicle-routing-problem]] with hundreds of customers.

## Important Problem Classes

| Problem | IP Formulation | Complexity |
|---|---|---|
| Knapsack | Binary variables, one capacity constraint | NP-hard (weakly) |
| Set cover | $y_j \in \{0,1\}$, cover constraints | NP-hard |
| Facility location | Open/close + assignment | NP-hard |
| TSP | Binary arc variables, subtour elimination | NP-hard |
| Scheduling | Binary job-machine assignments | NP-hard |
| Lot-sizing | Binary setup + continuous inventory | NP-hard |

## Solver Landscape

| Solver | Notes |
|---|---|
| **Gurobi** | Industry gold standard, academic free licenses |
| **CPLEX** (IBM) | Mature, enterprise-grade |
| **SCIP** | Open-source research solver |
| **CBC** | Open-source, used in PuLP by default |
| **OR-Tools** (Google) | Constraint programming + MIP |

Python: `gurobipy`, `python-mip`, `PuLP`, `cvxpy` (for MILP via `GLPK_MI`).

## Related Concepts

- [[linear-programming]]
- [[vehicle-routing-problem]]
- [[network-flows]]
- [[facility-location]]
- [[newsvendor-problem]]
- [[optimization]]
- [[algorithms-and-data-structures]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
