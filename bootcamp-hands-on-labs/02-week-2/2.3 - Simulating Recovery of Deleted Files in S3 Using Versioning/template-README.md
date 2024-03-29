# starting_infrastructure
# Description
Create an S3 bucket with a 'randomized' name.

## Parameters
The list of parameters for this template:


## Resources
The list of resources this template creates:

### MyBucket 
Type: AWS::S3::Bucket  
### MyLambdaFunction 
Type: AWS::Lambda::Function  
### MyLambdaRole 
Type: AWS::IAM::Role  
### MyApi 
Type: AWS::ApiGateway::RestApi  
### MyApiInvokeLambdaPermission 
Type: AWS::Lambda::Permission  
### MyApiRootMethod 
Type: AWS::ApiGateway::Method  
### MyApiDeployment 
Type: AWS::ApiGateway::Deployment  
### MyApiStage 
Type: AWS::ApiGateway::Stage  

## Outputs
The list of outputs this template exposes:

### BucketName 
Description: Name of the S3 bucket  

### ApiEndpoint 
Description: URL of the API Gateway endpoint  

### StageEndpoint 
Description: URL of the "v1" stage  

