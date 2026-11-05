---
title: "Database Management Systems"
full_name: "COMP3311 Database Management Systems"
type: source
tags: [courses, comp, undergraduate, databases, comp3311, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP3311"
confidence: medium
---

## 概述

COMP3311 資料庫管理系統為計算機科學三年級學生系統介紹資料庫系統的設計、實作與查詢優化，先修要求為 COMP2012 物件導向程式設計及 COMP2711 離散數學。課程以 Ramakrishnan & Gehrke《資料庫管理系統》或 Silberschatz《資料庫系統概念》為標準教材，涵蓋實體-關係（ER）模型與關係模型的轉換、函數相依性與正規化理論（1NF 至 BCNF）、關係代數與 SQL 進階查詢（窗口函數、遞歸查詢、CTE）、B+ 樹索引結構與查詢優化器的代價估算，以及 ACID 事務管理（兩階段鎖定、WAL 日誌與崩潰恢復）。學生完成課程後能夠設計正規化的關聯式資料庫模式、撰寫複雜 SQL 查詢並分析執行計劃、理解 NoSQL 資料庫（MongoDB、Redis、Cassandra）的使用場景，以及建構基本的 OLAP 星型模式數據倉庫。這些技能是數據分析流水線的基礎語言，亦直接支撐 ERP 系統、供應鏈資料管理及運籌學中大規模優化問題的資料前處理工作。

## Course Overview

COMP3311 covers the full lifecycle of database systems: conceptual design, logical modeling, physical storage, query processing, and transaction management. It bridges the gap between data collection and analytical use.

## Key Topics

### Data Modeling
- **Entity-Relationship (ER) model**: entities, relationships, cardinality (1:1, 1:N, M:N), weak entities, ISA hierarchies
- **ER to relational mapping**: converting diagrams to table schemas
- **Normalization**: functional dependencies, 1NF/2NF/3NF/BCNF, decomposition, lossless joins

### Relational Model and SQL
- **Relational algebra**: select (σ), project (π), join (⋈), union, difference, rename
- **SQL**: SELECT/FROM/WHERE, aggregation (GROUP BY, HAVING), subqueries, views, triggers
- **Advanced SQL**: window functions, CTEs, recursive queries (for hierarchical data)
- **Constraints**: primary/foreign keys, CHECK constraints, referential integrity

### Query Processing and Optimization
- **Query execution**: scan, sort-merge join, hash join, nested-loop join — when to use each
- **Index structures**: B+ trees (balanced, supports range queries), hash indexes
- **Query optimizer**: cost estimation, statistics (histograms), plan enumeration

### Transaction Management
- **ACID properties**: Atomicity, Consistency, Isolation, Durability
- **Concurrency control**: two-phase locking (2PL), deadlock detection/prevention, serializable schedules
- **Recovery**: write-ahead logging (WAL), REDO/UNDO, checkpointing

### Modern Extensions
- **NoSQL**: document (MongoDB), key-value (Redis), column-family (Cassandra), graph (Neo4j) — when to choose over RDBMS
- **Data warehousing**: OLAP vs. OLTP, star/snowflake schema, ETL pipelines

## OR/Analytics Relevance

- SQL is the lingua franca for pulling data in any analytics pipeline
- Query optimization uses cost-based reasoning analogous to OR optimization
- OLAP star schemas are how [[erp]] systems (SAP HANA) organize analytical queries
- Understanding indexes and join algorithms is critical for working with large OR datasets

## Related Concepts

- [[database-systems]]
- [[erp]]
- [[crm]]
- [[web-architecture]]
