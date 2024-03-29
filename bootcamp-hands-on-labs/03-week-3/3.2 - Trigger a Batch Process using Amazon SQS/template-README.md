# .\cfn_template
# Description
AWS CloudFormation template for deploying an ECS environment for handling batch workloads. The CloudFormation template creates an input and an output S3 bucket. Objects uploaded to the input S3 bucket creates an event that is put in a SQS queue. The ECS task contains a Docker container that pulls messages from the queue, reads the content and downloads the corresponding object from the S3 bucket. The Docker container then transforms the object and uploads it to the output S3 bucket. In this example template we are using images, in jpg format, to showcase the batch workload ECS architecture. Upload images with a .jpg suffix in the input S3 bucket to trigger the event.

## Parameters
The list of parameters for this template:

### DesiredCapacity 
Type: Number 
Default: 1 
Description: Number of desired instances in the AutoScaling Group and ECS Cluster 
### MaxSize 
Type: Number 
Default: 2 
Description: Maximum number of instances in the AutoScaling Group and ECS Cluster 
### DockerImage 
Type: String 
Default: andruestesq2c/csaa-ecs-batch:latest 
Description: Docker repository and image file to deploy as part of the ECS task. In the form repository/image 
### ECSAMI 
Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> 
Default: /aws/service/ecs/optimized-ami/amazon-linux-2/recommended/image_id 
Description: AMI ID 
### InstanceType 
Type: String 
Default: t3.small 
Description: The EC2 instance type 
### SSHLocation 
Type: String 
Default: 0.0.0.0/0 
Description: The IP address range that can be used to SSH to the EC2 instances 

## Resources
The list of resources this template creates:

### VPC 
Type: AWS::EC2::VPC  
### PublicSubnetOne 
Type: AWS::EC2::Subnet  
### PublicSubnetTwo 
Type: AWS::EC2::Subnet  
### InternetGateway 
Type: AWS::EC2::InternetGateway  
### GatewayAttachement 
Type: AWS::EC2::VPCGatewayAttachment  
### PublicRouteTable 
Type: AWS::EC2::RouteTable  
### PublicRoute 
Type: AWS::EC2::Route  
### PublicSubnetOneRouteTableAssociation 
Type: AWS::EC2::SubnetRouteTableAssociation  
### PublicSubnetTwoRouteTableAssociation 
Type: AWS::EC2::SubnetRouteTableAssociation  
### SQSBatchQueue 
Type: AWS::SQS::Queue  
### SQSBatchQueuePolicy 
Type: AWS::SQS::QueuePolicy  
### SQSDeadLetterQueue 
Type: AWS::SQS::Queue  
### SQSCloudWatchAlarm 
Type: AWS::CloudWatch::Alarm  
### myS3InputBucket 
Type: AWS::S3::Bucket  
### myS3OutputBucket 
Type: AWS::S3::Bucket  
### ECSCluster 
Type: AWS::ECS::Cluster  
### TaskDefinition 
Type: AWS::ECS::TaskDefinition  
### ECSAutoScalingGroup 
Type: AWS::AutoScaling::AutoScalingGroup  
### ContainerInstances 
Type: AWS::AutoScaling::LaunchConfiguration  
### InstanceSecurityGroup 
Type: AWS::EC2::SecurityGroup  
### ECSServiceRole 
Type: AWS::IAM::Role  
### AmazonEC2ContainerServiceAutoscaleRole 
Type: AWS::IAM::Role  
### EC2Role 
Type: AWS::IAM::Role  
### ECSTaskRole 
Type: AWS::IAM::Role  
### EC2InstanceProfile 
Type: AWS::IAM::InstanceProfile  

## Outputs
The list of outputs this template exposes:

### Cluster 
Description: The name of the ECS cluster  

### Task 
Description: The name of the ECS Task Definition  

### SQSBatchQueue 
Description: The SQS queue that is used to hold messages containing the name of the uploaded objects  

### InputBucket 
Description: The S3 bucket where images can be uploaded to  

### OutputBucket 
Description: The S3 bucket holding the resized images and thumbnails  

