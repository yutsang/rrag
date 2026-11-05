---
title: "Industrial Data Systems"
full_name: "IEDA3300 Industrial Data Systems"
type: source
tags: [courses, ieda, undergraduate, databases, data-management, ieda3300, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3300"
confidence: medium
---

## 概述

IEDA 3300「工業數據系統」是香港科技大學 IEDA 學系三年級本科生的必修課，旨在為工業工程師提供管理製造、物流及供應鏈數據的核心技術能力。課程涵蓋關聯式數據庫設計的完整流程：實體關係（ER）圖建模、ER 轉關聯模式、函數依賴與正規化（1NF/2NF/3NF/BCNF）；SQL 查詢語言（SELECT/JOIN/GROUP BY/子查詢/視圖/聚合函數）；以及索引結構（B+ 樹）、查詢優化與 ACID 事務控制。課程後半段延伸至現代數據系統，包括 OLAP vs OLTP、星形模式數據倉庫（ETL）、NoSQL 數據庫（文件型 MongoDB、鍵值型 Redis）及工業 IoT 時序數據庫（InfluxDB）。應用場景涵蓋製造業（工單追蹤、BOM 管理）、供應鏈（訂單與庫存管理）及 ERP 系統整合。本課是 IEDA 3560（數據分析）、IEDA 4410（數據驅動供應鏈管理）等下游數據密集型課程的技術前置，亦為學生參與 OR 研究中數據工程環節提供必要的系統性訓練。

## Course Overview

IEDA3300 brings database management into the IEDA curriculum — essential because modern OR implementations require storing and querying large operational datasets (orders, inventory, sensor data, customer transactions).

## Key Topics

### Data Modeling
- **Entity-Relationship (ER) diagrams**: entities, attributes, relationships, cardinality
- ER-to-relational mapping: one-to-many, many-to-many (junction tables)
- Weak entities, ISA (inheritance) hierarchies

### Relational Model and SQL
- Relations (tables), tuples (rows), attributes (columns)
- Primary keys, foreign keys, referential integrity
- Relational algebra: select, project, join, union, difference
- SQL: SELECT/FROM/WHERE/JOIN/GROUP BY/HAVING, subqueries, views
- Aggregate functions: COUNT, SUM, AVG, MIN, MAX
- Transaction control: COMMIT, ROLLBACK

### Normalization
- Functional dependencies
- First, second, third normal forms (1NF/2NF/3NF); BCNF
- Decomposition: lossless joins and dependency preservation

### Database Implementation
- Index structures: B+ trees for range queries, hash indexes for equality
- Query execution and optimization: cost estimation, join algorithms
- ACID properties and concurrency control basics

### Modern Data Systems
- Data warehousing: OLAP vs. OLTP, star schema, ETL
- NoSQL overview: document (MongoDB), key-value (Redis), column-family
- Industrial IoT data: time-series databases (InfluxDB), sensor data management

### Applications
- Manufacturing: tracking work-in-progress, bill of materials (BOM)
- Supply chain: order management, inventory tracking, supplier data
- Integration with ERP systems (see [[erp]])

## Related Concepts

- [[database-systems]]
- [[erp]]
- [[crm]]
- [[supply-chain-management]]
- [[web-architecture]]
