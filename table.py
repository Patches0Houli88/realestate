# load_data.py
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("real_estate_portfolio.db")

# Load CSVs into DataFrames and push to SQLite
tables = {
    "properties": "properties.csv",
    "agents": "agents.csv",
    "transactions": "transactions.csv"
}

for table, file in tables.items():
    df = pd.read_csv(file)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"✅ Loaded {file} into table: {table}")

# Optional preview
sample = pd.read_sql("SELECT * FROM transactions LIMIT 5", conn)
print("\nSample data from 'transactions':")
print(sample)

conn.close()