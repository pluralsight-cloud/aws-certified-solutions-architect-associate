# Installing and Configuring the Amazon CloudWatch Agent (Linux)

To configure the CloudWatch agent on a Linux instance to send custom application log files to CloudWatch, you need to follow these steps:

1. Create an IAM role with the relevant permissions and attach it to the Linux instance. (_see policy below_)
2. Install the CloudWatch agent in the instance.
3. Prepare the Configuration File (Manually).
4. Start the CloudWatch agent service in the instance (Manually).
5. Monitor the logs using CloudWatch web console.

## 1 - IAM Policy example

**Role Name**: AmazonEC2SessionManagerRole

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
      ],
      "Resource": ["*"]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:DescribeAssociation",
        "ssm:GetDeployablePatchSnapshotForInstance",
        "ssm:GetDocument",
        "ssm:DescribeDocument",
        "ssm:GetManifest",
        "ssm:GetParameter",
        "ssm:GetParameters",
        "ssm:ListAssociations",
        "ssm:ListInstanceAssociations",
        "ssm:PutInventory",
        "ssm:PutComplianceItems",
        "ssm:PutConfigurePackageResult",
        "ssm:UpdateAssociationStatus",
        "ssm:UpdateInstanceAssociationStatus",
        "ssm:UpdateInstanceInformation"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssmmessages:CreateControlChannel",
        "ssmmessages:CreateDataChannel",
        "ssmmessages:OpenControlChannel",
        "ssmmessages:OpenDataChannel"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2messages:AcknowledgeMessage",
        "ec2messages:DeleteMessage",
        "ec2messages:FailMessage",
        "ec2messages:GetEndpoint",
        "ec2messages:GetMessages",
        "ec2messages:SendReply"
      ],
      "Resource": "*"
    }
  ]
}
```

## 2 - Install CloudWatch Agent

Execute this user data at launch, or you can copy and paste each line as you see fit:

```bash
#!/bin/bash

sudo yum update -y

# Installing the agent
sudo yum install amazon-cloudwatch-agent -y

# Allowing rsyslogs to be collected and saved. This is NOT a default in AML2023
dnf install rsyslog -y
systemctl enable rsyslog --now

# Echo the config file contents into the JSON file.
sudo cat <<EOF >>/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
{
    "agent": {
        "metrics_collection_interval": 60,
        "run_as_user": "root",
        "region": "us-east-1",
        "debug": true
    },
    "logs": {
        "logs_collected": {
            "files": {
                "collect_list": [
                    {
                        "file_path": "/var/log/messages",
                        "log_group_name": "{instance_id}",
                        "log_stream_name": "messages",
                        "timezone": "UTC"
                    },
                    {
                        "file_path": "/var/log/secure",
                        "log_group_name": "{instance_id}",
                        "log_stream_name": "secure",
                        "timezone": "UTC"
                    }
                ]
            }
        }
    }
}
EOF

# Do not copy this if you want to manually start this agent.
# Fetching local config and starting agent
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```

## 3 - Prepare the Configuration File (Manually)

If you want to manually implement the file instead of using the above user data script, then here is a sample JSON you can use.

**File Location:** /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json

```json
{
  "agent": {
    "metrics_collection_interval": 60,
    "run_as_user": "root",
    "region": "us-east-1",
    "debug": true
  },
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/messages",
            "log_group_name": "{instance_id}",
            "log_stream_name": "messages",
            "timezone": "UTC"
          },
          {
            "file_path": "/var/log/secure",
            "log_group_name": "{instance_id}",
            "log_stream_name": "secure",
            "timezone": "UTC"
          }
        ]
      }
    }
  }
}
```

## 4 - Start the CloudWatch agent service in the instance (Manually)

Only needed if you did not run the full user data above.

### Starting and fetching config

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```

### Starting with existing config already fetched

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a start -m ec2 -s
```

## 5 - Monitor the logs using CloudWatch web console.

Your logs should now be pushing to CloudWatch Logs!
