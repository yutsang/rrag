---
title: "Operating Systems"
full_name: "COMP3511 Operating Systems"
type: source
tags: [courses, comp, undergraduate, operating-systems, concurrency, memory-management, comp3511, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP3511"
confidence: medium
---

## 概述

COMP3511 操作系統為計算機科學三年級學生提供現代操作系統核心機制的全面訓練，以 Silberschatz、Galvin 及 Gagne《操作系統概念》（第九至第十版，即「恐龍書」）為標準教材，先修要求為 COMP2012 資料結構及 COMP2611 計算機組織。課程系統涵蓋進程與執行緒管理（PCB、上下文切換、pthreads）、CPU 排程演算法（FCFS、SJF、Round Robin、Linux CFS）、同步與並行控制（信號量、監視器、Banker 演算法死鎖避免）、記憶體管理（分頁、TLB、虛擬記憶體與頁面置換演算法），以及檔案系統實作（inode、ext4 日誌）與 I/O 子系統（DMA、磁碟排程）。學生完成課程後能夠分析並發程序的競爭條件、設計防死鎖策略、理解容器技術（Docker namespaces 與 cgroups）的操作系統基礎，並對系統性能瓶頸（CPU、記憶體、I/O）進行系統性診斷。操作系統是軟硬件之間的核心抽象層，對於分佈式系統工程、雲端基礎設施設計及高性能運算應用均具有不可或缺的理論支撐作用。

## Course Overview

**Textbook**: Abraham Silberschatz, Peter Galvin & Greg Gagne, *Operating System Concepts* (9th ed.)

Covers the classic OS topics plus modern concerns like virtualization and multicore systems.

## Key Topics

### Process Management
- Process vs. program; process state diagram: new → ready → running → waiting → terminated
- Process Control Block (PCB): PID, state, registers, memory maps, open files
- **Context switching**: saving/restoring PCB; overhead; kernel mode vs. user mode
- Inter-process communication (IPC): shared memory, message passing, pipes, sockets
- **Threads**: user-space vs. kernel threads; threading models (many-to-one, one-to-one, many-to-many)
- POSIX threads (pthreads) API; thread pools

### CPU Scheduling
- Scheduling criteria: CPU utilization, throughput, turnaround time, waiting time, response time
- Algorithms:
  - **FCFS**: simple; convoy effect
  - **SJF / SRTF**: optimal average waiting time; predicting next burst (exponential averaging)
  - **Round Robin (RR)**: time quantum; preemptive; trade-off between response and context-switch overhead
  - **Priority scheduling**: starvation; aging solution
  - **Multilevel feedback queues**: modern schedulers (Linux CFS — Completely Fair Scheduler)
- Multiprocessor scheduling: processor affinity; NUMA; load balancing; gang scheduling

### Synchronization and Concurrency
- **Race conditions**: critical section problem; requirements (mutual exclusion, progress, bounded waiting)
- Software solutions: Peterson's algorithm; bakery algorithm
- Hardware support: test-and-set; compare-and-swap (CAS); atomic instructions
- **Semaphores**: counting and binary; P (wait) and V (signal) operations; busy-waiting vs. blocking
- **Monitors**: high-level synchronization; condition variables; Mesa vs. Hoare semantics
- **Classic problems**: dining philosophers; producer-consumer; readers-writers
- **Deadlock**: four conditions (mutual exclusion, hold-and-wait, no preemption, circular wait)
  - Prevention, avoidance (Banker's algorithm), detection and recovery

### Memory Management
- Address binding: compile time, load time, execution time
- Logical vs. physical address space; MMU (Memory Management Unit)
- **Contiguous allocation**: fixed vs. variable partitions; fragmentation; compaction
- **Paging**: page table; page number + offset; TLB (translation lookaside buffer); hierarchical page tables
- **Segmentation**: logical segments (code, data, stack); segment table
- **Virtual memory**: demand paging; page faults; page replacement algorithms:
  - FIFO, Optimal (Bélády's), LRU (clock approximation); Bélády's anomaly
  - Thrashing: working set model; page fault frequency

### File Systems
- File attributes; file operations; directory structures (single-level, tree, acyclic graph)
- Allocation methods: contiguous (simple; fragmentation), linked (no fragmentation; random access slow), indexed (FAT, inode)
- **Free space management**: bit vector, linked list, grouping
- UNIX/Linux filesystem: inodes; ext4 journal; symbolic vs. hard links
- NTFS (Windows): MFT; journaling; compression and encryption

### I/O Systems
- I/O hardware: polling, interrupts, DMA (direct memory access)
- Kernel I/O subsystem: buffering; caching; spooling; device drivers
- Disk scheduling: FCFS, SSTF, SCAN (elevator), C-SCAN, C-LOOK
- RAID: levels 0, 1, 5, 6, 10; performance and redundancy trade-offs

### Virtualization and Containers
- Type 1 (bare-metal) vs. Type 2 (hosted) hypervisors; VMware, KVM, Hyper-V
- Paravirtualization: Xen; guest OS awareness
- **Containers**: Docker; namespaces (PID, network, mount); cgroups for resource limits; image layers

## Related Concepts

- [[algorithms-and-data-structures]]
- [[database-systems]]
- [[web-architecture]]

## Source Materials

- COMP3511 Course Materials
