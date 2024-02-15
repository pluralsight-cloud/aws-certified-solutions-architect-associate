#!/bin/bash

sudo yum update -y
sudo yum install amazon-cloudwatch-agent -y
dnf install rsyslog -y
systemctl enable rsyslog --now

sudo cat <<EOF >>/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
{
    "agent": {
        "metrics_collection_interval": 60,
        "run_as_user": "root",
        "region": "{item("meta-data/placement/availability-zone")}",
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
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json