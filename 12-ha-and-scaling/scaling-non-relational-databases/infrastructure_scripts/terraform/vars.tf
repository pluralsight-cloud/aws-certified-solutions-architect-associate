variable "tf_state_bucket" {
  description = "The name of your Terraform state S3 bucket."
  type        = string
}

variable "tf_state_table" {
  description = "The name of your Terraform state DynamoDB table."
  type        = string
}
