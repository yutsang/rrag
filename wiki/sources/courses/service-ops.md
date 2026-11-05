---
title: "Service Operations Management"
full_name: "Service Operations Management (EEMT5520)"
type: source
tags: [course, hkust, service-operations, littles-law, queueing, newsvendor, revenue-management, eemt5520, level-5]
created: "2026-04-10"
updated: "2026-04-14"
source: "raw/courses/EEMT5520 Servicce Ops Mgt/"
confidence: high
author: "HKUST ISOM (Prof. Ronald S. Lau)"
date_published: "2026-06"
---

## 概述

EEMT5520「服務營運管理」是香港科技大學工程管理碩士（MSc EEMT）課程的核心必修科，由 Ronald S. Lau 教授（ISOM 系）主講，針對具備工程或技術背景的研究生，以定量分析框架系統介紹服務業運營管理。課程從服務的四大特性（不可儲存性 IHIP：無形性、異質性、生產消費同步性、易逝性）出發，依序展開六大模塊：流程分析（流程圖、瓶頸識別、生產節拍）、Little's Law（L = λW 在排隊與庫存中的通用性）、產能規劃（有效產能、利用率非線性擁堵效應）、排隊理論（M/M/1 穩態公式 L = ρ/(1-ρ)、M/M/s Erlang-C 公式、M/D/1 確定服務時間使等待減半、排隊池效應）、報童問題（臨界比 C_u/(C_u+C_o)、離散與正態需求求解、HKUST Cookie King 及 Arome Bakery 55 家分店案例）及收益管理（動態定價、容量控制 EMSR 保護水平、超額預訂最優量的報童結構）。課程個案包括國泰貨運碼頭 HK$48 億建設 vs. 外包的 NPV 決策（WACC 12.09%，NPV ≈ HK$26.7 億）、Arome Bakery 激勵設計問題（店長以退貨率考核但缺成本可見性）、Fat Angelo's 意大利餐廳等候行管理（Maister 八大等候心理原則）、759 Store 直接進口繞過經銷商的策略，以及 LeadNitro AI SaaS 產能規劃，是連結 IEDA 3250（隨機模型）與業界服務系統設計的重要應用橋樑。

## Course Overview

**EEMT5520 Service Operations Management** is a quantitative course in the HKUST EMBA program covering the analytical foundations of managing service operations. The course progresses from process fundamentals through stochastic models, building a toolkit for capacity and demand management decisions.

### Module Structure

| Module | Topic | Key Concepts |
|--------|-------|-------------|
| 1 | Service Concepts | Service characteristics, perishability, customer as co-producer |
| 2 | Process Analysis & Little's Law | Flow diagrams, bottleneck identification, L = λW |
| 3 | Capacity Planning | Effective capacity, utilization, bottleneck analysis |
| 4 | Queueing Models | M/M/1, M/M/s, M/D/1, limited population models |
| 5 | Newsvendor Problem | Critical ratio, discrete/continuous demand, optimal order quantity |
| 6 | Revenue Management | Dynamic pricing, capacity control, overbooking |

## Key Concepts and Frameworks

### Service Characteristics

Services differ fundamentally from manufacturing in several ways:

- **Perishability** -- service capacity cannot be stored; an empty airline seat on a departed flight is lost revenue forever.
- **Simultaneity** -- production and consumption happen concurrently; the customer is present during service delivery.
- **Variability** -- both demand arrival patterns and service times exhibit randomness.
- **Customer as flow unit** -- in service processes, the customer themselves flows through the system, unlike goods in manufacturing.

The Oasis Airlines case study illustrates how a Hong Kong-based long-haul budget carrier attempted to manage these challenges with an all-business-class model before ultimately failing due to demand variability and cost pressures.

### Process Analysis

Process analysis uses **flow diagrams** to map activities, buffers, and resources. Key metrics include:

- **Cycle time (T)** -- time to complete one unit at a resource.
- **Flow time** -- total time a flow unit spends in the system (from entry to exit).
- **Throughput (R)** -- rate at which flow units exit the process.
- **Bottleneck** -- the resource with the longest cycle time (or lowest capacity), constraining the entire process.

Examples covered include T-shirt production lines, insurance claims processing, and hair salon operations.

### Little's Law

[[littles-law|Little's Law]] establishes the universal relationship **L = λW**:

- L = average number of flow units in the system (inventory)
- λ = average throughput rate
- W = average flow time (time in system)

This holds for any stable system regardless of arrival distribution, service distribution, or number of servers. Applications range from calculating average customers in a bank queue to determining work-in-progress inventory in manufacturing.

### Capacity Planning

[[capacity-planning|Capacity planning]] determines the maximum sustainable throughput of a process:

- **Effective capacity** of resource pool i: $c_i / T_i$ (number of units divided by unit processing time).
- **Process capacity** $= \min(c_i / T_i)$ across all resources -- determined by the bottleneck.
- **Utilization** = throughput / capacity; when utilization approaches 1.0, congestion grows nonlinearly.
- **Capacity waste factor** accounts for setups, maintenance, and other non-productive time.

### Queueing Theory

[[queueing-theory|Queueing models]] provide steady-state performance metrics for systems with random arrivals and service times:

- **M/M/1**: Single server, Poisson arrivals (rate $\lambda$), exponential service (rate $\mu$). Key formulas: $\rho = \lambda/\mu$, $L = \frac{\rho}{1-\rho}$, $W = \frac{1}{\mu-\lambda}$.
- **M/M/s**: Multiple identical servers sharing one queue. Requires $\rho = \frac{\lambda}{s\mu} < 1$. Uses $P_0$ and $P_w$ calculations for waiting probability.
- **M/D/1**: Deterministic (constant) service times reduce average waiting by half compared to M/M/1.
- **Pooling effect**: Combining separate queues into one (e.g., two M/M/1 systems into one M/M/2) reduces average wait time -- demonstrated with the Pizza Hut drive-through example.

### Newsvendor Problem

The [[newsvendor-problem|newsvendor problem]] addresses single-period inventory decisions under demand uncertainty:

- **Critical ratio**: $P(D \leq Q^*) = \frac{C_u}{C_u + C_o}$, where $C_u$ = revenue - cost (underage cost) and $C_o$ = cost - salvage (overage cost).
- **Discrete demand**: Compute cumulative probabilities, find smallest $Q$ where $P(D \leq Q) \geq$ critical ratio.
- **Continuous demand** (normal): $Q^* = \mu + z\sigma$, where $z$ corresponds to the critical ratio in the standard normal table.
- Applications: newspaper vendors, Cookie King bakery at HKUST, fashion retail seasonal ordering.

### Revenue Management

[[revenue-management|Revenue management]] maximizes revenue from perishable capacity through three levers:

- **Dynamic pricing**: Adjust prices based on willingness to pay (WTP) and demand forecasts. Revenue = price x min(demand, capacity).
- **Capacity control**: Protect seats for high-fare customers using the newsvendor framework. Protection level $Q^*$ uses critical ratio $F(Q) = \frac{C_u}{C_u + C_o}$, with $C_u$ = full fare - discount fare and $C_o$ = discount fare.
- **Overbooking**: Accept more reservations than capacity to account for no-shows. Optimal overbooking quantity balances $C_u$ (cost of empty seat from underestimating no-shows) against $C_o$ (cost of denied boarding from overestimating no-shows).

The airline capacity control example (HK to London, 335 seats, full fare \$7950 vs. discount \$5250) demonstrates how marginal analysis and decision trees arrive at the same protection level ($Q^* = 23$ seats).

## Practical Examples

- **Pizza Hut M/M/1 vs M/M/2**: Demonstrated pooling benefits -- combining two single-server drive-through lanes into one two-server queue reduced average wait from 3 minutes to 0.75 minutes.
- **Cookie King at HKUST**: Discrete newsvendor problem -- cookies sell for \$7.9, cost \$4.9, markdown to \$2.9. Optimal production = 2,400 units with expected profit \$6,650.
- **Airline seat protection**: Full fare \$7,950 vs discount \$5,250, demand ~ Normal(25, 5). Critical factor = 0.3396, z = -0.41, optimal protection level $Q^*$ = 23 seats.
- **Textbook pricing with WTP**: Single price \$40 maximizes revenue at \$3,360; segmented pricing captures additional consumer surplus.
- **Arome Bakery replenishment**: 55-store Hong Kong chain uses daily newsvendor models for specialty buns. Aberdeen store (residential): mean 1,158, optimal $Q^* \approx$ 1,188/day at critical ratio 0.60. Jordan MTR store (commercial): mean 3,098, $Q^* \approx$ 3,260. Case highlights incentive design — store managers were scored on return rates but lacked cost visibility.
- **Cathay Pacific Cargo Terminal**: Long-horizon capacity decision (HBP case ST19A). HACTL's SuperTerminal 1 capped at 2.6M tonnes; a captive Cathay terminal would cost HK\$4.8B with a 20-year concession. Decision balances control, DNA-fit ("full-service cargo carrier"), and lack of terminal-operation experience.
- **Psychology of waiting**: Eight Maister principles (unoccupied vs occupied, pre-process vs in-process, uncertain vs known, unexplained, unfair, anxious, solo, valuable) complement analytical M/M/s design.

## Case Studies Covered

| Case | Primary concept | Key numbers / takeaways |
|------|----------------|-------------|
| **Cathay Pacific Air Cargo** | [[capacity-planning\|Capacity planning]] + NPV build-vs-contract | HACTL SuperTerminal 1 capped at 2.6M tonnes; HK\$4.8B build (rising to HK\$5.5B); 20-year concession; Cathay = 60% of SuperTerminal 1 volume; worksheet NPV with WACC 12.09% (debt 4.1% / equity 11.9% / risk premium 3%), HK\$240M straight-line depreciation, 60% initial utilization improving 2%/yr, 1% organic growth → NPV ≈ HK\$2.67B |
| **Arome Bakery** | [[newsvendor-problem\|Newsvendor]] + incentive design | 55 Hong Kong stores (Maxim's Group); June 2012 worksheet: Aberdeen residential store mean 1,158, σ ≈ 118; Jordan MTR store mean 3,098, σ ≈ 650 (commercial, weekday-skewed); selling price HK\$7.80, cost HK\$3.12, salvage 0 → $C_u = 4.68$, $C_o = 3.12$, critical ratio 0.60; $Q^*_\text{Aberdeen} \approx 1{,}188$, $Q^*_\text{Jordan} \approx 3{,}260$; HQ return-rate target 5% (actual 2.8–9.8%); store managers lacked cost visibility |
| **Fat Angelo's** | [[queueing-theory\|Waiting-line management]] + table turnover | Tsuen Wan location: 26 tables, ~100 covers, 3.5-person average party, 90-min average cycle time → one table freed every 3.5 min at full occupancy; peak dinner 7:30-9:00 pm, 65 parties arrive 6:30-9:45 pm, queue peaks at 28 parties waiting ≈ 98 min max wait; 40% balk when wait > 30 min; HK\$200 dinner / HK\$80 lunch avg spend; Groupon fee HK\$250K; levers = early-bird 15% discount, Groupon, bar diversion, Maister waiting psychology |
| **759 Store** | Retail strategy, supply-chain disintermediation, "lower margin with high turnover" (see [[financial-ratios\|Financial Ratios]] cross-course case) | Founded 2010 by Lam Wai-Chun (CEC International, HKEX 0759); peaked at ~280 stores, cut to 179 by 2019; 23,500+ SKUs from 61 countries (Japan 42%, Europe 16%); 90%+ direct imports bypassing HK's slotting-fee distributor duopoly (Wellcome, ParknShop take ~75% share); 37.5% gross margin vs competitors' 40–50%; FY2019 revenue HK\$1.84B, 2016 first operating loss; "Coca-Cola incident" (2011) crystallized sourcing strategy; case question = assortment/pricing under JPY appreciation and retail slowdown |
| **LeadNitro** | [[capacity-planning\|Capacity ramp-up]], scaling a SaaS operation, target-segment choice | AI SaaS for BDR lead generation (founded 2023, Austin TX); SaaS price USD 3,000/mo flat, 60-day time-based trial → value-based trial (30 days post first booked meeting); 20+ clients Q1 2024, target USD 150K/mo by Dec 2024; needs USD 2M raise by end-2024; 11 → 20 → 50 employees projected; valuation ~5–8× ARR (private B2B SaaS); GBA expansion dilemma (IP risk, talent pool); exercises capacity/scaling decisions and target-customer segmentation in a fast-growth service ops setting |
| **Oasis Airlines** | [[revenue-management\|Service characteristics]] & failed business model | All-business-class HK-long-haul budget carrier; failed from demand variability + cost pressure; illustrates perishability and simultaneity — the same fare-class and load-factor economics covered under [[revenue-management\|Revenue Management]] |

## Related Concepts

- [[littles-law|Little's Law]]
- [[queueing-theory|Queueing Theory]]
- [[newsvendor-problem|Newsvendor Problem]]
- [[revenue-management|Revenue Management]]
- [[capacity-planning|Capacity Planning]]

## Source Materials

- 01 - Service Concepts
- 04 - Process Analysis
- Little's Law Slides
- 05A - Process Capacity
- Capacity Planning Slides
- 05 - Queueing Models (Textbook)
- M/M/s Queueing Model Slides
- 08 - Newsvendor Problem (Textbook)
- Newsvendor Model Slides
- 09B - Revenue Management Slides
- Yield Management (Textbook)
- Cathay Pacific (A) Case + NPV Worksheet
- Arome Bakery Case + Sales Worksheet
- Fat Angelo's Case + Waiting-Line Worksheet
- 759 Store Case
- LeadNitro Case
