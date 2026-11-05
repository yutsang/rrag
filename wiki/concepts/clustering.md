---
title: "Clustering"
full_name: "Clustering (Unsupervised Learning)"
type: concept
tags: [machine-learning, unsupervised-learning, k-means, hierarchical-clustering, segmentation]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/applied-statistics"
confidence: high
---

## 概述

聚類分析是一種無監督學習方法，在沒有標籤的情況下將數據點分組為內部相似、外部相異的群組，目標是同時最大化群內相似度與群間差異度。K-means 演算法以歐氏距離為基礎，時間複雜度為 $O(n \cdot K \cdot \text{iter})$，適合大規模數據；層次聚類則以樹狀圖（dendrogram）呈現嵌套分組結構，時間複雜度 $O(n^2)$ 至 $O(n^3)$，適合探索性分析和確定自然聚類數量。EEMT5500 課程以 MovieLens 9,707部電影的18維類型向量為案例，展示如何用 K-means（K=10，nstart=25）和 Ward 層次聚類獲得不同但同樣有效的分組結果，並揭示聚類結果的主觀性——不存在唯一「正確」答案。特徵標準化（z-score）是 K-means 的關鍵前處理步驟，Hubway 共享單車案例清晰說明若忽略此步驟，Duration 變數會主導歐氏距離計算並壓制其他特徵的影響。聚類在商業應用中扮演多重角色：作為客戶細分的主要工具、與推薦系統結合實現內容過濾、以及識別離群值（如騎行時長異常的異常群組）；在運籌學中，聚類常作為「先分群後預測」兩階段策略的第一步，提升每個子群體的預測模型精度。

## Core Mechanism

**Clustering** is an **unsupervised learning** technique that groups data points into clusters based on similarity, without any pre-defined labels. Unlike [[linear-regression|Linear Regression]], [[logistic-regression|Logistic Regression]], or [[decision-trees|Decision Trees]], clustering does not require a target variable — it discovers structure in the data autonomously.

The fundamental goal is to maximize **intra-cluster similarity** (points within the same cluster are close together) while maximizing **inter-cluster dissimilarity** (points in different clusters are far apart).

## K-Means Clustering

**K-means** is the most widely used clustering algorithm due to its simplicity and speed. It partitions n observations into K clusters, where each observation belongs to the cluster with the nearest centroid.

### Algorithm (6 Steps)

1. **Specify K**: Choose the number of clusters (must be decided in advance)
2. **Random assignment**: Randomly assign each data point to one of K clusters
3. **Compute centroids**: Calculate the mean (centroid) of each cluster
4. **Re-assign**: Assign each point to the cluster whose centroid is nearest (using Euclidean distance)
5. **Re-compute centroids**: Recalculate the centroid of each cluster based on new assignments
6. **Repeat**: Iterate steps 4-5 until cluster assignments no longer change (convergence)

### Distance Metric

K-means uses **Euclidean distance** as the default similarity measure:

$$d(a, b) = \sqrt{\sum_i (a_i - b_i)^2}$$

This means all features are weighted equally, making **data normalization** critical when features have different scales (e.g., age in years vs. income in dollars).

**Worked distance example from the lectures**: *Toy Story* is categorized as animation, comedy, children, giving vector $(0,0,1,1,1,0,\ldots,0)$ over 18 genres. *Batman Forever* is action, adventure, comedy, crime: $(1,1,0,0,1,1,0,\ldots,0)$. Their distance is

$$d = \sqrt{(0-1)^2 + (0-1)^2 + (1-0)^2 + (1-0)^2 + (1-1)^2 + (0-1)^2 + 0 + \cdots} = \sqrt{5}$$

With 18 binary genre features and no magnitude disparity, normalization is unnecessary here; if release year or box office were added, z-scoring would be required.

### The nstart Parameter

Because K-means starts with random assignments, different runs can produce different results. The **nstart** parameter runs the algorithm multiple times with different random initializations and returns the best result (lowest total within-cluster sum of squares).

```r
km.out = kmeans(data, K, nstart = 25)
```

### Choosing K

Selecting the number of clusters is a fundamental challenge with **no universally agreed-upon method**. Common approaches:
- **Elbow method**: Plot total within-cluster sum of squares vs. K; look for an "elbow" where improvements diminish
- **Silhouette analysis**: Measures how similar each point is to its own cluster vs. neighboring clusters
- **Domain knowledge**: Business context often dictates a natural number of segments
- **Trial and error**: Iterate with different K values and interpret results

## Hierarchical Clustering

**Hierarchical clustering** builds a tree-like structure (dendrogram) that shows nested groupings at every level of similarity. The **agglomerative** (bottom-up) approach is most common:

1. **Start**: Each observation is its own cluster (n clusters total)
2. **Merge**: Find the two closest clusters and merge them (n-1 clusters)
3. **Repeat**: Continue merging until all observations belong to a single cluster
4. **Cut**: Choose a height at which to cut the dendrogram to produce K clusters

### Distance Between Clusters (Linkage)

When merging clusters, the definition of "distance between clusters" matters:

| Linkage Method | Definition | Characteristics |
|----------------|------------|-----------------|
| **Minimum (single)** | Distance between closest points in each cluster | Tends to produce elongated, chained clusters |
| **Maximum (complete)** | Distance between farthest points | Produces compact, spherical clusters |
| **Mean (average)** | Average distance between all pairs of points | Compromise between single and complete |
| **Centroid** | Distance between cluster centroids | Intuitive but can produce inversions in dendrogram |
| **Ward's method** | Minimizes increase in total within-cluster variance | Often produces the most balanced clusters |

### Reading a Dendrogram

- Data points are listed along the bottom
- **Height of vertical lines** represents the distance at which clusters are merged
- Cutting at different heights produces different numbers of clusters
- A large gap between merge heights suggests a "natural" number of clusters

```r
distances = dist(data)  # Compute pairwise Euclidean distances
hc.out = hclust(distances, method = "ward.D")
plot(hc.out)  # Visualize dendrogram
hc.clusters = cutree(hc.out, k = 10)  # Cut into 10 clusters
```

## Comparison: K-Means vs. Hierarchical

| Criterion | K-Means | Hierarchical |
|-----------|---------|--------------|
| **Speed** | $O(n \cdot K \cdot \text{iterations})$ — fast | $O(n^2)$ or $O(n^3)$ — slower |
| **K selection** | Must specify in advance | Can choose after viewing dendrogram |
| **Outlier sensitivity** | High — outliers skew centroids | Lower — outliers form small branches |
| **Cluster shape** | Assumes spherical clusters | No shape assumption |
| **Reproducibility** | Depends on random start | Deterministic |
| **Scalability** | Handles large datasets well | Struggles with very large n |
| **Output** | Cluster assignments only | Full hierarchy (dendrogram) |

## Case Study: MovieLens Genre Clustering (Lecture 7)

The course uses the **MovieLens** dataset to demonstrate both clustering methods on a real recommendation system dataset.

### Dataset

- **9,707 movies** with 18 binary genre features (Action, Adventure, Animation, Children, Comedy, Crime, Documentary, Drama, Fantasy, Film-Noir, Horror, Musical, Mystery, Romance, Sci-Fi, Thriller, War, Western)
- Each movie is represented as an 18-dimensional binary vector
- **ReleaseYear** is also included

### K-Means Results (K = 10)

Using `kmeans(movies[4:21], 10, nstart=25)`, the algorithm produced 10 genre-based clusters. Analysis using `tapply()` to compute the proportion of movies in each genre per cluster revealed:

- **Cluster 1**: Dominated by Action movies (100% Action)
- **Cluster 6**: Pure Romance cluster (100% Romance)
- **Cluster 8**: Romance-heavy cluster (100% Romance, with additional genres)

*Avengers: Age of Ultron* was assigned to **cluster 4**, which had 74.1% Action content. Other movies in this cluster included *Cutthroat Island*, *Mortal Kombat*, *Batman Forever*, *Star Wars: Episode IV*.

### Hierarchical Clustering Results (K = 10, Ward's method)

Using `hclust()` with Ward's D method and cutting at k = 10:

- **Cluster 5**: Action-heavy (72.4% Action)
- **Cluster 2**: Pure Romance (100% Romance)
- **Cluster 3**: Pure Romance (100% Romance)

*Avengers: Age of Ultron* was assigned to **cluster 5**. Nearby movies included *Heat*, *GoldenEye*, *Batman Forever* — similar action/adventure films.

The two methods produced **different but equally valid** clusterings, illustrating that clustering is inherently subjective — there is no single "correct" answer.

## Worked Example: Hubway Bike-Share Segmentation (HW3)

HW3 applies K-means to `HubwayTrips.csv`, trips taken by registered users of the Boston Hubway bike-share from June to September 2012. The nine variables mix a continuous `Duration` (seconds) and `Age` with six binary time-of-day / day-of-week indicators (Morning / Afternoon / Evening / Night, Weekday / Weekend) plus `Male`. The assignment exists mainly to teach **why normalization matters**: Duration varies from minutes to hours while the other features are on a 0/1 scale, so clustering raw data lets Duration dominate the Euclidean distance and collapse the segmentation into "long trips" vs. "short trips". Z-scoring every column first (mean 0, SD 1) forces each feature to carry equal geometric weight.

With 10 clusters and `nstart=25`, K-means surfaces interpretable rider segments directly from the centroids: weekday-morning commuters (two age bands, ~30 and ~49), weekday-evening riders, weekend-afternoon leisure users, late-night riders (predominantly younger males), and a tiny anomaly cluster of ~6 trips with a Duration centroid around **435,000 seconds** — essentially forgotten bikes or data-entry errors that the algorithm isolates because they are extreme even after normalization. That single anomaly cluster is the most analytically useful output: it demonstrates that K-means functions as an outlier detector when one cluster ends up containing a handful of pathological observations, and any serious downstream analysis should either drop or investigate that cluster before reporting marketing personas. The HW also shows that pushing K up or down materially changes interpretability — more clusters fragment the commuter archetypes unnecessarily, fewer blur the age-by-time-of-day structure.

```r
data = read.csv("HubwayTrips.csv")
dataNM = data.frame(scale(data, center = TRUE, scale = TRUE))
set.seed(7006)
km.out = kmeans(dataNM, 10, nstart = 25)
table(km.out$cluster)  # one tiny cluster (~6 trips) flags anomalies
```

## Practical Considerations

### Data Normalization

When features have different scales, normalization is essential:
- **Z-score normalization**: $\frac{x - \bar{x}}{s}$ — centers at 0, scales to standard deviation 1
- **Min-max normalization**: $\frac{x - x_{\min}}{x_{\max} - x_{\min}}$ — scales to [0, 1]

For the MovieLens data, normalization was not necessary because all genre features are binary (0/1) and thus on the same scale.

### Applications in Business

- **Customer segmentation**: Group customers by purchasing behavior for targeted marketing
- **Market research**: Identify natural product categories or competitor groups
- **Anomaly detection**: Points far from any cluster centroid may be outliers
- **Image compression**: Reduce color palette by clustering pixel colors
- **Document organization**: Group similar documents for topic discovery

## Business Applications from the Lecture

- **Marketing / customer segmentation**: discover distinct customer groups for targeted campaigns — see [[stp-marketing|Segmentation, Targeting, Positioning]] and [[marketing-mix|Marketing Mix]].
- **Fraud detection**: identify peer groups and normal behavior, then flag outliers per cluster — pairs naturally with [[benfords-law|Benford's Law]] screening.
- **Insurance**: identify customer groups with high average claim cost for pricing.
- **Stock selection**: identify groups of stocks with similar trends for basket trading.
- **Cluster-then-predict**: segment first, then build a separate [[linear-regression|Linear Regression]] or [[logistic-regression|Logistic Regression]] model per cluster — works best on large datasets to avoid overfitting.

## Related Concepts

- [[recommendation-systems|Recommendation Systems]] — clustering is used within collaborative filtering to group similar users or items
- [[pca|PCA]] — dimensionality reduction often applied before clustering to reduce noise
- [[decision-trees|Decision Trees]] — supervised partitioning analogous to unsupervised clustering
- [[nlp-basics|NLP Basics]] — text clustering groups documents by topic similarity
- [[linear-regression|Linear Regression]] — cluster membership can serve as a feature in regression models
- [[logistic-regression|Logistic Regression]] — cluster-then-predict is a common two-stage approach
- [[wiki/entities/hkust|HKUST]] — course home institution
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Statistical Learning for OR)

## Source Materials

- Lecture 7: Netflix (Clustering & Recommendation Systems)
- [[wiki/sources/courses/applied-statistics|EEMT5500 Applied Probability, Statistics and Data Analytics]]
