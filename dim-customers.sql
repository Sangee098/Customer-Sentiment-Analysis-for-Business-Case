--SQL statement to join the dim_customer with dim_geograpgy to enrich the customer data with geographic information

SELECT c.customerID,c.CustomerName,c.Email,c.Gender,c.Age,g.City,g.Country
FROM dbo.customers c
LEFT JOIN 
dbo.geography g
ON c.GeographyID=g.GeographyID;
