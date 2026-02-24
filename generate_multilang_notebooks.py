import nbformat as nbf
import os

langs = {
    "es": {
        "text1": """\
# 📊 Retail ETL Intelligence - Proceso de Análisis
Este notebook detalla el análisis exploratorio de datos (EDA) y el pipeline ETL aplicado al dataset Superstore. Está dirigido a reclutadores y profesionales de datos para revisar la lógica detrás de las transformaciones de datos y los insights presentados en la aplicación Streamlit.

## 1. Configuración del Entorno
Importando las librerías necesarias y cargando los datos sin procesar.""",
        "text2": """\
## 2. Exploración Básica de Datos
Veamos la estructura del dataset, los valores nulos y los tipos de datos.""",
        "text3": """\
## 3. Transformación de Datos (Lógica ETL)
Aquí aplicamos las transformaciones principales utilizadas en nuestro pipeline ETL:
- Análisis de fechas
- Derivación de `days_to_ship`, `profit_margin`, `quarter` y `year`
- Normalización de nombres de columnas
""",
        "text4": """\
## 4. Insights Analíticos Clave
### A. Fuga de Rentabilidad en Bookcases (Estanterías) y Tables (Mesas)
Notamos que ciertas sub-categorías tienen márgenes consistentemente negativos debido a altas tasas de descuento.""",
        "text5": """\
### B. Rendimiento de Ventas por Región
Veamos qué regiones impulsan la mayor cantidad de ingresos.""",
        "text6": """\
## 5. Conclusión
El dataset ha sido limpiado, procesado y exportado a `output/superstore_clean.csv`.
Este análisis alimenta directamente el dashboard de Streamlit, proporcionando filtros dinámicos y soporte multilingüe."""
    },
    "pt": {
        "text1": """\
# 📊 Retail ETL Intelligence - Processo de Análise
Este notebook detalha a análise exploratória de dados (EDA) e o pipeline ETL aplicado ao dataset Superstore. Destina-se a recrutadores e profissionais de dados para revisar a lógica por trás das transformações de dados e dos insights apresentados no aplicativo Streamlit.

## 1. Configuração do Ambiente
Importanto as bibliotecas necessárias e carregando os dados brutos.""",
        "text2": """\
## 2. Exploração Básica de Dados
Vamos analisar a estrutura do dataset, valores ausentes e tipos de dados.""",
        "text3": """\
## 3. Transformação de Dados (Lógica ETL)
Aqui aplicamos as principais transformações usadas em nosso pipeline ETL:
- Análise de datas
- Derivação de `days_to_ship`, `profit_margin`, `quarter` e `year`
- Normalização dos nomes das colunas
""",
        "text4": """\
## 4. Principais Insights Analíticos
### A. Vazamento de Lucratividade em Bookcases (Estantes) e Tables (Mesas)
Notamos que certas subcategorias apresentam margens consistentemente negativas devido a altas taxas de desconto.""",
        "text5": """\
### B. Desempenho de Vendas por Região
Vejamos quais regiões geram mais receita.""",
        "text6": """\
## 5. Conclusão
O dataset foi limpo, processado e exportado para `output/superstore_clean.csv`.
Esta análise alimenta diretamente o painel do Streamlit, fornecendo filtros dinâmicos e suporte multilíngue."""
    }
}

code1 = """\
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load raw dataset
df_raw = pd.read_csv('data/superstore.csv', encoding='windows-1252')
df_raw.head()"""

code2 = """\
print("Dataset Shape:", df_raw.shape)
print("\\nMissing Values:\\n", df_raw.isnull().sum()[df_raw.isnull().sum() > 0])
print("\\nData Types:\\n", df_raw.dtypes)"""

code3 = """\
df = df_raw.copy()

# Fix types
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed', dayfirst=True)

# Feature Engineering
df['days_to_ship'] = (df['Ship Date'] - df['Order Date']).dt.days
df['profit_margin'] = (df['Profit'] / df['Sales']) * 100
df['quarter'] = df['Order Date'].dt.quarter
df['year'] = df['Order Date'].dt.year

# Normalizing column names for easier access (snake_case)
df.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df.columns]

# Drop duplicates
df = df.drop_duplicates()

df[['order_id', 'order_date', 'days_to_ship', 'profit_margin']].head()"""

code4 = """\
subcat_profit = df.groupby('sub_category')['profit'].sum().reset_index().sort_values('profit')
print("Bottom 5 Sub-categories by Profit:\\n", subcat_profit.head())

# Visualizing Discount vs Profit Margin
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x='discount', y='profit_margin', hue='category', alpha=0.6, ax=ax)
ax.set_title("Discount vs Profit Margin")
plt.show()"""

code5 = """\
region_sales = df.groupby('region')['sales'].sum().reset_index().sort_values('sales', ascending=False)
display(region_sales)"""

def create_notebook(lang_code, lang_dict):
    nb = nbf.v4.new_notebook()

    nb['cells'] = [
        nbf.v4.new_markdown_cell(lang_dict['text1']),
        nbf.v4.new_code_cell(code1),
        nbf.v4.new_markdown_cell(lang_dict['text2']),
        nbf.v4.new_code_cell(code2),
        nbf.v4.new_markdown_cell(lang_dict['text3']),
        nbf.v4.new_code_cell(code3),
        nbf.v4.new_markdown_cell(lang_dict['text4']),
        nbf.v4.new_code_cell(code4),
        nbf.v4.new_markdown_cell(lang_dict['text5']),
        nbf.v4.new_code_cell(code5),
        nbf.v4.new_markdown_cell(lang_dict['text6'])
    ]

    filename = f'analysis_process_{lang_code}.ipynb'
    with open(filename, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    
    print(f"Notebook '{filename}' created successfully.")

if __name__ == '__main__':
    for lang_code, lang_dict in langs.items():
        create_notebook(lang_code, lang_dict)
