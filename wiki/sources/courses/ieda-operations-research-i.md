---
title: "Operations Research I"
full_name: "IEDA3010 Operations Research I"
type: source
tags: [courses, ieda, undergraduate, operations-research, ieda3010, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3010"
confidence: medium
---

## 概述

IEDA 3010「運籌學 I」是香港科技大學 IEDA 學系三年級本科生的核心必修課，前置要求為 IEDA 2010 及線性代數基礎，採用 Hillier & Lieberman 的《Introduction to Operations Research》（第 9 版，McGraw-Hill）為主要教材。課程系統涵蓋確定性最佳化的三大支柱：線性規劃（LP 建模、圖解法、單純形法、大 M 法與兩階段法、LP 對偶理論、靈敏度分析與影子價格）、整數規劃（分支定界、Gomory 割平面、集合覆蓋與資本預算等 IP 建模）及動態規劃（Bellman 最優性原理、最短路徑、資源分配、設備替換與庫存問題）。課程亦涵蓋網絡最佳化專題（Dijkstra 最短路徑、Ford-Fulkerson 最大流、最小費用流），並以運輸問題與分配問題為 LP 特例加以說明。LP 對偶理論與 DP 的 Bellman 方程是 OR 博士課程中定價、隨機控制及收益管理研究的直接先修知識，整數規劃建模語言更廣泛應用於供應鏈設計、排程及設施選址等實際問題。

## Course Overview

IEDA3010 Operations Research I is the foundational OR course in the IEDA undergraduate curriculum. It covers the core deterministic optimization models that form the basis for all subsequent OR work.

**Textbook**: Hillier & Lieberman, *Introduction to Operations Research*, 9th edition (McGraw-Hill).

## Key Topics

### Linear Programming
- LP formulation: decision variables, objective function, constraints
- Graphical method (2-variable case), corner-point theorem
- Simplex method: basis, pivoting, entering/leaving variables
- Big-M and two-phase methods for finding initial BFS
- LP duality: primal-dual pairs, complementary slackness
- Sensitivity analysis: ranging for RHS and objective coefficients, shadow prices

### Transportation and Assignment
- Transportation problem: balanced/unbalanced formulation, northwest corner, Vogel's approximation
- Assignment problem: Hungarian algorithm
- These are LP special cases solved more efficiently as [[network-flows]]

### Integer Programming
- Pure and mixed integer programs; binary variables
- Branch-and-bound algorithm: branching, bounding, pruning
- Gomory cutting planes
- Classic IP formulations: set covering, capital budgeting, fixed-charge

### Dynamic Programming
- Principle of optimality, Bellman equation
- Deterministic DP: shortest path, resource allocation, equipment replacement, inventory
- Stage-state-decision decomposition

### Network Models (Selected Topics)
- Shortest path: Dijkstra's algorithm
- Maximum flow: Ford-Fulkerson
- Minimum cost flow: transportation as special case

## OR PhD Relevance

This course is the direct precursor to OR PhD work:
- LP duality is foundational for understanding MIP formulations and pricing in revenue management
- DP formalism connects to stochastic control and reinforcement learning
- IP modeling is the language of supply chain design ([[facility-location]], crew scheduling, etc.)

## Related Concepts

- [[linear-programming]]
- [[integer-programming]]
- [[network-flows]]
- [[vehicle-routing-problem]]
- [[newsvendor-problem]]
- [[facility-location]]
