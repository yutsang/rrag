---
title: "Database Systems"
full_name: "Database Management Systems (DBMS)"
type: concept
tags: [computer-science, databases, data-management, sql]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/comp-database-systems"
confidence: high
---

## 概述

資料庫管理系統（DBMS）提供結構化數據的持久存儲、高效查詢與並發訪問管理，其核心設計由 E.F. Codd 於1970年提出的關聯模型奠基：關係代數（選擇 σ、投影 π、連結 ⋈）構成 SQL 的語義基礎，而正規化理論（1NF 至 BCNF）透過函數依賴分析消除冗餘與更新異常。查詢優化器是 DBMS 的智能核心，它將 SQL 解析為關係代數邏輯計劃，再透過動態規劃從指數級搜尋空間中選出最低 I/O 代價的物理計劃（選擇表掃描、索引掃描、排序合併連結或雜湊連結）。ACID 事務語義（原子性、一致性、隔離性、持久性）通過兩段鎖定協議（2PL）保證可串行化，Write-Ahead Logging（WAL）提供崩潰恢復能力，而不同隔離級別在並發性能與異常保護之間提供可調節的權衡。NoSQL 系統（文件型 MongoDB、鍵值型 Redis、列族型 Cassandra、圖型 Neo4j）各自針對關聯模型的特定弱點（靈活 Schema、超高寫入吞吐、圖遍歷）提供解決方案，而 CAP 定理從理論上界定了分佈式系統在一致性、可用性和分區容錯性三者間的根本性取捨。在運籌學與機器學習的交叉點上，SQL 視窗函數（LAG、LEAD、ROW_NUMBER）是時序特徵工程的主力工具，OLAP 星型/雪花型 Schema 支撐分析型聚合查詢，而[[erp|ERP]]系統的所有交易數據均存儲在關聯資料庫中，是供應鏈優化和需求預測的原始數據來源。

## What It Is

A **Database Management System (DBMS)** is software that manages organized collections of data, providing:
- **Data persistence**: data survives beyond process lifetimes
- **Query language**: express what data you want (SQL) without specifying how to retrieve it
- **Concurrency control**: multiple users can safely access data simultaneously
- **Recovery**: data survives system crashes (ACID guarantees)

## Relational Model

Proposed by E.F. Codd (1970). Data organized in **relations** (tables):
- **Relation** = named set of **tuples** (rows), each with identical **attributes** (columns)
- **Schema** = name + attribute names/types; **instance** = current set of tuples
- **Primary key**: attribute(s) uniquely identifying each tuple
- **Foreign key**: attribute(s) referencing primary key of another relation — enforces referential integrity

**Relational algebra** defines query operations:
- $\sigma_c(R)$: **Select** — filter rows satisfying condition $c$
- $\pi_A(R)$: **Project** — keep only attributes $A$
- $R_1 \bowtie_{c} R_2$: **Join** — combine tuples where condition $c$ holds
- $R_1 \cup R_2$, $R_1 - R_2$: **Union**, **Difference**
- $R_1 \times R_2$: **Cartesian product**

## SQL

**SQL (Structured Query Language)** is the universal language for relational databases:

```sql
SELECT  e.name, d.dept_name, e.salary
FROM    employees e
JOIN    departments d ON e.dept_id = d.id
WHERE   e.salary > 50000
GROUP BY d.dept_name
HAVING  COUNT(*) > 5
ORDER BY e.salary DESC
LIMIT   10;
```

**Key clauses**: SELECT (columns), FROM (tables), WHERE (row filter), JOIN (combine tables), GROUP BY (aggregate), HAVING (filter on aggregates), ORDER BY (sort), LIMIT (top-k).

**Aggregation**: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`. Window functions: `ROW_NUMBER()`, `RANK()`, `LAG()` — essential for time series analytics.

**Subqueries**: nested SELECT in WHERE or FROM. CTEs (`WITH` clause): named subqueries for readability and reuse.

## Normalization

**Functional dependency (FD)**: $A \to B$ means knowing $A$ determines $B$.

**Normal forms** eliminate redundancy and update anomalies:

| Form | Requirement |
|---|---|
| 1NF | All attributes are atomic (no repeating groups) |
| 2NF | 1NF + no partial dependency on composite key |
| 3NF | 2NF + no transitive dependency (non-key → non-key) |
| BCNF | Every non-trivial FD's LHS is a superkey |

**Decomposition**: split tables to achieve higher normal form. Must be lossless (can reconstruct original) and dependency-preserving.

## Query Processing and Optimization

**Query execution pipeline**: parse SQL → logical plan (relational algebra) → physical plan (specific algorithms) → execute.

**Physical operators**:
- **Table scan**: read entire table $O(N)$
- **Index scan**: follow B+ tree to qualifying rows $O(\log N + k)$
- **Sort-merge join**: sort both inputs, merge in $O(N \log N)$
- **Hash join**: build hash table on smaller relation, probe with larger $O(N)$ average
- **Nested loop join**: $O(N \cdot M)$ — only good when inner relation is small or indexed

**Cost-based optimizer**: estimates row counts and I/O costs for each plan; uses statistics (histograms, NDV — number of distinct values). Chooses minimum-cost plan from exponential search space via dynamic programming.

**Indexes**: B+ tree index on column(s) enables fast lookup and range queries. Hash index for equality only. Trade-off: indexes speed up reads, slow down writes (must maintain index).

## Transactions and ACID

A **transaction** is a sequence of operations executed atomically.

**ACID properties**:
- **Atomicity**: all-or-nothing; on failure, rollback all changes
- **Consistency**: transaction leaves database in a valid state
- **Isolation**: concurrent transactions behave as if serialized
- **Durability**: committed changes survive crashes (write-ahead log)

**Concurrency control** — prevent anomalies when multiple transactions run simultaneously:
- **Two-phase locking (2PL)**: acquire all locks before releasing any — guarantees serializability
- **Isolation levels**: Read Uncommitted < Read Committed < Repeatable Read < Serializable. Higher levels prevent more anomalies but reduce concurrency.
- **Deadlock**: cycle in lock wait graph; detected and broken by aborting one transaction.

**Write-ahead logging (WAL)**: log changes before applying them. On crash recovery: REDO committed transactions, UNDO incomplete ones.

## NoSQL

For workloads that don't fit relational model:

| Type | Examples | Use case |
|---|---|---|
| **Document** | MongoDB, CouchDB | Semi-structured JSON data, flexible schema |
| **Key-Value** | Redis, DynamoDB | Cache, session store, simple lookups |
| **Column-family** | Cassandra, HBase | Wide rows, time series, high write throughput |
| **Graph** | Neo4j, TigerGraph | Network analysis, knowledge graphs |

**CAP theorem**: distributed systems can guarantee at most 2 of: Consistency, Availability, Partition tolerance.

## OR/Analytics Relevance

- **Feature engineering**: SQL is the primary tool for extracting ML training features from transactional databases
- **OLAP**: analytical queries (GROUP BY, window functions) over large historical datasets; star/snowflake schemas in data warehouses
- **[[erp]] systems** (SAP, Oracle): built on relational databases; all operational data lives here
- **Real-time OR**: databases store current inventory, customer orders, vehicle positions for online decision-making

## Related Concepts

- [[erp]]
- [[crm]]
- [[web-architecture]]
- [[algorithms-and-data-structures]]
- [[machine-learning-advanced]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
- [[wiki/mocs/cs-data-science|CS and Data Science MOC]]
