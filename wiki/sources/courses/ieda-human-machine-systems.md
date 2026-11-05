---
title: "IEDA 4200 Design of Logistics and Manufacturing Systems"
full_name: "IEDA 4200: Design of Logistics and Manufacturing Systems"
type: source
tags: [courses, ieda, undergraduate, facilities-planning, logistics, manufacturing, ieda4200, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA4200/2021 Fall/IEDA4200_Syllabus2021.pdf"
confidence: high
author: "Xuan Qiu"
date_published: "2021-09-01"
---

## 概述

IEDA 4200「物流與製造系統設計」（原名「人機系統設計」）是香港科技大學 IEDA 學系四年級本科生的選修課，由邱璇教授於 2021 年秋季主講，採用 Tompkins、White、Bozer & Tanchoco 合著的《Facilities Planning》（第 4 版，Wiley，2010）為教材。課程系統介紹工廠、倉庫及配送中心的設施規劃理論與方法，涵蓋設施選址模型（重心法 Weiszfeld 迭代、P 中位數問題、集合覆蓋/P 中心整數規劃，對應 [[wiki/concepts/facility-location|Facility Location]]）、機器佈局與群體技術（Muther 系統化佈局規劃 SLP、零件族分類、製造單元 U 形佈局、零件-機器聚類算法）、流量與活動關係分析（從-到矩陣、活動關係圖 REL chart、綜合親近度評分）、佈局設計（CRAFT/CORELAP/ALDEP 啟發式算法、通道結構規劃）、倉庫作業（儲存策略：專用、隨機、ABC 分類；揀貨方式：單單、批量、分區；COI 法則最優貨位分配；S 形路徑啟發式）及產品-流程-排程設計（線平衡、節拍時間）。課程附設 6 次電腦實驗，使用設施規劃軟體 v1.0 進行重心模型計算與 REL chart 生成佈局，並以設施重設計為期末專案，為供應鏈網絡設計及 IEDA 3460（需求供應分析）的設施選址模型提供工廠與倉庫層面的具體實作基礎。

## Course Overview

**IEDA 4200 Design of Logistics and Manufacturing Systems** (Fall 2021, Prof. Xuan Qiu) provides fundamental concepts, theories, and procedures for facilities planning — the discipline of designing physical layouts for factories, warehouses, and distribution centers to optimize material flow, space utilization, and operational efficiency.

**Textbook**: Tompkins, White, Bozer & Tanchoco, *Facilities Planning*, 4th Ed., Wiley (2010).

## Course Outline

| Module | Topic |
|--------|-------|
| 1 | Introduction to Facilities Planning |
| 2 | Facility Location Models |
| 3 | Machine Layout and Group Technology |
| 4 | Flow and Activity Relationships |
| 5 | Layout Design |
| 6 | Warehouse Operations and Layout |
| 7 | Product, Process, and Schedule Design |

## Key Topics

### Facility Location Models (Module 2)

Strategic placement of facilities within a supply network. Methods:
- **Gravity/centroid model**: minimize total weighted distance ΣW_i · d(X, P_i). Solved iteratively using Weiszfeld's algorithm.
- **P-median problem**: locate p facilities to minimize total demand-weighted travel distance. NP-hard in general; solved by heuristics or Lagrangian relaxation.
- **Set covering / p-center**: minimize maximum distance (minimax formulation) for emergency service coverage.
- **Integer programming formulations**: fixed-charge facility location — see [[wiki/concepts/facility-location|Facility Location]].

### Machine Layout and Group Technology (Module 3)

**Systematic Layout Planning (SLP)**: Muther's structured methodology for designing manufacturing layouts. Steps: (1) input data collection, (2) material flow analysis, (3) activity relationship chart, (4) space requirements, (5) space available, (6) layout alternatives, (7) evaluation.

**Group Technology (GT)**: classifies parts with similar geometries, processes, or materials into **part families** and groups machines into **manufacturing cells**. Benefits: reduced setup times, lower work-in-progress, improved quality.

**Cellular manufacturing**: U-shaped or linear cells where each cell handles a complete family of parts. The **part-machine incidence matrix** and cluster algorithms (binary ordering, rank-order clustering) identify natural groupings.

### Flow and Activity Relationship Analysis (Module 4)

**From-to chart**: matrix of material flows between all department pairs. Entry (i,j) = total weight-distance units moved from department i to j per period.

**Activity relationship chart (REL chart)**: captures non-material-flow relationships (supervision convenience, noise/vibration proximity, shared equipment). Each pair rated A (absolutely necessary to be close) through X (undesirable to be close) with a reason code.

**Combined flow-relationship diagram**: integrates quantitative flow data and qualitative relationship ratings into a composite closeness score for each department pair, driving layout generation.

### Layout Design (Module 5)

**Space requirements**: computed from production volumes, cycle times, machine counts, and allowances for aisles, maintenance, and future growth.

**Block layouts**: assign department blocks to floor area satisfying space constraints and closeness requirements. Heuristic methods:
- **CRAFT (Computerized Relative Allocation of Facilities Technique)**: starts with an initial layout and performs pairwise department exchanges to reduce total material handling cost.
- **CORELAP**: constructs layout by placing highest-closeness-rated departments first.
- **ALDEP**: random placement with improvement by selecting high-relationship pairs.

**Aisle structure**: determines paths for material handling equipment; must balance access to all departments against floor space consumed.

### Warehouse Operations and Layout (Module 6)

**Warehouse functions**: receiving, putaway, storage, order picking, packing, shipping.

**Storage policies**:
- **Dedicated storage**: fixed location for each SKU. Simple but underutilizes space.
- **Randomized storage**: assign to any available slot. Higher utilization; more travel.
- **Class-based storage**: group SKUs by velocity (ABC analysis); dedicate zones to each class.

**Order picking**: the most labor-intensive activity (typically 50–60% of warehouse operating cost). Strategies:
- **Single-order picking**: one picker per order.
- **Batch picking**: pick multiple orders simultaneously; sort afterward.
- **Zone picking**: divide warehouse into zones; each picker handles their zone (pick-and-pass or simultaneous).

**Optimal picking path**: TSP-like problem on warehouse graph. Practical heuristics:
- **S-shape (traversal) routing**: traverse alternating aisles completely.
- **Return routing**: enter each aisle and return to main aisle without traversing.
- **Largest gap heuristic**: leave aisle via the larger of the two gaps from the farthest pick.

**Warehouse layout**: slot fast-moving items near the I/O point to minimize travel. The **COI (Cube per Order Index)** rule: rank items by volume / order frequency; assign lowest COI (fastest, smallest) items to closest locations.

### Product, Process, and Schedule Design (Module 7)

**Product structure / BOM**: defines component relationships; drives material requirements.

**Process plans**: specify sequence of operations, machines, and tooling for each part.

**Production schedules**: master schedule determines which products are produced in which quantities and when, feeding the layout's capacity utilization.

**Line balancing**: allocate tasks to workstations to achieve a target cycle time (takt time = available time / demand rate) while minimizing the number of stations. Solved as an assignment problem.

## Related Concepts

- [[wiki/concepts/facility-location|Facility Location]] — optimization models for facility placement
- [[wiki/concepts/supply-chain-management|Supply Chain Management]] — facilities as a key supply chain driver
- [[wiki/concepts/capacity-planning|Capacity Planning]] — production rate and bottleneck analysis

## Source Materials

- raw/courses/IEDA/IEDA4200/2021 Fall/IEDA4200_Syllabus2021.pdf
