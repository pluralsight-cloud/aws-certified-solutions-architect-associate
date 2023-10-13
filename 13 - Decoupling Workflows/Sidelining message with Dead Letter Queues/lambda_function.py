import json
import boto3
import os

sqs = boto3.client("sqs")
DLQ_URL = os.environ["DLQ_URL"]


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
                send_to_dlq(message, "Invalid message format")
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


def send_to_dlq(message, reason):
    try:
        sqs.send_message(
            QueueUrl=DLQ_URL,
            MessageBody=json.dumps({"originalEvent": message, "failureReason": reason}),
        )
    except Exception as e:
        print(f"Failed to send message to DLQ: {e}")
