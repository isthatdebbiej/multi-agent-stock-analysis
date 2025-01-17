import boto3
from utils.logger import get_logger

logger = get_logger("S3Storage")

class S3Storage:
    def __init__(self, bucket_name):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name
        logger.info(f"Connected to S3 bucket {bucket_name}")

    def upload_file(self, file_path, object_name):
        try:
            self.s3.upload_file(file_path, self.bucket_name, object_name)
            logger.info(f"Uploaded {object_name} to S3")
        except Exception as e:
            logger.error(f"Failed to upload file: {e}")
            raise
