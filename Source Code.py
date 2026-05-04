# ═══════════════════════════════════════════════════════
#  PHASE 3 ANALYSIS — RETAIL STOCK-OUT REDUCTION
#  Covers: US-01, US-02, US-03, US-04, US-05
#  VS Code / Local Environment Ready
# ═══════════════════════════════════════════════════════

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── CONFIG — update this path to your CSV location ───
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
CSV_PATH   = os.path.join(BASE_DIR, "retail_store_inventory.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── LOAD CSV ─────────────────────────────────────────
print("="*55)
print("Loading data...")

if not os.path.exists(CSV_PATH):
    print(f"\n❌ CSV not found at: {CSV_PATH}")
    print("Make sure retail_store_inventory.csv is in the same folder as this script")
    exit()

df = pd.read_csv(CSV_PATH)
df.columns = df.columns.str.strip()
print(f"✓ Loaded {len(df):,} rows and {len(df.columns)} columns")
print(f"  Columns: {df.columns.tolist()}\n")

# ── CLEAN & PREPARE DATA ─────────────────────────────
df['Date']               = pd.to_datetime(df['Date'], errors='coerce')
df['Inventory Level']    = pd.to_numeric(df['Inventory Level'],    errors='coerce')
df['Units Sold']         = pd.to_numeric(df['Units Sold'],         errors='coerce')
df['Demand Forecast']    = pd.to_numeric(df['Demand Forecast'],    errors='coerce')
df['Price']              = pd.to_numeric(df['Price'],              errors='coerce')
df['Competitor Pricing'] = pd.to_numeric(df['Competitor Pricing'], errors='coerce')
df['Holiday/Promotion']  = pd.to_numeric(df['Holiday/Promotion'],  errors='coerce')

print("✓ Data cleaned and ready\n")


# ════════════════════════════════════════════════════
#  US-01 — LOW STOCK RISK FLAG
#  Flag: Inventory Level < Units Sold × 1.5
# ════════════════════════════════════════════════════
print("="*55)
print("US-01: Low Stock Risk by Product, Store & Category")
print("="*55)

df['Low_Stock_Flag'] = df['Inventory Level'] < (df['Units Sold'] * 1.5)
df['Risk_Flag'] = df['Low_Stock_Flag'].map({True: 'Low Stock Risk', False: 'OK'})

us01 = df[['Store ID', 'Product ID', 'Category',
           'Inventory Level', 'Units Sold', 'Risk_Flag']].copy()
us01.to_csv(f"{OUTPUT_DIR}/US01_low_stock_risk.csv", index=False)

us01_summary = us01[us01['Risk_Flag'] == 'Low Stock Risk'] \
    .groupby('Category').size().reset_index(name='Low Stock Count')

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(us01_summary['Category'], us01_summary['Low Stock Count'], color='#e74c3c')
ax.set_title('US-01: Low Stock Risk Count by Category\n(Inventory Level < Units Sold × 1.5)',
             fontsize=13, fontweight='bold')
ax.set_xlabel('Category')
ax.set_ylabel('Number of Low Stock Records')
plt.xticks(rotation=45, ha='right')
for i, v in enumerate(us01_summary['Low Stock Count']):
    ax.text(i, v + 10, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/US01_low_stock_risk.png", dpi=150)
plt.show()

total_low = df['Low_Stock_Flag'].sum()
print(f"✓ Total low stock rows flagged: {total_low:,} ({total_low/len(df)*100:.1f}%)")
print(f"✓ US-01 saved\n")


# ════════════════════════════════════════════════════
#  US-02 — FORECAST ACCURACY BY SEASON & CATEGORY
#  Exclude negative Demand Forecast values
# ════════════════════════════════════════════════════
print("="*55)
print("US-02: Forecast Accuracy by Seasonality & Category")
print("="*55)

negative_forecasts = df[df['Demand Forecast'] < 0]
print(f"⚠️  Data quality flag: {len(negative_forecasts):,} rows with negative Demand Forecast excluded")

df_clean = df[df['Demand Forecast'] >= 0].copy()
df_clean['Forecast_Error'] = abs(df_clean['Demand Forecast'] - df_clean['Units Sold'])

us02 = df_clean.groupby(['Seasonality', 'Category'])['Forecast_Error'].mean().reset_index()
us02.columns = ['Seasonality', 'Category', 'Avg Forecast Error (MAE)']
us02.to_csv(f"{OUTPUT_DIR}/US02_forecast_accuracy.csv", index=False)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

season_mae = df_clean.groupby('Seasonality')['Forecast_Error'].mean().reset_index()
axes[0].bar(season_mae['Seasonality'], season_mae['Forecast_Error'], color='#3498db')
axes[0].set_title('US-02: Avg Forecast Error by Seasonality', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Seasonality')
axes[0].set_ylabel('Mean Absolute Error (MAE)')
for i, v in enumerate(season_mae['Forecast_Error']):
    axes[0].text(i, v + 0.05, f"{v:.2f}", ha='center', fontweight='bold')
plt.setp(axes[0].xaxis.get_majorticklabels(), rotation=45, ha='right')

pivot2 = us02.pivot(index='Category', columns='Seasonality',
                    values='Avg Forecast Error (MAE)').fillna(0)
pivot2.plot(kind='bar', ax=axes[1], colormap='Set2')
axes[1].set_title('US-02: Forecast Error by Category & Seasonality', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('MAE')
axes[1].legend(title='Seasonality', bbox_to_anchor=(1.05, 1))
plt.setp(axes[1].xaxis.get_majorticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/US02_forecast_accuracy.png", dpi=150)
plt.show()
print("✓ US-02 complete\n")


# ════════════════════════════════════════════════════
#  US-03 — PROMOTION IMPACT ON INVENTORY & SALES
# ════════════════════════════════════════════════════
print("="*55)
print("US-03: Promotion Impact on Inventory Level & Units Sold")
print("="*55)

df['Promo_Label'] = df['Holiday/Promotion'].map({1: 'Promotion Day', 0: 'Normal Day'})

us03 = df.groupby(['Category', 'Promo_Label']).agg(
    Avg_Inventory_Level=('Inventory Level', 'mean'),
    Avg_Units_Sold=('Units Sold', 'mean')
).reset_index()
us03.to_csv(f"{OUTPUT_DIR}/US03_promo_impact.csv", index=False)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

pivot3a = us03.pivot(index='Category', columns='Promo_Label',
                     values='Avg_Inventory_Level').fillna(0)
pivot3a.plot(kind='bar', ax=axes[0], color=['#e74c3c', '#95a5a6'])
axes[0].set_title('US-03: Avg Inventory Level\nPromotion vs Normal Days',
                  fontsize=12, fontweight='bold')
axes[0].set_xlabel('Category')
axes[0].set_ylabel('Avg Inventory Level')
axes[0].legend(title='Day Type')
plt.setp(axes[0].xaxis.get_majorticklabels(), rotation=45, ha='right')

pivot3b = us03.pivot(index='Category', columns='Promo_Label',
                     values='Avg_Units_Sold').fillna(0)
pivot3b.plot(kind='bar', ax=axes[1], color=['#e74c3c', '#95a5a6'])
axes[1].set_title('US-03: Avg Units Sold\nPromotion vs Normal Days',
                  fontsize=12, fontweight='bold')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Avg Units Sold')
axes[1].legend(title='Day Type')
plt.setp(axes[1].xaxis.get_majorticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/US03_promo_impact.png", dpi=150)
plt.show()

if 'Promotion Day' in pivot3a.columns and 'Normal Day' in pivot3a.columns:
    pivot3a['Stock_Drop'] = pivot3a['Normal Day'] - pivot3a['Promotion Day']
    print("📉 Categories with biggest inventory drop on promo days:")
    print(pivot3a[['Stock_Drop']].sort_values('Stock_Drop', ascending=False).to_string())
print("✓ US-03 complete\n")


# ════════════════════════════════════════════════════
#  US-04 — PRICE GAP VS COMPETITOR PRICING
# ════════════════════════════════════════════════════
print("="*55)
print("US-04: Price Gap vs Competitor Pricing by Region & Category")
print("="*55)

df['Price_Gap']      = df['Price'] - df['Competitor Pricing']
df['Price_Gap_%']    = ((df['Price'] - df['Competitor Pricing']) / df['Competitor Pricing']) * 100
df['Underpriced_Flag'] = df['Price_Gap_%'] < -15

us04 = df.groupby(['Region', 'Category']).agg(
    Avg_Price=('Price', 'mean'),
    Avg_Competitor_Price=('Competitor Pricing', 'mean'),
    Avg_Price_Gap=('Price_Gap', 'mean'),
    Avg_Price_Gap_Pct=('Price_Gap_%', 'mean'),
    Underpriced_Rows=('Underpriced_Flag', 'sum')
).reset_index()
us04.to_csv(f"{OUTPUT_DIR}/US04_price_gap_analysis.csv", index=False)

pivot4 = us04.pivot(index='Category', columns='Region',
                    values='Avg_Price_Gap_Pct').fillna(0)

fig, ax = plt.subplots(figsize=(12, 6))
pivot4.plot(kind='bar', ax=ax, colormap='RdYlGn')
ax.axhline(y=-15, color='red', linestyle='--', linewidth=1.5, label='−15% threshold')
ax.set_title('US-04: Avg Price Gap % vs Competitor by Region & Category\n'
             '(Below red line = underpriced by >15%)',
             fontsize=12, fontweight='bold')
ax.set_xlabel('Category')
ax.set_ylabel('Avg Price Gap (%)')
ax.legend(title='Region', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/US04_price_gap.png", dpi=150)
plt.show()

underpriced_total = df['Underpriced_Flag'].sum()
print(f"⚠️  Rows where we are >15% below competitor price: {underpriced_total:,}")
print("✓ US-04 complete\n")


# ════════════════════════════════════════════════════
#  US-05 — OVERSTOCK & LOW STOCK % BY STORE & REGION
# ════════════════════════════════════════════════════
print("="*55)
print("US-05: Overstock & Low Stock % by Store & Region")
print("="*55)

df['Overstock_Flag'] = df['Inventory Level'] > (df['Demand Forecast'] * 2.5)

us05 = df.groupby(['Store ID', 'Region']).agg(
    Total_Rows=('Inventory Level', 'count'),
    Overstock_Count=('Overstock_Flag', 'sum'),
    Low_Stock_Count=('Low_Stock_Flag', 'sum')
).reset_index()

us05['Overstock_%'] = (us05['Overstock_Count'] / us05['Total_Rows'] * 100).round(1)
us05['Low_Stock_%'] = (us05['Low_Stock_Count']  / us05['Total_Rows'] * 100).round(1)
us05.to_csv(f"{OUTPUT_DIR}/US05_overstock_lowstock_summary.csv", index=False)

print("\n📊 Summary Table — % Overstock & Low Stock by Store & Region:")
print(us05[['Store ID', 'Region', 'Overstock_%', 'Low_Stock_%']].to_string(index=False))

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].bar(us05['Store ID'].astype(str), us05['Overstock_%'], color='#f39c12')
axes[0].set_title('US-05: Overstock % by Store\n(Inventory Level > Demand Forecast × 2.5)',
                  fontsize=11, fontweight='bold')
axes[0].set_xlabel('Store ID')
axes[0].set_ylabel('Overstock %')
for i, v in enumerate(us05['Overstock_%']):
    axes[0].text(i, v + 0.3, f"{v}%", ha='center', fontsize=9, fontweight='bold')

axes[1].bar(us05['Store ID'].astype(str), us05['Low_Stock_%'], color='#e74c3c')
axes[1].set_title('US-05: Low Stock % by Store\n(Inventory Level < Units Sold × 1.5)',
                  fontsize=11, fontweight='bold')
axes[1].set_xlabel('Store ID')
axes[1].set_ylabel('Low Stock %')
for i, v in enumerate(us05['Low_Stock_%']):
    axes[1].text(i, v + 0.3, f"{v}%", ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/US05_overstock_lowstock.png", dpi=150)
plt.show()
print("✓ US-05 complete\n")


# ════════════════════════════════════════════════════
#  SAVE COMBINED EXCEL — ALL 5 USER STORIES
# ════════════════════════════════════════════════════
print("="*55)
print("💾 Saving combined Excel file...")

with pd.ExcelWriter(f"{OUTPUT_DIR}/phase3_all_findings.xlsx",
                    engine='openpyxl') as writer:
    us01.to_excel(writer, sheet_name='US01 Low Stock Risk',    index=False)
    us02.to_excel(writer, sheet_name='US02 Forecast Accuracy', index=False)
    us03.to_excel(writer, sheet_name='US03 Promo Impact',      index=False)
    us04.to_excel(writer, sheet_name='US04 Price Gap',         index=False)
    us05.to_excel(writer, sheet_name='US05 Stock Summary',     index=False)

print("✓ Excel saved with 5 sheets")

print("\n✅ ALL DONE — All 5 user stories complete!")
print(f"\nAll files saved to: {OUTPUT_DIR}")
print("  US01_low_stock_risk.csv / .png")
print("  US02_forecast_accuracy.csv / .png")
print("  US03_promo_impact.csv / .png")
print("  US04_price_gap_analysis.csv / .png")
print("  US05_overstock_lowstock_summary.csv / .png")
print("  phase3_all_findings.xlsx (5 sheets)")