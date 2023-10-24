"""CloudWatch Logs Application Example

Return: Returns the body from a POST request and logs it
to CloudWatch logs.
"""

import logging
import boto3
from botocore.exceptions import ClientError
from flask import Flask, request
import os

app = Flask(__name__)

# Create a CloudWatch client
cloudwatch = boto3.client("logs")

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a handler for CloudWatch logs
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
logger.addHandler(handler)

# Setting global environment variables
LOG_GROUP_NAME = os.environ["LOG_GROUP_NAME"]
LOG_STREAM_NAME = os.environ["LOG_STREAM_NAME"]


@app.route("/", methods=["POST"])
def log():
    # Get the log message from the request body
    message = request.get_data().decode("utf-8")

    # Send the log message to CloudWatch logs
    try:
        response = cloudwatch.put_log_events(
            logGroupName=os.environ["LOG_GROUP_NAME"],
            logStreamName=os.environ["LOG_STREAM_NAME"],
            logEvents=[
                {"timestamp": int(round(time.time() * 1000)), "message": message}
            ],
        )
        logger.info("Sent message to CloudWatch logs: %s", message)
    except ClientError as e:
        logger.error("Failed to send message to CloudWatch logs: %s", e)

    return "OK"


@app.route("/", methods=["GET"])
def home():
    return "Pluralsight and ACG for life!"


if __name__ == "__main__":
    app.run()
