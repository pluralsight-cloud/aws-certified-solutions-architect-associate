# starting_infrastructure
# Description
Create a VPC with an Auto Scaling Group of EC2 instances. Fronts the ASG with an Application Load Balancer. Meant for us-east-1. No key pairs, only Session Manager for connecting to EC2. VPC contains Public and Private subnets that span 3-AZ in the Region.


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

### VPC 
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
### DatabaseSubnet1 
Type: AWS::EC2::Subnet  
### DatabaseSubnet2 
Type: AWS::EC2::Subnet  
### DatabaseSubnet3 
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
### RouteTableDatabase1Association 
Type: AWS::EC2::SubnetRouteTableAssociation  
### RouteTableDatabase2Association 
Type: AWS::EC2::SubnetRouteTableAssociation  
### RouteTableDatabase3Association 
Type: AWS::EC2::SubnetRouteTableAssociation  
### Igw 
Type: AWS::EC2::InternetGateway  
### IGWAttachment 
Type: AWS::EC2::VPCGatewayAttachment  
### NatGw1 
Type: AWS::EC2::NatGateway  
### NatGw1ElasticIP 
Type: AWS::EC2::EIP  
### SystemsManagerEC2Role 
Type: AWS::IAM::Role  
### EC2InstanceProfile 
Type: AWS::IAM::InstanceProfile  
### ApplicationLoadBalancer 
Type: AWS::ElasticLoadBalancingV2::LoadBalancer  
### TargetGroup 
Type: AWS::ElasticLoadBalancingV2::TargetGroup  
### MyListener 
Type: AWS::ElasticLoadBalancingV2::Listener  
### MyAutoScalingGroup 
Type: AWS::AutoScaling::AutoScalingGroup  
### LaunchTemplate 
Type: AWS::EC2::LaunchTemplate  
### AlbSecurityGroup 
Type: AWS::EC2::SecurityGroup  
### Ec2SecurityGroup 
Type: AWS::EC2::SecurityGroup  

## Outputs
The list of outputs this template exposes:

### LoadBalancerDNSName 
Description: DNS Name of the ALB  

