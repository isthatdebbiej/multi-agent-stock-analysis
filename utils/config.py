
NEWS_SOURCES = [
    "https://www.reuters.com/rss", 
    "https://www.bloomberg.com/rss"
]

REDDIT_SUBREDDITS = ["stocks", "WallStreetBets"]

FRED_API_KEY = "your-api-key"  
NEWS_API_KEY = "your-api-key"

AWS_CONFIG = {
    "S3_BUCKET": "your-s3-bucket",  # S3 bucket name
    "DYNAMODB_TABLE": "your-dynamodb-table",  # DynamoDB table name
    "TIMESTREAM_DB": "your-timestream-db",  # Timestream database name
    "TIMESTREAM_TABLE": "your-timestream-table",  # Timestream table name
}

DB_CONFIG = {
    "dbname": "your_db_name",  # RDS database name
    "user": "your_user",  # RDS username
    "password": "your_password",  # RDS password
    "host": "your_rds_endpoint",  # RDS host endpoint (e.g., rds.amazonaws.com)
    "port": 5432,  # RDS port (default for PostgreSQL)
}

# NoSQL - DynamoDB configuration
NOSQL_CONFIG = {
    "DYNAMODB_TABLE": "your-dynamodb-table",  # DynamoDB table name
    "REGION": "us-west-2"  # AWS region (e.g., us-west-2)
}

# S3 - S3 storage configuration
S3_CONFIG = {
    "S3_BUCKET": "your-s3-bucket",  # S3 bucket name for storing files
    "REGION": "us-west-2"  # AWS region (e.g., us-west-2)
}

# TimeSeries - Timestream configuration
TIMESTREAM_CONFIG = {
    "DB_NAME": "your-timestream-db",  # Timestream database name
    "TABLE_NAME": "your-timestream-table",  # Timestream table name
    "REGION": "us-west-2"  # AWS region (e.g., us-west-2)
}

