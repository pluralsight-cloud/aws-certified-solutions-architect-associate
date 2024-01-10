# 1.3 Standing up Single EC2 Apache Web Server Instance & Sending Logs to Amazon CloudWatch

## Steps

### 1. Install the CloudWatch Agent

```bash
sudo yum install -y amazon-cloudwatch-agent
```

### 2. Create Agent Config File

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

### 4. Setting up the CloudWatch Metric Filter

Use the following text to create a metric filter that matches for any 404 status codes

```bash
%\b404\b%
```