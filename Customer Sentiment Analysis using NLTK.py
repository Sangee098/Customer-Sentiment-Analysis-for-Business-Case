import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

#to fetch data from the sql database by using sql query
def fetch_data_from_sql(): #We are collecting the data from database, connection paramenter inside the conn_str variable
    conn_str=(
        "Driver={SQL Server};"
        "Server=SANGEETHA\\SQLEXPRESS04;"
        "Database=PortfolioProject_MarketingAnalytics;"
        "Trusted_Connection=yes;"
    )

    conn=pyodbc.connect(conn_str) #connect to database using pyodbc

    query="SELECT ReviewID,CustomerID,ProductID,ReviewDate,Rating,ReviewText FROM dbo.customer_reviews" #sql query to fetch the data 

    df=pd.read_sql(query,conn) #collecting and storing the values in the df variable

    conn.close() #close the connection to free up the resource

    # Return the fetched data as a DataFrame
    return df


customer_review_df=fetch_data_from_sql()  #fetching and storing all the review data in customer_review_df variable

sia= SentimentIntensityAnalyzer() #initializing the vader sentiment analyser 

def calculate_sentiment(reviews):
    sentiment=sia.polarity_scores(reviews) 
    #returns the compound score, which is a normalized score between -1(Most Negative) to 1 (Most postive), we are categorizing based on -0.5 to 0.5
    return sentiment['compound'] 

def categorize_Sentiment(score,rating):  #defining a function to categorize sentiment based on both sentiment score and review ratings
    if score>0.05: #positive review score
        if rating >=4:
            return 'Positive'
        elif rating ==3:
            return 'Mixed posiive' #positive review but neutral rating 
        else:
            return 'Mixed Negative' #positive review but negtive rating
    elif score<-0.05: #Negative review score
        if rating >=4:
            return 'Mixed Postive' #positive rating but negative reviews
        elif rating ==3:
            return 'Mixed Negative' #Neutal rating but negative reviews
        else:
            return 'Negative' #Neutral rating but negative review
    else: #Neutral review
        if rating >= 4:
            return 'Positive' #neutral review and positive rating
        elif rating ==3:
            return 'Neutral' #neutral review and rating
        else:
            return 'Negative' #neutral review and rating 
        

#categorize score to sentiments

def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0' #strongly postive comment
    elif 0.0<=score>0.5:
        return '0.0 to 0.49' # Mildly positive comment
    elif -0.5<=score>0.0:
        return '-0.5 to 0.0' #Mildly Negative Comment
    else:
        return '-1 to -0.49' #Strongly Negative comment
    


#customer_review_df dataframe has all the data retrived from the sql server
#creating 3 new columns in customer_review_df dataframe using the sentiment score as Sentimentscore,SentimentCategory and sentimentBucketList
customer_review_df['Sentimentscore']=customer_review_df['ReviewText'].apply(calculate_sentiment) #applying calculate_sentiment function on ReviewText

customer_review_df['SentimentCategory']=customer_review_df.apply(lambda row:categorize_Sentiment(row['Sentimentscore'],row['Rating']),axis=1) #categorize_Sentiment has two parameters, hence used lambda function to pass the Sentimentscore and rating
#axis=1 indicated the categorize_Sentiment should analyse each row values
customer_review_df['sentimentBucketList']=customer_review_df['Sentimentscore'].apply(sentiment_bucket) #applying the sentiment_bucket function to Sentimentscore

print(customer_review_df.head())

customer_review_df.to_csv('customer_review_with_Sentiment2.csv',index=False) #exporting the data to csv file 
