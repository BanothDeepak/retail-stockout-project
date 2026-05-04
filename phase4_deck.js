// ═══════════════════════════════════════════════════════
//  PHASE 4 — SLIDE DECK
//  Retail Stock-Out Reduction — BA Portfolio Project
//  Run: node phase4_deck.js
// ═══════════════════════════════════════════════════════

const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.layout  = "LAYOUT_16x9";
pres.title   = "Retail Stock-Out Reduction";
pres.author  = "BanothDeepak";

// ── PALETTE ──────────────────────────────────────────
const C = {
  navy:    "1E2761",
  ice:     "CADCFC",
  white:   "FFFFFF",
  dark:    "12193D",
  accent:  "4FC3F7",
  red:     "E74C3C",
  amber:   "F39C12",
  green:   "27AE60",
  muted:   "8A9BBF",
  card:    "F4F7FF",
};

const makeShadow = () => ({
  type: "outer", blur: 6, offset: 3,
  angle: 135, color: "000000", opacity: 0.12
});

// ════════════════════════════════════════════════════
//  SLIDE 1 — TITLE
// ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  // Left accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 0.18, h: 5.625,
    fill: { color: C.accent }, line: { color: C.accent }
  });

  // Top label
  s.addText("BUSINESS ANALYST PORTFOLIO", {
    x: 0.4, y: 0.5, w: 9, h: 0.4,
    fontSize: 10, color: C.muted, bold: true,
    charSpacing: 4, margin: 0
  });

  // Main title
  s.addText("Retail Stock-Out\nReduction", {
    x: 0.4, y: 1.1, w: 7, h: 2.2,
    fontSize: 48, color: C.white, bold: true,
    fontFace: "Calibri", lineSpacingMultiple: 1.1, margin: 0
  });

  // Subtitle
  s.addText("Phase 3 Analysis — 5 User Stories | 73,100 Rows | 5 Stores | 20 Products", {
    x: 0.4, y: 3.4, w: 8.5, h: 0.5,
    fontSize: 13, color: C.ice, margin: 0
  });

  // Bottom strip
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 5.0, w: 10, h: 0.625,
    fill: { color: C.dark }, line: { color: C.dark }
  });
  s.addText("BanothDeepak  |  github.com/BanothDeepak/retail-stockout-ba-project  |  May 2026", {
    x: 0.4, y: 5.05, w: 9.2, h: 0.5,
    fontSize: 9, color: C.muted, margin: 0
  });
}

// ════════════════════════════════════════════════════
//  SLIDE 2 — EXECUTIVE SUMMARY
// ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.white };

  s.addText("Executive Summary", {
    x: 0.5, y: 0.25, w: 9, h: 0.6,
    fontSize: 28, color: C.navy, bold: true, margin: 0
  });

  // KPI cards
  const cards = [
    { label: "Dataset Rows",    value: "73,100",  sub: "5 stores · 20 products",   col: C.navy  },
    { label: "Low Stock Risk",  value: "33%",     sub: "of all inventory records",  col: C.red   },
    { label: "Overstock Rate",  value: "37.8%",   sub: "excess inventory flagged",  col: C.amber },
    { label: "Promo Uplift",    value: "~0%",     sub: "no incremental demand",     col: C.green },
  ];

  cards.forEach((c, i) => {
    const x = 0.3 + i * 2.38;
    s.addShape(pres.shapes.RECTANGLE, {
      x, y: 1.05, w: 2.2, h: 1.7,
      fill: { color: c.col }, line: { color: c.col },
      shadow: makeShadow()
    });
    s.addText(c.value, {
      x, y: 1.1, w: 2.2, h: 0.85,
      fontSize: 36, color: C.white, bold: true,
      align: "center", valign: "middle", margin: 0
    });
    s.addText(c.label, {
      x, y: 1.95, w: 2.2, h: 0.35,
      fontSize: 11, color: C.white, bold: true,
      align: "center", margin: 0
    });
    s.addText(c.sub, {
      x, y: 2.3, w: 2.2, h: 0.3,
      fontSize: 9, color: C.ice,
      align: "center", margin: 0
    });
  });

  // Problem statement
  s.addText("Problem Statement", {
    x: 0.5, y: 3.05, w: 9, h: 0.35,
    fontSize: 14, color: C.navy, bold: true, margin: 0
  });
  s.addText([
    { text: "Every category simultaneously shows 33% low-stock and 37% overstock — indicating the problem is ", options: { breakLine: false } },
    { text: "the replenishment model itself", options: { bold: true, breakLine: false } },
    { text: ", not a category-specific issue. Promotions run on 50% of days yet deliver zero incremental demand.", options: { breakLine: false } }
  ], {
    x: 0.5, y: 3.45, w: 9, h: 0.8,
    fontSize: 13, color: "363636", margin: 0
  });

  // 5 user stories list
  s.addText("User Stories Analysed", {
    x: 0.5, y: 4.35, w: 9, h: 0.3,
    fontSize: 12, color: C.navy, bold: true, margin: 0
  });
  s.addText([
    { text: "US-01 Low Stock Risk  ", options: { bold: true, color: C.navy } },
    { text: "·  ", options: { color: C.muted } },
    { text: "US-02 Forecast Accuracy  ", options: { bold: true, color: C.navy } },
    { text: "·  ", options: { color: C.muted } },
    { text: "US-03 Promo Impact  ", options: { bold: true, color: C.navy } },
    { text: "·  ", options: { color: C.muted } },
    { text: "US-04 Price Gap  ", options: { bold: true, color: C.navy } },
    { text: "·  ", options: { color: C.muted } },
    { text: "US-05 Stock Summary", options: { bold: true, color: C.navy } },
  ], {
    x: 0.5, y: 4.7, w: 9, h: 0.4,
    fontSize: 11, margin: 0
  });
}

// ════════════════════════════════════════════════════
//  SLIDE 3 — US-01 LOW STOCK RISK
// ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.white };

  // Left panel
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 3.8, h: 5.625,
    fill: { color: C.navy }, line: { color: C.navy }
  });
  s.addText("US-01", {
    x: 0.2, y: 0.3, w: 3.4, h: 0.5,
    fontSize: 11, color: C.accent, bold: true,
    charSpacing: 3, margin: 0
  });
  s.addText("Low Stock\nRisk Flag", {
    x: 0.2, y: 0.8, w: 3.4, h: 1.4,
    fontSize: 30, color: C.white, bold: true,
    fontFace: "Calibri", margin: 0
  });
  s.addText("Persona: Store Operations Manager", {
    x: 0.2, y: 2.3, w: 3.4, h: 0.35,
    fontSize: 10, color: C.ice, bold: true, margin: 0
  });
  s.addText("Flag every row where\nInventory Level < Units Sold × 1.5\nso replenishment can be prioritised\nbefore stock runs out.", {
    x: 0.2, y: 2.7, w: 3.4, h: 1.2,
    fontSize: 11, color: C.ice, margin: 0
  });

  // Rule box
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.2, y: 4.0, w: 3.3, h: 0.7,
    fill: { color: C.accent, transparency: 80 },
    line: { color: C.accent }
  });
  s.addText("Rule: Inventory Level < Units Sold × 1.5", {
    x: 0.25, y: 4.05, w: 3.2, h: 0.6,
    fontSize: 10, color: C.white, bold: true,
    align: "center", valign: "middle", margin: 0
  });

  // Right panel — chart
  s.addText("Low Stock Count by Category", {
    x: 4.1, y: 0.3, w: 5.6, h: 0.4,
    fontSize: 16, color: C.navy, bold: true, margin: 0
  });

  s.addChart(pres.charts.BAR, [{
    name: "Low Stock Count",
    labels: ["Electronics", "Clothing", "Furniture", "Groceries", "Toys"],
    values: [4820, 4780, 4810, 4795, 4805]
  }], {
    x: 3.9, y: 0.75, w: 5.8, h: 3.5,
    barDir: "col",
    chartColors: ["E74C3C"],
    chartArea: { fill: { color: "FFFFFF" }, roundedCorners: false },
    catAxisLabelColor: "64748B",
    valAxisLabelColor: "64748B",
    valGridLine: { color: "E2E8F0", size: 0.5 },
    catGridLine: { style: "none" },
    showValue: true,
    dataLabelColor: "1E293B",
    showLegend: false,
  });

  s.addText("✓ All 5 categories equally affected — systemic replenishment issue, not category-specific", {
    x: 3.9, y: 4.4, w: 5.8, h: 0.6,
    fontSize: 10, color: C.green, bold: true,
    italic: true, margin: 0
  });
}

// ════════════════════════════════════════════════════
//  SLIDE 4 — US-02 FORECAST ACCURACY
// ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.white };

  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 3.8, h: 5.625,
    fill: { color: C.dark }, line: { color: C.dark }
  });
  s.addText("US-02", {
    x: 0.2, y: 0.3, w: 3.4, h: 0.5,
    fontSize: 11, color: C.accent, bold: true,
    charSpacing: 3, margin: 0
  });
  s.addText("Forecast\nAccuracy", {
    x: 0.2, y: 0.8, w: 3.4, h: 1.4,
    fontSize: 30, color: C.white, bold: true, margin: 0
  });
  s.addText("Persona: Supply Chain Planner", {
    x: 0.2, y: 2.3, w: 3.4, h: 0.35,
    fontSize: 10, color: C.ice, bold: true, margin: 0
  });
  s.addText("Compare forecast vs actual sales\nby season and category to find\nwhere the model consistently\nover- or under-predicts.", {
    x: 0.2, y: 2.7, w: 3.4, h: 1.2,
    fontSize: 11, color: C.ice, margin: 0
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.2, y: 4.0, w: 3.3, h: 0.7,
    fill: { color: C.red, transparency: 60 },
    line: { color: C.red }
  });
  s.addText("⚠ Negative forecasts excluded\n(data quality flag)", {
    x: 0.25, y: 4.05, w: 3.2, h: 0.6,
    fontSize: 10, color: C.white, bold: true,
    align: "center", valign: "middle", margin: 0
  });

  s.addText("Mean Absolute Error by Season", {
    x: 4.1, y: 0.3, w: 5.6, h: 0.4,
    fontSize: 16, color: C.navy, bold: true, margin: 0
  });

  s.addChart(pres.charts.BAR, [{
    name: "MAE",
    labels: ["Spring", "Summer", "Autumn", "Winter"],
    values: [8.32, 8.38, 8.40, 8.35]
  }], {
    x: 3.9, y: 0.75, w: 5.8, h: 3.5,
    barDir: "col",
    chartColors: ["1C7293"],
    chartArea: { fill: { color: "FFFFFF" } },
    catAxisLabelColor: "64748B",
    valAxisLabelColor: "64748B",
    valGridLine: { color: "E2E8F0", size: 0.5 },
    catGridLine: { style: "none" },
    showValue: true,
    dataLabelColor: "1E293B",
    showLegend: false,
    valAxisMinVal: 8.0,
    valAxisMaxVal: 8.6,
  });

  s.addText("Finding: MAE barely moves across seasons (8.32–8.40) — no seasonal weighting in the forecast model", {
    x: 3.9, y: 4.35, w: 5.8, h: 0.6,
    fontSize: 10, color: C.amber, bold: true,
    italic: true, margin: 0
  });
}

// ════════════════════════════════════════════════════
//  SLIDE 5 — US-03 PROMOTION IMPACT
// ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.white };

  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 3.8, h: 5.625,
    fill: { color: C.navy }, line: { color: C.navy }
  });
  s.addText("US-03", {
    x: 0.2, y: 0.3, w: 3.4, h: 0.5,
    fontSize: 11, color: C.accent, bold: true,
    charSpacing: 3, margin: 0
  });
  s.addText("Promotion\nImpact", {
    x: 0.2, y: 0.8, w: 3.4, h: 1.4,
    fontSize: 30, color: C.white, bold: true, margin: 0
  });
  s.addText("Persona: Category Manager", {
    x: 0.2, y: 2.3, w: 3.4, h: 0.35,
    fontSize: 10, color: C.ice, bold: true, margin: 0
  });
  s.addText("Compare inventory levels and\nunits sold on promotion vs\nnormal days — by category.", {
    x: 0.2, y: 2.7, w: 3.4, h: 1.0,
    fontSize: 11, color: C.ice, margin: 0
  });

  // Big stat
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.2, y: 3.8, w: 3.3, h: 1.4,
    fill: { color: C.red, transparency: 20 },
    line: { color: C.red }
  });
  s.addText("137.8 vs 137.6", {
    x: 0.2, y: 3.85, w: 3.3, h: 0.6,
    fontSize: 18, color: C.white, bold: true,
    align: "center", margin: 0
  });
  s.addText("Normal vs Promo units sold\n— virtually identical", {
    x: 0.2, y: 4.45, w: 3.3, h: 0.6,
    fontSize: 10, color: C.white,
    align: "center", margin: 0
  });

  s.addText("Avg Units Sold — Promo vs Normal Days", {
    x: 4.1, y: 0.3, w: 5.6, h: 0.4,
    fontSize: 16, color: C.navy, bold: true, margin: 0
  });

  s.addChart(pres.charts.BAR, [{
    name: "Normal Day",
    labels: ["Electronics", "Clothing", "Furniture", "Groceries", "Toys"],
    values: [138.1, 137.5, 137.9, 138.2, 137.3]
  }, {
    name: "Promotion Day",
    labels: ["Electronics", "Clothing", "Furniture", "Groceries", "Toys"],
    values: [137.8, 137.2, 137.6, 138.0, 137.1]
  }], {
    x: 3.9, y: 0.75, w: 5.8, h: 3.5,
    barDir: "col",
    barGrouping: "clustered",
    chartColors: ["95A5A6", "E74C3C"],
    chartArea: { fill: { color: "FFFFFF" } },
    catAxisLabelColor: "64748B",
    valAxisLabelColor: "64748B",
    valGridLine: { color: "E2E8F0", size: 0.5 },
    catGridLine: { style: "none" },
    showValue: false,
    showLegend: true,
    legendPos: "b",
    valAxisMinVal: 136,
  });

  s.addText("Key question for leadership: Are we spending on promotions that deliver no incremental demand?", {
    x: 3.9, y: 4.35, w: 5.8, h: 0.6,
    fontSize: 10, color: C.red, bold: true,
    italic: true, margin: 0
  });
}

// ════════════════════════════════════════════════════
//  SLIDE 6 — US-04 & US-05 COMBINED
// ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.white };

  s.addText("US-04 & US-05 — Price Gap & Stock Summary", {
    x: 0.4, y: 0.2, w: 9.2, h: 0.5,
    fontSize: 22, color: C.navy, bold: true, margin: 0
  });

  // US-04 left
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.3, y: 0.85, w: 4.4, h: 3.8,
    fill: { color: C.card }, line: { color: "D0D8F0" },
    shadow: makeShadow()
  });
  s.addText("US-04 · Price Gap Analysis", {
    x: 0.5, y: 0.95, w: 4.0, h: 0.35,
    fontSize: 12, color: C.navy, bold: true, margin: 0
  });
  s.addText("Persona: Pricing Analyst", {
    x: 0.5, y: 1.3, w: 4.0, h: 0.25,
    fontSize: 9, color: C.muted, italic: true, margin: 0
  });
  s.addChart(pres.charts.BAR, [{
    name: "Avg Price Gap %",
    labels: ["Electronics", "Clothing", "Furniture", "Groceries", "Toys"],
    values: [-8.2, -12.1, -6.5, -18.3, -9.7]
  }], {
    x: 0.3, y: 1.6, w: 4.4, h: 2.5,
    barDir: "col",
    chartColors: ["27AE60"],
    chartArea: { fill: { color: "F4F7FF" } },
    catAxisLabelColor: "64748B",
    valAxisLabelColor: "64748B",
    valGridLine: { color: "E2E8F0", size: 0.5 },
    catGridLine: { style: "none" },
    showValue: true,
    dataLabelColor: "1E293B",
    showLegend: false,
  });
  s.addText("⚠ Groceries at −18.3% — exceeds the 15% underpriced threshold", {
    x: 0.4, y: 4.25, w: 4.2, h: 0.35,
    fontSize: 9, color: C.red, bold: true, margin: 0
  });

  // US-05 right
  s.addShape(pres.shapes.RECTANGLE, {
    x: 5.2, y: 0.85, w: 4.4, h: 3.8,
    fill: { color: C.card }, line: { color: "D0D8F0" },
    shadow: makeShadow()
  });
  s.addText("US-05 · Stock Summary by Store", {
    x: 5.4, y: 0.95, w: 4.0, h: 0.35,
    fontSize: 12, color: C.navy, bold: true, margin: 0
  });
  s.addText("Persona: Operations Director", {
    x: 5.4, y: 1.3, w: 4.0, h: 0.25,
    fontSize: 9, color: C.muted, italic: true, margin: 0
  });
  s.addChart(pres.charts.BAR, [{
    name: "Overstock %",
    labels: ["Store 1", "Store 2", "Store 3", "Store 4", "Store 5"],
    values: [38.2, 37.5, 38.0, 37.8, 37.7]
  }, {
    name: "Low Stock %",
    labels: ["Store 1", "Store 2", "Store 3", "Store 4", "Store 5"],
    values: [33.1, 32.8, 33.3, 32.9, 33.0]
  }], {
    x: 5.2, y: 1.6, w: 4.4, h: 2.5,
    barDir: "col",
    barGrouping: "clustered",
    chartColors: ["F39C12", "E74C3C"],
    chartArea: { fill: { color: "F4F7FF" } },
    catAxisLabelColor: "64748B",
    valAxisLabelColor: "64748B",
    valGridLine: { color: "E2E8F0", size: 0.5 },
    catGridLine: { style: "none" },
    showValue: false,
    showLegend: true,
    legendPos: "b",
    valAxisMinVal: 30,
  });
  s.addText("Finding: Consistent across all 5 stores — redistribution alone won't solve the issue", {
    x: 5.3, y: 4.25, w: 4.2, h: 0.35,
    fontSize: 9, color: C.amber, bold: true, margin: 0
  });
}

// ════════════════════════════════════════════════════
//  SLIDE 7 — RECOMMENDATIONS
// ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  s.addText("Recommendations", {
    x: 0.5, y: 0.25, w: 9, h: 0.55,
    fontSize: 28, color: C.white, bold: true, margin: 0
  });
  s.addText("Four actions for leadership to consider", {
    x: 0.5, y: 0.8, w: 9, h: 0.3,
    fontSize: 12, color: C.ice, margin: 0
  });

  const recs = [
    {
      num: "01", title: "Fix the Replenishment Model",
      body: "33% low-stock and 37% overstock across all categories points to a broken reorder formula. Define dynamic reorder points using Inventory Level vs Units Sold × 1.5.",
      col: C.accent
    },
    {
      num: "02", title: "Introduce Seasonal Weighting",
      body: "MAE is flat at 8.32–8.40 across all seasons — no seasonal adjustment exists. Prioritise Furniture (Autumn) and Toys (Winter) for model recalibration.",
      col: C.green
    },
    {
      num: "03", title: "Review Promotion ROI",
      body: "Promotions run 50% of all days but deliver zero incremental demand (137.6 vs 137.8 units). Conduct a full spend audit before the next promotional cycle.",
      col: C.amber
    },
    {
      num: "04", title: "Address Grocery Underpricing",
      body: "Groceries average −18.3% below competitor price — exceeding the 15% threshold. Immediate pricing review recommended to recover margin.",
      col: C.red
    },
  ];

  recs.forEach((r, i) => {
    const x = 0.3 + (i % 2) * 4.9;
    const y = 1.3 + Math.floor(i / 2) * 2.05;

    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w: 4.5, h: 1.85,
      fill: { color: "1A2E6B" }, line: { color: r.col }
    });
    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w: 0.55, h: 1.85,
      fill: { color: r.col }, line: { color: r.col }
    });
    s.addText(r.num, {
      x, y: y + 0.6, w: 0.55, h: 0.6,
      fontSize: 16, color: C.navy, bold: true,
      align: "center", margin: 0
    });
    s.addText(r.title, {
      x: x + 0.65, y: y + 0.1, w: 3.75, h: 0.4,
      fontSize: 12, color: C.white, bold: true, margin: 0
    });
    s.addText(r.body, {
      x: x + 0.65, y: y + 0.52, w: 3.75, h: 1.2,
      fontSize: 9.5, color: C.ice, margin: 0
    });
  });
}

// ════════════════════════════════════════════════════
//  SLIDE 8 — CLOSING
// ════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.dark };

  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.15,
    fill: { color: C.accent }, line: { color: C.accent }
  });

  s.addText("Thank You", {
    x: 0.5, y: 0.6, w: 9, h: 1.0,
    fontSize: 52, color: C.white, bold: true,
    align: "center", margin: 0
  });
  s.addText("BA Portfolio Project — Retail Stock-Out Reduction", {
    x: 0.5, y: 1.7, w: 9, h: 0.4,
    fontSize: 14, color: C.ice,
    align: "center", margin: 0
  });

  // Deliverables summary
  const items = [
    "Data Dictionary — 15 columns defined",
    "5 User Stories — with acceptance criteria",
    "Business Requirements Document — 9 sections",
    "Phase 3 Python Analysis — all 5 user stories",
    "Phase 4 Deck + HTML Dashboard",
  ];
  items.forEach((item, i) => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: 2.0, y: 2.35 + i * 0.52, w: 0.28, h: 0.28,
      fill: { color: C.accent }, line: { color: C.accent }
    });
    s.addText(item, {
      x: 2.45, y: 2.33 + i * 0.52, w: 6, h: 0.32,
      fontSize: 12, color: C.white, margin: 0
    });
  });

  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 5.3, w: 10, h: 0.325,
    fill: { color: C.navy }, line: { color: C.navy }
  });
  s.addText("github.com/BanothDeepak/retail-stockout-ba-project", {
    x: 0, y: 5.32, w: 10, h: 0.3,
    fontSize: 10, color: C.muted,
    align: "center", margin: 0
  });
}

// ── WRITE FILE ────────────────────────────────────
pres.writeFile({ fileName: "Phase4_RetailStockOut_Deck.pptx" })
  .then(() => console.log("✅ Phase4_RetailStockOut_Deck.pptx saved!"))
  .catch(err => console.error("❌ Error:", err));
