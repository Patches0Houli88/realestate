# realestate
Real Estate transactions DB
🏘️ Real Estate Analytics Dashboard

This project simulates a complete data analysis pipeline for a real estate business. 
It includes:

Synthetic data for properties, agents, and transactions

A normalized SQLite database

Advanced SQL queries for insights

A Streamlit dashboard for interactive exploration

📂 Project Structure

realestate_db/
├── agents.csv
├── properties.csv
├── transactions.csv
├── load_data.py
├── real_estate_portfolio.db
├── real_estate_queries.sql
├── real_estate_dashboard.py
├── requirements.txt
└── README.md

⚙️ Setup Instructions

1. Install Requirements

pip install -r requirements.txt

2. Load Data into SQLite

Make sure your CSV files are present, then run:

python load_data.py

This will create real_estate_portfolio.db with 3 tables: properties, agents, and transactions.

3. Run the SQL Queries (Optional)

sqlite3 real_estate_portfolio.db < real_estate_queries.sql

4. Launch the Dashboard

streamlit run real_estate_dashboard.py

📊 Dashboard Features

Top Agents by Sales

Average Sale Price by Property Type

Transactions by State

Monthly Sales Trends

Over List Price Sales Viewer

Each tab shows a chart and/or data table based on queries.

💼 Why This Project

This project demonstrates:

Relational database design

Data ingestion and transformation

Business-focused query writing

Python and SQL integration

Dashboard building with Streamlit

It can be used as a portfolio piece to showcase your data analytics capabilities.

✅ Tools Used

Python 3.8+

SQLite3

Pandas

Streamlit

Plotly

📬 Questions or Feedback?

Feel free to fork, adapt, or reach out with suggestions. Happy analyzing!

