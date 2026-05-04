# 🛒 Retail Stock-Out Reduction — BA Portfolio Project

> **Status:** ✅ Complete  
> **Date:** May 2026  
> **Author:** BanothDeepak  
> **GitHub:** github.com/BanothDeepak/retail-stockout-ba-project

---

## 📌 Project Overview

| Field | Detail |
|---|---|
| Project | Retail Stock-Out Reduction |
| Dataset | Retail Store Inventory Forecasting (Kaggle) |
| Rows | 73,100 |
| Stores | 5 |
| Products | 20 |
| Categories | 5 (Electronics, Clothing, Furniture, Groceries, Toys) |
| Tools | Python · pandas · matplotlib · VS Code · GitHub |

---

## 🎯 Business Problem

A retail chain is experiencing simultaneous stock-out and overstock situations across all stores.
Analysis revealed this is a **systemic replenishment model failure** — not a category-specific issue.

---

## 📋 Phase Tracker

| Phase | Name | Status | Deliverable |
|---|---|---|---|
| 1 | Project Scoping | ✅ Done | Project title + context |
| 2 | Requirements Gathering | ✅ Done | Data Dictionary + User Stories + BRD |
| 3 | Data Analysis | ✅ Done | Python scripts + CSV + PNG + Excel |
| 4 | Dashboard & Deck | ✅ Done | PowerPoint (8 slides) + HTML Dashboard |
| 5 | Portfolio Packaging | ✅ Done | PDF Case Study + LinkedIn + Notion |

---

## 👥 User Stories

### US-01 · Store Operations Manager
**As a** store operations manager,  
**I want to** see which products have inventory below 1.5× daily units sold,  
**So that** I can prioritise replenishment before stock runs out.

**Rule:** `Inventory Level < Units Sold × 1.5`  
**Finding:** ~4,800 low-stock rows per category — systemic, not isolated

---

### US-02 · Supply Chain Planner
**As a** supply chain planner,  
**I want to** compare forecast accuracy against actual sales by season and category,  
**So that** I can identify where the model consistently over/under-predicts.

**Rule:** `MAE = |Demand Forecast - Units Sold|`  
**Finding:** MAE flat at 8.32–8.40 — no seasonal weighting in the model  
**Data Quality Flag:** Negative Demand Forecast values excluded (min: -10.07)

---

### US-03 · Category Manager
**As a** category manager,  
**I want to** see how inventory and sales change on promotional vs normal days,  
**So that** I can ensure adequate stock before promotions go live.

**Rule:** Split by `Holiday/Promotion = 1` vs `0`  
**Finding:** 137.6 vs 137.8 avg units sold — promotions deliver zero incremental demand

---

### US-04 · Pricing Analyst
**As a** pricing analyst,  
**I want to** compare our prices against competitor pricing by region and category,  
**So that** I can identify where we are underpriced and losing margin.

**Rule:** Flag rows where `Price Gap % < -15%`  
**Finding:** Groceries at -18.3% — exceeds the 15% alert threshold

---

### US-05 · Operations Director
**As an** operations director,  
**I want** a single summary of overstock and low-stock % by store and region,  
**So that** I can make strategic redistribution decisions.

**Rules:**  
- Overstock: `Inventory Level > Demand Forecast × 2.5`  
- Low Stock: `Inventory Level < Units Sold × 1.5`  

**Finding:** Consistent ~38% overstock and ~33% low-stock across all 5 stores

---

## 📊 Key Findings

| # | Finding | Impact |
|---|---|---|
| 1 | All 5 categories at 33% low-stock + 37% overstock simultaneously | Replenishment model is broken |
| 2 | Forecast MAE flat across all seasons | No seasonal weighting exists |
| 3 | Promotions on 50% of days, zero uplift | Promotion spend is wasted |
| 4 | Groceries -18.3% below competitor price | Margin is being lost nationally |

---

## 💡 Recommendations

1. **Fix the Replenishment Model** — Set dynamic reorder points using `Units Sold × 1.5`
2. **Introduce Seasonal Weighting** — Start with Furniture (Autumn) and Toys (Winter)
3. **Conduct Promotion ROI Audit** — Review all promotion types before next cycle
4. **Review Grocery Pricing Nationally** — Immediate pricing review to recover margin

---

## 📁 Deliverables

- [ ] Data Dictionary (15 columns)
- [ ] 5 User Stories with acceptance criteria
- [ ] Business Requirements Document (9 sections)
- [ ] Python Analysis Script (phase3_analysis.py)
- [ ] Output CSVs + PNGs + Excel (phase3_all_findings.xlsx)
- [ ] PowerPoint Deck (Phase4_RetailStockOut_Deck.pptx)
- [ ] HTML Dashboard (Phase4_Dashboard.html)
- [ ] PDF Case Study (Phase5_BA_CaseStudy.pdf)
- [ ] GitHub Repository pushed and live

---

## 🔗 Links

- GitHub: github.com/BanothDeepak/retail-stockout-ba-project
- Dataset: Kaggle — Retail Store Inventory Forecasting (anirudhchauhan)