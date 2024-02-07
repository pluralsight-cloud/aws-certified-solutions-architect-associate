import boto3
from botocore.exceptions import ClientError
import random
import os

TABLE_NAME = os.getenv("TABLE_NAME", default="Quotes")


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE_NAME)  # Replace with your DynamoDB table name

    try:
        # Perform the scan operation on the table
        response = table.scan()
        items = response["Items"]

        # Check if the table has items
        if not items:
            return {"statusCode": 404, "body": "No items found in the table."}

        # Select a random item
        random_item = random.choice(items)
        print(random_item)
        return {"statusCode": 200, "body": f'{random_item["quote"]} -- {random_item["author"]}'}

    except ClientError as e:
        print(e)
        return {"statusCode": 500, "body": "Error scanning the DynamoDB table."}
