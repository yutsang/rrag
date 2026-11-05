---
title: "STP Marketing"
full_name: "Segmentation, Targeting, and Positioning (STP)"
type: concept
tags: [marketing, segmentation, targeting, positioning, strategy]
created: "2026-04-10"
updated: "2026-04-14"
source: "wiki/sources/courses/marketing"
confidence: high
---

## 概述

STP（市場細分、目標市場選擇、市場定位）是現代行銷策略的核心三步驟框架，位於環境掃描與[[wiki/concepts/consumer-behavior|消費者行為]]分析之後、[[wiki/concepts/marketing-mix|行銷組合]]（4P）設計之前，是將異質市場轉化為可服務細分群體並制定差異化定位的關鍵橋樑。市場細分（Segmentation）按地理、人口、心理（VALS框架：動機×資源）和行為（場合、利益訴求、使用率、忠誠度、購買準備階段）四大維度劃分群體，有效細分須同時滿足可衡量性、可接達性、足夠規模、可差異化響應和可執行性五個條件；加油站市場案例（Road Warriors、True Blues、Generation F3、Homebodies、Price Shoppers五個細分）典型地呈現了同一物理商品如何因細分維度不同而需要截然不同的價值主張。目標市場選擇（Targeting）的四種策略——無差異（大眾行銷）、差異化（多細分）、集中（利基）和微行銷（個人化）——須與[[wiki/concepts/porters-five-forces|波特通用策略]]對應：利基聚焦策略自然匹配集中定位，而「陷入中間」的策略既不具規模成本優勢又無差異化溢價，是最危險的定位陷阱。定位（Positioning）的競爭優勢公式 $V_A - P_A > V_B - P_B$ 統一了所有定位決策：增加感知價值（產品、服務、通路、人員、形象五類差異化來源）或降低消費者成本均可拓寬優勢。感知地圖（描述消費者對品牌的當前認知）與定位地圖（呈現未來定位目標）在 Music2Go 模擬中每輪重繪，DreamWave 團隊的重定位軌跡驗證了「消費者理想點優先於工程師理想點」的核心教訓。在數字時代，[[wiki/concepts/clustering|聚類算法]]和[[wiki/concepts/logistic-regression|邏輯迴歸]]從行為數據中自動生成細分結果，[[wiki/concepts/ab-testing|A/B 測試]]取代焦點小組成為定位測試的主流工具，個人化行銷通過[[wiki/concepts/recommendation-systems|推薦系統]]和[[wiki/concepts/crm|CRM]]驅動的行為觸發活動實現市場級別的一對一 STP 執行。

## What STP Is

**STP** stands for **Segmentation, Targeting, and Positioning** -- the three sequential steps a firm uses to identify which customers to serve and how to serve them distinctively. It sits between the analytical phase of marketing (environment scanning, [[wiki/concepts/consumer-behavior|consumer behavior]] analysis) and the tactical phase (designing the [[wiki/concepts/marketing-mix|Marketing Mix]]). Every element of the 4Ps should flow from STP decisions: the product features chosen, the price set, the channels used, and the messages communicated all reflect who the firm is targeting and how it wants to be perceived.

```mermaid
graph TD
    A[Heterogeneous<br>Market] --> B[Segmentation]
    B --> C[Targeting]
    C --> D[Positioning]
    D --> E[Tailored<br>Marketing Mix]
    B -.> B1[Geographic]
    B -.> B2[Demographic]
    B -.> B3[Psychographic]
    B -.> B4[Behavioral]
    C -.> C1[Undifferentiated]
    C -.> C2[Differentiated]
    C -.> C3[Concentrated]
    C -.> C4[Micromarketing]
    D -.> D1[Perceptual Map]
    D -.> D2[Value Proposition]
    D -.> D3[Positioning Statement]

    style A fill:#dae8fc,stroke:#6c8ebf
    style B fill:#fff2cc,stroke:#d6b656
    style C fill:#fff2cc,stroke:#d6b656
    style D fill:#fff2cc,stroke:#d6b656
    style E fill:#d5e8d4,stroke:#82b366
```

## Segmentation

**Market segmentation** is the process of dividing a broad market into distinct subgroups of consumers who share similar needs, characteristics, or behaviors and who might require separate marketing strategies. Effective segmentation is the foundation of targeted marketing -- without it, firms either waste resources on mass approaches or miss high-value niches.

### Segmentation Bases for Consumer Markets

| Base | Variables | Example |
|------|-----------|---------|
| **Geographic** | Region, city size, density, climate | Urban vs. rural pricing for delivery services |
| **Demographic** | Age, gender, income, education, family size, occupation, religion, ethnicity | Luxury brands targeting high-income professionals |
| **Psychographic** | Social class, lifestyle, personality traits | VALS framework classifying consumers by motivations and resources |
| **Behavioral** | Occasion, benefits sought, usage rate, loyalty status, readiness stage | Gasoline market: "road warriors" vs. "price shoppers" |

The gasoline market example from SBMT5030 illustrates multi-variable segmentation effectively. Five distinct segments emerge -- **road warriors** (higher-income loyalists who buy premium fuel and premium services), **true blues** (brand-loyal, moderate usage, respond to loyalty programs), **generation F3** (fuel, food, and fast -- convenience-driven younger drivers willing to pay for speed), **homebodies** (not brand or station loyal, buy on convenience alone), and **price shoppers** (purely cost-driven, will drive extra miles to save pennies). Each segment requires a fundamentally different value proposition -- premium branded service for road warriors, clean in-store retail and hot food for generation F3, discount-forward communication for price shoppers. The same physical commodity (regular unleaded) is wrapped in entirely different marketing mixes.

### Lifestyle and Psychographic Segmentation

Psychographic segmentation goes beyond demographics to capture *how* people live. The **VALS** framework (Values, Attitudes, Lifestyles) classifies consumers by primary motivation (ideals, achievement, self-expression) and resources (high to low). **AIO** inventories (Activities, Interests, Opinions) build lifestyle profiles from survey data. Panera Bread targets a "healthy eating lifestyle" subculture; MINI Cooper targets an "adventurous, individualistic, open-minded, creative, tech-savvy, young at heart" self-concept. These segments cut across income and age brackets. Modern digital analytics replicates psychographic segmentation through behavioral signals (browsing, social posts, search history) processed with [[wiki/concepts/clustering|clustering]] and [[wiki/concepts/nlp-basics|NLP]] techniques.

### Behavioral Segmentation in Depth

Behavioral variables often produce the sharpest distinctions between customer groups:

- **Occasion** -- when the product is bought or used (Champagne for celebrations, Kodak "Kodak Moments" for travel).
- **Benefits sought** -- primary benefit that motivates purchase (Colgate segments toothpaste buyers by economy, cavity prevention, cosmetic whitening, flavor preference).
- **User status** -- nonuser, ex-user, potential user, first-time user, regular user. Each stage calls for different messaging.
- **Usage rate** -- light, medium, heavy. The Pareto principle (80/20) often applies: heavy users drive most revenue.
- **Loyalty status** -- hard-core loyals, split loyals, shifting loyals, switchers. Loyalty programs target split loyals and reward hard-core loyals.
- **Readiness stage** -- unaware, aware, informed, interested, desirous, intending to buy. Maps directly onto the marketing funnel.

### Segmentation Bases for B2B Markets

B2B segmentation uses a different set of variables, organized in a nested hierarchy from broad to narrow:

1. **Demographic** -- industry, company size, location
2. **Operating variables** -- technology, user/nonuser status, customer capabilities
3. **Purchasing approaches** -- purchasing function organization, power structure, buyer-seller relationship, purchasing policies, purchasing criteria
4. **Situational factors** -- urgency of order, specific application, size of order
5. **Personal characteristics** -- buyer-seller similarity, attitudes toward risk, loyalty

### Requirements for Effective Segmentation

A segment must be **measurable** (size and purchasing power can be quantified), **accessible** (can be reached and served), **substantial** (large or profitable enough to justify a tailored strategy), **differentiable** (responds differently to different marketing mixes), and **actionable** (effective programs can be designed for it).

## Targeting

Once segments are identified, the firm must evaluate each segment's attractiveness and select one or more to enter. This evaluation considers segment size and growth, structural attractiveness (competition intensity, substitute threats, buyer/supplier power -- connecting to [[wiki/concepts/porters-five-forces|Porter's Five Forces]]), and the firm's own objectives and resources.

### Targeting Strategies

| Strategy | Description | When to Use | Risk |
|----------|-------------|-------------|------|
| **Undifferentiated (Mass)** | Single offer for the entire market | Commodity products with universal appeal | Vulnerable to focused competitors |
| **Differentiated (Multi-segment)** | Different offers for different segments | Sufficient resources to serve multiple segments | Higher costs; cannibalization risk |
| **Concentrated (Niche)** | Deep focus on one or few segments | Limited resources; strong niche knowledge | Over-reliance on a single segment |
| **Micromarketing** | Tailored to local areas or individual customers | Digital capability for personalization | Scalability challenges; high cost |

Coca-Cola exemplifies **differentiated targeting**: Coca-Cola Classic for mainstream, Diet Coke historically positioned toward weight-conscious women, Coke Zero Sugar for males who want full taste without calories, Coke Life for natural-sweetener seekers, plus regional/flavor variants (Cherry, Vanilla, local fruit flavors in Asia). Marriott similarly uses a multi-brand architecture with over 30 brands targeting distinct segments -- from Fairfield Inn and SpringHill Suites (economy/midscale), through Courtyard and Residence Inn (business), to JW Marriott, W Hotels, and Ritz-Carlton (luxury). Marriott's strategy demonstrates that a multi-brand house can capture more total market share than any single master brand could.

**Micromarketing** splits further into **local marketing** (tailoring to local customer groups -- cities, neighborhoods, stores; e.g., McDonald's serving rice burgers in Asia, McSpicy Paneer in India) and **individual marketing** (one-to-one customization enabled by mass customization technology and digital platforms; e.g., NikeID custom sneakers, Coca-Cola "Share a Coke" personalized bottles, Amazon's algorithmic product recommendations). Individual marketing is also called "one-to-one marketing" or "markets-of-one marketing" and is the logical endpoint of [[wiki/concepts/recommendation-systems|recommendation systems]] and behaviorally triggered [[wiki/concepts/crm|CRM]] campaigns.

### Porter's Generic Strategies and Targeting

Targeting intersects with [[wiki/concepts/porters-five-forces|Porter's Five Forces]] analysis through **Porter's generic strategies**: cost leadership (broad market, low cost), differentiation (broad market, unique value), cost focus (narrow market, low cost), differentiation focus (narrow market, unique value). The course warns explicitly against being "stuck in the middle" -- neither clearly low-cost nor clearly differentiated -- because such firms forfeit both scale economies and price premiums. Niche (concentrated) targeting naturally aligns with focus strategies and often builds strong brand loyalty that raises switching costs.

## Positioning

**Positioning** is the act of designing the company's offering and image to occupy a distinctive place in the minds of the target market. It answers: "Why should a customer in our target segment choose us over the competition?"

### The Competitive Advantage Formula

The course emphasizes a formal value equation:

> $V_A - P_A > V_B - P_B$

Where V = perceived value and P = price. A firm achieves competitive advantage when its value-minus-price surplus exceeds that of competitors. This can be achieved by increasing perceived value (product quality, brand image, service) or by reducing price, or ideally both.

### Points of Parity, Contention, and Difference

The course distinguishes three kinds of value elements in competitive positioning:

- **Point of parity** -- both offerings provide roughly the same level of benefits on this attribute (e.g., two laptops both offer Wi-Fi). Necessary to compete but does not differentiate.
- **Point of contention** -- both marketers claim superiority on an attribute, yet neither can conclusively prove it (e.g., "best image quality" in DSLR marketing). Buyers often discount these claims.
- **Point of difference** -- one offering is clearly and demonstrably superior on a value element (e.g., a car with the highest independently verified fuel economy rating, or Volvo's safety record). This is the foundation of durable positioning.

A strong positioning strategy builds on at least one credible point of difference while maintaining parity on category-defining attributes.

### Worked Example: Music2Go Perceptual Maps

The SBMT5030 Music2Go simulation tracks perceptual maps for the headphone market across Periods 2024-2028, with separate maps for the Music, Gaming, and Fitness segments. Each team's three products plot against the segment's **ideal point** on two key buying dimensions, and the map redraws every decision round as competitors adjust product specs, price, and advertising. The student team DreamWave Inc. (World 2) used the perceptual map as their core competitive-positioning instrument: DreamTune's 2025-2026 repositioning trajectory was driven explicitly by mapping distance to the ideal Music-segment point rather than by internal engineering preferences. Prof. Salvacruz's finale debrief warns that "consumer ideals" and "engineering ideals" often diverge -- perceptual-map data should override engineering intuition when they conflict. This is the most direct classroom drill of point-of-difference hunting described below.

### Perceptual Maps vs. Positioning Maps

The course distinguishes the two terms that are often used interchangeably:

- **Perceptual maps** show how consumers currently *perceive* brands on subjective dimensions (emphasis on perception rather than measured attributes). Primarily descriptive of current and past market state.
- **Positioning maps** show the positioning of brands as measured more objectively and emphasize *future* positioning goals.

In practice, both are two-dimensional plots with competing brands located on axes representing key buying dimensions -- price vs. quality, traditional vs. modern, functional vs. emotional, or low moisturizing vs. high moisturizing (the classic bar soap example with Dove, Lux, Zest, Dial, Lifebuoy). These maps reveal:

- **Gaps** in the market where no brand currently positions (potential blue-ocean opportunities)
- **Clusters** of brands competing head-to-head (red-ocean areas with commoditization pressure)
- **Movement trajectories** as brands reposition over time (e.g., Cadillac moving toward younger buyers)

### Sources of Differentiation

Firms can build competitive advantage through five distinct sources of differentiation:

1. **Product differentiation** -- features, performance, design (Apple iPhone, Tesla)
2. **Service differentiation** -- delivery, installation, customer support (Zappos, Nordstrom)
3. **Channel differentiation** -- coverage, expertise, convenience of distribution (Caterpillar dealer network)
4. **People differentiation** -- trained, friendly, knowledgeable staff (Singapore Airlines, Ritz-Carlton)
5. **Image differentiation** -- symbols, media, atmospheres, events (Volvo = safety, BMW = driving, Apple = design, Red Bull = extreme sports)

### Positioning Statement

A formal positioning statement follows this template:

> "To [target segment], [brand] is the [category] that [key benefit/point of difference] because [reason to believe]."

For example: "To busy professionals who need a quick energy boost, Red Bull is the energy drink that gives you wings because of its unique blend of caffeine, taurine, and B-vitamins."

### Choosing a Positioning Strategy

Firms must select which differences to promote. Not every difference is worth establishing. The criteria for a good differentiator are: **important** (delivers a valued benefit), **distinctive** (competitors don't offer it), **superior** (better than other ways to get the same benefit), **communicable** (visible and explainable), **preemptive** (hard to copy), **affordable** (buyers can pay for it), and **profitable** (the firm can introduce it profitably).

Common positioning errors include **underpositioning** (failing to establish any clear position), **overpositioning** (giving too narrow a picture), **confused positioning** (inconsistent messages), and **doubtful positioning** (claims buyers find hard to believe).

## STP in Practice: An Integrated Example

Consider the hotel industry. **Segmentation** identifies distinct traveler groups: budget leisure, business mid-range, luxury, extended stay, resort/vacation. **Targeting** depends on the firm's portfolio -- Marriott International targets multiple segments through differentiated brands. **Positioning** differentiates each brand within its target segment: Courtyard positions as "the hotel designed by business travelers" while Ritz-Carlton positions around "creating memorable experiences." Each brand then builds its [[wiki/concepts/marketing-mix|Marketing Mix]] to deliver on that positioning promise.

## Connection to CRM

STP provides the strategic foundation for **Customer Relationship Management** ([[wiki/concepts/crm|CRM]]). Segmentation identifies which customer groups exist; targeting determines which are worth investing in; positioning shapes the value proposition that attracts and retains them. CRM systems then operationalize these strategies through personalized communication, loyalty programs, and lifetime value optimization -- effectively implementing micromarketing at scale.

## Limitations and Considerations

- **Over-segmentation** can fragment the market to the point where no segment is large enough to serve profitably. The solution is segment consolidation or tiered offerings.
- Segments are not static -- they evolve with demographic shifts, cultural changes, and technological disruption. Periodic resegmentation (every 2-3 years) is standard practice.
- **Ethical concerns** arise when segmentation leads to discriminatory practices (redlining in insurance and lending, predatory targeting of vulnerable groups with payday loans or gambling, dark patterns in digital advertising that exploit cognitive biases studied in [[wiki/concepts/behavioral-economics|behavioral economics]]).
- **Positioning errors** include underpositioning (failing to establish any clear position), overpositioning (giving too narrow a picture), confused positioning (inconsistent messages), and doubtful positioning (claims buyers find implausible).
- In digital markets, behavioral and psychographic segmentation increasingly relies on data analytics and [[wiki/concepts/clustering|clustering]] algorithms, blurring the line between traditional marketing segmentation and machine learning classification. [[wiki/concepts/logistic-regression|Logistic regression]] and tree-based classifiers are used to score prospects for targeting campaigns, and the output looks very much like a demographic-behavioral segmentation table -- but generated from data rather than managerial judgment. Positioning tests are increasingly run as online [[wiki/concepts/ab-testing|A/B experiments]] rather than offline focus groups.

## Related Concepts

- [[wiki/concepts/marketing-mix|Marketing Mix]]
- [[wiki/concepts/consumer-behavior|Consumer Behavior]]
- [[wiki/concepts/clustering|Clustering]]
- [[wiki/concepts/porters-five-forces|Porter's Five Forces]]
- [[wiki/concepts/crm|CRM]]
- [[wiki/concepts/ab-testing|A/B Testing]]
- [[wiki/concepts/behavioral-economics|Behavioral Economics]]
- [[wiki/concepts/recommendation-systems|Recommendation Systems]]
- [[wiki/concepts/logistic-regression|Logistic Regression]]

## Source Materials

- [[wiki/sources/courses/marketing|SBMT5030 Marketing Management and Strategy]]
- Lecture 07: STP
- Lecture 05: Consumer and Buyer Behavior
