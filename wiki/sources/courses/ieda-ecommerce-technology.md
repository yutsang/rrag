---
title: "E-Commerce Technology and Applications"
full_name: "IEDA3302 E-Commerce Technology and Applications"
type: source
tags: [courses, ieda, undergraduate, ecommerce, web-technology, supply-chain, ieda3302, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3302"
confidence: medium
---

## 概述

IEDA 3302「電子商務技術與應用」是香港科技大學 IEDA 學系三年級本科生的選修課，以工業工程視角切入電商，有別於商學院側重商業策略的 ISOM 2400 及數據分析的 ISOM 3310。課程涵蓋電商系統的技術架構（三層架構、微服務、REST API、橫向擴展與快取）、各類商業模式（B2C、B2B EDI、市場平台、C2C 信任機制）、數字供應鏈整合（EDI、XML/JSON、ERP-WMS-電商平台 API 對接、即時庫存同步）、數字物流與履約（WMS 揀貨優化、最後一哩路線最佳化、越庫作業、逆向物流）、支付安全（TLS 流程、PCI-DSS、代幣化、詐欺偵測機器學習）及電商數據分析（需求預測、轉化漏斗分析、動態定價、RFM 客戶細分）。課程強調 IEDA 的運營效率視角，分析如何藉數字化手段消除供應鏈中的瓶頸與庫存浪費，是 IEDA 3300（工業數據系統）知識在電商場景的直接延伸，並與 IEDA 3460（需求供應分析）及 IEDA 4410（數據驅動供應鏈管理）形成緊密的課程銜接。

## Course Overview

IEDA3302 is the industrial engineering department's take on e-commerce, distinct from ISOM2400 (business focus) and ISOM3310 (analytics focus). The IEDA perspective emphasizes system integration, supply chain digitization, and operational efficiency.

## Key Topics

### E-Commerce Architectures
- Web application architecture: frontend (HTML/CSS/JS), backend (APIs, databases), CDN — see [[web-architecture]]
- Three-tier architecture: presentation, application, data tiers
- Microservices vs. monolithic architectures; API gateways; REST and GraphQL APIs
- Scalability patterns: horizontal scaling; load balancing; caching layers (Redis, CDN)

### E-Commerce Business Models and Operations
- B2C platforms: product catalog management; shopping cart; checkout flow; payment gateway
- B2B e-commerce: EDI (Electronic Data Interchange); XML/JSON-based data exchange; procurement portals
- Marketplace models: seller onboarding; commission structures; fulfillment options (FBM, FBA)
- C2C platforms: trust mechanisms; reputation systems; escrow payments
- See [[ecommerce-models]]

### Digital Supply Chain Integration
- **EDI** (Electronic Data Interchange): ANSI X12 / EDIFACT standards; purchase orders, invoices, ASN
- **XML/JSON** data formats for inter-system communication
- **API integration**: connecting ERP, WMS, and e-commerce platforms — see [[erp]]
- Real-time inventory synchronization: preventing overselling; safety stock buffers
- Order management systems (OMS): multi-channel order routing; split shipments

### Digital Logistics and Fulfillment
- Warehouse management systems (WMS): pick-and-pack optimization; barcode/RFID
- Last-mile delivery: carrier selection; route optimization — see [[vehicle-routing-problem]]
- Cross-docking; drop-shipping; 3PL (third-party logistics) integration
- Returns management (reverse logistics): restocking; quality inspection; refurbishment
- Real-time tracking: GPS, RFID, IoT sensors; customer visibility portals

### Payment Systems and Security
- Payment flow: customer → payment gateway → acquirer → card network → issuer bank → settlement
- Digital wallets, BNPL (Buy Now Pay Later); cryptocurrency payments intro
- Fraud detection: rule-based systems; ML-based scoring — see [[machine-learning-advanced]]
- PCI-DSS compliance; tokenization; encryption — see [[cryptography]]

### Analytics for E-Commerce Operations
- Demand forecasting for inventory planning: time series + promotional uplift
- Conversion funnel analysis; cart abandonment; exit intent
- Dynamic pricing: market-based; competitor price monitoring — see [[revenue-management]]
- Customer segmentation: RFM (Recency, Frequency, Monetary) analysis — see [[clustering]]

## Related Concepts

- [[ecommerce-models]]
- [[web-architecture]]
- [[erp]]
- [[supply-chain-management]]
- [[vehicle-routing-problem]]
- [[revenue-management]]

## Source Materials

- IEDA3302 Course Materials
