import os
import pulumi
import pulumi_aws as aws

# Setting variables
bucket_name = "our-cool-bucket-name-1231232"
table_name = "TerraformStateLock"
AWS_REGION = os.environ.get("REGION", "us-east-1")


# Create an S3 bucket
bucket = aws.s3.Bucket(bucket_name)

# Create a DynamoDB table
table = aws.dynamodb.Table(
    table_name,
    attributes=[{"name": "LockID", "type": "S"}],
    hash_key="LockID",
    read_capacity=1,
    write_capacity=1,
)

# Export the bucket name and table ARN
pulumi.export("bucket_name", bucket.id)
pulumi.export("table_arn", table.arn)
