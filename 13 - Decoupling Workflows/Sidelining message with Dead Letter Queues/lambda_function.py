import json
import boto3
import os

sqs = boto3.client("sqs")
QUEUE_URL = os.environ["QUEUE_URL"]


def lambda_handler(event, context):
    for record in event["Records"]:
        try:
            message = json.loads(record["body"])

            # Ensure the message has the expected structure
            if not all(
                key in message
                for key in [
                    "eventId",
                    "orderId",
                    "customerFirstName",
                    "customLastName",
                    "customerEmail",
                ]
            ):
                # sends failed messages back to the SQS queue if needed
                sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps(message))
                print(
                    "Failed to process message. Invalid or missing fields. Returning to queue."
                )
                continue

            # Create and log the formatted string
            formatted_string = f"""
            Event ID: {message['eventId']}
            Order ID: {message['orderId']}
            Customer First Name: {message['customerFirstName']}
            Customer Last Name: {message['customLastName']}
            Customer Email: {message['customerEmail']}
            """

            print(formatted_string)

        except json.JSONDecodeError:
            print("Failed to parse message body")
            continue

    return {"statusCode": 200, "body": "Processing complete"}
