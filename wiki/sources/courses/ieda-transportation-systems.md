---
title: "IEDA 3901 Transportation Systems"
full_name: "IEDA 3901: Transportation Systems"
type: source
tags: [courses, ieda, undergraduate, transportation, logistics, ieda3901, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3901/Bon_Source/IEDA 3901 Syllabus.pdf"
confidence: high
author: "Jin Qi"
date_published: "2021-01-01"
---

## 概述

IEDA 3901「交通系統」是香港科技大學 IEDA 學系三年級本科生的選修課，由金琦博士（Jin Qi）於 2021 年春季主講，參考教材包括 Sussman 的《Introduction to Transportation Systems》、Khisty 的《Transportation Engineering: An Introduction》及 Papacostas & Prevedouros 的《Transportation Engineering and Planning》。課程從工程與運營管理雙重視角介紹交通系統，系統涵蓋交通系統分類與性能指標（容量、吞吐量、速度、可靠性）、運輸經濟學（成本結構、需求彈性、Ramsey 定價、擁堵外部性、Braess 悖論）、交通流量理論（流量-密度-速度基本圖、自由流與擁堵態勢、衝擊波分析）及四步驟出行需求模型（出行生成迴歸模型、重力模型出行分配、Logit 模式選擇、Wardrop 用戶均衡路徑分配與 Frank-Wolfe 算法）。課程評核包括四次作業（20%）、小組專案（20%）、期中（25%）及期末考試（35%），並以香港交通規劃及物流基礎設施為具體應用情境，與 IEDA 3410（路徑與車隊管理）及 IEDA 3460（需求供應分析）形成互補，為城市物流規劃、港口容量設計及供應鏈網絡優化提供交通工程基礎。

## Course Overview

**IEDA 3901 Transportation Systems** (Spring 2021, Dr. Jin Qi) introduces students to transportation systems from both engineering and operations management perspectives. The course develops conceptual understanding of the transportation planning process and core quantitative techniques in transportation economics, traffic flow theory, and demand modeling.

**Prerequisites**: None specified beyond standard IEDA curriculum.  
**References**: Sussman (2000) *Introduction to Transportation Systems*; Khisty (2002) *Transportation Engineering: An Introduction*; Papacostas & Prevedouros (2000) *Transportation Engineering and Planning*.

## Course Outline

| Module | Topic |
|--------|-------|
| 1 | Introduction to Transportation Systems |
| 2 | Transportation Economics |
| 3 | Traffic Flow Fundamentals |
| 4 | Transportation Planning and Demand Modeling |
| 5 | Contemporary Topics |

## Key Topics

### Introduction to Transportation Systems (Module 1)

Transportation systems are classified by mode (road, rail, air, waterway, pipeline) and by function (passenger vs. freight). Key performance metrics: capacity, throughput, speed, reliability, and cost per ton-mile. The concept of **modal split** describes how travelers or shippers choose among available modes.

System structure: transportation infrastructure (roads, ports, airports), vehicles, operators, and regulatory frameworks all interact. Understanding this structure is prerequisite for planning and policy analysis.

### Transportation Economics (Module 2)

**Cost structure**: transportation industries have high fixed costs (infrastructure, rolling stock) and relatively low variable costs, leading to significant economies of scale and scope.

**Demand elasticity**: price elasticity of demand for transportation services varies by mode and trip purpose. Business travel is relatively inelastic; leisure travel is more elastic. Freight elasticity depends on the value-to-weight ratio of goods.

**Pricing principles**: marginal cost pricing is economically efficient but may not recover fixed costs. **Ramsey pricing** (inverse elasticity rule) recovers costs while minimizing welfare loss. Congestion pricing (e.g., road tolls) aligns private and social costs.

**Network externalities**: congestion creates negative externalities — each additional user imposes costs on others. Braess's paradox illustrates that adding capacity can sometimes worsen average travel times in equilibrium.

### Traffic Flow Theory (Module 3)

**Flow-density-speed relationship**: the fundamental diagram of traffic flow relates:
- Flow (q): vehicles per hour
- Density (k): vehicles per kilometer
- Speed (u): km/hour
- Identity: q = k · u

**Free-flow regime**: density below critical value; speed near free-flow speed; flow increases with density.  
**Congested regime**: density above critical value; speed drops; flow decreases with density.  
**Capacity**: maximum sustainable flow rate at the critical density.

**Shockwave analysis**: changes in flow conditions propagate as waves. The speed of a shockwave between two flow states is w = (q₂ − q₁)/(k₂ − k₁).

**Queuing at bottlenecks**: when demand exceeds capacity, queues form upstream. Deterministic queuing models track queue length and delay as a function of arrival and departure rates — directly related to [[wiki/concepts/queueing-theory|Queueing Theory]].

### Transportation Planning and Demand Modeling (Module 4)

The **four-step model** is the standard framework for forecasting travel demand in a region:

1. **Trip Generation**: predict the number of trips produced by and attracted to each zone, using regression models on land use, demographics, and socioeconomic data.
2. **Trip Distribution**: assign generated trips between origin-destination pairs. The **gravity model** (T_ij = A_i · O_i · D_j / d_ij^β) is the most common formulation — analogous to Newton's law of gravitation.
3. **Modal Choice (Mode Split)**: allocate trips to modes using **logit models** — P(mode m) = exp(V_m) / Σ_k exp(V_k) where V_m is the systematic utility of mode m (a function of travel time, cost, comfort).
4. **Trip Assignment (Route Choice)**: load trips onto the network. **User equilibrium** (Wardrop's first principle): in equilibrium, no traveler can reduce travel time by unilaterally switching routes. Solved by minimizing a Beckmann objective function via Frank-Wolfe algorithm.

### Logistics Infrastructure Planning

The course connects transportation theory to logistics: port capacity planning, intermodal terminal design, and the interaction between transportation network structure and supply chain design. This bridges to [[wiki/concepts/facility-location|Facility Location]] and [[wiki/concepts/supply-chain-management|Supply Chain Management]].

## Related Concepts

- [[wiki/concepts/queueing-theory|Queueing Theory]] — analytical models for congestion and delay
- [[wiki/concepts/facility-location|Facility Location]] — transportation network and facility co-design
- [[wiki/concepts/supply-chain-management|Supply Chain Management]] — logistics and freight transportation

## Source Materials

- raw/courses/IEDA/IEDA3901/Bon_Source/IEDA 3901 Syllabus.pdf
- raw/courses/IEDA/IEDA3901/ESU_Source/Syllabus.pdf
