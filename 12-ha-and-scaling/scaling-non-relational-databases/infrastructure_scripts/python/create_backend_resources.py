import boto3
import logging
import os

# Setting variables
bucket_name = "our-cool-bucket-name-1231232"
table_name = "TerraformStateLock"
AWS_REGION = os.environ.get("REGION", "us-east-1")

# Create a session
session = boto3.Session(region=AWS_REGION)

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create an S3 client using the session
s3 = session.client("s3")

# Create an S3 bucket
try:
    logger.info(f"Creating S3 bucket {bucket_name}")
    s3.create_bucket(Bucket=bucket_name)
except:
    logger.error(f"Failed to create S3 bucket {bucket_name}")
    raise

# Create a DynamoDB client and table
dynamodb = session.client("dynamodb")

try:
    logger.info(f"Creating DynamoDB table {table_name}")
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "LockID", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "LockID", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 2, "WriteCapacityUnits": 2},
    )
except:
    logger.error(f"Failed to create DynamoDB table {table_name}")
    raise
