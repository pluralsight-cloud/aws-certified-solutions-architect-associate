# starting_infrastructure
# Description
Create a VPC with EC2 instance and IAM role for Systems Manager in us-east-1. No key pairs. Creates a Log Group for Apache Access Logs.


## Parameters
The list of parameters for this template:

### LatestAmiId 
Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> 
Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2  

## Resources
The list of resources this template creates:

### VPC 
Type: AWS::EC2::VPC  
### PublicSubnet1 
Type: AWS::EC2::Subnet  
### PublicSubnet2 
Type: AWS::EC2::Subnet  
### PublicSubnet3 
Type: AWS::EC2::Subnet  
### RouteTablePublic 
Type: AWS::EC2::RouteTable  
### RouteTablePublicAssociation1 
Type: AWS::EC2::SubnetRouteTableAssociation  
### RouteTablePublicAssociation2 
Type: AWS::EC2::SubnetRouteTableAssociation  
### RouteTablePublicAssociation3 
Type: AWS::EC2::SubnetRouteTableAssociation  
### RouteTablePublicRoute0 
Type: AWS::EC2::Route  
### Igw 
Type: AWS::EC2::InternetGateway  
### IGWAttachment 
Type: AWS::EC2::VPCGatewayAttachment  
### ApacheLogGroup 
Type: AWS::Logs::LogGroup  
### SystemsManagerEC2Role 
Type: AWS::IAM::Role  
### EC2InstanceProfile 
Type: AWS::IAM::InstanceProfile  
### EC2Instance 
Type: AWS::EC2::Instance  
### MySecurityGroup 
Type: AWS::EC2::SecurityGroup  

## Outputs
The list of outputs this template exposes:

### WebServerDNS 
Description: The public DNS address of the web server  

