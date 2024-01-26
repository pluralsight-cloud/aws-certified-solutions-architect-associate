# CloudWatch Agent Commands

---

## Installation Command

```bash
sudo yum install -y amazon-cloudwatch-agent
```

## Create Config File

```bash 
sudo vim /tmp/cloudwatch-agent-config.json 
```

## Start the Agent

Start the agent with the new config file:

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/tmp/cloudwatch-agent-config.json -s
```

