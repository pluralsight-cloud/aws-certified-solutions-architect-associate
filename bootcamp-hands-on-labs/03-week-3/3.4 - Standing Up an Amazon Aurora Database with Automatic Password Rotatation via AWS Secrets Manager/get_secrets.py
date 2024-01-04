import boto3
import json

# Initialize a session using AWS SDK
session = boto3.session.Session(region_name="us-east-1")
client = session.client(service_name="secretsmanager")

# Define the secret you want to retrieve
secret_name = "YourSecretNameHere"  # Replace with your actual secret name

# Use the client to retrieve the secret
try:
    response = client.get_secret_value(SecretId=secret_name)
    # Error handling omitted for brevity

    # Decode the secret string and convert to JSON
    secret = response["SecretString"]
    secret_dict = json.loads(secret)

    # Extract the username and password values
    username = secret_dict["username"]
    password = secret_dict["password"]

    # Set environment variables values
    DB_USERNAME = username
    DB_PASSWORD = password

    # For confirmation (Not to be used in production)
    print("Copy and paste the following line to export Environment Variables for use:")
    print(f"export DB_USERNAME={DB_USERNAME} && export DB_PASSWORD='{DB_PASSWORD}'")

except Exception as e:
    print(f"Error retrieving secret: {e}")
