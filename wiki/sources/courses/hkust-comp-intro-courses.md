---
title: "HKUST Introductory CS Courses"
full_name: "HKUST Introductory Computer Science (COMP1001/1021/2011/2012/2611/2711)"
type: source
tags: [courses, comp, undergraduate, programming, data-structures, discrete-math, comp1001, comp1021, comp2011, comp2012, comp2611, comp2711, level-1]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP"
confidence: medium
---

## 概述

COMP1001、COMP1021、COMP2011、COMP2012、COMP2611 及 COMP2711 構成香港科技大學計算機科學本科課程的基礎階段，從計算機科學概論與 Python 入門，逐步進入 C++ 面向對象程序設計、資料結構實現及計算機組織，面向一、二年級學生，無特定先修要求。COMP1021 以 Python 為教學語言，覆蓋程序設計基礎至物件導向初步；COMP2011/2012 深入 C++ 的記憶體管理、模板及從零實現鏈結串列、平衡樹、雜湊表等核心資料結構；COMP2611 引入 MIPS 組合語言，教授數位邏輯、處理器流水線架構與記憶體階層（快取、虛擬記憶體）。離散數學課 COMP2711 以 Rosen《離散數學》為參考，培養邏輯推理、演算法正確性分析（迴圈不變量、主定理）及圖論基礎。這些課程共同使學生掌握從 Python 腳本到底層 C++ 系統程式設計的全棧能力、理解 Big-O 複雜度分析，並為 COMP3711 演算法、COMP3511 操作系統、COMP4211 機器學習等高年級課程奠定不可或缺的編程與數學基礎。

## Course Structure

| Course | Content | Language |
|---|---|---|
| COMP1001 | Exploring Computer Science | App Inventor / various |
| COMP1021 | Introduction to Computer Science | Python |
| COMP2011 | Programming with C++ | C++ |
| COMP2012 | Object-Oriented Programming and Data Structures | C++ |
| COMP2611 | Computer Organization | Assembly / C |
| COMP2711 | Discrete Mathematical Tools for CS | Mathematics |

## COMP1001: Exploring Computer Science

- Computational thinking: decomposition, pattern recognition, abstraction, algorithms
- Visual programming with MIT App Inventor: events, blocks, mobile app development
- Intro to web technologies: HTML/CSS basics
- Social impacts of computing: privacy, intellectual property, digital divide

## COMP1021: Introduction to Computer Science

**Language**: Python

- Variables, types, expressions; input/output
- Control flow: if/elif/else; while loops; for loops; range()
- Functions: def, parameters, return values; recursion
- Lists, tuples, dictionaries, sets; list comprehensions
- File I/O; exception handling; try/except
- Object-oriented intro: classes, objects, methods, inheritance
- Algorithm intro: linear search, binary search, bubble sort; Big-O intuition
- Intro to graphics/animation: pygame or turtle

## COMP2011: Programming with C++

- Procedural programming in C++: variables, types, operators
- Functions: pass by value vs. reference; function overloading; default parameters
- Arrays and pointers: pointer arithmetic; pointer-array duality; dynamic memory (`new`/`delete`)
- Structs; intro to classes: data members, member functions, constructors/destructors
- Recursion: factorial, Fibonacci, Tower of Hanoi, recursive data structures
- File I/O: streams; reading/writing formatted data
- Memory model: stack vs. heap; dangling pointers; memory leaks

## COMP2012: Object-Oriented Programming and Data Structures

**Language**: C++

### OOP Concepts
- Classes: encapsulation; access control (`public`/`private`/`protected`)
- Operator overloading; copy constructor; Rule of Three/Five
- Inheritance: derived classes; virtual functions; pure virtual; abstract base classes
- Polymorphism: dynamic dispatch; vtable; `dynamic_cast`
- Templates: function templates; class templates; `std::vector`, `std::map`, `std::set`

### Data Structures (implemented from scratch)
- **Linked lists**: singly, doubly, circular; insert/delete/search $O(n)$
- **Stacks**: array and linked-list implementations; applications (balanced parentheses, expression evaluation, DFS)
- **Queues**: circular array; deque; priority queue (binary heap); BFS applications
- **Binary search trees (BST)**: insert, delete, search $O(h)$; height $h = O(n)$ worst case
- **AVL trees**: height-balanced BST; rotations; $O(\log n)$ operations
- **Hash tables**: chaining vs. open addressing; load factor; amortized $O(1)$ operations
- **Graphs**: adjacency matrix vs. list; BFS; DFS; connected components; topological sort
- See [[algorithms-and-data-structures]]

## COMP2611: Computer Organization

**Language**: MIPS Assembly (or ARM for newer offerings)

- Number representations: two's complement; IEEE 754 floating point; endianness
- Digital logic: gates; combinational circuits (ALU, multiplexer); sequential circuits (flip-flops, registers)
- **MIPS ISA**: R/I/J format instructions; register file; load/store architecture
- Assembly programming: arithmetic, branching, loops, procedure calls (stack frame, $ra, $sp)
- Datapath design: single-cycle; multi-cycle; pipelining
- **Pipelining**: IF, ID, EX, MEM, WB stages; data hazards (forwarding, stalls); control hazards (branch prediction)
- Memory hierarchy: locality principle; caches (direct-mapped, set-associative, fully-associative); cache miss types (compulsory, capacity, conflict)
- Virtual memory intro: page tables; TLB; page faults

## COMP2711: Discrete Mathematical Tools for CS

Overlaps with [[hkust-discrete-math|MATH2343 Discrete Mathematics]]. CS-oriented emphasis:
- Propositional and predicate logic; proof techniques (direct, contradiction, induction)
- Set theory; relations; functions; counting (permutations, combinations)
- Graph theory: paths, trees, connectivity; spanning trees; planar graphs
- Number theory: modular arithmetic; RSA intro — see [[cryptography]]
- Algorithm correctness: loop invariants; recurrence relations; Master theorem

## Related Concepts

- [[algorithms-and-data-structures]]
- [[database-systems]]
- [[cryptography]]

## Source Materials

- COMP1001 Course Materials
- COMP1021 Course Materials
- COMP2011 Course Materials
- COMP2012 Course Materials
- COMP2611 Course Materials
- COMP2711 Course Materials
