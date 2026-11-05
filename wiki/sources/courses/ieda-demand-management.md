---
title: "IEDA 4420 Dynamic Pricing and Revenue Optimization"
full_name: "IEDA 4420: Dynamic Pricing and Revenue Optimization"
type: source
tags: [courses, ieda, undergraduate, revenue-management, pricing, demand, ieda4420, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA4420/IEDA4420_Project.pdf"
confidence: medium
author: "Guillermo Gallego"
date_published: "2022-01-01"
---

## 概述

IEDA 4420「動態定價與收益優化」是香港科技大學 IEDA 學系四年級本科生的選修課，由 Guillermo Gallego 教授於 2022 年春季主講，作為 IEDA 4100（供應管理）的需求端對應課程，兩者共同構成 IEDA 3460（需求供應分析）的完整理論基礎。課程深入探討收益管理（Revenue Management / Yield Management）的理論與實踐，系統涵蓋需求建模與預測（歷史訂位曲線、指數平滑、截尾需求的反截尾 EM 估計）、單資源容量控制（EMSR-a/EMSR-b 多艙位保護水平算法，結構等同報童問題的臨界比）、動態定價（隨機動態規劃 V_t(x)、最優定價結構性結果、零售降價策略）、網絡收益管理（多航段聯程定價的 LP 對偶影子價格競標控制、重新優化）及超額預訂（no-show 分佈建模、最優超訂量的報童結構）。課程無完整教材，以課程專案作為核心考核：學生須選定一個真實行業（航空、酒店、零售、網約車等），深入研究現行收益管理實踐，評估其優劣並提出改善方案，最終呈交書面報告並進行 25 分鐘展示，直接對接 OR 研究與業界的動態定價應用場景。

## Course Overview

**IEDA 4420 Dynamic Pricing and Revenue Optimization** (Spring 2022, Prof. Guillermo Gallego) is the demand-side complement to IEDA 4100 (supply management), together forming the foundation for IEDA 3460 (Demand and Supply Analytics). The course focuses on how firms use pricing and capacity allocation to match stochastic demand with fixed or perishable supply.

No dedicated syllabus was recovered; content is reconstructed from the course project description and curriculum context. The course project asks students to analyze a specific revenue management problem in practice, covering: industry overview, current RM practice, strengths/weaknesses assessment, and improvement proposals.

## Key Topics

### Core Revenue Management Framework

**Revenue management (RM)** — also called yield management — uses data-driven pricing and inventory control to maximize revenue from a fixed, perishable capacity. Classic industries: airlines (seats), hotels (rooms), rental cars, sports/entertainment (event seats). Increasingly applied to retail, e-commerce, and manufacturing. See [[wiki/concepts/revenue-management|Revenue Management]].

The fundamental RM problem: a seller has C units of a perishable good and faces stochastic demand from customer segments with different willingness-to-pay. The seller must decide when to accept or reject requests from each segment.

### Demand Forecasting and Modeling

Accurate demand forecasting is the prerequisite for effective RM. Methods:
- **Historical booking curves**: track the evolution of bookings as the departure/event date approaches. Fit pickup models.
- **Time series models**: exponential smoothing, Holt-Winters for seasonal patterns. See [[wiki/concepts/arma-models|ARMA Models]] for foundations.
- **Unconstrained demand estimation**: observed bookings are censored when capacity sells out. Detruncation (EM algorithm, booking curve projection) estimates true demand.
- **Demand segmentation**: separate fare/product classes have different demand distributions. Model each segment separately.

### Single-Resource Capacity Control

**Expected Marginal Seat Revenue (EMSR)**: the core algorithm for static multi-class seat inventory control. For n fare classes ordered p₁ > p₂ > ... > pₙ:

- **EMSR-a (Belobaba, 1987)**: protection level y_j for class j satisfies P(D_j > y_j) = p_{j+1}/p_j where D_j is demand for classes 1 through j.
- **EMSR-b**: uses aggregated demand distribution for classes 1...j; typically outperforms EMSR-a.

The **newsvendor structure** is explicit: [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] with the critical ratio equal to the relative price ratio.

### Dynamic Pricing

**Dynamic pricing** adjusts prices over time in response to remaining capacity and time-to-sale. The stochastic dynamic program:

V_t(x) = max_p { p · λ(p)Δt + V_{t+Δt}(x − 1) · λ(p)Δt + V_{t+Δt}(x) · (1 − λ(p)Δt) }

where x = remaining capacity, t = time remaining, λ(p) = demand rate as a function of price.

**Structural results**:
- Optimal price p*(x,t) is decreasing in x (more inventory → lower price) and increasing or non-monotone in t depending on demand elasticity.
- The revenue function V_t(x) is concave in x.

**Markdown pricing**: for retail, prices only decrease over time (one-direction constraint). Optimal stopping-time structure.

### Network Revenue Management

For airlines with multiple flight legs and connecting itineraries, single-leg RM is suboptimal — accepting a low-fare passenger on one leg may displace a high-value connecting passenger.

**Bid price controls**: assign a shadow price (bid price) π_i to each leg i. Accept a request for itinerary j at fare f_j if and only if f_j ≥ Σ_{i∈j} π_i. Bid prices are the LP dual variables from the deterministic network RM LP.

**Re-optimization**: update bid prices as bookings accumulate and the LP is re-solved with updated inventory and demand forecasts.

### Overbooking

Airlines overbook because of no-shows. The optimal overbooking level balances:
- **Spoilage cost**: empty seats when passengers who were denied boarding would have shown up.
- **Denied boarding cost**: compensation paid to bumped passengers.

Mathematically equivalent to the newsvendor problem: overbook to level y* where P(show-ups ≤ y*) = c_u / (c_u + c_o).

### Supply Chain Connections

IEDA 4420 is explicitly paired with IEDA 4100 in the curriculum. Connections:
- **Supply contracts with price-dependent demand**: when retailers face downward-sloping demand, the wholesale price affects both the retailer's order quantity and the retail price, complicating contract design.
- **Postponement and dynamic pricing**: firms that can delay commitments (postponement) can also price more dynamically.
- **Demand shaping**: RM is not purely reactive — firms can use pricing to shift demand across time periods or products to better utilize supply. See [[wiki/concepts/supply-chain-management|Supply Chain Management]].

## Project Structure

The course project requires students to:
1. Select a specific RM problem in a real industry (airlines, hotels, retail, ride-sharing, etc.).
2. Understand the industry context, customer characteristics, and current RM practice.
3. Assess strengths and weaknesses of the current approach.
4. Propose and quantify improvement opportunities.

Deliverables: written proposal (March), final written report + 25-minute presentation (May).

## Related Concepts

- [[wiki/concepts/revenue-management|Revenue Management]] — core topic of the course
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — structural foundation for capacity control
- [[wiki/concepts/arma-models|ARMA Models]] — demand forecasting methods
- [[wiki/concepts/supply-chain-management|Supply Chain Management]] — demand-supply integration

## Source Materials

- raw/courses/IEDA/IEDA4420/IEDA4420_Project.pdf
