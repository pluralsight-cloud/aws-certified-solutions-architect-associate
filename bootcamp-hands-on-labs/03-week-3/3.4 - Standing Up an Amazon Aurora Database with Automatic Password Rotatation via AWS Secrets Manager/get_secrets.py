import boto3
import json
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "REPLACE_ME"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    # Initialize a session using AWS SDK
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']

    # JSON loading secret
    secret_dict = json.loads(secret)

    # Extract the username and password values from the secret
    username = secret_dict["username"]
    password = secret_dict["password"]

    # Setting file path for saving current values
    file_path = "/tmp/secret_values.txt"
    value_to_write = f"EXPORT MYSQL_USERNAME={username}\nEXPORT MYSQL_PASSWORD={password}"

    # Writing values to local text file
    try:
        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write the value to the file
            file.write(value_to_write)

        print(f"Value successfully written to file at {file_path}")

    except Exception as e:
        print(f"Error writing to file: {e}")
