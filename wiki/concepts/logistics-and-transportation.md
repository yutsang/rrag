---
title: "Logistics and Transportation"
full_name: "Logistics and Freight Transportation"
type: concept
tags: [logistics, transportation, supply-chain, operations]
created: "2026-04-14"
updated: "2026-04-14"
source: "https://en.wikipedia.org/wiki/Logistics"
confidence: high
---

## 概述

物流與運輸（Logistics and Transportation）涵蓋從起源地到目的地的貨物計劃、執行與控制，是供應鏈管理的核心執行功能，物流成本通常佔產品總成本的 10–15%，佔多數國家 GDP 的 8–15%。五大運輸模式（航空、海運、鐵路、公路、管道）各有其速度—成本—容量取捨定位：航空適合高值時敏貨物，海運以最低成本移動全球 80% 貿易量，公路則主導最後一哩配送。現代貨運廣泛採用多式聯運（Intermodal），標準貨櫃（20 呎 TEU / 40 呎 FEU）使不同模式之間無需重新裝卸即可轉換，既降低搬運成本又保持靈活性。倉儲是運輸的靜態互補功能，越庫作業（Cross-Docking）透過消除儲存環節進一步壓縮週期時間。在運籌學中，物流問題的核心模型包括：最小費用流（網絡流，適用於幹線路由）、車輛路線問題（VRP，適用於末端配送）及設施選址（倉庫與配送中心佈局）；貨運定價則融合收益管理的負載因子與艙位控制邏輯。第三方物流（3PL）與第四方物流（4PL）的興起反映了外包策略與資產輕量化的趨勢，而 Amazon、Zara 等企業將物流效率作為核心競爭優勢的案例，說明物流系統設計已從成本中心演變為戰略能力的來源。

## What It Is

**Logistics** encompasses the planning, execution, and control of the movement and storage of goods, services, and information from origin to destination to meet customer requirements. **Transportation** is the physical movement component — the largest single cost in most logistics systems.

Together, logistics and transportation bridge supply and demand across geographic space and time, enabling modern global commerce.

## Why It Matters

- **Cost driver**: Logistics costs represent 8–15% of GDP in most countries and 10–15% of product value in manufacturing supply chains.
- **Customer service driver**: Delivery speed, reliability, and flexibility directly determine customer satisfaction.
- **Competitive advantage**: Superior logistics is a key differentiator for companies like Amazon (same-day delivery), Zara (fast fashion replenishment), and DHL (global express).
- **Supply chain backbone**: All [[wiki/concepts/supply-chain-management|Supply Chain Management]] activities depend on reliable logistics execution.

## Transportation Modes

Each mode occupies a distinct position in the speed-cost-capacity trade-off space:

| Mode | Speed | Cost | Capacity | Best For |
|---|---|---|---|---|
| Air | Fastest | Highest | Low | High-value, time-sensitive |
| Ocean | Slowest | Lowest | Very high | Bulk commodities, containerized goods |
| Rail | Medium | Medium | High | Heavy/bulk over long distances |
| Road/Truck | Flexible | Medium-high | Medium | Door-to-door, last mile |
| Pipeline | Continuous | Low | High | Liquids and gases |

### Air Transportation
**Air freight** is used when speed justifies cost — typically products with high value-to-weight ratios (electronics, pharmaceuticals, perishables) or time-critical components. Key structures:
- **Freighter aircraft** (dedicated cargo) vs. **belly cargo** on passenger flights
- **Hub-and-spoke** routing: cargo consolidates at major hubs (Hong Kong, Dubai, Memphis) before onward distribution
- **Air waybill (AWB)**: the freight contract and shipment document

### Ocean/Water Transportation
**Ocean shipping** moves ~80% of world trade by volume. Key structures:
- **Container shipping**: 20-ft (TEU) and 40-ft (FEU) standard containers enable intermodal transfer
- **Liner services**: scheduled routes with fixed ports of call; spot vs. contract rates
- **Tramp shipping**: non-scheduled, chartered for specific cargo
- **Vessel types**: containerships, bulk carriers (coal, grain), tankers (oil, LNG), Ro-Ro (vehicles)

### Land Transportation
**Trucking** dominates last-mile delivery and short/medium haul in most economies:
- **FTL (Full Truckload)**: shipper fills entire trailer; lower per-unit cost
- **LTL (Less-Than-Truckload)**: shared trailer with multiple shippers; higher per-unit cost but flexible
- **Rail freight**: cost-efficient for heavy, bulk commodities over long distances; less flexible than trucking
- **Drayage**: short-distance trucking connecting ports/rail terminals to warehouses

### Intermodal Transportation
Modern freight chains multiple modes using standardized containers without repacking. A typical Asia-to-Europe shipment: factory truck → port → container ship → port → train → distribution center truck. Intermodalism reduces handling cost and damage while enabling each mode to serve its optimal distance range.

## Freight Networks and Routing

### Hub-and-Spoke vs. Point-to-Point
- **Hub-and-spoke**: cargo flows from origins to a central hub, then fans out to destinations. Achieves scale economies at hubs but adds a handling step.
- **Point-to-point**: direct routes between origin-destination pairs. Only viable for high-volume corridors.

### Vehicle Routing Problem (VRP)
Determining optimal routes for a fleet of vehicles to serve a set of delivery locations while minimizing cost or distance. Extensions: VRP with time windows (VRPTW), capacitated VRP (CVRP). Connects to [[vehicle-routing-problem]].

### Network Flows
Logistics networks can be modeled as minimum-cost flow problems on directed graphs: nodes are facilities/ports, arcs are transport links with capacity and cost. Connects to [[network-flows]].

## Warehousing

Warehouses are the stationary complement to transportation — they store inventory between movements.

### Warehouse Operations
- **Receiving**: inbound shipment check-in, quality inspection
- **Put-away**: moving goods to storage locations (slotting)
- **Picking**: retrieving items for outbound orders (labor-intensive — 50–60% of warehouse cost)
- **Packing and shipping**: consolidating and dispatching outbound orders

### Cross-Docking
**Cross-docking** eliminates storage entirely: inbound goods are transferred directly to outbound vehicles with minimal or no storage time. Requirements:
- Precise inbound scheduling (tight time windows)
- High-frequency, reliable inbound flows
- Matching of inbound loads to outbound routes

Used by Walmart (store replenishment) and Amazon (fresh grocery). Key benefit: eliminates storage cost and reduces cycle time.

### Distribution Center (DC) vs. Fulfilment Center (FC)
- **DC**: bulk-to-case break; serves retail stores with pallets/cases
- **FC**: case-to-unit break; serves individual consumers with single items (e-commerce)

## Third Party Logistics (3PL)

**3PLs** are logistics service providers that manage transportation, warehousing, and related functions on behalf of shippers.

| Classification | Description | Example |
|---|---|---|
| 1PL | Shipper manages own logistics | Factory with own fleet |
| 2PL | Asset-based carrier | Maersk, UPS |
| 3PL | Full logistics services (asset + management) | DHL, Ceva, Toll |
| 4PL | Supply chain integrator managing multiple 3PLs | Accenture Supply Chain |

**3PL trade-offs**:
- *Pros*: Scale economies, expertise, flexibility, capital-light
- *Cons*: Loss of control, information asymmetry, service level risk

## Transportation Economics

### Economies of Scale
Per-unit transport cost falls with load size — driving the logic of consolidation. A fully loaded 40ft container ship costs far less per TEU than a half-loaded one.

### Distance Decay
Cost per km decreases at longer distances — fixed costs (loading, documentation, terminal handling) are spread over more distance. This makes long-haul ocean/rail more cost-efficient per km than short-haul trucking.

### Rate Structures
- **Shipper perspective**: minimize freight cost per unit shipped
- **Carrier perspective**: maximize revenue per vehicle-km (load factor, yield management)
- Freight rate negotiation balances shipper volume commitments against carrier capacity guarantees

## Practical Trade-offs

| Decision | Key Trade-off |
|---|---|
| Mode selection | Speed vs. cost vs. reliability |
| In-house vs. 3PL | Control vs. flexibility vs. cost |
| FTL vs. LTL | Volume vs. flexibility |
| Warehouse location | Proximity to suppliers vs. customers |
| Cross-dock vs. store | Handling cost vs. schedule reliability |

## Related Concepts

- [[wiki/concepts/supply-chain-management|Supply Chain Management]]
- [[wiki/concepts/scor-model|SCOR Model]]
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]]
- [[wiki/concepts/revenue-management|Revenue Management]]
- [[wiki/concepts/ecommerce-models|E-commerce Models]]
- [[vehicle-routing-problem]]
- [[network-flows]]
- [[wiki/sources/courses/ieda-logistics-freight-transportation|IEDA 2410: Logistics and Freight Transportation]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
