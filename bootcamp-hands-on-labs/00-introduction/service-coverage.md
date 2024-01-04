
# In-Scope AWS Services

This document is meant to be a best-effort note of  which services are covered within the projects nested within this bootcamp.

## Key

✅ = Used

❌ = Cannot Use in Sandbox

⚠️ = Theoretical Coverage / Partial Usage

❔= Unknown / Might run into issues

## Analytics

| Service Name                                             | Coverage |
|----------------------------------------------------------|----------|
| Amazon Athena                                            | ✅        |
| AWS Data Exchange                                        | ❌        |
| AWS Data Pipeline                                        | ⚠️       |
| Amazon EMR                                               | ⚠️       |
| AWS Glue (w/ Athena)                                     | ✅        |
| Amazon Kinesis                                           | ✅        |
| AWS Lake Formation                                       | ⚠️       |
| Amazon Managed Streaming for Apache Kafka (Amazon MSK)   | ⚠️       |
| Amazon OpenSearch Service (Amazon Elasticsearch Service) | ❌        |
| Amazon QuickSight                                        | ❌        |
| Amazon Redshift ️                                        | ⚠️       |

## Application Integration

| Service Name                                    | Coverage |
|-------------------------------------------------|----------|
| Amazon AppFlow ️                                | ❌        |
| AWS AppSync                                     | ❌        |
| Amazon EventBridge (Amazon CloudWatch Events)   | ✅        |
| Amazon MQ                                       | ❔        |
| Amazon Simple Notification Service (Amazon SNS) | ✅        |
| Amazon Simple Queue Service (Amazon SQS)        | ✅        |
| AWS Step Functions                              |          |

## AWS Cost Management

| Service Name              | Coverage |
|---------------------------|----------|
| AWS Budgets               | ❌        |
| AWS Cost and Usage Report | ❌        |
| AWS Cost Explorer         | ❌        |
| Savings Plans             | ❌        |

## Compute

| Service Name                          | Coverage |
|---------------------------------------|----------|
| AWS Batch                             | ✅        |
| Amazon EC2                            | ✅        |
| Amazon EC2 Auto Scaling               | ✅        |
| AWS Elastic Beanstalk                 |          |
| AWS Outposts                          | ❌        |
| AWS Serverless Application Repository | ⚠️       |
| VMware Cloud on AWS                   | ❌        |
| AWS Wavelength                        | ❌        |

## Containers

| Service Name        | Coverage |
|---------------------|----------|
| Amazon ECR          | ✅        |
| Amazon ECS          | ✅        |
| Amazon ECS Anywhere | ❌        |
| Amazon EKS          | ⚠️       |
| Amazon EKS Anywhere | ❌        |
| Amazon EKS Distro   | ❌        |

## Database

| Service Name                                   | Coverage |
|------------------------------------------------|----------|
| Amazon Aurora                                  |          |
| Amazon Aurora Serverless                       |          |
| Amazon DocumentDB (with MongoDB compatibility) | ⚠️       |
| Amazon DynamoDB                                | ✅        |
| Amazon ElastiCache                             | ⚠️       |
| Amazon Keyspaces (for Apache Cassandra)        | ⚠️       |
| Amazon Neptune                                 | ⚠️       |
| Amazon Quantum Ledger Database (Amazon QLDB)   |          |
| Amazon RDS                                     | ✅        |
| Amazon Redshift                                | ⚠️       |
| Amazon Timestream                              | ⚠️       |

## Developer Tools

| Service Name | Coverage |
|--------------|----------|
| AWS X-Ray    |          |

## Front-End Web and Mobile

| Service Name       | Coverage |
|--------------------|----------|
| AWS Amplify        | ❌        |
| Amazon API Gateway | ✅        |
| AWS Device Farm    | ❌        |
| Amazon Pinpoint    | ❌        |

## Machine Learning

| Service Name          | Coverage |
|-----------------------|----------|
| Amazon Comprehend     | ⚠️       |
| Amazon Forecast       | ⚠️       |
| Amazon Fraud Detector | ❌        |
| Amazon Kendra ️       | ⚠️       |
| Amazon Lex ️          | ⚠️       |
| Amazon Polly ️        | ⚠️       |
| Amazon Rekognition ️  | ⚠️       |
| Amazon SageMaker      | ⚠️       |
| Amazon Textract ️     | ⚠️       |
| Amazon Transcribe ️   | ⚠️       |
| Amazon Translate ️    | ⚠️       |

## Management and Governance

| Service Name                            | Coverage      |
|-----------------------------------------|---------------|
| AWS Auto Scaling                        | ✅             |
| AWS CloudFormation                      | ✅             |
| AWS CloudTrail                          | ✅             |
| Amazon CloudWatch                       | ✅             |
| AWS Command Line Interface (AWS CLI)    | ✅             |
| AWS Compute Optimizer                   | ❌             |
| AWS Config ️                            | ⚠️            |
| AWS Control Tower                       | ❌             |
| AWS License Manager                     | ❌             |
| Amazon Managed Grafana ️                | ⚠️            |
| Amazon Managed Service for Prometheus ️ | ⚠️            |
| AWS Management Console                  | ✅             |
| AWS Organizations                       | ❌             |
| AWS Personal Health Dashboard           |               |
| AWS Proton                              | ❌             |
| AWS Service Catalog                     | ❌             |
| AWS Systems Manager  (_Partial_)        | ✅ (_Partial_) |
| AWS Trusted Advisor                     |               |
| AWS Well-Architected Tool               | ❌             |

## Media Services

| Service Name                   | Coverage |
|--------------------------------|----------|
| Amazon Elastic Transcoder ️    | ⚠️       |
| Amazon Kinesis Video Streams ️ | ⚠️       |

## Migration and Transfer

| Service Name                                              | Coverage |
|-----------------------------------------------------------|----------|
| AWS Application Discovery Service                         | ❌        |
| AWS Application Migration Service (CloudEndure Migration) | ❌        |
| AWS Database Migration Service (AWS DMS)                  | ❌        |
| AWS DataSync                                              | ❌        |
| AWS Migration Hub                                         | ❌        |
| AWS Server Migration Service (AWS SMS)                    | ❌        |
| AWS Snow Family                                           | ❌        |
| AWS Transfer Family                                       | ❌        |

## Networking and Content Delivery:

| Service Name                 | Coverage |
|------------------------------|----------|
| Amazon CloudFront            |          |
| AWS Direct Connect           | ❌        |
| Elastic Load Balancing (ELB) | ✅        |
| AWS Global Accelerator       |          |
| AWS PrivateLink              |          |
| Amazon Route 53 ️            | ⚠️       |
| AWS Transit Gateway          |          |
| Amazon VPC                   | ✅        |
| AWS VPN                      |          |

## Security, Identity, and Compliance

| Service Name                               | Coverage |
|--------------------------------------------|----------|
| AWS Artifact                               | ❌        |
| AWS Audit Manager                          | ❌        |
| AWS Certificate Manager (ACM)              | ❌        |
| AWS CloudHSM                               | ❌        |
| Amazon Cognito ️                           | ⚠️       |
| Amazon Detective                           | ❌        |
| AWS Directory Service                      | ❌        |
| AWS Firewall Manager                       | ❌        |
| Amazon GuardDuty                           | ❌        |
| AWS Identity and Access Management (IAM) ✅ | ✅        |
| Amazon Inspector                           |          |
| AWS Key Management Service (AWS KMS) ✅     | ✅        |
| Amazon Macie                               | ❌        |
| AWS Network Firewall                       |          |
| AWS Resource Access Manager (AWS RAM)      | ❌        |
| AWS Secrets Manager                        |          |
| AWS Security Hub                           | ❌        |
| AWS Shield                                 | ❌        |
| AWS Single Sign-On                         | ❌        |
| AWS WAF                                    |          |

## Serverless

| Service Name | Coverage |
|--------------|----------|
| AWS AppSync  |          |
| AWS Fargate  | ✅        |
| AWS Lambda   | ✅        |

## Storage

| Service Name                            | Coverage |
|-----------------------------------------|----------|
| AWS Backup                              |          |
| Amazon Elastic Block Store (Amazon EBS) | ✅        |
| Amazon Elastic File System (Amazon EFS) |          |
| Amazon FSx (for all types)              |          |
| Amazon S3                               | ✅        |
| Amazon S3 Glacier                       | ❌        |
| AWS Storage Gateway                     | ❌        |
