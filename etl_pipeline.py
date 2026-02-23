import pandas as pd
import numpy as np
import datetime
import os

def run_etl():
    print("Starting ETL Process...")
    start_time = datetime.datetime.now()
    log_dir = "output"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "etl_log.txt")
    
    # 1. EXTRACTION
    data_path = "data/superstore.csv"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Source file {data_path} not found.")
    
    try:
        df_superstore = pd.read_csv(data_path, encoding='windows-1252')
    except UnicodeDecodeError:
        df_superstore = pd.read_csv(data_path, encoding='utf-8')
    
    rows_initial = len(df_superstore)
    
    # Create fictitious realistic budget per category
    categories = df_superstore['Category'].unique() if 'Category' in df_superstore.columns else []
    budget_data = {
        'Category': categories,
        'annual_budget': [500000, 750000, 600000][:len(categories)]
    }
    df_budget = pd.DataFrame(budget_data)
    
    # Create fictitious targets per region per quarter
    regions = df_superstore['Region'].unique() if 'Region' in df_superstore.columns else []
    targets_data = []
    for region in regions:
        for q in [1, 2, 3, 4]:
            targets_data.append({'Region': region, 'quarter': q, 'regional_target': np.random.randint(50000, 150000)})
    df_targets = pd.DataFrame(targets_data)
    
    # 2. TRANSFORMATION
    df = df_superstore.copy()
    
    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=True)
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed', dayfirst=True)
    
    # Calculate new columns
    df['days_to_ship'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['profit_margin'] = (df['Profit'] / df['Sales']) * 100
    df['quarter'] = df['Order Date'].dt.quarter
    df['year'] = df['Order Date'].dt.year
    
    # Detect and handle anomalies
    null_counts = df.isnull().sum()
    duplicate_count = df.duplicated().sum()
    
    # Outliers using IQR for Sales and Profit
    Q1_sales = df['Sales'].quantile(0.25)
    Q3_sales = df['Sales'].quantile(0.75)
    IQR_sales = Q3_sales - Q1_sales
    outliers_sales = ((df['Sales'] < (Q1_sales - 1.5 * IQR_sales)) | (df['Sales'] > (Q3_sales + 1.5 * IQR_sales))).sum()

    Q1_profit = df['Profit'].quantile(0.25)
    Q3_profit = df['Profit'].quantile(0.75)
    IQR_profit = Q3_profit - Q1_profit
    outliers_profit = ((df['Profit'] < (Q1_profit - 1.5 * IQR_profit)) | (df['Profit'] > (Q3_profit + 1.5 * IQR_profit))).sum()
    
    df = df.drop_duplicates()
    rows_after_dedup = len(df)
    
    # Normalize column names to snake_case
    df.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df.columns]
    df_budget.columns = [col.lower().replace(' ', '_') for col in df_budget.columns]
    df_targets.columns = [col.lower().replace(' ', '_') for col in df_targets.columns]
    
    # Merge sources
    df_master = df.merge(df_budget, on='category', how='left')
    df_master = df_master.merge(df_targets, on=['region', 'quarter'], how='left')
    
    columns_created = ['days_to_ship', 'profit_margin', 'quarter', 'year', 'annual_budget', 'regional_target']
    
    # 3. LOAD
    output_path = os.path.join(log_dir, "superstore_clean.csv")
    df_master.to_csv(output_path, index=False)
    
    # Log Generation
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("=== ETL EXECUTION LOG ===\n")
        f.write(f"Timestamp: {datetime.datetime.now()}\n")
        f.write(f"Rows Initial: {rows_initial}\n")
        f.write(f"Duplicates Removed: {duplicate_count}\n")
        f.write(f"Rows Final: {rows_after_dedup}\n")
        f.write(f"Columns Created: {', '.join(columns_created)}\n")
        f.write("\n--- Data Quality Report ---\n")
        f.write("Nulls Detected:\n")
        for idx, val in null_counts[null_counts > 0].items():
            f.write(f"  - {idx}: {val}\n")
        if (null_counts > 0).sum() == 0:
            f.write("  - None\n")
        f.write(f"Outliers Detected in Sales: {outliers_sales}\n")
        f.write(f"Outliers Detected in Profit: {outliers_profit}\n")
        f.write("\n--- Integrated Sources Summary ---\n")
        f.write("1. Superstore Data (Main)\n")
        f.write("2. Annual Budget Data (Mock)\n")
        f.write("3. Regional Targets Data (Mock)\n")
        
    print(f"ETL Process Completed. Output saved to {output_path} and logic written to {log_file}")

if __name__ == "__main__":
    run_etl()
