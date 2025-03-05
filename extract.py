import pandas as pd
import os

def extract_data(file_path, sheet_name=None):
    """
    Extracts data from an Excel/CSV file and loads it into a DataFrame.
    If an Excel sheet name is provided, it reads the specific sheet.
    """
    print(f"Starting extraction from {file_path}...")
    
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide an Excel or CSV file.")
    
    print(f"Successfully extracted {len(df)} records from {sheet_name if sheet_name else 'CSV File'}")
    return df

if __name__ == "__main__":
    # File path
    excel_file_path = "SAP-DataSet.xlsx"
    csv_file_path = ""  # Optional CSV file
    
    # Sheets to extract from Excel
    sheets = ['KNA1', 'VBAK', 'VBAP', 'LIKP', 'LIPS', 'VTTK', 'VTTP']
    
    # Extract data from Excel
    excel_dataframes = {sheet: extract_data(excel_file_path, sheet) for sheet in sheets}
    
    # Extract data from CSV (if needed)
    csv_data = extract_data(csv_file_path) if os.path.exists(csv_file_path) else None
    
    # Save extracted data for transformation step
    for sheet, df in excel_dataframes.items():
        df.to_csv(f"{sheet}.csv", index=False)
    
    if csv_data is not None:
        csv_data.to_csv("extracted_data.csv", index=False)

    print("Extraction process completed. Data saved successfully!")
