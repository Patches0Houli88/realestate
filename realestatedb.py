import sqlite3
import pandas as pd

# Connect to your project DB (creates if not exist)
conn = sqlite3.connect("realestate_db.db")

# Load and insert each table
pd.read_csv("properties.csv").to_sql("properties", conn, if_exists="replace", index=False)
pd.read_csv("agents.csv").to_sql("agents", conn, if_exists="replace", index=False)
pd.read_csv("transactions.csv").to_sql("transactions", conn, if_exists="replace", index=False)

# Optional: preview a table
df = pd.read_sql("SELECT * FROM transactions LIMIT 5;", conn)
print(df)

conn.close()