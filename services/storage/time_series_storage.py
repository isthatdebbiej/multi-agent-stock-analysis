import boto3
from utils.logger import get_logger

logger = get_logger("TimeSeriesStorage")

class TimeSeriesStorage:
    def __init__(self, database_name, table_name):
        self.client = boto3.client("timestream-write")
        self.database_name = database_name
        self.table_name = table_name
        logger.info("Connected to Amazon Timestream")

    def write_data(self, records):
        try:
            self.client.write_records(
                DatabaseName=self.database_name,
                TableName=self.table_name,
                Records=records
            )
            logger.info(f"Wrote {len(records)} records to Timestream")
        except Exception as e:
            logger.error(f"Failed to write records: {e}")
            raise
