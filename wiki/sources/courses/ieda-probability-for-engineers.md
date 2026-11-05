---
title: "IEDA 2520: Probability for Engineers"
full_name: "IEDA 2520 Probability for Engineers"
type: source
tags: [courses, ieda, undergraduate, probability, statistics, ieda2520, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA2520"
confidence: high
author: "Zhang, J."
date_published: "2020-09-06"
---

## 概述

IEDA 2520「工程概率論」是香港科技大學 IEDA 學系二年級本科生的必修課，前置要求為高考純數或應用數學（或 MATH 1013/1014），由張繼恒教授於 2020 年秋季以 Zoom 形式授課。課程以 Sheldon M. Ross 所著《A First Course in Probability》（Pearson，第 8 版）為參考教材，並提供完整講義取代。課程以 Python（`numpy`、`matplotlib`、`pandas`）貫穿全程，涵蓋描述性統計、樣本空間與事件代數、條件概率與 Bayes 定理、離散隨機變數（Bernoulli、Binomial、Geometric、Poisson 分佈）、連續隨機變數（Uniform、Exponential、Normal 分佈）、聯合分佈與協方差，以及大數定律（LLN）和中心極限定理（CLT）的蒙地卡羅模擬驗證。學生透過 Python Jupyter Notebook 完成作業，將理論與數值實作結合，為後續的 IEDA 2540（工程統計）、IEDA 3250（隨機模型）及所有隨機建模課程提供不可缺少的概率基礎。

## Course Overview

**IEDA 2520: Probability for Engineers** is taught by Prof. Jiheng Zhang (Fall 2020, via Zoom). It is a systematic introduction to probability theory with Python-based computation throughout, making abstract concepts concrete through simulation and visualization. The textbook is Sheldon M. Ross, *A First Course in Probability*, Pearson, 8th Edition (optional — comprehensive class notes are provided on Canvas).

- **Prerequisite**: AL Pure Mathematics or AL Applied Mathematics (MATH 1013 + 1014)

## Course Outline

### Module 1: Descriptive Statistics
- Frequency tables, histograms, stem-and-leaf plots
- Sample mean, variance, median, percentile
- Chebyshev's inequality for data (empirical bound on spread)
- Python tools: `numpy`, `matplotlib`, `pandas` for data summarization

### Module 2: Elements of Probability
- **Sample space** and events; set operations (union, intersection, complement)
- **Axioms of probability**: non-negativity, normalization, additivity
- **Conditional probability**: P(A|B) = P(A∩B) / P(B)
- **Bayes' Rule**: P(A|B) = P(B|A)P(A) / P(B); posterior updating
- **Independence**: P(A∩B) = P(A)·P(B)
- Python: `random` module, simulation-based probability estimation

### Module 3: Random Variables
- **Discrete random variables**: PMF, CDF, expectation, variance
  - Key distributions: Bernoulli, Binomial, Geometric, Poisson
- **Continuous random variables**: PDF, CDF, expectation, variance
  - Key distributions: Uniform, Exponential, Normal (Gaussian)
- **Joint distributions**: joint PMF/PDF, marginal distributions, covariance, correlation
- **Functions of random variables**: change-of-variables, sums of random variables

### Module 4: Limiting Theorems
- **Law of Large Numbers (LLN)**: sample mean converges to population mean as n→∞
- **Central Limit Theorem (CLT)**: sum of i.i.d. random variables converges in distribution to Normal, regardless of original distribution
- Python: demonstrating CLT convergence via Monte Carlo simulation

## Python Integration

A defining feature of IEDA 2520 is computational reinforcement of theory. Students:
- Simulate random experiments (coin flips, dice rolls, Poisson arrivals)
- Visualize probability distributions and CDFs
- Empirically verify LLN and CLT convergence
- Use Python notebooks (`.ipynb`) for homework submission

This approach makes IEDA 2520 a bridge between mathematics and data science — students leave with both theoretical understanding and practical coding skills applicable to later courses in [[wiki/concepts/linear-regression|Linear Regression]], [[wiki/concepts/clustering|Clustering]], and [[wiki/concepts/arma-models|ARMA Models]].

## Relationship to IEDA 2540

IEDA 2520 covers probability foundations; [[wiki/sources/courses/ieda-engineering-statistics|IEDA 2540]] extends this into statistical inference (estimation, hypothesis testing, regression). Together they form the complete probability-statistics sequence required for all quantitative IEDA courses. Historically, these were offered as a single course (IELM 2510).

## Key Textbook: Ross (2010)

Sheldon Ross's *A First Course in Probability* is the standard reference for engineering probability. It is notable for:
- Rigorous but accessible treatment of discrete and continuous probability
- Extensive worked examples from engineering and science contexts
- Coverage through joint distributions, moment generating functions, and limit theorems

See [[probability-theory]] for the underlying mathematical theory.

## Related Concepts

- [[probability-theory]]
- [[wiki/concepts/linear-regression|Linear Regression]]
- [[wiki/concepts/arma-models|ARMA Models]]
- [[wiki/concepts/clustering|Clustering]]
- [[wiki/concepts/queueing-theory|Queueing Theory]]
- [[wiki/concepts/garch|GARCH]]
- [[wiki/sources/courses/ieda-engineering-statistics|IEDA 2540: Engineering Statistics]]

## Source Materials

- raw/courses/IEDA/IEDA2520/Syllabus.pdf
- raw/courses/IEDA/IEDA2520/0.Intro/
- raw/courses/IEDA/IEDA2520/1.Descriptive Statistics/
- raw/courses/IEDA/IEDA2520/2.Elements of Probability/
- raw/courses/IEDA/IEDA2520/3.Random Variables/
- raw/courses/IEDA/IEDA2520/4.Limiting Theorems/
