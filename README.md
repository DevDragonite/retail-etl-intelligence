# 📊 Retail ETL Intelligence

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## Overview
**Retail ETL Intelligence** is a comprehensive data engineering and analytics portfolio project. It demonstrates the ability to extract, transform, and load (ETL) scattered retail data into a streamlined format, surfaced via an interactive, multi-lingual Streamlit dashboard. 

![Screenshot Placeholder](app_screenshot.png) 
> *(Add a screenshot of your app here)*

## Business Problem Resuelto
A major US retail chain was struggling to make strategic decisions due to fragmented data sources. Sales records, departmental budgets, and regional targets were siloed, leading to contradictory reporting. This project solves that by unifying the data into a single source of truth and presenting actionable insights through a clean, performant, and accessible UI.

## Tech Stack
- **Data Manipulation**: Pandas, NumPy
- **App Framework**: Streamlit
- **Data Visualization**: Plotly (Custom themed)
- **Environment**: Python 3.x with `venv`

## Project Structure
```text
retail-etl-intelligence/
├── data/
│   └── superstore.csv          # Raw data
├── output/
│   ├── superstore_clean.csv    # Transformed data via ETL
│   ├── etl_log.txt             # ETL processing logs
│   └── qa_log.txt              # Quality Assurance logs
├── app.py                      # Main Streamlit application
├── config.py                   # Global configs & Color Palette
├── etl_pipeline.py             # ETL script
├── translations.py             # i18n Dictionary (EN/ES/PT)
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Key Findings
- 🔻 **Profitability Leak**: Sub-category *Bookcases* consistently generates an average margin of -25%, largely driven by high discount rates.
- 📈 **Seasonality**: Q4 contributes heavily to annual revenue, requiring inventory alignment at least 3 months prior to meet demand spikes.
- 🚚 **Operational Bottlenecks**: Standard Class shipping averages ~5.5 days, causing potential customer dissatisfaction in coastal and high-demand states.

## Installation & Execution

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/retail-etl-intelligence.git
   cd retail-etl-intelligence
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the ETL Pipeline**:
   ```bash
   python etl_pipeline.py
   ```

5. **Launch the Dashboard**:
   ```bash
   streamlit run app.py
   ```

## Language Support
The dashboard features an integrated i18n system supporting:
- 🇪🇸 Español
- 🇬🇧 English
- 🇧🇷 Português

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please ensure to update tests and QA logs as appropriate.

---
*Developed by a Senior Data Analyst showcasing Data Engineering & Visualization skills.*
