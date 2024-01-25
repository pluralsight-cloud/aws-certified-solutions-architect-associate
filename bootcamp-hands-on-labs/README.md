# Project Introduction

> This is a Work in Progress!

Hello! 👋

Welcome to the **AWS Certified Solutions Architect Associate** exam hands-on capstone project!
Within this repository, you will find different hands-on projects that are meant to serve as an interactive way of
learning the different concepts required to pass the **AWS SAA-C03** exam.

The different demonstrations and labs are broken into 4 separate weeks.
This framework was decided on in order to provide a more condensed, rapid pace for learning and passing the exam.

While it is designed with a 4-week timeline in mind, by no means, do you need to complete this within that time frame.
Please, take the time that works for you. We are not wanting to just cram the content for the sake of doing it quickly.
Everyone learns at a different pace, and everyone has their own blocks of free time/study time that they can dedicate.
There is no one-size fits all approach with this. In other words...

**Take the time you need that is required to best reinforce what you are learning!**

## Project Framework

Let us breakdown what you can expect on a weekly basis for this project.
Each week will consist of different learning concepts, goals, and objectives.

### Week 1

Here, we will begin by reviewing some of the core concepts required for this exam.
You will work with some of the fundamental services like AWS IAM and Amazon EC2 (along with a few other topics related to these.)

#### 1.1 - Creating and Assuming an Administrator AWS IAM Role

Work on creating a new AdminAccess IAM Role that you will assume and for leveraging tasks.
We will also work on creating a CloudFormation template that allows you to leverage this IAM Role easily in future projects. 

#### 1.2 - Creating a CloudTrail Trail and EventBridge Alert for Console Sign-Ins

You will create your very own CloudTrail Trail for capturing all API activity and events within your AWS accounts.
We will dive into log file validation and integrity, and cover details on why you would use this in the real-world.
After, you will create a new Amazon EventBridge Rule that sends a notification to your chosen email whenever a specific IAM user logs in to the console.

#### 1.3 - Standing up an Apache Web Server EC2 Instance & Sending Logs to Amazon CloudWatch

During this project, you will deploy a single EC2 instance that hosts a simple Apache Web Server.
Once deployed and verified as working, you will then set up custom CloudWatch Logs for all HTTPD logs captured on the host.
Using the above CloudWatch Logs, you will create a metric and alarm based on any ERROR captures in the log files.

### Week 2

#### 2.1 - Creating a Custom AMI and Deploying an Auto Scaling Group

Now that we have some basics covered from week 1, let's build off of that!
In this project, we will go ahead and standup another Apache Web Server EC2 instance, but this time, we will look at how
 to create a custom AMI using the instance. 
Once the AMI is created we will deploy the AMI using a Launch Template that is used by an Auto Scaling Group that site 
behind an Application Load Balancer (ALB). 

#### 2.2 - Assigning Static IPs to NLBs with ALB Target Groups

During this project, you will deploy two different ELBs.
The first will be a ALB that will route traffic to the same type of Auto Scaling Group used before. However, this time, 
the ALB will be a private ALB (not interent accessible).
Once the ALB is created and deployed, we will then deploy a public-facing NLB that will front the ALB we created.
With the NLB, we will see how you can assign static IPs to the NLB endpoints, allowing for easier allow-listing and 
reference for any custom DNS entries you may have.


#### 2.3 - Simulating Recovery of Deleted Files in S3 Using Versioning

With this project, you will demonstrate setting up a production S3 bucket for storage of an organizations critical files.
While setting this bucket up, we will ensure we turn on versioning of files.
Once versioning is in place, we will simulate "accidental deletion" of said files in the bucket, and then look at how 
we can easily restore the last working version using Delete Markers.

### Week 3

Week 3 will begin to move into more advanced topics and scenarios. 

#### 3.1 - Deploying a Serverless Application Using AWS Lambda, API Gateway, and DynamoDB

Let's explore deploying a simple serverless application using several key services that will appear on this exam.
You will deploy an API Gateway to front your application, and this gateway will invoke a Lambda Function that interacts
with an Amazon DynamoDB table within your account.

#### 3.2 - Trigger a Batch Process using Amazon SQS

In this hands-on learning activity, you will trigger a batch process task using SQS.
This learning activity uses images on the format to showcase the batch processing architecture.
Objects uploaded to the input S3 bucket trigger an event that sends object details to the SQS queue.
The ECS task deploys a Docker container that reads from that queue, parses the message containing the object name,
and then downloads the object. Once transformed, it will upload the objects to the S3 output bucket.

#### 3.3 - Implementing Blue Green Deployments via Amazon Elastic Beanstalk

In this lab, we will create a blue/green deployment using Elastic Beanstalk.
We will accomplish this by creating and cloning an Elastic Beanstalk environment.
This is an important concept if you're looking to avoid disrupting live applications when testing changes to the application.
By the end of this lab, you should be able to create your very own blue/green deployment using Elastic Beanstalk

#### 3.4 - Standing Up an Amazon Aurora Database with Automatic Password Rotation via AWS Secrets Manager

In this hands-on project, you will explore setting up a brand-new Amazon Aurora MySQL database, and an EC2 instance that
will be used to connect to said database. During database creation, you will leverage AWS Secrets Manager to create and 
manage your DB password for you.
Within the EC2, you will leverage the Secrets Manager password to create a new table and populate sample data generated for you.
After testing is completed, you will then force rotation of the DB password, and verify you no longer can connect with
the old credentials.
You will then re-establish connection using the new, automatically updated credentials!

### Week 4

This week touches on a lot of remaining services to make sure we cover as much as possible!

#### 4.1 - Sending VPC Flow Logs to S3 via Kinesis Data Firehose

Let's work on creating a VPC-wide Flow Log, and send those to a Kinesis Data Firehose for easy, scalable ingestion.
We will demonstrate transformation of the log records using a Lambda function as well.

#### 4.2 - Sending Subnet VPC Flow Logs to S3 & Parsing the Logs via Amazon Athena

In this project, you will create a VPC Flow Log for a specific subnet that will mimic a proprietary application.
We will send the data to Amazon S3 directly, and then query that data using Amazon Athena using SQL-like commands.

#### 4.3 - Using ALB Behind Amazon CloudFront & Use a Custom Header to Control Access

For this hands-on work, you will create a simple webpage with static and dynamic content using an Amazon EC2 instance.
This EC2 instance will be in an Auto Scaling Group that is fronted by a public-facing ALB.
We want to restrict access to the ALB to only come from Amazon CloudFront. You will create a new distribution that
leverages the ALB as an origin server.
Once in place, we will implement security controls to enforce all connections to flow through CloudFront instead of 
directly hitting the ALB. We will do so using Custom Header requirements!

#### 4.4 - Hosting a Wordpress Application on ECS Fargate with RDS DB and Parameter Store

For this project, you will stand up a new Wordpress application hosted on ECS Fargate containers.
We will demonstrate creating an Amazon RDS instance to store our data, and creating new AWS Systems Manager Parameter 
Store Parameters to use as Environment Variables within our Task Definitions.
Using these parameters, we will automatically connect to our RDS instance while setting up our Wordpress app!