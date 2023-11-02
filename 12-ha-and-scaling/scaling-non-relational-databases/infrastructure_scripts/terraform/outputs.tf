output "tf_state_bucket" {
  value       = aws_s3_bucket.tf_state_bucket.id
  description = "Name of the S3 bucket for the state locking."
}

output "tf_state_table" {
  value       = aws_dynamodb_table.tf_state_lock_table.name
  description = "Name of the DynamoDB Table for the state locking."
}
