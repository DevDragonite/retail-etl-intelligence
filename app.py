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
    st.session_state.lang = "Español"

if "page" not in st.session_state:
    st.session_state.page = "Bienvenida"

# --- CSS STYLING (PREMIUM LIQUID GLASS) ---
def apply_custom_css():
    css = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* App Background - elegant soft gradient */
        .stApp {{
            background: linear-gradient(135deg, #e0e7f1 0%, #f4f6fa 100%);
            font-family: 'Inter', sans-serif;
        }}
        
        /* Typography */
        html, body, [class*="css"] {{
            color: #1a202c !important; 
            font-family: 'Inter', sans-serif;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #0f172a !important;
            font-weight: 700;
            letter-spacing: -0.02em;
        }}
        
        /* Liquid Glass Containers for Metrics and general containers */
        [data-testid="stMetric"], .st-emotion-cache-12oz5g7, .st-emotion-cache-1r6slb0, .css-1r6slb0 {{
            background: rgba(255, 255, 255, 0.75) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border-radius: 20px !important;
            border: 1px solid rgba(255, 255, 255, 0.9) !important;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.07) !important;
            padding: 1.5rem !important;
            transition: all 0.3s ease;
            box-sizing: border-box !important;
        }}
        
        [data-testid="stPlotlyChart"] {{
            background: rgba(255, 255, 255, 0.75) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border-radius: 20px !important;
            border: 1px solid rgba(255, 255, 255, 0.9) !important;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.07) !important;
            padding: 0 !important; /* NO PADDING to avoid internal scrollbars */
            box-sizing: border-box !important;
            overflow: hidden !important;
        }}
        
        [data-testid="stPlotlyChart"] iframe {{
            /* Ensure the iframe itself doesn't cause overflow */
            max-width: 100% !important;
            max-height: 100% !important;
        }}
        
        [data-testid="stMetric"]:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(31, 38, 135, 0.12) !important;
            border: 1px solid rgba(255, 255, 255, 1) !important;
        }}
        
        /* Metric Typography */
        [data-testid="stMetricValue"] {{
            font-size: 2.0rem !important; /* Reduced to avoid text cutoff at 100% zoom */
            font-weight: 800 !important;
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        [data-testid="stMetricLabel"] {{
            font-size: 0.95rem !important;
            color: #475569 !important;
            font-weight: 600 !important;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        
        /* Tabs styling - Pill shape full width */
        .stTabs [data-baseweb="tab-list"] {{
            display: flex;
            gap: 10px;
            background: rgba(255, 255, 255, 0.4);
            padding: 6px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.6);
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.02);
            width: 100%;
        }}
        .stTabs [data-baseweb="tab"] {{
            flex: 1; /* Distribute evenly */
            justify-content: center;
            height: 42px;
            background: rgba(226, 232, 240, 0.6); /* Darker background to look like a button */
            border-radius: 12px;
            padding: 8px 12px;
            font-weight: 800 !important; /* Bolded as requested */
            color: #1e293b !important; /* Darker base text keeping visibility */
            border: 1px solid rgba(203, 213, 225, 0.5) !important;
            transition: all 0.2s ease;
            white-space: nowrap;
        }}
        .stTabs [aria-selected="true"] {{
            background: rgba(255, 255, 255, 1) !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.06) !important;
            color: #1e40af !important;
        }}
        .stTabs [data-baseweb="tab-highlight"] {{
            display: none;
        }}
        
        /* Welcome Storytelling elements */
        .welcome-card {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            padding: 3.5rem;
            border: 1px solid rgba(255, 255, 255, 1);
            box-shadow: 0 15px 50px rgba(15, 23, 42, 0.06);
            margin-bottom: 2rem;
        }}
        .welcome-pillar {{
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 1.8rem;
            margin: 1.2rem 0;
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 8px 25px rgba(0,0,0,0.03);
            border-left: 5px solid #3b82f6;
            transition: all 0.3s ease;
        }}
        .welcome-pillar * {{
            color: #1e293b !important;
        }}
        .welcome-pillar:hover {{
            transform: translateX(8px);
            background: rgba(255, 255, 255, 0.8);
            box-shadow: 0 12px 30px rgba(0,0,0,0.05);
        }}
        .welcome-text {{
            font-size: 1.15rem;
            line-height: 1.8;
            color: #334155;
        }}
        
        .stButton>button {{
            border-radius: 12px;
            font-weight: 600;
            border: 1px solid rgba(0,0,0,0.1);
            background: white;
            color: #1e293b;
        }}
        
        hr {{
            border-top: 1px solid rgba(15, 23, 42, 0.08);
            margin: 2.5rem 0;
        }}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    return css

custom_css = apply_custom_css()

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
    flag_urls = {
        "Español": "https://flagcdn.com/w20/ve.png",
        "English": "https://flagcdn.com/w20/us.png",
        "Português": "https://flagcdn.com/w20/br.png"
    }
    
    active_lang = st.session_state.lang
    other_langs = [l for l in LANGS.keys() if l != active_lang]
    
    # Iterate over the non-active languages and inject dynamic CSS for each specific position
    inner_css = ""
    for idx, lang_opt in enumerate(other_langs, start=1):
        inner_css += f"""
        div[data-testid="stPopoverBody"] [data-testid="stButton"]:nth-of-type({idx}) button p::before {{
            content: ""; display: inline-block; width: 18px; height: 13px;
            background-image: url('{flag_urls[lang_opt]}'); background-size: cover; 
            margin-right: 8px; vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }}
        """
        
    # CSS injection for natively unsupported images in Streamlit buttons
    css_flags = f"""
    <style>
    /* Main popover button flag */
    div[data-testid="stPopover"] > div > button p::before {{
        content: ""; display: inline-block; width: 18px; height: 13px;
        background-image: url('{flag_urls[active_lang]}'); background-size: cover; 
        margin-right: 8px; vertical-align: middle; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }}
    {inner_css}
    </style>
    """
    st.markdown(css_flags, unsafe_allow_html=True)
    
    with st.popover(active_lang):
        for lang_option in other_langs:
            if st.button(lang_option, use_container_width=True, key=f"btn_{lang_option}"):
                st.session_state.lang = lang_option
                st.rerun()

t = LANGS[st.session_state.lang]

# --- SIDEBAR NAVIGATION & FILTERS ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3121/3121693.png", width=80) 
st.sidebar.markdown(f"### {t['sidebar_title']}")

# Navigation Logic fixed for state persistence mapping
nav_options = [t["nav_welcome"], t["nav_dashboard"]]

# Check if current st.session_state.page is a valid option in current language, if not reset to welcome
if st.session_state.page not in nav_options:
    if "Dashboard" in st.session_state.page:
        st.session_state.page = t["nav_dashboard"]
    else:
        st.session_state.page = t["nav_welcome"]

st.session_state.page = st.sidebar.radio("Navegación", nav_options, index=nav_options.index(st.session_state.page))
is_dashboard = st.session_state.page == t["nav_dashboard"]

# Filters
df_filtered = df_master.copy()
min_year_val = int(df_master['year'].min())
max_year_val = int(df_master['year'].max())
selected_years = (min_year_val, max_year_val)

if is_dashboard:
    st.sidebar.markdown("---")
    selected_years = st.sidebar.slider(t["year_range"], min_year_val, max_year_val, (min_year_val, max_year_val))

# Download Data Button (Sidebar)
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
    
    # We use st.markdown with standard string manipulation and strict no-indentation
    # to prevent Streamlit from wrapping inner elements as markdown code blocks.
    st.markdown(f"""
<div class="welcome-card" style="margin: 0; padding: 2.5rem;">
<h1 style="font-size: 3.2rem; margin-bottom: 0.8rem; text-align: center; color: #0f172a; font-family: 'Inter', sans-serif;">{t["hero_title"]}</h1>
<p style="text-align: center; font-size: 1.3rem; color: #64748b; margin-bottom: 2.5rem; font-weight: 500; font-family: 'Inter', sans-serif;">
<em>{t['welcome_title']}</em>
</p>
<p class="welcome-text" style="font-family: 'Inter', sans-serif;">{t['welcome_story_1']}</p>
<p class="welcome-text" style="font-family: 'Inter', sans-serif;">{t['welcome_story_2'].replace('**', '<strong>').replace('**', '</strong>')}</p>

<div class="welcome-pillar" style="font-family: 'Inter', sans-serif;">
<h4 style="margin-bottom: 0.5rem; color: #0f172a;">{t['welcome_pillar_1_title']}</h4>
<p style="margin:0; color: #1e293b;">{t['welcome_pillar_1_desc']}</p>
</div>
<div class="welcome-pillar" style="font-family: 'Inter', sans-serif;">
<h4 style="margin-bottom: 0.5rem; color: #0f172a;">{t['welcome_pillar_2_title']}</h4>
<p style="margin:0; color: #1e293b;">{t['welcome_pillar_2_desc']}</p>
</div>
<div class="welcome-pillar" style="font-family: 'Inter', sans-serif;">
<h4 style="margin-bottom: 0.5rem; color: #0f172a;">{t['welcome_pillar_3_title']}</h4>
<p style="margin:0; color: #1e293b;">{t['welcome_pillar_3_desc']}</p>
</div>

<div style="text-align: center; margin-top: 2rem; font-family: 'Inter', sans-serif;">
<p style="font-weight: 600; font-size: 1.2rem; color: #0f172a;">
{t['welcome_cta'].replace('**', '<strong>').replace('**', '</strong>')}
</p>
</div>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; margin-top: 2rem;'><img src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white'> <img src='https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white'> <img src='https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white'> <img src='https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white'></p>", unsafe_allow_html=True)


elif st.session_state.page == t["nav_dashboard"]:
    # ---------------- MAIN DASHBOARD SECTION ----------------
    st.title("📊 Dashboard")
    st.write("")
    
    # Global Filters (Horizontal layout top of dashboard)
    with st.expander(f"🎛️ {t['global_filters']}", expanded=True):
        f_col1, f_col2 = st.columns(2)
        
        # Translation format functions for filters
        def tf_region(r):
            if st.session_state.lang == "Español": return {"Central": "Centro", "East": "Este", "South": "Sur", "West": "Oeste"}.get(r, r)
            if st.session_state.lang == "Português": return {"Central": "Centro", "East": "Leste", "South": "Sul", "West": "Oeste"}.get(r, r)
            return r

        def tf_category(c):
            if st.session_state.lang == "Español": return {"Furniture": "Mobiliario", "Office Supplies": "Material de Oficina", "Technology": "Tecnología"}.get(c, c)
            if st.session_state.lang == "Português": return {"Furniture": "Móveis", "Office Supplies": "Material de Escritório", "Technology": "Tecnologia"}.get(c, c)
            return c

        with f_col1:
            all_regions = sorted(df_master['region'].dropna().unique())
            selected_regions = st.multiselect(t["region_filter"], all_regions, default=all_regions, format_func=tf_region)
        with f_col2:
            all_categories = sorted(df_master['category'].dropna().unique())
            selected_categories = st.multiselect(t["category_filter"], all_categories, default=all_categories, format_func=tf_category)

    # Apply Filters to Dashboard Data
    df_filtered = df_master[
        (df_master['year'] >= selected_years[0]) & 
        (df_master['year'] <= selected_years[1]) &
        (df_master['region'].isin(selected_regions)) &
        (df_master['category'].isin(selected_categories))
    ]
    
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
        fig_yoy.update_layout(
            xaxis=dict(tickmode='linear', tick0=1, dtick=1, showgrid=False), 
            yaxis=dict(showgrid=True, zeroline=False, showticklabels=False, title=""),
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Inter", weight="bold"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
            margin=dict(t=60, b=40, l=40, r=40)
        )
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
            fig_region.update_traces(textfont=dict(family="Inter", weight="bold", color="black"), textposition="outside")
            fig_region.update_layout(
                title=t["sales_region_title"], 
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                yaxis=dict(showgrid=False, showticklabels=False, title=""),
                font=dict(weight="bold"),
                margin=dict(t=60, b=40, l=40, r=40)
            )
            st.plotly_chart(fig_region, use_container_width=True)
            
        with col1_2:
            fig_tree = px.treemap(
                df_filtered, path=['category', 'sub_category'], values='sales', title=t["sales_category_title"],
                color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"]]
            )
            fig_tree.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                margin=dict(t=60, l=20, r=20, b=20),
                font=dict(family="Inter", weight="bold")
            )
            fig_tree.update_traces(textinfo="label+value", textfont=dict(color="black", weight="bold"))
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
            fig_heat.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(t=60, l=40, r=40, b=40)
            )
            st.plotly_chart(fig_heat, use_container_width=True)
            
        with col2_2:
            fig_scatter = px.scatter(
                df_filtered, x='discount', y='profit_margin', color='category', trendline='ols', title=t["profit_scatter_title"],
                color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"]], opacity=0.6
            )
            fig_scatter.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                font=dict(weight="bold"),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
                margin=dict(t=60, l=40, r=40, b=40)
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
            
        subcat_profit = df_filtered.groupby('sub_category')['profit'].sum().reset_index().sort_values('profit', ascending=False)
        top_bottom_df = pd.concat([subcat_profit.head(10), subcat_profit.tail(10)]).sort_values('profit', ascending=True)
        top_bottom_df['color'] = np.where(top_bottom_df['profit'] > 0, COLORS["SUCCESS"], COLORS["DANGER"])
        
        fig_bar_profit = go.Figure(data=[go.Bar(
            y=top_bottom_df['sub_category'], x=top_bottom_df['profit'], orientation='h', marker_color=top_bottom_df['color'],
            text=top_bottom_df['profit'].apply(lambda x: f"${x:,.0f}"), textposition='auto'
        )])
        fig_bar_profit.update_traces(textfont=dict(family="Inter", weight="bold", color="black", size=11), textposition="auto", cliponaxis=False)
        fig_bar_profit.update_layout(
            title=t["profit_bar_title"], height=500, 
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, showticklabels=False, title=""),
            font=dict(weight="bold"),
            margin=dict(t=60, l=100, r=80, b=40)
        )
        st.plotly_chart(fig_bar_profit, use_container_width=True, config={'displayModeBar': False})
        st.warning(t["profit_insight"])

    def render_tab_ops(df_filtered, t):
        st.subheader(t["tab_ops"])
        col3_1, col3_2 = st.columns(2)
        with col3_1:
            fig_box = px.box(
                df_filtered, x='ship_mode', y='days_to_ship', color='ship_mode', title=t["ops_box_title"],
                color_discrete_sequence=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"], COLORS["WARNING"]]
            )
            fig_box.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(t=60, l=40, r=40, b=40)
            )
            st.plotly_chart(fig_box, use_container_width=True)
            
        with col3_2:
            state_sales = df_filtered.groupby('state')['sales'].sum().reset_index()
            state_sales['state_code'] = state_sales['state'].map(us_state_to_abbrev)
            state_sales = state_sales.dropna(subset=['state_code'])
            fig_geo = px.choropleth(
                state_sales, locations='state_code', locationmode='USA-states', color='sales', scope="usa", title=t["ops_geo_title"],
                color_continuous_scale=[COLORS["SECONDARY"], COLORS["PRIMARY"]]
            )
            fig_geo.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
                geo=dict(bgcolor='rgba(0,0,0,0)'),
                margin=dict(t=60, l=10, r=10, b=10),
                dragmode=False
            )
            st.plotly_chart(fig_geo, use_container_width=True, config={'displayModeBar': False, 'scrollZoom': False})
            
        df_timeline = df_filtered.copy()
        df_timeline['week'] = df_timeline['order_date'].dt.to_period('W').dt.start_time
        weekly_orders = df_timeline.groupby('week')['order_id'].nunique().reset_index()
        fig_line_ops = px.line(weekly_orders, x='week', y='order_id', title=t["ops_timeline_title"], line_shape='spline', color_discrete_sequence=[COLORS["ACCENT"]])
        fig_line_ops.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=60, l=40, r=40, b=40)
        )
        st.plotly_chart(fig_line_ops, use_container_width=True)
        st.info(t["ops_insight"])

    def render_tab_conclusions(t):
        st.subheader(t["conclusions_title"])
        
        labels = {
            "Español": ["🔍 Hallazgo", "💥 Impacto", "✅ Acción Recomendada", "📈 Predicción"],
            "English": ["🔍 Finding", "💥 Impact", "✅ Recommended Action", "📈 Prediction"],
            "Português": ["🔍 Descoberta", "💥 Impacto", "✅ Ação Recomendada", "📈 Previsão"]
        }
        L = labels.get(st.session_state.lang, labels["Español"])
        
        def render_finding(title_key, finding_key, impact_key, action_key, pred_key):
            st.markdown(f"#### {t[title_key]}")
            st.markdown(f"**{L[0]}:** {t[finding_key]}")
            st.markdown(f"**{L[1]}:** {t[impact_key]}")
            st.markdown(f"**{L[2]}:** {t[action_key]}")
            st.success(f"**{L[3]}:** {t[pred_key]}")
            st.markdown("---")
            
        render_finding('conc_f1_title', 'conc_f1_finding', 'conc_f1_impact', 'conc_f1_action', 'conc_f1_prediction')
        render_finding('conc_f2_title', 'conc_f2_finding', 'conc_f2_impact', 'conc_f2_action', 'conc_f2_prediction')
        render_finding('conc_f3_title', 'conc_f3_finding', 'conc_f3_impact', 'conc_f3_action', 'conc_f3_prediction')
        
        # Footer in Conclusions
        footer_labels = {
            "Español": "Desarrollado por Hely Camargo utilizando:",
            "English": "Developed by Hely Camargo using:",
            "Português": "Desenvolvido por Hely Camargo utilizando:"
        }
        f_text = footer_labels.get(st.session_state.lang, footer_labels["Español"])
        techs = "Python, Pandas, Plotly Express & Streamlit"
        
        st.markdown(f"<div style='text-align: right; margin-top: 2rem;'><span style='color: black; font-weight: bold;'>{f_text} {techs}</span></div>", unsafe_allow_html=True)

    # Tabs Array
    tab1, tab2, tab3, tab4 = st.tabs([t["tab_sales"], t["tab_profit"], t["tab_ops"], t["tab_conclusions"]])
    with tab1: render_tab_sales(df_filtered, t)
    with tab2: render_tab_profit(df_filtered, t)
    with tab3: render_tab_ops(df_filtered, t)
    with tab4: render_tab_conclusions(t)
