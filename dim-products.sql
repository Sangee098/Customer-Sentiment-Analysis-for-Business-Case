--SQL query to categorize products based on their price


SELECT ProductID,ProductName,Price, 
CASE WHEN price < 50 THEN 'low'
     WHEN price BETWEEN 50 AND 200 THEN 'medium'
	 ELSE 'high'
END AS Price_Category
FROM dbo.products;
