-- real_estate_queries.sql

-- 1. Top 5 agents by total sales
SELECT a.name, a.agency, SUM(t.sales_price) AS total_sales
FROM agents a
JOIN transactions t ON a.agent_id = t.agent_id
GROUP BY a.agent_id
ORDER BY total_sales DESC
LIMIT 5;

-- 2. Average sale price by property type
SELECT p.type, ROUND(AVG(t.sales_price), 2) AS avg_sales_price
FROM transactions t
JOIN properties p ON t.property_id = p.property_id
GROUP BY p.type;

-- 3. Number of transactions by state
SELECT p.state, COUNT(t.transaction_id) AS total_transactions
FROM transactions t
JOIN properties p ON t.property_id = p.property_id
GROUP BY p.state
ORDER BY total_transactions DESC;

-- 4. Monthly sales trends
SELECT 
  strftime('%Y-%m', t.sales_date) AS month,
  COUNT(*) AS total_sales,
  ROUND(AVG(t.sales_price), 2) AS avg_price
FROM transactions t
GROUP BY month
ORDER BY month;

-- 5. Properties that sold above listing price
SELECT p.address, p.city, p.state, p.list_price, t.sales_price
FROM transactions t
JOIN properties p ON t.property_id = p.property_id
WHERE t.sales_price > p.list_price
ORDER BY t.sales_price - p.list_price DESC;
