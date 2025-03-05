import pandas as pd

def clean_data(df, table_name):
    """
    Cleans and transforms the extracted data.
    """
    print(f"Starting data cleaning for {table_name}...")
    
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Fill missing values with appropriate defaults
    df = df.fillna('Unknown')
    
    # Ensure date format consistency
    date_columns = [col for col in df.columns if 'date' in col.lower()]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # Strip leading/trailing spaces from string columns
    str_columns = df.select_dtypes(include=['object']).columns
    df[str_columns] = df[str_columns].apply(lambda x: x.str.strip())
    
    print(f"{table_name} data cleaned successfully.")
    return df

if __name__ == "__main__":
    # Load extracted CSV files
    tables = ['KNA1', 'VBAK', 'VBAP', 'LIKP', 'LIPS', 'VTTK', 'VTTP']
    cleaned_data = {}

    for table in tables:
        print(f"Processing transformation for {table}...")
        df = pd.read_csv(f"{table}.csv")
        cleaned_data[table] = clean_data(df, table)
        print(f"Transformation complete for {table}.")

    # Save transformed data as CSV and Excel
    writer = pd.ExcelWriter("transformed_data.xlsx", engine='xlsxwriter')

    for table, df in cleaned_data.items():
        df.to_csv(f"cleaned_{table}.csv", index=False)
        df.to_excel(writer, sheet_name=table, index=False)
        print(f"Cleaned data saved for {table}. Ready for loading.")

    writer.close()
    
    print("All transformations are complete! Ready for data loading.")
