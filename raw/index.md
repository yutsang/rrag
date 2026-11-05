---
title: "Raw Asset Index"
full_name: "原始資料索引"
type: overview
tags: [index, raw]
created: "2026-04-07"
updated: "2026-04-14"
source: ""
confidence: high
---

## 概述

此索引追蹤 raw/ 目錄中所有原始資料檔案，並映射到對應的 wiki 來源頁面。每次消化完畢後，原始檔案從子目錄移除，但目錄結構保留供下次使用。

## Inbox Folders

| Folder | Drop files here when… |
|---|---|
| `raw/docs/` | Official documentation, guides, READMEs |
| `raw/articles/` | Web-clipped articles, blog posts |
| `raw/courses/` | University course materials (lectures, slides, readings, HW) |
| `raw/papers/` | Academic papers (PDFs): journal articles, conference papers, preprints |
| `raw/assets/` | Images referenced by source pages |

## Workflow

1. Drop new files into the appropriate subfolder above.
2. Run `/ingest` (single source) or `/batch-ingest` (3+ sources) to digest into `wiki/`.
3. After digestion is confirmed, delete the source files — the folder structure stays.

## Asset Mapping

### raw/courses/ — Digested 2026-04-14, Deleted 2026-04-14

All undergraduate course materials below have been digested into `wiki/sources/courses/` and source files deleted. Folder structure preserved for future drops.

| Department | Courses | Wiki source page(s) |
|---|---|---|
| IEDA | IEDA1010/1020, 2010, 2200, 2410, 2520, 2540 | ieda1010-1020-professional-development, ieda2010-industrial-engineering-survey, ieda2200-engineering-management, ieda2410-logistics-freight-transportation, ieda2520-probability-for-engineers, ieda2540-engineering-statistics |
| IEDA | IEDA3010, 3230, 3250, 3270, 3300, 3302, 3330, 3410, 3460, 3560, 3901 | ieda3010-operations-research-i, ieda3230-engineering-economy, ieda3250-stochastic-models, ieda3270-quality-engineering, ieda3300-industrial-data-systems, ieda3302-ecommerce-technology, ieda3330-financial-derivatives, ieda3410-routing-fleet-management, ieda3460-demand-supply-analytics, ieda3560-data-analytics, ieda3901-transportation-systems |
| IEDA | IEDA4100, 4130, 4180, 4200, 4331, 4410, 4420, 4510, 4960 | ieda4100-supply-management, ieda4130-system-simulation, ieda4180-service-engineering, ieda4200-human-machine-systems, ieda4331-financial-derivatives, ieda4410-data-driven-scm, ieda4420-demand-management, ieda4510-financial-analytics, ieda4960-fyp |
| MATH | MATH1003/1012/1013/1014/1023/1024 | hkust-calculus-sequence |
| MATH | MATH2011/2023, 2111/2131, 2343, 2351/3343, 2411/2511 | hkust-multivariable-calculus, hkust-linear-algebra, hkust-discrete-math, hkust-odes-pdes, hkust-probability-statistics |
| MATH | MATH3033/4033, 4424/4514, 4432 | hkust-advanced-analysis, hkust-financial-mathematics, hkust-stochastic-modeling |
| COMP | COMP1001/1021/2011/2012/2611/2711 | hkust-comp-intro-courses |
| COMP | COMP3211, 3311, 3511, 3632, 3711, 4211, 4321, 4331, 4621 | comp3211-fundamentals-ai, comp3311-database-systems, comp3511-operating-systems, comp3632-cybersecurity, comp3711-algorithms, comp4211-machine-learning, comp4321-search-engines, comp4331-data-mining, comp4621-computer-networks |
| FINA | FINA1203, 1303, 2203, 2303, 3103 | fina1203-personal-finance, fina1303-financial-markets, fina2203-business-finance, fina2303-financial-management, fina3103-investments |
| ECON | ECON2103, 2113, 2123 | econ2103-introductory-economics, econ2113-microeconomics, econ2123-macroeconomics |
| ISOM | ISOM1500, 1700, 2010, 2400, 2500, 2700, 3000E, 3310 | isom1500-quantitative-analysis, isom1700-introduction-to-business, isom2010-computers-business-applications, isom2400-ecommerce, isom2500-business-statistics, isom2700-operations-management, isom3000e-digital-business-strategy, isom3310-ebusiness-web-analytics |
| ACCT | ACCT2010, 2200, 3610 | acct2010-principles-of-accounting, acct2200-managerial-accounting, acct3610-business-law |
| MGMT | MGMT1110, 2110 | mgmt1110-introduction-to-management, mgmt2110-organizational-behavior |
| PHYS | PHYS1001/1002/1003, 1112/1114/1312 | phys-intro-courses, phys-advanced-courses |
