--Query to clean the whitespace issue in reviews

SELECT reviewID,CustomerID,ProductID,ReviewDate,rating, REPLACE(Reviewtext,'  ',' ') AS reviewtext FROM customer_reviews --Replacing the double space with ' ' with the help of REPLACE
ORDER BY rating desc;
