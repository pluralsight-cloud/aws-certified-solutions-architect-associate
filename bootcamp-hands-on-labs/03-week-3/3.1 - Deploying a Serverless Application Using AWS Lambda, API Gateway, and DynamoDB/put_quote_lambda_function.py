import boto3
from botocore.exceptions import ClientError
import http.client
import json
import os

TABLE_NAME = os.getenv("TABLE_NAME", default="Quotes")


def get_quote():
    # Get a random quote from the internet
    conn = http.client.HTTPSConnection("zenquotes.io")
    conn.request("GET", "/api/random")
    response = conn.getresponse()

    if response.status == 200:
        data = json.loads(response.read().decode())
        quote = data[0]["q"]
        author = data[0]["a"]

        # Return the quote in the response
        return {"quote": quote, "author": author}
    else:
        # Handle any potential errors
        return {"body": f"Failed to fetch a quote. Error code: {response.status}"}


def put_quote(quote):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE_NAME)

    item = {
        "quote": quote["quote"],
        "author": quote["author"],
    }

    try:
        response = table.put_item(Item=item)
        return "Quote successfully written to DynamoDB."
    except ClientError as e:
        print(e)
        return "Error writing item to DynamoDB."


def lambda_handler(event, context):
    return put_quote(get_quote())
