# app.py (Streamlit Dashboard)
import streamlit as st
import sqlite3
import pandas as pd

# Connect to SQLite DB
conn = sqlite3.connect("real_estate_portfolio.db")

st.title("🏘️ Real Estate Analytics Dashboard")

# Tabs for different reports
tabs = st.tabs([
    "Top Agents",
    "Price Trends",
    "State Activity",
    "Monthly Sales",
    "Over List Sales"
])

with tabs[0]:
    st.subheader("Top 5 Agents by Total Sales")
    df = pd.read_sql("""
        SELECT a.name, a.agency, SUM(t.sales_price) AS total_sales
        FROM agents a
        JOIN transactions t ON a.agent_id = t.agent_id
        GROUP BY a.agent_id
        ORDER BY total_sales DESC
        LIMIT 5;
    """, conn)
    st.dataframe(df)
    st.bar_chart(df.set_index("name")["total_sales"])

with tabs[1]:
    st.subheader("Average Sale Price by Property Type")
    df = pd.read_sql("""
        SELECT p.type, ROUND(AVG(t.sales_price), 2) AS avg_sales_price
        FROM transactions t
        JOIN properties p ON t.property_id = p.property_id
        GROUP BY p.type;
    """, conn)
    st.bar_chart(df.set_index("type"))

with tabs[2]:
    st.subheader("Number of Transactions by State")
    df = pd.read_sql("""
        SELECT p.state, COUNT(t.transaction_id) AS total_transactions
        FROM transactions t
        JOIN properties p ON t.property_id = p.property_id
        GROUP BY p.state
        ORDER BY total_transactions DESC;
    """, conn)
    st.bar_chart(df.set_index("state"))

with tabs[3]:
    st.subheader("Monthly Sales Trends")
    df = pd.read_sql("""
        SELECT strftime('%Y-%m', t.sales_date) AS month,
               COUNT(*) AS total_sales,
               ROUND(AVG(t.sales_price), 2) AS avg_price
        FROM transactions t
        GROUP BY month
        ORDER BY month;
    """, conn)
    st.line_chart(df.set_index("month"))

with tabs[4]:
    st.subheader("Properties Sold Over Listing Price")
    df = pd.read_sql("""
        SELECT p.address, p.city, p.state, p.list_price, t.sales_price
        FROM transactions t
        JOIN properties p ON t.property_id = p.property_id
        WHERE t.sales_price > p.list_price
        ORDER BY t.sales_price - p.list_price DESC;
    """, conn)
    st.dataframe(df)

conn.close()
