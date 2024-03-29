# starting_infrastructure
# Description
CloudFormation to create a VPC, Subnets, ALB and an EC2 instance

## Parameters
The list of parameters for this template:

### InstanceType 
Type: String 
Default: t3.small 
Description: EC2 instance type 
### LatestAmiId 
Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> 
Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2  

## Resources
The list of resources this template creates:

### MyVPC 
Type: AWS::EC2::VPC  
### PublicSubnet1 
Type: AWS::EC2::Subnet  
### PublicSubnet2 
Type: AWS::EC2::Subnet  
### PublicSubnet3 
Type: AWS::EC2::Subnet  
### PrivateSubnet1 
Type: AWS::EC2::Subnet  
### PrivateSubnet2 
Type: AWS::EC2::Subnet  
### PrivateSubnet3 
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
### RouteTablePrivate1 
Type: AWS::EC2::RouteTable  
### RouteTablePrivate1Association1 
Type: AWS::EC2::SubnetRouteTableAssociation  
### RouteTablePrivate1Route0 
Type: AWS::EC2::Route  
### RouteTablePrivate2 
Type: AWS::EC2::RouteTable  
### RouteTablePrivate2Association1 
Type: AWS::EC2::SubnetRouteTableAssociation  
### RouteTablePrivate2Route0 
Type: AWS::EC2::Route  
### RouteTablePrivate3 
Type: AWS::EC2::RouteTable  
### RouteTablePrivate3Association1 
Type: AWS::EC2::SubnetRouteTableAssociation  
### RouteTablePrivate3Route0 
Type: AWS::EC2::Route  
### Igw 
Type: AWS::EC2::InternetGateway  
### IGWAttachment 
Type: AWS::EC2::VPCGatewayAttachment  
### NatGw1 
Type: AWS::EC2::NatGateway  
### NatGw1ElasticIP 
Type: AWS::EC2::EIP  
### SystemsManagerRole 
Type: AWS::IAM::Role  
### InstanceProfile 
Type: AWS::IAM::InstanceProfile  
### EC2Instance 
Type: AWS::EC2::Instance  
### ALBSecurityGroup 
Type: AWS::EC2::SecurityGroup  
### InstanceSecurityGroup 
Type: AWS::EC2::SecurityGroup  
### LoadBalancer 
Type: AWS::ElasticLoadBalancingV2::LoadBalancer  
### TargetGroup 
Type: AWS::ElasticLoadBalancingV2::TargetGroup  
### Listener 
Type: AWS::ElasticLoadBalancingV2::Listener  

## Outputs
The list of outputs this template exposes:

### LoadBalancerDNSName 
Description: DNS Name of the Load Balancer  

