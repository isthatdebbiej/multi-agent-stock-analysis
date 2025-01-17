import boto3
from utils.logger import get_logger

logger = get_logger("NoSQLStorage")

class NoSQLStorage:
    def __init__(self, table_name):
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(table_name)
        logger.info(f"Connected to DynamoDB table {table_name}")

    def put_item(self, item):
        try:
            self.table.put_item(Item=item)
            logger.info("Inserted item into DynamoDB")
        except Exception as e:
            logger.error(f"Failed to insert item: {e}")
            raise
