import boto3
import json


def lambda_handler(event, context):
    print(f"Received event: {event}")

    # Setting boto3 client
    ec2 = boto3.client("ec2")

    # Grabbing instance ID from event
    instance_id = event["detail"]["instance-id"]

    # Restarting instance
    response = ec2.start_instances(InstanceIds=[instance_id])
    print("Started instance: " + instance_id)
    return {"statusCode": 200, "body": json.dumps("Started instance: " + instance_id)}
