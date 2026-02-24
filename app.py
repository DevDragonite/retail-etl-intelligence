import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from config import COLORS, APP_NAME, APP_ICON, LAYOUT, INITIAL_SIDEBAR_STATE
from translations import LANGS

# --- PAGE CONFIG ---
st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE
)

# --- INITIALIZE SESSION STATE ---
if "lang" not in st.session_state:
    st.session_state.lang = "🇪🇸 Español"

if "page" not in st.session_state:
    st.session_state.page = "Bienvenida"

# --- CSS STYLING (LIQUID GLASS MINIMALISTA) ---
def apply_custom_css():
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* App Background - subtle gradient for glassmorphism */
        .stApp {{
            background: linear-gradient(135deg, #f6f8fb 0%, #e5ebf4 100%);
            font-family: 'Inter', sans-serif;
        }}
        
        /* Typography */
        html, body, [class*="css"] {{
            color: {COLORS['TEXT']};
            font-family: 'Inter', sans-serif;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {COLORS['PRIMARY']} !important;
            font-weight: 600;
        }}
        
        /* Liquid Glass Containers for Metrics and general containers */
        [data-testid="stMetric"], .st-emotion-cache-12oz5g7, .st-emotion-cache-1r6slb0, .css-1r6slb0 {{
            background: rgba(255, 255, 255, 0.55) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border-radius: 16px !important;
            border: 1px solid rgba(255, 255, 255, 0.8) !important;
            box-shadow: 0 4px 20px rgba(31, 38, 135, 0.05) !important;
            padding: 1.2rem 1.5rem !important;
            transition: all 0.3s ease;
        }}
        
        [data-testid="stMetric"]:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(31, 38, 135, 0.08) !important;
        }}
        
        /* Metric Typography */
        [data-testid="stMetricValue"] {{
            font-size: 2.2rem !important;
            font-weight: 700 !important;
            background: -webkit-linear-gradient(45deg, {COLORS['PRIMARY']}, {COLORS['SECONDARY']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        [data-testid="stMetricLabel"] {{
            font-size: 1rem !important;
            color: #666 !important;
            font-weight: 500 !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        /* Tabs styling - Pill shape */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 10px;
            background: rgba(255, 255, 255, 0.3);
            padding: 5px;
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.5);
            margin-bottom: 1rem;
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 40px;
            background: transparent;
            border-radius: 10px;
            padding: 8px 20px;
            font-weight: 500;
            color: #555;
            border: none !important;
        }}
        .stTabs [aria-selected="true"] {{
            background: rgba(255, 255, 255, 0.9) !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
            color: {COLORS['PRIMARY']} !important;
            font-weight: 600;
        }}
        .stTabs [data-baseweb="tab-highlight"] {{
            display: none;
        }}
        
        /* Welcome Storytelling elements */
        .welcome-card {{
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(16px);
            border-radius: 20px;
            padding: 3rem;
            border: 1px solid rgba(255, 255, 255, 0.9);
            box-shadow: 0 10px 40px rgba(0,0,0,0.03);
            margin-bottom: 2rem;
        }}
        .welcome-pillar {{
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid rgba(255, 255, 255, 0.7);
            box-shadow: 0 4px 15px rgba(0,0,0,0.02);
            border-left: 4px solid {COLORS['ACCENT']};
            transition: transform 0.2s ease;
        }}
        .welcome-pillar:hover {{
            transform: translateX(5px);
            background: rgba(255, 255, 255, 0.6);
        }}
        
        .stButton>button {{
            border-radius: 12px;
            font-weight: 600;
        }}
        
        hr {{
            border-top: 1px solid rgba(0, 0, 0, 0.05);
            margin: 2rem 0;
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

us_state_to_abbrev = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
    "District of Columbia": "DC"
}


# --- HEADER & LANGUAGE HAMBURGER MENU ---
col_logo, col_space, col_lang = st.columns([1, 6, 1])
with col_lang:
    # We use a popover for the hamburger menu look "inside the dashboard"
    with st.popover("🌐 Idioma"):
        for lang_option in LANGS.keys():
            if st.button(lang_option, use_container_width=True):
                st.session_state.lang = lang_option
                st.rerun()

t = LANGS[st.session_state.lang]

# --- SIDEBAR NAVIGATION & FILTERS ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3121/3121693.png", width=80) 
st.sidebar.markdown(f"### {t['sidebar_title']}")

# Navigation
st.session_state.page = st.sidebar.radio("Navegación", [t["nav_welcome"], t["nav_dashboard"]], index=0 if st.session_state.page == "Bienvenida" or st.session_state.page == t["nav_welcome"] else 1)
is_dashboard = st.session_state.page == t["nav_dashboard"]

# Filters only applied if in Dashboard
df_filtered = df_master.copy()

if is_dashboard:
    st.sidebar.markdown("---")
    st.sidebar.subheader(t["global_filters"])

    # Year Filters (Reverted from exact dates)
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

    # Download Data Button
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.sidebar.markdown("---")
    st.sidebar.download_button(
       label=t["download_data"],
       data=csv,
       file_name='retail_data_filtered.csv',
       mime='text/csv',
    )


st.sidebar.markdown("---")
st.sidebar.markdown(f"*{t['developed_by']}*")

# ==========================================================
# PAGE CONTENT RENDERING
# ==========================================================

if st.session_state.page == t["nav_welcome"]:
    # ---------------- STORYTELLING WELCOME SECTION ----------------
    st.markdown(f"""
    <div class="welcome-card">
        <h1 style="font-size: 3rem; margin-bottom: 0.5rem; text-align: center;">{t["hero_title"]}</h1>
        <p style="text-align: center; font-size: 1.2rem; color: #555; margin-bottom: 2rem;">
            <em>{t['welcome_title']}</em>
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8;">{t['welcome_story_1']}</p>
        <p style="font-size: 1.1rem; line-height: 1.8;">{t['welcome_story_2']}</p>
        
        <div class="welcome-pillar">
            <h4>{t['welcome_pillar_1_title']}</h4>
            <p style="margin:0; color:#444;">{t['welcome_pillar_1_desc']}</p>
        </div>
        <div class="welcome-pillar">
            <h4>{t['welcome_pillar_2_title']}</h4>
            <p style="margin:0; color:#444;">{t['welcome_pillar_2_desc']}</p>
        </div>
        <div class="welcome-pillar">
            <h4>{t['welcome_pillar_3_title']}</h4>
            <p style="margin:0; color:#444;">{t['welcome_pillar_3_desc']}</p>
        </div>
        
        <br>
        <div style="text-align: center;">
            <p style="font-weight: 600; font-size: 1.1rem;">{t['welcome_cta']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center;'><img src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white'> <img src='https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white'> <img src='https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white'> <img src='https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white'></p>", unsafe_allow_html=True)


elif st.session_state.page == t["nav_dashboard"]:
    # ---------------- MAIN DASHBOARD SECTION ----------------
    st.title("📊 Dashboard")
    st.write("")
    
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

    # Functions for Tabs
    def render_tab_sales(df_filtered, t):
        st.subheader(t["tab_sales"])
        df_yoy = df_filtered.copy()
        df_yoy['month'] = df_yoy['order_date'].dt.month
        monthly_sales = df_yoy.groupby(['year', 'month'])['sales'].sum().reset_index()
        
        fig_yoy = px.line(
            monthly_sales, x='month', y='sales', color='year', 
            title=t["sales_yoy_title"], markers=True,
            color_discrete_sequence=[COLORS["PRIMARY"], "rgba(31, 38, 135, 0.4)", COLORS["ACCENT"], COLORS["WARNING"]]
        )
        fig_yoy.update_layout(xaxis=dict(tickmode='linear', tick0=1, dtick=1), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_yoy, use_container_width=True)
        
        col1_1, col1_2 = st.columns(2)
        with col1_1:
            region_profit = df_filtered.groupby('region').agg({'sales': 'sum', 'profit_margin': 'mean'}).reset_index()
            conditions = [
                (region_profit['profit_margin'] > 15),
                (region_profit['profit_margin'] >= 5) & (region_profit['profit_margin'] <= 15),
                (region_profit['profit_margin'] < 5)
            ]
            choices = [COLORS["SUCCESS"], COLORS["WARNING"], COLORS["DANGER"]]
            region_profit['color'] = np.select(conditions, choices, default=COLORS["TEXT_MUTED"])
            
            fig_region = go.Figure(data=[go.Bar(
                x=region_profit['region'], y=region_profit['sales'], marker_color=region_profit['color'],
                text=region_profit['sales'].apply(lambda x: f"${x:,.0f}"), textposition='auto'
            )])
            fig_region.update_layout(title=t["sales_region_title"], plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_region, use_container_width=True)
            
        with col1_2:
            fig_tree = px.treemap(
                df_filtered, path=['category', 'sub_category'], values='sales', title=t["sales_category_title"],
                color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"]]
            )
            fig_tree.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=50, l=25, r=25, b=25))
            st.plotly_chart(fig_tree, use_container_width=True)
        st.info(t["sales_insight"])

    def render_tab_profit(df_filtered, t):
        st.subheader(t["tab_profit"])
        col2_1, col2_2 = st.columns(2)
        with col2_1:
            heat_df = df_filtered.pivot_table(values='profit_margin', index='category', columns='quarter', aggfunc='mean')
            fig_heat = px.imshow(
                heat_df, text_auto=".1f", aspect="auto", title=t["profit_heatmap_title"],
                color_continuous_scale=[COLORS["DANGER"], COLORS["WARNING"], COLORS["SUCCESS"]]
            )
            fig_heat.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_heat, use_container_width=True)
            
        with col2_2:
            fig_scatter = px.scatter(
                df_filtered, x='discount', y='profit_margin', color='category', trendline='ols', title=t["profit_scatter_title"],
                color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"]], opacity=0.6
            )
            fig_scatter.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_scatter, use_container_width=True)
            
        subcat_profit = df_filtered.groupby('sub_category')['profit'].sum().reset_index().sort_values('profit', ascending=False)
        top_bottom_df = pd.concat([subcat_profit.head(10), subcat_profit.tail(10)]).sort_values('profit', ascending=True)
        top_bottom_df['color'] = np.where(top_bottom_df['profit'] > 0, COLORS["SUCCESS"], COLORS["DANGER"])
        
        fig_bar_profit = go.Figure(data=[go.Bar(
            y=top_bottom_df['sub_category'], x=top_bottom_df['profit'], orientation='h', marker_color=top_bottom_df['color']
        )])
        fig_bar_profit.update_layout(title=t["profit_bar_title"], height=600, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_bar_profit, use_container_width=True)
        st.warning(t["profit_insight"])

    def render_tab_ops(df_filtered, t):
        st.subheader(t["tab_ops"])
        col3_1, col3_2 = st.columns(2)
        with col3_1:
            fig_box = px.box(
                df_filtered, x='ship_mode', y='days_to_ship', color='ship_mode', title=t["ops_box_title"],
                color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"], COLORS["WARNING"]]
            )
            fig_box.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_box, use_container_width=True)
            
        with col3_2:
            state_sales = df_filtered.groupby('state')['sales'].sum().reset_index()
            state_sales['state_code'] = state_sales['state'].map(us_state_to_abbrev)
            state_sales = state_sales.dropna(subset=['state_code'])
            fig_geo = px.choropleth(
                state_sales, locations='state_code', locationmode='USA-states', color='sales', scope="usa", title=t["ops_geo_title"],
                color_continuous_scale=[COLORS["SECONDARY"], COLORS["PRIMARY"]]
            )
            fig_geo.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', geo=dict(bgcolor='rgba(0,0,0,0)'))
            st.plotly_chart(fig_geo, use_container_width=True)
            
        df_timeline = df_filtered.copy()
        df_timeline['week'] = df_timeline['order_date'].dt.to_period('W').dt.start_time
        weekly_orders = df_timeline.groupby('week')['order_id'].nunique().reset_index()
        fig_line_ops = px.line(weekly_orders, x='week', y='order_id', title=t["ops_timeline_title"], line_shape='spline', color_discrete_sequence=[COLORS["ACCENT"]])
        fig_line_ops.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_line_ops, use_container_width=True)
        st.info(t["ops_insight"])

    def render_tab_conclusions(t):
        st.subheader(t["tab_conclusions"])
        findings_table = f"""
        | {t['conc_finding']} | {t['conc_impact']} | {t['conc_action']} | {t['conc_priority']} |
        |---|---|---|---|
        | {t['conc_row1_1']} | {t['conc_row1_2']} | {t['conc_row1_3']} | {t['conc_row1_4']} |
        | {t['conc_row2_1']} | {t['conc_row2_2']} | {t['conc_row2_3']} | {t['conc_row2_4']} |
        | {t['conc_row3_1']} | {t['conc_row3_2']} | {t['conc_row3_3']} | {t['conc_row3_4']} |
        """
        st.markdown(findings_table)
        st.markdown("---")
        st.subheader(t["conc_arch_title"])
        st.markdown(t["conc_arch_prob"])
        st.markdown(t["conc_arch_decisions"])
        st.markdown(t["conc_arch_scale"])
        st.markdown("---")
        st.subheader(t["conc_about_title"])
        st.markdown(t["conc_about_desc"])

    # Tabs Array
    tab1, tab2, tab3, tab4 = st.tabs([t["tab_sales"], t["tab_profit"], t["tab_ops"], t["tab_conclusions"]])
    with tab1: render_tab_sales(df_filtered, t)
    with tab2: render_tab_profit(df_filtered, t)
    with tab3: render_tab_ops(df_filtered, t)
    with tab4: render_tab_conclusions(t)
