---
title: "Network Flows"
full_name: "Network Flow Optimization"
type: concept
tags: [optimization, operations-research, graph-theory, network-flows]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/ieda-routing-fleet-management"
confidence: high
---

## 概述

網絡流優化是在有向圖 G = (N, A) 上分配流量以最小化成本的運籌學框架，統一涵蓋最短路徑、最大流、最小費用流（Minimum Cost Flow, MCF）及最小生成樹（MST）等基礎問題。最小費用流是最一般的網絡流模型：min Σ cij xij，約束為各節點的流量守恆（供給/需求平衡）及弧容量上下限，最短路徑和最大流均為其特例。網絡流問題具有特殊的數學結構：約束矩陣完全么模（Totally Unimodular），因此 LP 鬆弛的最優解在整數資料下自動為整數，無需分支定界。網絡單純形法（Network Simplex）利用樹形基可行解的結構，在實際中比通用 LP 求解器快 10–100 倍，大型運輸問題甚至快千倍。核心演算法包括 Dijkstra（非負邊權最短路，O((V+E)logV)）、Bellman-Ford（允許負邊權，O(VE)）、Ford-Fulkerson / Edmonds-Karp（最大流）及 Kruskal / Prim（最小生成樹），最大流最小割定理（Max-Flow Min-Cut Theorem）是其核心對偶結果。應用範疇涵蓋物流路由、供應鏈運輸規劃、二部圖匹配、航班人員排班及電信容量規劃，並作為設施選址 Benders 分解的運輸子問題和車輛路線問題列生成的定價子問題基礎。

## What It Is

Network flow models represent a system as a **directed graph** $G = (N, A)$ where $N$ is a set of nodes and $A$ is a set of directed arcs. Each arc $(i,j)$ carries a **flow** $x_{ij}$ with capacity $u_{ij}$, cost $c_{ij}$, and lower bound $l_{ij}$. The general minimum-cost flow problem is:

$$\min \sum_{(i,j) \in A} c_{ij} x_{ij} \quad \text{s.t.} \quad \sum_j x_{ij} - \sum_k x_{ki} = b_i \; \forall i \in N, \quad l_{ij} \leq x_{ij} \leq u_{ij}$$

where $b_i > 0$ for supply nodes, $b_i < 0$ for demand nodes, and $b_i = 0$ for transshipment nodes.

## Core Problems

### 1. Shortest Path
Find the minimum-cost path from source $s$ to sink $t$.

**Dijkstra's algorithm** (non-negative edge weights): greedy, O((V + E) log V) with a priority queue. Used for GPS routing, network routing protocols.

**Bellman-Ford** (handles negative edges): dynamic programming relaxation, O(VE). Detects negative cycles. Used in financial arbitrage detection, distributed routing (OSPF).

**Floyd-Warshall** (all-pairs): O(V³) DP. Practical for dense graphs, $V \leq 1000$.

### 2. Maximum Flow
Find the maximum amount of flow from source $s$ to sink $t$ respecting capacities.

**Ford-Fulkerson**: augment along any $s$-$t$ path in the residual graph. Convergence issue with irrational capacities.

**Edmonds-Karp**: Ford-Fulkerson using BFS for shortest augmenting path. O(VE²). Provably converges.

**Max-flow min-cut theorem** (Ford & Fulkerson, 1956): The maximum flow equals the minimum capacity of any $s$-$t$ cut. Fundamental duality result in combinatorics.

Applications: network reliability, bipartite matching (via flow reduction), project scheduling (critical path via max flow), airline scheduling.

### 3. Minimum Cost Flow (MCF)
The most general network flow problem: send required amounts of flow at minimum cost.

**Network simplex method**: the most efficient algorithm in practice, exploiting the tree structure of basic feasible solutions. Typically $O(VE \log V \log(VC))$ but extraordinarily fast empirically.

Special cases of MCF:
- Shortest path: single unit of flow from $s$ to $t$
- Maximum flow: infinite capacity, minimize negative flow
- Transportation problem: bipartite supply-demand network
- Assignment problem: unit capacities in bipartite matching

### 4. Minimum Spanning Tree (MST)
Find a tree connecting all nodes with minimum total edge weight.

**Kruskal's algorithm**: sort edges by weight, add edge if it doesn't create a cycle (union-find). O(E log E).

**Prim's algorithm**: grow tree greedily from a starting node. O((V + E) log V) with priority queue.

Applications: network design (telecommunications backbone), cluster analysis, approximation algorithms for TSP (Christofides uses MST as subroutine).

## Why Network Flows Are Special

Network flow LPs have a **totally unimodular** constraint matrix — meaning every LP relaxation has an integer optimal solution. This is why network flow problems with integer data automatically yield integer solutions without branch-and-bound.

Practical impact: network simplex is 10–100× faster than general LP simplex for equivalent problems, and 1000× faster for large transportation problems.

## Key Reference

Ahuja, Magnanti, Orlin — *Network Flows: Theory, Algorithms, and Applications* (Prentice Hall, 1993). The definitive textbook, used in IEDA3410.

## Applications in OR

| Application | Network Flow Model |
|---|---|
| Logistics routing | Shortest path / MCF |
| Supply chain | Transportation / MCF |
| Project scheduling | Critical path (longest path) |
| Matching (workers to jobs) | Bipartite max flow |
| Airline crew scheduling | MCF + IP |
| Telecommunications | Max flow (capacity planning) |

## Related Concepts

- [[linear-programming]]
- [[vehicle-routing-problem]]
- [[integer-programming]]
- [[supply-chain-management]]
- [[logistics-and-transportation]]
- [[algorithms-and-data-structures]]
- [[facility-location]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
