---
title: "Algorithms and Data Structures"
full_name: "Algorithms and Data Structures"
type: concept
tags: [computer-science, algorithms, data-structures, computational-complexity]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/comp-algorithms"
confidence: high
---

## 概述

演算法與資料結構是計算機科學的核心，研究如何高效地組織數據（陣列、雜湊表、平衡二元搜尋樹、堆積、B+ 樹、圖）及求解計算問題（排序、搜尋、最短路徑、最小生成樹）。Big-O 漸近複雜度分析提供了比較演算法效率的統一語言，從 $O(1)$ 哈希查詢到 $O(n!)$ 全排列暴力搜尋，構成評估算法實用性的基本工具。動態規劃（DP）是連結算法理論與運籌學的核心橋樑：最優子結構與重疊子問題這兩個條件直接對應 Bellman 最優性原理，DP 在庫存批次定劃（Wagner-Whitin）、收益管理（嵌套預定）及隨機控制（Bellman 方程）中均有直接應用。貪心算法在活動選擇、Huffman 編碼及 Dijkstra 最短路徑等具有貪心選擇性質的問題上達到最優解，但在 0-1 背包和旅行商問題上失效，後者需 DP 或分支定界法。NP 完全性理論（Cook-Levin 定理：SAT 是第一個 NP 完全問題）為整數規劃、車輛路徑規劃等 OR 核心問題的計算難度提供了理論依據，也解釋了為何大規模實例需要啟發式算法和近似算法而非精確求解。字符串算法（KMP、Rabin-Karp）和後綴陣列在 NLP 文本索引與生物信息學序列比對中具有直接應用價值。

## Complexity Analysis

**Big-O notation**: $f(n) = O(g(n))$ means $f$ grows no faster than $g$ asymptotically. Ignores constants and lower-order terms.

| Complexity | Name | Example |
|---|---|---|
| $O(1)$ | Constant | Hash table lookup |
| $O(\log n)$ | Logarithmic | Binary search |
| $O(n)$ | Linear | Linear scan |
| $O(n \log n)$ | Linearithmic | Merge sort |
| $O(n^2)$ | Quadratic | Insertion sort, naive matrix multiply |
| $O(n^3)$ | Cubic | Floyd-Warshall, matrix multiply (naive) |
| $O(2^n)$ | Exponential | Brute-force TSP |
| $O(n!)$ | Factorial | All permutations |

**Space complexity**: memory usage as a function of input size.

**Amortized analysis**: average cost per operation over a sequence (e.g., dynamic array append: $O(1)$ amortized despite occasional $O(n)$ resize).

## Core Data Structures

### Arrays and Linked Lists
- **Array**: $O(1)$ access, $O(n)$ insert/delete. Cache-friendly.
- **Dynamic array** (Python list, C++ vector): amortized $O(1)$ append.
- **Linked list**: $O(1)$ insert at known position, $O(n)$ search.

### Hash Tables
$O(1)$ average for insert/search/delete. Collisions handled by chaining or open addressing. Load factor $\alpha < 0.75$ keeps performance good.

Applications: frequency counting, memoization in DP, set operations.

### Trees
**Binary search tree (BST)**: $O(h)$ operations where $h$ is height. Unbalanced: $O(n)$ worst case.

**Balanced BSTs**: AVL trees, Red-Black trees — $O(\log n)$ guaranteed. Used in `std::set`, `java.util.TreeMap`.

**B+ trees**: balanced, high branching factor, optimized for disk access. Used in database indexes. Supports range queries.

**Heap** (priority queue): complete binary tree with heap property. $O(\log n)$ insert and extract-min. Used in Dijkstra's algorithm, scheduling.

### Graphs
Represented as adjacency list (sparse: $O(V + E)$ space) or adjacency matrix (dense: $O(V^2)$). See [[network-flows]] for graph algorithms.

## Fundamental Algorithms

### Sorting
- **Merge sort**: $O(n \log n)$, stable, divide and conquer. $T(n) = 2T(n/2) + O(n)$ — Master theorem gives $O(n \log n)$.
- **Quicksort**: $O(n \log n)$ average, $O(n^2)$ worst (with random pivot → expected $O(n \log n)$). In-place, cache-efficient.
- **Heapsort**: $O(n \log n)$ worst, in-place but not stable.
- **Counting/Radix sort**: $O(n + k)$ for integers in range $[0, k)$ — beats comparison lower bound $O(n \log n)$.

### Searching
- **Binary search**: $O(\log n)$ on sorted array.
- **BFS/DFS**: $O(V + E)$ graph traversal.

### String Algorithms
- **KMP**: $O(n + m)$ pattern matching (avoids re-scanning).
- **Rabin-Karp**: hash-based, average $O(n + m)$, useful for multiple patterns.
- **Suffix arrays**: enables $O(m \log n)$ search and many string operations; used in bioinformatics and text indexing.

## Dynamic Programming

**DP** solves problems with **optimal substructure** (optimal solution contains optimal sub-solutions) and **overlapping subproblems** (same subproblems solved repeatedly → memoize).

**Two approaches**:
- **Top-down (memoization)**: recursive + cache
- **Bottom-up (tabulation)**: fill table iteratively

### Classic DP Problems

**Longest Common Subsequence (LCS)**: $dp[i][j] = dp[i-1][j-1] + 1$ if match, else $\max(dp[i-1][j], dp[i][j-1])$. $O(mn)$.

**0/1 Knapsack**: $dp[i][w] = \max(dp[i-1][w], dp[i-1][w-w_i] + v_i)$. $O(nW)$ — pseudo-polynomial.

**Bellman-Ford** (shortest path with negative edges): $dp[v][k]$ = min cost path to $v$ using $\leq k$ edges. $O(VE)$.

**Matrix chain multiplication**: $O(n^3)$ DP for optimal parenthesization.

**Edit distance (Levenshtein)**: $O(mn)$ DP; used in spell-check, diff tools, sequence alignment.

**DP in OR**: inventory lot-sizing (Wagner-Whitin algorithm), stochastic DP (Bellman equation for MDPs), revenue management (see [[revenue-management]]).

## Greedy Algorithms

Greedy makes the locally optimal choice at each step. Works when the **greedy choice property** holds.

Correct greedy algorithms:
- Activity selection / interval scheduling
- Huffman encoding
- Dijkstra's shortest path (non-negative weights)
- Prim's/Kruskal's MST
- Fractional knapsack

Fails for: 0/1 knapsack, TSP.

## NP-Completeness

**P**: decision problems solvable in polynomial time.
**NP**: decision problems verifiable in polynomial time.
**NP-complete**: in NP and NP-hard (every NP problem reduces to it in polynomial time).

**Cook-Levin theorem** (1971): SAT is NP-complete. From SAT, hundreds of problems shown NP-complete via polynomial reductions: 3-SAT → Vertex Cover → Hamiltonian Cycle → TSP.

**Implications for OR**: [[vehicle-routing-problem]], [[integer-programming]] (in general), graph coloring, scheduling are NP-hard → exact solvers use B&B; heuristics for large instances.

## Related Concepts

- [[network-flows]]
- [[integer-programming]]
- [[vehicle-routing-problem]]
- [[linear-programming]]
- [[database-systems]]
- [[optimization]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
- [[wiki/mocs/cs-data-science|CS and Data Science MOC]]
