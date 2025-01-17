import os
from services.data_collector.fred_api import FREDData
from services.data_collector.yahoo_finance import YahooFinance
from services.data_collector.reddit_scrapper import RedditScraper
from services.data_collector.news_api import NewsScraper
from services.data_collector.sec_scrapper import SECFilings
from services.storage.sql_storage import SQLStorage
from services.storage.nosql_storage import NoSQLStorage
from services.storage.time_series_storage import TimeSeriesStorage
from services.storage.s3_storage import S3Storage
from utils.config import AWS_CONFIG, DB_CONFIG, S3_CONFIG, NOSQL_CONFIG, TIMESTREAM_CONFIG
from utils.db_handler import DBHandler

# Initialize agents
sql_storage = SQLStorage(DB_CONFIG)
nosql_storage = NoSQLStorage(NOSQL_CONFIG["DYNAMODB_TABLE"])
time_series_storage = TimeSeriesStorage(TIMESTREAM_CONFIG["DB_NAME"], TIMESTREAM_CONFIG["TABLE_NAME"])
s3_storage = S3Storage(S3_CONFIG["S3_BUCKET"])

def fetch_data():
    # Fetch Yahoo Finance Data
    yahoo_data = YahooFinance.fetch_historical_data("AAPL", "2023-01-01", "2023-12-31")
    print("Yahoo Finance Data:", yahoo_data)
    
    # Fetch News
    news = NewsScraper.fetch_rss_news(["https://www.reuters.com/rss", "https://www.bloomberg.com/rss"])
    print("News Articles:", news)
    
    # Fetch Reddit Data
    reddit_scraper = RedditScraper(client_id="your_client_id", client_secret="your_client_secret", user_agent="your_user_agent")
    reddit_posts = reddit_scraper.fetch_subreddit_posts("stocks")
    print("Reddit Posts:", reddit_posts)

    # Fetch SEC Filings
    sec_filings = SECFilings.fetch_filings("0000320193", "10-K")
    print("SEC Filings:", sec_filings)

    # Fetch FRED Data
    fred_data = FREDData(api_key="26f11bc01fe6b9e1a5875b1e0f68265a")
    economic_data = fred_data.fetch_series("GDP", "2020-01-01", "2023-12-31")
    print("FRED Data:", economic_data)

    return yahoo_data, news, reddit_posts, sec_filings, economic_data


def store_data(yahoo_data, news, reddit_posts, sec_filings, economic_data):
    # Store data in SQL (RDS)
    sql_storage.create_table()
    sql_storage.insert_data("yahoo_data", yahoo_data)
    
    # Store News in DynamoDB (NoSQL)
    for headline in news:
        nosql_storage.put_item({"headline": headline})
    
    # Store Reddit Posts in DynamoDB (NoSQL)
    for post in reddit_posts:
        nosql_storage.put_item({"post": post})
    
    # Store SEC Filings in S3
    for filing in sec_filings:
        s3_storage.upload_file(filing['file_path'], filing['file_name'])
    
    # Store FRED Data in Timestream (TimeSeries)
    for record in economic_data:
        time_series_storage.write_to_timeseries(record)

def main():
    db_handler = DBHandler(DB_CONFIG["dbname"], DB_CONFIG["user"], DB_CONFIG["password"], DB_CONFIG["host"], DB_CONFIG["port"])
    db_handler.connect()

    yahoo_data, news, reddit_posts, sec_filings, economic_data = fetch_data()

    store_data(yahoo_data, news, reddit_posts, sec_filings, economic_data)
    
    db_handler.close()

if __name__ == "__main__":
    main()
