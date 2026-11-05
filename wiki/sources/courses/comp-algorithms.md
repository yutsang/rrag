---
title: "Design and Analysis of Algorithms"
full_name: "COMP3711 Design and Analysis of Algorithms"
type: source
tags: [courses, comp, undergraduate, algorithms, comp3711, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP3711"
confidence: medium
---

## 概述

COMP3711 演算法設計與分析是香港科技大學計算機科學系三年級的核心必修課，以 Cormen、Leiserson、Rivest 及 Stein《演算法導論》（CLRS，第三版，MIT Press）為標準教材，先修要求為 COMP2012 資料結構及 MATH2343/COMP2711 離散數學。課程系統介紹演算法設計的四大範式（分治法、動態規劃、貪心演算法、圖演算法）及嚴格的複雜度分析工具（漸近符號、主定理、均攤分析），並以具體問題（排序、最短路徑、網路流、字串匹配）驅動每個理論模塊。學生完成課程後能夠設計並嚴格證明演算法的正確性與效率、理解 P 與 NP 的計算複雜性分類體系、應用近似演算法（如頂點覆蓋 2-近似、TSP Christofides 1.5-近似）處理 NP 難問題，以及使用 Ford-Fulkerson 框架求解最大流與二部圖匹配問題。這些技術是運籌學研究的計算主幹：Dijkstra 與 Bellman-Ford 是網路流優化的基礎，動態規劃遞推式廣泛出現在庫存模型與隨機最優控制中，NP 困難性分析則解釋了為何車輛路徑規劃與整數規劃需要啟發式求解器。

## Course Overview

COMP3711 Design and Analysis of Algorithms covers the fundamental paradigms for constructing efficient algorithms and the formal tools to analyze their correctness and complexity. The course bridges theory and practice — every algorithm topic is motivated by a concrete problem (sorting, routing, scheduling, graph processing).

**Prerequisites**: COMP2011/2012 (data structures), MATH2343/2711 (discrete math)
**Credits**: 3 units

## Key Topics

### Algorithm Analysis
- **Asymptotic notation**: Big-O, Ω, Θ — formalizing "how fast does this scale?"
- **Recurrence relations**: Master theorem for divide-and-conquer analysis (T(n) = aT(n/b) + f(n))
- **Time vs. space complexity**: trade-offs in practical algorithm selection

### Divide and Conquer
- Merge sort, quicksort (average vs. worst case), binary search
- Integer multiplication (Karatsuba), matrix multiplication (Strassen O(n^2.807))
- Closest pair of points in O(n log n)

### Greedy Algorithms
- Activity selection, interval scheduling, Huffman encoding
- Minimum spanning trees: Kruskal's and Prim's algorithms
- Single-source shortest paths: Dijkstra's algorithm (requires non-negative weights)
- Proof technique: exchange argument / greedy-stays-ahead

### Dynamic Programming
- Optimal substructure + overlapping subproblems
- Classic problems: longest common subsequence, edit distance, matrix chain multiplication, 0/1 knapsack, coin change
- DP on graphs: all-pairs shortest paths (Floyd-Warshall), Bellman-Ford (handles negative edges)

### Graph Algorithms
- BFS and DFS (with timestamps), topological sort, SCC (Tarjan/Kosaraju)
- Bipartite matching (augmenting paths), maximum flow (Ford-Fulkerson)
- NP-completeness: P vs. NP, reductions, Cook-Levin theorem, common NP-complete problems (3-SAT, Vertex Cover, TSP)

### Advanced Topics (selected semesters)
- Randomized algorithms (Las Vegas vs. Monte Carlo), quickselect
- Approximation algorithms (vertex cover 2-approx, TSP 1.5-approx via Christofides)
- String matching: KMP, Rabin-Karp

## Textbook

Cormen, Leiserson, Rivest, Stein (CLRS) — *Introduction to Algorithms*, 3rd edition. MIT Press. The standard reference for undergraduate algorithms worldwide.

## OR Relevance

This course directly feeds into OR PhD work:
- **Graph algorithms** (Dijkstra, Bellman-Ford, max flow) are the computational backbone of [[network-flows]]
- **DP** recurrences appear in inventory models, [[newsvendor-problem]] extensions, and stochastic control
- **NP-completeness** explains why [[vehicle-routing-problem]] and [[integer-programming]] require heuristics
- **Approximation algorithms** are the bridge between exact OR formulations and practical solver design

## Related Concepts

- [[algorithms-and-data-structures]]
- [[network-flows]]
- [[vehicle-routing-problem]]
- [[integer-programming]]
- [[linear-programming]]
- [[optimization]]
