
DATABASE_URL = "sqlite:///data_collector.db"  
NEWS_SOURCES = ["https://www.reuters.com/rss", "https://www.bloomberg.com/rss"]
REDDIT_SUBREDDITS = ["stocks", "WallStreetBets"]
FRED_API_KEY = "26f11bc01fe6b9e1a5875b1e0f68265a"  
NEWS_API_KEY = "1016e2533f4b4153b16a86be4e46a2a5"

AWS_CONFIG = {
    "S3_BUCKET": "your-s3-bucket",
    "DYNAMODB_TABLE": "your-dynamodb-table",
    "TIMESTREAM_DB": "your-timestream-db",
    "TIMESTREAM_TABLE": "your-timestream-table",
}

DB_CONFIG = {
    "dbname": "your_db_name",
    "user": "your_user",
    "password": "your_password",
    "host": "your_rds_endpoint",
    "port": 5432,
}

