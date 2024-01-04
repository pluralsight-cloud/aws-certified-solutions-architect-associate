# 1.3 Standing up Single EC2 Apache Web Server Instance & Sending Logs to Amazon CloudWatch

## Steps

### 1. EC2 User Data

Copy this user data into the EC2 launch config:

```bash
#!/bin/bash
# Updating YUM. Installing HTTPD.
yum update -y
yum install -y httpd.x86_64

# Starting and enabling HTTPD
systemctl start httpd.service
systemctl enable httpd.service

# Setting homepage index.html file.
cat <<EOF >> /var/www/html/index.html
<html>
    <style>
    
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
    }
    </style>
    <title>Pluralsight CSAA Prep</title>
    <body>
        <span style="padding-top: 200px;"></span>
        <img src="https://aestes-ps-static-assets-us-east-1.s3.amazonaws.com/public-assets/ps-logo.png" style="max-width: 400px; display: block; margin-left: auto; margin-right: auto; width: 50%;"/>
        <span style="padding-top: 100px;"></span>
        <p></p>
        <h1> <center>Hello Cloud Gurus from $(hostname -f)!</center></h1>
    </body>
<html>
EOF

# Restarting HTTPD service.
systemctl restart httpd.service
```

### 2. Install the CloudWatch Agent

```bash
sudo yum install -y amazon-cloudwatch-agent
```

### 3. Create Agent Config File

#### Create Config File

```bash 
sudo vim /tmp/cloudwatch-agent-config.json 
```

#### Fill In the Config File

__/tmp/cloudwatch-agent-config.json__

```json
{
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/httpd/access_log",
            "log_group_name": "Apache-Access-Logs",
            "log_stream_name": "{instance_id}"
          },
          {
            "file_path": "/var/log/httpd/error_log",
            "log_group_name": "Apache-Error-Logs",
            "log_stream_name": "{instance_id}"
          }
        ]
      }
    }
  }
}
```

### 3. Start the Agent

Start the agent with the new config file:

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/tmp/cloudwatch-agent-config.json -s
```