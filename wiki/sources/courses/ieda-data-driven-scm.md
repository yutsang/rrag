---
title: "IEDA 4410 Data-Driven Supply Chain Management"
full_name: "IEDA 4410: Data-Driven Supply Chain Management"
type: source
tags: [courses, ieda, undergraduate, supply-chain, analytics, data, ieda4410, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA4410/2022 Fall/IEDA4410_Syllabus2022.pdf"
confidence: high
author: "Xuan Qiu"
date_published: "2022-09-01"
---

## 概述

IEDA 4410「數據驅動的供應鏈管理」是香港科技大學 IEDA 學系四年級本科生的選修課，由邱璇教授於 2022 年秋季主講，採用 Simchi-Levi、Kaminsky & Simchi-Levi 的《Designing and Managing the Supply Chain》（McGraw-Hill）為教材，評核方式包括作業（5%）、課堂參與（15%）、小組專案（15%）、期中（25%）及期末考試（40%）。課程以數據分析視角重新審視供應鏈核心問題，系統涵蓋庫存管理（EOQ、安全庫存、Type I/II 服務水準）、風險匯聚策略（集中庫存的 √n 效應）、牛鞭效應控制（根本原因：需求信號處理、短缺博弈、批量訂購、價格波動；Barilla SpA 案例的 CRP 連續補貨方案）、外包與全球供應鏈（自製或外購、Zara 快時尚垂直整合案例）、延遲策略（HP 打印機本地化推遲、時間延遲 vs. 形態延遲）、智能定價與收益管理（動態定價、Allegiant Airline 拆分定價案例）、供應合約與風險分擔（回購合約、收益共享合約、數量彈性合約的渠道協調）、共享經濟平台（Uber 峰時定價、資產利用率）及全球供應鏈設計（Apple/Foxconn/TSMC 案例）。課程直接連結 OR 研究中的供應鏈協調理論，為學生理解從商業案例到數學模型的完整轉化提供系統性訓練。

## Course Overview

**IEDA 4410 Data-Driven Supply Chain Management** (Fall 2022, Prof. Xuan Qiu) introduces supply chain management through the lens of data analytics. The ability to capture, aggregate, and analyze supply chain data is increasingly a competitive mandate. The course uses real-world cases to show how analytics creates competitive advantage.

**Textbook**: Simchi-Levi, Kaminsky & Simchi-Levi, *Designing and Managing the Supply Chain: Concepts, Strategies, and Case Studies*, McGraw-Hill.

## Course Outline

| Week | Topic | Case Study |
|------|-------|------------|
| 1 | Introduction | — |
| 2 | Inventory management | Ch. 2 |
| 3 | Risk pooling strategies | Sport Obermeyer (Ch. 2) |
| 4 | Bullwhip effect controlling | Barilla SpA (Ch. 5) |
| 5 | Outsourcing | Zara: Fast Fashion |
| 6 | Postponement | HP (Ch. 13), Zara online model |
| 7 | Smart pricing | Allegiant Airline (Ch. 13) |
| 8 | Supply contracts and risk sharing | Ch. 4 |
| 9 | Sharing economy | Uber |
| 10 | Supply chain design strategies | Apple Global Supply Chain |

## Key Topics

### Inventory Management (Week 2)

Foundational inventory models:
- **EOQ**: Q* = √(2DS/H). Trades ordering frequency against holding cost.
- **Reorder point**: R = d̄L + z_α σ_L. Safety stock buffers lead-time demand uncertainty.
- **Service levels**: Type I (cycle service level) vs. Type II (fill rate). Fill rate = 1 − ESC/Q where ESC is the expected shortfall per cycle.

See [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] for the stochastic single-period version and [[wiki/concepts/supply-chain-management|Supply Chain Management]] for multi-echelon extensions.

### Risk Pooling Strategies (Week 3)

**Risk pooling**: consolidating inventory across locations or products reduces variability and required safety stock. Under independence, σ_pooled = σ_individual / √n. Under correlation ρ, σ_pooled = σ_individual √(n + n(n−1)ρ) / n.

**Case: Sport Obermeyer**: seasonal fashion items with high demand uncertainty. The company must commit to production before demand is known. The newsvendor model governs the trade-off between over- and under-production. Data from early orders can be used to update forecasts (Bayesian updating).

**Centralization vs. decentralization**: central warehouses benefit from risk pooling; local warehouses provide faster response. The optimal network balances these.

### Bullwhip Effect Controlling (Week 4)

The **bullwhip effect** (Lee, Padmanabhan & Whang, 1997): demand variability amplifies as orders propagate upstream in a supply chain. A retailer's orders are more variable than consumer demand; a distributor's orders are even more variable.

Root causes:
1. **Demand signal processing**: each stage forecasts independently; forecasting errors compound.
2. **Rationing and shortage gaming**: when supply is tight, buyers inflate orders.
3. **Order batching**: economies of scale in ordering create artificial demand spikes.
4. **Price fluctuations**: promotional deals induce forward buying.

**Remedies** (case: Barilla SpA): Barilla's pasta supply chain suffered severe bullwhip. Solution: **Continuous Replenishment Program (CRP)** — Barilla takes over replenishment decisions for distributors, using actual sell-through data. Information sharing eliminates demand distortion.

### Outsourcing and Global Supply Chains (Week 5)

**Make-or-buy**: outsource when a supplier has lower cost or better capability; keep in-house when quality, IP, or responsiveness requires control.

**Case: Zara (Fast Fashion)**: Zara's competitive advantage is speed-to-market. Unlike competitors who outsource to low-cost Asia, Zara manufactures ~50% in-house in Spain/Portugal. This enables 2-week design-to-shelf cycles vs. industry standard 6 months. Higher unit cost is offset by fewer markdowns and stockouts.

**Total cost of outsourcing**: includes unit cost, transportation, lead time, coordination, and **supply chain risk** — disruptions at distant suppliers can be catastrophic.

### Postponement (Week 6)

**Postponement**: delay product differentiation as long as possible to serve multiple market segments from a common platform.

**Case: HP Printers**: HP ships undifferentiated printers to Europe; power supplies (country-specific) are added locally. Reduces safety stock by pooling across countries.

**Form postponement**: delay physical differentiation (configure-to-order vs. build-to-stock).  
**Time postponement**: delay shipment until demand is known (air freight instead of sea).

Postponement requires modular product design and flexible processes — upfront investment in product redesign yields ongoing supply chain savings.

### Smart Pricing (Week 7)

**Dynamic pricing** adjusts prices in response to demand conditions, competition, and inventory levels. Connects to [[wiki/concepts/revenue-management|Revenue Management]].

**Case: Allegiant Airline**: ultra-low-cost carrier with dynamic ancillary revenue model. Pricing of fees (seat selection, baggage, priority boarding) is disaggregated from base fare.

**Price discrimination**: charge different prices to different segments based on willingness to pay. Mechanisms: advance purchase discounts, capacity controls (booking limits), customer-chosen bundles.

### Supply Contracts and Risk Sharing (Week 8)

Coordinating a supply chain where manufacturer and retailer are independent profit-maximizers:

- **Buyback contract**: manufacturer offers to repurchase unsold units at price b. Retailer orders more (closer to integrated optimum). Manufacturer absorbs more risk.
- **Revenue sharing**: manufacturer charges lower wholesale price; receives share φ of retailer revenue. Equivalent to buyback under certain conditions.
- **Quantity flexibility**: manufacturer agrees to supply up to x% more than ordered at the same price; retailer commits to purchasing at least y% of original order.

All these contracts can coordinate the channel (achieve total supply chain profit equal to the integrated optimum) under the right parameter choices.

### Sharing Economy (Week 9)

**Platform business models**: Uber, Airbnb, and Didi connect supply (drivers, hosts) with demand dynamically. Supply chain implications:
- **Surge pricing**: prices rise when demand exceeds supply, simultaneously attracting more drivers and dampening demand.
- **Asset utilization**: platforms monetize idle capacity (cars, apartments).
- **Risk transfer**: asset ownership risk borne by individual suppliers, not the platform.
- **Matching and routing**: algorithms match supply and demand in real time with minimum wait times — an operational research problem.

### Supply Chain Design Strategies (Week 10)

**Case: Apple Global Supply Chain**: Apple designs products in Cupertino, manufactures via Foxconn in China (final assembly), sources components globally (TSMC for chips, Samsung/LG for screens), and sells through Apple Stores and e-commerce. This vertical-disintegration model requires massive coordination.

**Supply chain design dimensions**: facility locations, supplier relationships, product modularity, inventory policies, transportation modes. Design choices are coupled — a highly distributed network requires more coordination and creates more bullwhip risk.

## Related Concepts

- [[wiki/concepts/supply-chain-management|Supply Chain Management]] — foundational framework
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — inventory under uncertainty
- [[wiki/concepts/revenue-management|Revenue Management]] — dynamic pricing and smart pricing
- [[wiki/concepts/facility-location|Facility Location]] — supply chain network design
- [[wiki/concepts/scor-model|SCOR Model]] — supply chain reference architecture

## Source Materials

- raw/courses/IEDA/IEDA4410/2022 Fall/IEDA4410_Syllabus2022.pdf
