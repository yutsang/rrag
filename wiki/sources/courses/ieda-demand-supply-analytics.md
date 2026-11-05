---
title: "IEDA 3460 Demand and Supply Analytics"
full_name: "IEDA 3460: Demand and Supply Analytics"
type: source
tags: [courses, ieda, undergraduate, supply-chain, operations, ieda3460, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3460/syllabus_2022.pdf"
confidence: high
author: "Allen Wu"
date_published: "2022-09-01"
---

## 概述

IEDA 3460「需求與供應分析」是香港科技大學 IEDA 學系三年級本科生的整合性必修課，由 Allen Wu 教授於 2022 年秋季主講，採用 Chopra & Meindl 的《Supply Chain Management: Strategy, Planning, & Operation》（第 6 版）為教材，評核方式包括作業（15%）、期中報告與展示（35%）及期末考試（50%）。課程以總經理視角審視供應鏈，系統涵蓋供應鏈設計與設施選址（整數規劃建模）、總體計劃（追趕策略 vs. 平準策略的線性規劃）、庫存管理（EOQ 周期庫存、安全庫存計算 z·σ_L、報童模型最優臨界比、多級庫存與風險匯聚）、運輸規劃（直達 vs. 輻射中樞、奶車路線與越庫）、供應鏈風險管理（冗餘、靈活性、延遲策略）及供應鏈協調（牛鞭效應根源、VMI、CPFR、回購合約與收益共享合約）。課程亦探討採購（自製或外購、TCO 分析、反向拍賣）及電商對供應鏈設計的顛覆性影響。作為 IEDA 4100（供應管理）與 IEDA 4420（動態定價）的整合橋樑，本課為學生建立從策略到執行的完整供應鏈分析框架，是工業工程與運籌學 OR 研究的重要應用基礎。

## Course Overview

**IEDA 3460 Demand and Supply Analytics** (Fall 2022, Prof. Allen Wu) is the integrative supply chain course in the IEDA curriculum, bridging the supply-side (IEDA 4100) and demand-side (IEDA 4420) specializations. The course views the supply chain from a general manager's perspective: supply chains are networks of organizations that supply and transform materials and distribute final products to customers. When designed and managed properly, they are a crucial source of competitive advantage.

**Textbook**: Chopra & Meindl, *Supply Chain Management: Strategy, Planning, & Operation*, 6th Ed.

## Course Outline

| Week | Topic |
|------|-------|
| 1 | Supply Chain Design, Planning & Operation |
| 2 | Facility Location |
| 3 | Supply Chain Planning |
| 4–6 | Inventory Management |
| 7 | Transportation |
| 8 | Supply Chain Risks |
| 9 | Supply Chain Coordination |
| 10 | Sourcing |
| 11 | E-Commerce and Supply Chains |

## Key Topics

### Supply Chain Design and Facility Location (Weeks 1–2)

Supply chain design involves decisions about the number, location, and capacity of facilities (warehouses, plants, distribution centers). These are **strategic decisions** with long time horizons that determine the physical configuration of the network. The **facility location problem** (see [[wiki/concepts/facility-location|Facility Location]]) seeks to place facilities at minimum cost while satisfying customer demand within service-level constraints.

Chopra & Meindl frame facility decisions as one of the six **supply chain performance drivers**: facilities, inventories, transportation, information, sourcing, and pricing. The responsiveness–efficiency trade-off runs through all of them: more facilities increase responsiveness but raise fixed costs; consolidation improves efficiency but lengthens lead times.

### Supply Chain Planning (Week 3)

Aggregate planning translates demand forecasts into production, workforce, and inventory decisions over a medium-term horizon (typically 3–18 months). Approaches include:
- **Chase strategy**: adjust production to match demand each period — low inventory, high labour flexibility cost.
- **Level strategy**: maintain constant production rate — builds inventory in low-demand periods.
- **Mixed strategies**: combination, solved as a linear program with capacity and workforce constraints.

The key output is a disaggregated **master production schedule (MPS)** that feeds inventory and purchasing decisions.

### Inventory Management (Weeks 4–6)

Inventory is the largest cost lever in most supply chains. The course covers:

- **Cycle stock** (EOQ): trade-off between ordering cost and holding cost. EOQ = √(2DS/H) where D is annual demand, S is ordering cost, H is holding cost per unit per year.
- **Safety stock**: buffer against demand and supply uncertainty. Safety stock = z · σ_L where z is the service-level z-score and σ_L is the standard deviation of demand during lead time.
- **Newsvendor model**: single-period stochastic inventory for perishable or fashion goods. The optimal order quantity satisfies the critical ratio CR = (p − c)/(p − s), equating underage and overage costs. See [[wiki/concepts/newsvendor-problem|Newsvendor Problem]].
- **Multi-echelon inventory**: coordination across distribution tiers to avoid the **bullwhip effect** — demand variability amplification as orders propagate upstream.
- **Risk pooling**: centralizing inventory reduces total safety stock by exploiting demand correlation. Var(D_total) = Σ Var(D_i) + 2·ΣΣ Cov(D_i, D_j); under independence, pooling saves √n factor.

### Transportation (Week 7)

Transportation decisions span mode selection (road, rail, air, sea, intermodal), carrier type (private, dedicated, common carrier), and routing/scheduling. Key trade-offs:
- **Direct shipping vs. hub-and-spoke**: direct minimizes transit time; hub-and-spoke reduces total distance when shipments are small.
- **Milk runs**: a single truck visits multiple suppliers/customers, reducing per-unit cost.
- **Cross-docking**: goods transferred directly from inbound to outbound vehicles at a terminal, eliminating warehousing.
- **Transportation network design** is closely linked to [[wiki/concepts/facility-location|Facility Location]] — the two problems are often solved jointly.

### Supply Chain Risks (Week 8)

Supply chain disruptions (natural disasters, supplier failures, geopolitical events) can be catastrophic. Mitigation strategies:
- **Redundancy**: multiple suppliers, safety stock buffers, backup capacity.
- **Flexibility**: dual sourcing, postponement, modular product design.
- **Resilience**: rapid detection and response systems, pre-negotiated contingency contracts.
- **Risk pooling across products and geographies**: diversifying demand reduces exposure.

### Supply Chain Coordination (Week 9)

The **bullwhip effect** arises when each stage of the supply chain independently optimizes its own ordering, amplifying variability. Root causes: demand signal processing, rationing game, order batching, price fluctuations. Remedies:
- **Information sharing**: sharing point-of-sale data with upstream suppliers (e.g., VMI — Vendor-Managed Inventory).
- **Collaborative planning**: joint forecasting (CPFR — Collaborative Planning, Forecasting, and Replenishment).
- **Contract design**: buyback contracts, revenue sharing contracts, and quantity flexibility contracts can coordinate the channel and improve total supply chain profit.

### Sourcing (Week 10)

Sourcing decisions include make-or-buy, supplier selection, and contract negotiation. Key frameworks:
- **Total cost of ownership (TCO)**: beyond purchase price, includes transportation, inspection, inventory, and risk costs.
- **Supplier portfolio management**: sole-source vs. multi-source trade-off between economies and risk.
- **Procurement auctions**: reverse auctions for commodity inputs; relationship-based procurement for complex components.

### E-Commerce and Supply Chains (Week 11)

E-commerce fundamentally reshapes supply chain design:
- **Direct-to-consumer (DTC) fulfillment**: eliminates retail tier but requires individual-order picking capability.
- **Last-mile delivery**: the most expensive and difficult segment; options include carrier delivery, locker networks, and drone/autonomous vehicle delivery.
- **Omnichannel fulfillment**: coordinating store, warehouse, and online channels to serve customers flexibly.

## Related Concepts

- [[wiki/concepts/supply-chain-management|Supply Chain Management]] — overarching framework for the course
- [[wiki/concepts/facility-location|Facility Location]] — Week 2 strategic network design
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — core stochastic inventory model
- [[wiki/concepts/revenue-management|Revenue Management]] — pricing driver of demand
- [[wiki/concepts/queueing-theory|Queueing Theory]] — service system models relevant to distribution
- [[wiki/concepts/scor-model|SCOR Model]] — supply chain reference framework

## Source Materials

- raw/courses/IEDA/IEDA3460/syllabus_2022.pdf
