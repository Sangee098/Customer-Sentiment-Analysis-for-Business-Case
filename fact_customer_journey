--Query to find the duplicate values in the customer journey data by using the CTE(Common Table Expression)

WITH DuplicateRecords AS  
(SELECT Journeyid,customerid, productid,visitdate, stage, Action, Duration,
--Using Windows function ROW_NUMBER(), all the duplicate values having the same customerid, productid,visitdate, stage, Action values will be numbered as 2 
ROW_NUMBER() OVER (PARTITION BY customerid, productid,visitdate, stage, Action ORDER BY Journeyid) AS row_num FROM dbo.customer_journey ) 

SELECT * FROM DuplicateRecords
WHERE row_num>1; --To filter only the duplicate value and confirm that the data has 79 duplicate values

-- Outer query selects the final cleaned and standardized data

SELECT Journeyid,customerid, productid,visitdate, UPPER(stage) AS stage, Action,
COALESCE(duration,avg_duration) as Duration --replace the null values with the avg_duration of the specific date, which can be retrieved from the sub_query
FROM 
(SELECT Journeyid,customerid, productid,visitdate, stage, Action, duration,
AVG(duration) OVER(PARTITION BY visitDate) as avg_duration,  --Average duration of the specific date as we are partitioning the data based on the visit_date
ROW_NUMBER() OVER (PARTITION BY customerID, productid,visitdate, stage, action ORDER BY Journeyid) as row_number FROM customer_journey) AS subquery
WHERE row_number=1; --retrieving only the first occurrence of the duplicate group identified in the subquery
