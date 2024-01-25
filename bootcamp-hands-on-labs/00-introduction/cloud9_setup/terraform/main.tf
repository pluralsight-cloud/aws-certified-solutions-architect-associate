provider "aws" {
  region = var.aws_region
}

terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.15.0"
    }
  }
}

resource "aws_cloud9_environment_ec2" "cloud9" {
  instance_type   = "t3.small"
  name            = "csaa"
  connection_type = "CONNECT_SSM"
}
