--Query to clean and normalize the engagement data 


SELECT e.EngagementID, e.ContentID, 
Upper(REPLACE(e.ContentType,'Socialmedia','Social Media')) AS ContentType, --using REPLACE, replacing 'Socialmedia' to 'Social Media' and converting them to uppercase using UPPER
Likes, 
FORMAT(CONVERT(DATE,EngagementDate),'dd.MM.yyyy') AS EngagementDate, -- converting the EngagementDate to Date type and formatting that to 'dd.mm.yyyy' format
e.CampaignID,e.ProductID, 
LEFT(e.Viewsclickscombined,CHARINDEX('-',e.Viewsclickscombined)-1) AS Views, --Using CHARINDEX and - placement, seggregating the Viewsclickscombined to views and clicks seperately
RIGHT(e.Viewsclickscombined,LEN(e.Viewsclickscombined)-CHARINDEX('-',Viewsclickscombined)) AS clicks --Subtracting the length by '-' index to retrive the clicks 
FROM engagement_data e
WHERE e.ContentType != 'NEWSLETTER'; --Filter out rows where the content type is 'Newsletter' as these are not relevent for our analysis
