import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "127.0.0.1"
DB_NAME = "sap_data_warehouse"

# Create a database connection
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

def load_data(file_path, table_name):
    """
    Loads cleaned data into MySQL database.
    """
    df = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
    print(f"Starting to load {len(df)} records into {table_name}...")
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"{table_name} loaded successfully into the database.")

if __name__ == "__main__":
    # Tables to load
    tables = ['KNA1', 'VBAK', 'VBAP', 'LIKP', 'LIPS', 'VTTK', 'VTTP']
    
    for table in tables:
        print(f"Initiating load process for {table}...")
        load_data(f"cleaned_{table}.csv", table)
        print(f"Data successfully loaded for {table}.")
    
    print("All data loading processes are complete! Database is ready.")
