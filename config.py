# config.py

# Light Mode Color Palette for Retail ETL Intelligence
COLORS = {
    "PRIMARY": "#2C5F8A",     # Deep corporate blue
    "SECONDARY": "#4A9B8E",   # Soft emerald green
    "ACCENT": "#E8834A",      # Warm orange
    "SUCCESS": "#5BAD8F",     # Success green
    "WARNING": "#F0B94A",     # Amber yellow
    "DANGER": "#D95F5F",      # Soft red
    "BG": "#F8F9FA",          # Very light gray
    "SURFACE": "#FFFFFF",     # Pure white
    "TEXT": "#1A2332",        # Dark blue, almost black
    "TEXT_MUTED": "#6B7A8D",  # Blue-gray
    "BORDER": "#E2E8F0"       # Border gray
}

# General App Config
APP_NAME = "Retail ETL Intelligence"
APP_ICON = "📊"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Custom Plotly Template Based on Color Palette
from plotly import graph_objects as go
import plotly.io as pio

custom_template = go.layout.Template()
custom_template.layout = go.Layout(
    paper_bgcolor=COLORS["SURFACE"],
    plot_bgcolor=COLORS["SURFACE"],
    font=dict(color=COLORS["TEXT"]),
    title=dict(font=dict(color=COLORS["PRIMARY"])),
    colorway=[COLORS["PRIMARY"], COLORS["SECONDARY"], COLORS["ACCENT"], COLORS["SUCCESS"], COLORS["WARNING"], COLORS["DANGER"]],
    xaxis=dict(
        gridcolor=COLORS["BORDER"],
        zerolinecolor=COLORS["BORDER"],
        tickfont=dict(color=COLORS["TEXT_MUTED"]),
        title_font=dict(color=COLORS["TEXT_MUTED"])
    ),
    yaxis=dict(
        gridcolor=COLORS["BORDER"],
        zerolinecolor=COLORS["BORDER"],
        tickfont=dict(color=COLORS["TEXT_MUTED"]),
        title_font=dict(color=COLORS["TEXT_MUTED"])
    )
)

pio.templates["retail_light"] = custom_template
pio.templates.default = "retail_light"
