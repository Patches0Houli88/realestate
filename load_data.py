# load_data.py
import sqlite3
import pandas as pd

# Connect to the SQLite database (creates if it doesn't exist)
conn = sqlite3.connect("real_estate_portfolio.db")

# Load and clean each CSV
def clean_properties(df):
    # Convert letter codes to full labels
    type_map = {
        'A': 'Single Family',
        'B': 'Condo',
        'C': 'Townhome',
        'D': 'Multi-Family',
        'E': 'Ranch'
    }
    df['type'] = df['type'].map(type_map)
    return df

def clean_transactions(df):
    # Format sales_date to YYYY-MM-DD
    df['sales_date'] = pd.to_datetime(df['sales_date'], errors='coerce').dt.strftime('%Y-%m-%d')
    return df

# Load and clean
properties_df = clean_properties(pd.read_csv("properties.csv"))
agents_df = pd.read_csv("agents.csv")
transactions_df = clean_transactions(pd.read_csv("transactions.csv"))

# Save to SQLite
properties_df.to_sql("properties", conn, if_exists="replace", index=False)
agents_df.to_sql("agents", conn, if_exists="replace", index=False)
transactions_df.to_sql("transactions", conn, if_exists="replace", index=False)

print("✅ Data cleaned and loaded into real_estate_portfolio.db")

conn.close()