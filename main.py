from services.data_collector import DataCollector
from services.storage.sql_storage import SQLStorage
from services.storage.nosql_storage import NoSQLStorage
from services.storage.time_series_storage import TimeSeriesStorage
from services.storage.s3_storage import S3Storage
from utils.config import AWS_CONFIG, DB_CONFIG

# Initialize agents
sql_storage = SQLStorage(DB_CONFIG)
nosql_storage = NoSQLStorage(AWS_CONFIG["DYNAMODB_TABLE"])
time_series_storage = TimeSeriesStorage(AWS_CONFIG["TIMESTREAM_DB"], AWS_CONFIG["TIMESTREAM_TABLE"])
s3_storage = S3Storage(AWS_CONFIG["S3_BUCKET"])

# Fetch data
data_collector = DataCollector()
stock_data = data_collector.fetch_stock_prices("AAPL", "2023-01-01", "2023-12-31")
news_headlines = data_collector.scrape_news("https://finance.yahoo.com/")

# Store in RDS
sql_storage.create_table()
sql_storage.insert_data(stock_data)

# Store in DynamoDB
for headline in news_headlines:
    nosql_storage.put_item({"headline": headline})

# Store in S3
s3_storage.upload_file("path/to/stock_data.csv", "stock_data.csv")
