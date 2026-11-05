---
title: "IEDA 4180 Service Engineering and Management"
full_name: "IEDA 4180: Service Engineering and Management"
type: source
tags: [courses, ieda, undergraduate, service-operations, management, ieda4180, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA4180/2022F/Syllabus_IEDA4180.pdf"
confidence: high
author: "Xin Wang"
date_published: "2022-08-16"
---

## 概述

IEDA 4180「服務工程與管理」是香港科技大學 IEDA 學系四年級本科生的選修課，由王新教授於 2022 年秋季主講，前置要求為 IEDA 2520、IEDA 2540 及 IEDA 3010，並建議具備 IEDA 3250 及 IEDA 4130 的背景知識。課程以服務業（佔美國 GDP 70%、就業 80%）為研究對象，參考 Johnston、Clark & Shulver 的《Service Operations Management》（Pearson），從理解服務（IHIP 特性、服務利潤鏈）、設計服務（顧客旅程藍圖、接觸點管理、服務失誤恢復）、交付服務（數據驅動顧客管理：邏輯迴歸流失預測、IEDA 3560 分類方法；容量規劃與排隊模型定人；供應商 SLA 設計）到改善服務（根本原因分析、SPC 屬性管制圖、生產力分析與 DEA 標竿比較）的完整週期展開教學。評核以小組作業（40%）與諮詢式專案（60%）為主，學生組成虛擬諮詢團隊，對真實服務企業進行流程診斷與策略建議或深度策略分析，直接應用 IEDA 課程中的排隊理論、容量規劃、線性迴歸、聚類分析等定量工具，是工業工程知識在服務行業最具整合性的應用課程。

## Course Overview

**IEDA 4180 Service Engineering and Management** (Fall 2022, Prof. Xin Wang) provides analytical tools and an integrated viewpoint for managing service firms. The service sector represents the largest and fastest-growing segment of modern economies, encompassing banks, hospitals, call centers, restaurants, transportation providers, and government agencies. Almost every manufacturing firm also has service units.

**Prerequisites**: IEDA 2520, 2540, and IEDA 3010. Knowledge of IEDA 3250 (Stochastic Models) and IEDA 4130 (Simulation) helpful.  
**Text**: Johnston, Clark & Shulver, *Service Operations Management: Improving Service Delivery*, Pearson (recommended, not required).

## Course Structure

The course is organized around five themes that mirror the lifecycle of a service firm:

| Theme | Topics |
|-------|--------|
| Understanding Services | Introduction, service strategy, service concept |
| Designing Service | Customer and supplier understanding |
| Delivering Service | Customer experience, supplier management, resource management |
| Improving Service | Monitoring, problem-finding, quality improvement |
| Implementing Service | Creating and implementing the strategy |

## Key Topics

### Service Concept and Strategy

A **service concept** defines what the service is, how it is delivered, and what value it creates for customers. Unlike products, services are characterized by **IHIP**: Intangibility, Heterogeneity, Inseparability (of production and consumption), and Perishability.

**Service strategy** requires choosing a target segment and designing operations to serve it profitably. The **service-profit chain** (Heskett et al.) links internal service quality → employee satisfaction → productivity → external service value → customer satisfaction → loyalty → profitability.

Positioning choices: cost leadership (McDonald's) vs. differentiation (Four Seasons); self-service vs. full-service; standardized vs. customized.

### Managing Customers with Data Analytics

Module 5 applies predictive analytics to service management — consistent with [[wiki/concepts/linear-regression|Linear Regression]] and [[wiki/concepts/logistic-regression|Logistic Regression]] from IEDA 3560. Applications include:
- **Customer segmentation**: cluster customers by behavior (see [[wiki/concepts/clustering|Clustering]]).
- **Churn prediction**: logistic regression or decision tree to identify at-risk customers.
- **Lifetime value modeling**: forecast customer revenue streams to optimize retention spending.
- **Demand forecasting for staffing**: regression on historical demand patterns to plan labor.

Course materials include: *Lecture 5 - Managing Customers Using Data Analytics*, with supporting Excel files (Distribution Plot, Raw Data).

### Predicting Customer Purchases (Module 6)

Applies classification models to purchasing behavior: logistic regression, decision trees, and ensemble methods to predict whether a customer will buy, upgrade, or churn. Key managerial insight: the cost-benefit of a retention intervention depends on predicted churn probability and customer value.

### Designing the Customer Experience (Module 8)

**Service blueprinting**: maps customer journey (front stage) against service operations (back stage). Identifies **fail points** (where service failures are likely) and **wait points** (where customers queue).

**Moment of truth**: any interaction where the customer forms an impression of service quality. Managing these touchpoints is core to experience design.

**Physical evidence** (servicescape): ambient conditions, spatial layout, and artifacts all shape customer perceptions.

### Designing the Service Process (Module 9)

Process design tools borrowed from operations management:
- **Process flow diagrams**: map activities, decisions, and flows.
- **Capacity analysis**: identify bottlenecks using [[wiki/concepts/capacity-planning|Capacity Planning]] techniques.
- **Queueing models**: size waiting areas and staff levels for target service levels. See [[wiki/concepts/queueing-theory|Queueing Theory]].
- **Poka-yoke** (mistake-proofing): design processes to prevent common errors.

**Service recovery**: when failures occur, effective recovery (apology, compensation, fix) can restore customer loyalty and sometimes increase it above pre-failure levels (the "service recovery paradox").

### Managing Suppliers (Module 7)

Service firms depend on suppliers just as manufacturers do. Key concepts:
- **Supplier relationship management**: transaction vs. partnership orientations.
- **Quality agreements (SLAs)**: measurable service standards for key inputs.
- **Outsourcing vs. in-house**: apply total cost of ownership logic to service inputs.

### Quality Control and Productivity (Modules 13–15)

**Learning from problems**: systematic root-cause analysis using fishbone diagrams, 5-Whys, Pareto charts.

**Quality control**: statistical process control (SPC) adapted for services — attribute charts (p-chart for defect rates), variable charts (X̄ and R charts) for measurable quality dimensions.

**Productivity analysis**: ratio of output to input. For services, output is often intangible (customer satisfaction, cases resolved). **Data Envelopment Analysis (DEA)** benchmarks service units relative to efficient peers — see DEA concept.

### Creating and Implementing Strategy

The capstone theme integrates all modules. Students apply the Connect-Deliver-Improve-Implement framework to analyze a real service firm. Two project types:
- **Type 1 (Application)**: interview operations managers, document processes, apply course frameworks, present recommendations.
- **Type 2 (Strategy Analysis)**: examine corporate strategy of a service firm, assess effectiveness, identify opportunities.

## Related Concepts

- [[wiki/concepts/queueing-theory|Queueing Theory]] — waiting time and capacity models for service systems
- [[wiki/concepts/capacity-planning|Capacity Planning]] — bottleneck analysis for service processes
- [[wiki/concepts/revenue-management|Revenue Management]] — pricing of perishable service capacity
- [[wiki/concepts/linear-regression|Linear Regression]] — demand forecasting for staffing
- [[wiki/concepts/clustering|Clustering]] — customer segmentation

## Source Materials

- raw/courses/IEDA/IEDA4180/2022F/Syllabus_IEDA4180.pdf
- raw/courses/IEDA/IEDA4180/2022F/Lecture 1 - Introduction to Service.pdf
- raw/courses/IEDA/IEDA4180/2022F/Lecture 5 - Managing Customers Using Data Analytics.pdf
- raw/courses/IEDA/IEDA4180/2022F/Lecture 14 - Productivity Analysis and Data Envelopment Analysis.pdf
