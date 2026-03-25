import pandas as pd
import sqlite3
import os
from pathlib import Path

# 1. Setup Paths
# Make sure your CSV files are in a folder named 'data'
base_path = Path(__file__).parent.parent
data_dir = base_path / "data"
db_dir = base_path / "database"

# Create the database directory if it doesn't exist
db_dir.mkdir(exist_ok=True)
db_path = db_dir / "streaming_data.db"

def clean_column_names(df):
    """Cleans column names for SQL compatibility (lowercase, no spaces)"""
    df.columns = [col.strip().replace(' ', '_').replace('.', '').lower() for col in df.columns]
    return df

def csv_to_sqlite():
    # Connect to (or create) the SQLite database
    conn = sqlite3.connect(db_path)
    print(f"Connected to database at: {db_path}")

    # Process each CSV in the data folder
    for file in data_dir.glob("*.csv"):
        table_name = file.stem.lower().replace(" ", "_")
        print(f"Processing {file.name} into table '{table_name}'...")
        
        # Load and clean data
        df = pd.read_csv(file)
        df = clean_column_names(df)
        
        # Write to SQL
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Successfully imported {len(df)} rows.")

    conn.close()
    print("\nAll done! You can now open 'streaming_data.db' in VS Code.")

if __name__ == "__main__":
    csv_to_sqlite()