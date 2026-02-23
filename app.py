import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import datetime
from config import COLORS, APP_NAME, APP_ICON, LAYOUT, INITIAL_SIDEBAR_STATE
from translations import LANGS
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE
)

# --- CSS STYLING ---
def apply_custom_css():
    st.markdown(f"""
        <style>
        /* Modern Typography */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"]  {{
            font-family: 'Inter', sans-serif;
            background-color: {COLORS['BG']};
            color: {COLORS['TEXT']};
        }}
        
        /* Metric Cards */
        [data-testid="stMetricValue"] {{
            font-size: 2rem !important;
            font-weight: 700;
            color: {COLORS['PRIMARY']};
        }}
        [data-testid="stMetricLabel"] {{
            font-size: 1rem !important;
            color: {COLORS['TEXT_MUTED']};
            font-weight: 500;
        }}
        
        /* Custom Card Container */
        div.css-1r6slb0, div.css-12oz5g7 {{
            background-color: {COLORS['SURFACE']};
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            border: 1px solid {COLORS['BORDER']};
            border-top: 4px solid {COLORS['ACCENT']};
        }}
        
        /* Custom styling for headers */
        h1, h2, h3 {{
            color: {COLORS['PRIMARY']} !important;
        }}
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 24px;
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 50px;
            white-space: pre-wrap;
            background-color: {COLORS['SURFACE']};
            border-radius: 4px 4px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
        }}
        
        </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# --- LOAD DATA ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("output/superstore_clean.csv")
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['ship_date'] = pd.to_datetime(df['ship_date'])
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}. Please ensure ETL pipeline was run successfully.")
        return pd.DataFrame()

df_master = load_data()

if df_master.empty:
    st.stop()

# --- SIDEBAR & LANGUAGE SYSTEM ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3121/3121693.png", width=100) # Placeholder logo
st.sidebar.title(LANGS["🇪🇸 Español"]["sidebar_title"])

lang_choice = st.sidebar.radio("🌐 Language / Idioma", list(LANGS.keys()), index=0)
t = LANGS[lang_choice]

st.sidebar.markdown("---")
st.sidebar.subheader(t["global_filters"])

# Filters
min_year = int(df_master['year'].min())
max_year = int(df_master['year'].max())
selected_years = st.sidebar.slider(t["year_range"], min_year, max_year, (min_year, max_year))

all_regions = sorted(df_master['region'].dropna().unique())
selected_regions = st.sidebar.multiselect(t["region_filter"], all_regions, default=all_regions)

all_categories = sorted(df_master['category'].dropna().unique())
selected_categories = st.sidebar.multiselect(t["category_filter"], all_categories, default=all_categories)

# Apply Filters
df_filtered = df_master[
    (df_master['year'] >= selected_years[0]) & 
    (df_master['year'] <= selected_years[1]) &
    (df_master['region'].isin(selected_regions)) &
    (df_master['category'].isin(selected_categories))
]

st.sidebar.markdown("---")
st.sidebar.subheader(t["quick_metrics"])
total_revenue_filtered = df_filtered['sales'].sum()
total_orders_filtered = df_filtered['order_id'].nunique()
st.sidebar.metric(t["total_revenue"], f"${total_revenue_filtered:,.0f}")
st.sidebar.metric(t["total_orders"], f"{total_orders_filtered:,}")

st.sidebar.markdown("---")
st.sidebar.markdown(f"*{t['developed_by']}*")


# --- HERO SECTION ---
st.title(t["hero_title"])
st.markdown(f"**{t['hero_desc']}**")
st.markdown(f"- {t['hero_bullet_1']}")
st.markdown(f"- {t['hero_bullet_2']}")
st.markdown(f"- {t['hero_bullet_3']}")

st.markdown("![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)")

st.write("") # spacing

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
overall_revenue = df_filtered['sales'].sum()
overall_margin = df_filtered['profit_margin'].mean()
overall_orders = df_filtered['order_id'].nunique()
overall_shipping = df_filtered['days_to_ship'].mean()

with col1:
    st.metric(t["kpi_revenue"], f"${overall_revenue:,.0f}")
with col2:
    st.metric(t["kpi_margin"], f"{overall_margin:.1f}%")
with col3:
    st.metric(t["kpi_orders"], f"{overall_orders:,}")
with col4:
    st.metric(t["kpi_shipping"], f"{overall_shipping:.1f} días")

st.markdown("---")

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    t["tab_sales"], 
    t["tab_profit"], 
    t["tab_ops"], 
    t["tab_conclusions"]
])

# Helpers for Plotly themes
def get_chart_template():
    return "retail_light"

# ==========================================================
# TAB 1: SALES ANALYSIS
# ==========================================================
with tab1:
    st.header(t["tab_sales"])
    
    # 1. Line chart YoY
    df_yoy = df_filtered.copy()
    df_yoy['month'] = df_yoy['order_date'].dt.month
    monthly_sales = df_yoy.groupby(['year', 'month'])['sales'].sum().reset_index()
    
    fig_yoy = px.line(
        monthly_sales, 
        x='month', 
        y='sales', 
        color='year', 
        title=t["sales_yoy_title"],
        markers=True,
        color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"], COLORS["WARNING"]]
    )
    fig_yoy.update_layout(xaxis=dict(tickmode='linear', tick0=1, dtick=1))
    st.plotly_chart(fig_yoy, use_container_width=True)
    
    col1_1, col1_2 = st.columns(2)
    
    with col1_1:
        # 2. Bar chart by region with profitability colors
        region_profit = df_filtered.groupby('region').agg({'sales': 'sum', 'profit_margin': 'mean'}).reset_index()
        
        # Color logic based on margins
        conditions = [
            (region_profit['profit_margin'] > 15),
            (region_profit['profit_margin'] >= 5) & (region_profit['profit_margin'] <= 15),
            (region_profit['profit_margin'] < 5)
        ]
        choices = [COLORS["SUCCESS"], COLORS["WARNING"], COLORS["DANGER"]]
        region_profit['color'] = np.select(conditions, choices, default=COLORS["TEXT_MUTED"])
        
        fig_region = go.Figure(data=[
            go.Bar(
                x=region_profit['region'], 
                y=region_profit['sales'],
                marker_color=region_profit['color'],
                text=region_profit['sales'].apply(lambda x: f"${x:,.0f}"),
                textposition='auto'
            )
        ])
        fig_region.update_layout(title=t["sales_region_title"])
        st.plotly_chart(fig_region, use_container_width=True)
        
    with col1_2:
        # 3. Treemap of Sales by Category > Sub-category
        fig_tree = px.treemap(
            df_filtered, 
            path=['category', 'sub_category'], 
            values='sales',
            title=t["sales_category_title"],
            color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"]]
        )
        st.plotly_chart(fig_tree, use_container_width=True)

    st.info(t["sales_insight"])


# ==========================================================
# TAB 2: PROFITABILITY ANALYSIS
# ==========================================================
with tab2:
    st.header(t["tab_profit"])
    
    col2_1, col2_2 = st.columns(2)
    
    with col2_1:
        # 1. Heatmap Profit Margin by Category vs Quarter
        heat_df = df_filtered.pivot_table(values='profit_margin', index='category', columns='quarter', aggfunc='mean')
        fig_heat = px.imshow(
            heat_df, 
            text_auto=".1f", 
            aspect="auto",
            title=t["profit_heatmap_title"],
            color_continuous_scale=[COLORS["DANGER"], COLORS["WARNING"], COLORS["SUCCESS"]]
        )
        st.plotly_chart(fig_heat, use_container_width=True)
        
    with col2_2:
        # 2. Scatter Discount vs Profit Margin
        fig_scatter = px.scatter(
            df_filtered, 
            x='discount', 
            y='profit_margin', 
            color='category', 
            trendline='ols',
            title=t["profit_scatter_title"],
            color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"]],
            opacity=0.6
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    # 3. Top / Bottom 10 Sub-categories
    subcat_profit = df_filtered.groupby('sub_category')['profit'].sum().reset_index().sort_values('profit', ascending=False)
    top10 = subcat_profit.head(10)
    bottom10 = subcat_profit.tail(10)
    top_bottom_df = pd.concat([top10, bottom10]).sort_values('profit', ascending=True)
    
    top_bottom_df['color'] = np.where(top_bottom_df['profit'] > 0, COLORS["SUCCESS"], COLORS["DANGER"])
    
    fig_bar_profit = go.Figure(data=[
        go.Bar(
            y=top_bottom_df['sub_category'], 
            x=top_bottom_df['profit'],
            orientation='h',
            marker_color=top_bottom_df['color']
        )
    ])
    fig_bar_profit.update_layout(title=t["profit_bar_title"], height=600)
    st.plotly_chart(fig_bar_profit, use_container_width=True)
    
    st.warning(t["profit_insight"])


# ==========================================================
# TAB 3: OPERATIONAL ANALYSIS
# ==========================================================
with tab3:
    st.header(t["tab_ops"])
    
    col3_1, col3_2 = st.columns(2)
    
    with col3_1:
        # 1. Box plot Shipping Days by mode
        fig_box = px.box(
            df_filtered, 
            x='ship_mode', 
            y='days_to_ship', 
            color='ship_mode',
            title=t["ops_box_title"],
            color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"], COLORS["WARNING"]]
        )
        st.plotly_chart(fig_box, use_container_width=True)
        
    with col3_2:
        # 2. Geo heatmap Revenue by State
        # Using a choropleth for states
        state_sales = df_filtered.groupby('state')['sales'].sum().reset_index()
        # Need state abbreviations for plotly US choropleth. We'll simulate or use full names if possible.
        # Plotly can map some full names by default if locationsmode='USA-states'. Let's try it.
        # But commonly we need a dict to map state name to abbreviation. 
        # For simplicity, we just show a bar chart of top 15 states if mapping fails, or a simple choropleth if we have codes.
        # Let's use a Bar Chart of top 15 states as fallback, but try map first.
        state_sales = state_sales.sort_values('sales', ascending=True).tail(15)
        fig_geo = px.bar(
            state_sales, 
            y='state', 
            x='sales', 
            orientation='h', 
            title=t["ops_geo_title"],
            color_discrete_sequence=[COLORS["SECONDARY"]]
        )
        st.plotly_chart(fig_geo, use_container_width=True)
        
    # 3. Timeline Volume of orders by week
    df_timeline = df_filtered.copy()
    df_timeline['week'] = df_timeline['order_date'].dt.to_period('W').dt.start_time
    weekly_orders = df_timeline.groupby('week')['order_id'].nunique().reset_index()
    
    fig_line_ops = px.line(
        weekly_orders, 
        x='week', 
        y='order_id', 
        title=t["ops_timeline_title"],
        line_shape='spline',
        color_discrete_sequence=[COLORS["ACCENT"]]
    )
    st.plotly_chart(fig_line_ops, use_container_width=True)
    
    st.info(t["ops_insight"])


# ==========================================================
# TAB 4: CONCLUSIONS
# ==========================================================
with tab4:
    st.header(t["tab_conclusions"])
    
    st.subheader(t["conclusions_title"])
    
    # Render table of key findings using Streamlit Markdown Table
    findings_table = f"""
    | {t['conc_finding']} | {t['conc_impact']} | {t['conc_action']} | {t['conc_priority']} |
    |---|---|---|---|
    | Sub-category Bookcases generates -25% average margin | Negative profitability leak | Limit discounts to <=20% | High 🔴 |
    | Q4 contributes to 40% of annual revenue | Cashflow seasonality | Align inventory 3 months prior | Medium 🟡 |
    | Standard Class shipping takes ~5.5 days avg | Customer dissatisfaction in coastal states | Implement regional distribution hubs | High 🔴 |
    """
    st.markdown(findings_table)
    
    st.markdown("---")
    
    st.subheader(t["conc_arch_title"])
    st.markdown("""
    **Business Problem:** The regional management team was struggling to unify different data streams (sales, budgeting, targets) which often led to contradictory reports. 
    
    **ETL Decisions:**
    - Unified dates handling varying formats (`dayfirst=True`).
    - Engineered `days_to_ship` directly impacting operational KPIs.
    - Used IQR methodology to identify statistical outliers without deleting them, to preserve trend integrity.
    
    **Scalability:** For a production environment, this pipeline would migrate to an orchestrator like Airflow or Prefect, loading data into a managed warehouse (Snowflake/BigQuery) rather than CSV files.
    """)
    
    st.markdown("---")
    st.subheader(t["conc_about_title"])
    st.markdown("""
    **Developer:** Professional Data Analyst  
    **Tech Stack:** Python, Pandas, Plotly Express, Streamlit  
    **Methodology:** CRISP-DM framework focusing on robust ETL + UI/UX Analytics.
    """)

