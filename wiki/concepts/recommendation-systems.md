---
title: "Recommendation Systems"
full_name: "Recommendation Systems (Collaborative and Content-Based Filtering)"
type: concept
tags: [machine-learning, recommendation-systems, collaborative-filtering, content-filtering, netflix]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/applied-statistics"
confidence: high
---

## 概述

推薦系統是透過分析用戶行為或物品特徵來預測用戶偏好的機器學習應用，廣泛應用於電子商務、串流媒體和社交平台，Netflix 估計其推薦系統每年帶來逾10億美元的訂閱保留價值。三大主流方法為協同過濾（基於用戶或物品的相似性，核心挑戰是冷啟動問題與數據稀疏性）、基於內容的過濾（基於物品特徵向量匹配，可解釋但易陷入過度專化）以及兩者兼顧的混合方法。EEMT5500 課程以 Netflix Prize 競賽（2006-2009，100萬美元獎金，4.8萬用戶 × 1.78萬部電影的稀疏評分矩陣）為案例，展示矩陣分解（SVD）如何成為協同過濾的最佳演算法，而最終冠軍 BellKor's Pragmatic Chaos 整合逾100個模型的集成方案，說明單一算法難以突破性能上限。MovieLens 案例進一步示範如何透過18維類型向量的聚類將電影分組，以「同群推薦」實現輕量級內容過濾。現代推薦系統已演進至深度學習（神經協同過濾、自動編碼器）、圖神經網絡（用戶-物品交互圖）和強化學習（最優化長期參與度而非單次點擊率）等方向；在運籌學中，推薦系統與收益管理結合，用於動態個性化定價和庫存導向的商品展示排序。

## Core Mechanism

A **recommendation system** (or recommender system) predicts a user's preference for an item they have not yet interacted with, based on available data about users, items, and past interactions. These systems are among the most commercially valuable machine learning applications, driving engagement and revenue for companies like Netflix, Amazon, Spotify, and YouTube.

### The Three Approaches

| Approach | Data Used | Method | Strengths | Weaknesses |
|----------|-----------|--------|-----------|------------|
| **Collaborative Filtering** | User-item interaction matrix | Find similar users or items | No item features needed; captures implicit patterns | Cold start problem; data sparsity |
| **Content-Based Filtering** | Item attributes/features | Match item features to user preferences | No cold start for items; transparent | Requires feature engineering; limited discovery |
| **Hybrid** | Both interaction and feature data | Combine CF and content methods | Best overall performance | More complex to implement |

## Collaborative Filtering

**Collaborative filtering (CF)** operates on the principle that users who agreed in the past will agree in the future. It uses only the user-item interaction matrix (ratings, purchases, clicks) without any information about item attributes.

### User-Based CF

1. For a target user, find the most similar users (neighbors) based on their rating patterns
2. Predict the target user's rating for an unseen item as the weighted average of neighbors' ratings for that item
3. Recommend items with the highest predicted ratings

**Similarity metrics**: Pearson correlation, cosine similarity, or Euclidean distance between user rating vectors.

### Item-Based CF

1. For a target item, find the most similar items based on their rating patterns across users
2. Predict a user's rating for the target item based on their ratings of similar items
3. More stable than user-based CF because item similarity changes less frequently than user similarity

### Challenges

- **Cold start problem**: New users have no interaction history; new items have no ratings. CF cannot make recommendations in these cases.
- **Data sparsity**: In typical systems, users rate only a tiny fraction of available items. The user-item matrix is >99% empty.
- **Scalability**: Computing pairwise similarity for millions of users and items is computationally expensive.
- **Popularity bias**: CF tends to recommend popular items, reducing diversity and serendipity.

## Content-Based Filtering

**Content-based filtering** recommends items similar to those a user has previously liked, based on item features (genre, director, keywords, description, etc.).

### How It Works

1. Build a **feature vector** for each item (e.g., genre tags for movies)
2. Build a **user profile** as a weighted combination of feature vectors of items the user has liked
3. Compute similarity between the user profile and candidate items
4. Recommend items with highest similarity to the user profile

In the MovieLens case study, each movie is represented as an 18-dimensional binary genre vector (Action, Adventure, Comedy, Drama, etc.). [[clustering|Clustering]] groups movies with similar genre profiles, and movies in the same cluster as a user's favorites can be recommended.

### Advantages

- No cold start for items (features are available immediately)
- Transparent and explainable ("recommended because you liked similar action movies")
- No dependence on other users' data

### Limitations

- Requires meaningful item features (manual curation or NLP extraction)
- Cannot capture quality or user-specific taste beyond the defined features
- Tends toward over-specialization (recommending only items very similar to past preferences)

## Hybrid Systems

**Hybrid recommender systems** combine collaborative and content-based methods to leverage the strengths of both:

- **Weighted**: Combine scores from CF and content-based models with tuned weights
- **Switching**: Use content-based when user history is sparse, CF when sufficient data exists
- **Feature augmentation**: Use content features as input to CF models
- **Cascade**: Use one method to produce a candidate set, another to re-rank

Most production systems use hybrid approaches. The Netflix Prize winner (BellKor's Pragmatic Chaos) used an ensemble of over 100 models combining different CF and content-based techniques.

## Case Study: The Netflix Prize (2006-2009)

The **Netflix Prize** is one of the most famous machine learning competitions in history.

### Competition Details

- **Prize**: $1,000,000 for the first team to improve Netflix's recommendation algorithm (Cinematch) by 10% on RMSE. Progress prizes of $50,000/year were awarded for the best submission, provided it improved by >1% over the prior year.
- **Dataset**: ~100 million training ratings and ~3 million test ratings across 480,000 users and 17,770 movies.
- **Timeline**: Launched October 2, 2006. By October 8 (6 days later), one team had already beaten Cinematch. By June 2007, over 20,000 teams from 150 countries had registered.
- **Progress prizes**:
  - 2007: **BellKor** (AT&T Research) at 8.43% improvement
  - 2008: **BellKor + BigChaos** joint submission (last progress prize because the next 1% would have hit the grand prize threshold)
- **Grand prize**: On June 26, 2009, **BellKor's Pragmatic Chaos** (BellKor + Pragmatic Theory + BigChaos) submitted a 10.05% improvement, triggering the 30-day "last call" window.

### Key Insights from the Competition

1. **Ensemble methods win**: The winning solution combined over 100 individual models. No single algorithm achieved the 10% improvement.

2. **Matrix factorization dominates**: [[pca|SVD (Singular Value Decomposition)]] and related matrix factorization techniques proved most effective for collaborative filtering at scale. The user-item matrix $R \in \mathbb{R}^{m \times n}$ is approximated as $R \approx U \Sigma V^\top$ where $U$ holds user latent factors and $V$ holds item latent factors.

3. **Temporal dynamics matter**: User preferences drift over time; models accounting for rating inflation and taste drift performed better.

4. **The last 1% is hardest**: Many teams achieved 8-9% improvement within months, but the final percentage point took years of effort.

### Impact on the Industry

The Netflix Prize catalyzed enormous investment in recommendation systems across the tech industry. Netflix estimated that its recommendation system was worth **$1 billion per year** in retained subscriptions — users who found content they enjoyed were less likely to cancel. Netflix in 2009 had 40+ million subscribers and $3.6 billion in revenue; today the number is an order of magnitude larger and the recommendation system shapes what nearly every subscriber watches.

## MovieLens Clustering Application (Lecture 7)

The course connects [[clustering|Clustering]] to recommendation systems using the MovieLens dataset:

1. **Represent movies as genre vectors**: 18-dimensional binary vectors
2. **Cluster movies** using K-means (K=10) or hierarchical clustering
3. **Find a user's favorite movie** (e.g., *Avengers: Age of Ultron*, assigned to cluster 4)
4. **Recommend other movies from the same cluster**: *Batman Forever*, *Star Wars: Episode IV*, *Mortal Kombat*

This demonstrates a simple but effective content-based approach where clustering serves as a pre-computation step for finding similar items.

## Modern Recommendation Architectures

While EEMT5500 covers foundational approaches, modern systems have evolved significantly:

- **Deep learning**: Neural collaborative filtering, autoencoders for matrix completion
- **Reinforcement learning**: Optimizing for long-term engagement rather than single-click prediction
- **Graph neural networks**: Modeling user-item interactions as graph structures
- **Transformer-based**: Sequential recommendation using attention mechanisms
- **Multi-objective**: Balancing relevance, diversity, novelty, and fairness

The foundational concepts of collaborative and content-based filtering remain central to all these advanced approaches.

## Toy Example from the Lecture

| User | Avengers | Apollo 13 | Top Gun | Terminator |
|------|----------|-----------|---------|------------|
| Amy  | 5        | —         | 4       | 5          |
| Bob  | —        | 3         | 2       | —          |
| Carl | —        | 4         | 5       | 4          |
| Dan  | 4        | 5         | 2       | —          |

**Collaborative filtering** suggests *Avengers: Age of Ultron* to Carl because Amy rated it highly and Amy and Carl show similar preferences on *Top Gun* and *Terminator*. **Content filtering** instead notes that Amy liked *Avengers*, which was directed by Joss Whedon, is in the action/adventure/sci-fi genres, and stars Robert Downey Jr. — so it recommends Whedon's *Serenity*, *Jurassic Park* (same genres), and Downey's *Sherlock Holmes*. A **hybrid** system first finds Amy and Carl as similar users, then uses content features to surface *Justice League* (same genres as items both liked) even though neither has seen it before.

## Related Concepts

- [[clustering|Clustering]] — groups similar items or users, forming the basis for cluster-based recommendation
- [[nlp-basics|NLP Basics]] — text features from item descriptions enable content-based filtering
- [[linear-regression|Linear Regression]] — rating prediction can be framed as a regression problem
- [[pca|PCA]] — dimensionality reduction for sparse user-item matrices (related to SVD/matrix factorization)
- [[decision-trees|Decision Trees]] — can model user preferences as decision rules
- [[ab-testing|A/B Testing]] — essential for evaluating recommendation algorithm changes in production
- [[ecommerce-models|E-commerce Models]] — major e-commerce platforms depend on recommendation systems for conversion
- [[wiki/entities/hkust|HKUST]] — course home institution

## Source Materials

- Lecture 7: Netflix (Clustering & Recommendation Systems)
- [[wiki/sources/courses/applied-statistics|EEMT5500 Applied Probability, Statistics and Data Analytics]]
