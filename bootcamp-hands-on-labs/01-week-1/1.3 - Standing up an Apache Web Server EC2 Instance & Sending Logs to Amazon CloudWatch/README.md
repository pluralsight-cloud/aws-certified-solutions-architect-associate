# 1.3 Standing up Single EC2 Apache Web Server Instance & Sending Logs to Amazon CloudWatch

## Steps

### 1. Install and Test the CloudWatch Agent

Let's go ahead and install the Amazon CloudWatch Agent

1. Navigate to Amazon EC2
2. Find the **ApacheWebServer** instance and select it
3. Locate and select `Connect`
4. Under the _Session Manager_ menu, select `Connect`
5. Once install the agent using the the following code: [Install CloudWatch Agent](#installation-command)
6. Now, create the agent config file that will contain the configuration: [Create Agent Config File](#create-config-file)
7. Within the file, copy and paste the following code: [Agent Config File](#fill-in-the-config-file)
8. Save the file (press **esc** and then enter `:wq!` and then press **enter**)
9. Restart the agent and load the newly created config file: [Reload Agent](#start-the-agent)
11. Navigate to Amazon CloudWatch
12. Find and select `Log Groups`
13. Select `Apache-Access-Logs` from the Log Groups list
14. You should see a Log Stream with the instance ID, select it
15. Find and select the `Start tailing` button on the top right 
16. Navigate to the public IP of the web server and refresh the page several times. (_Make sure you are connecting via HTTP and not HTTPS_)
17. You should start seeing logs entries appear in the log stream

#### Installation Command

```bash
sudo yum install -y amazon-cloudwatch-agent
```

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

#### Start the Agent

Start the agent with the new config file:

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/tmp/cloudwatch-agent-config.json -s
```

---

### Setting up the CloudWatch Metric Filter

Now let us test metric filters and alarms within CloudWatch using this new log stream!

1. First, navigate to a fake page within the Apache Web Server in your browser (**Example**: http://3.87.13.214/fake.html)
2. Navigate back to the CloudWatch Log Stream and view the tailing session. You should see an entry with a `404` in there. We will use this `404` status to create a metric filter and an alarm.
3. End the tailing session, and navigate to the `Apache-Access-Logs` Log Group.
4. On the bottom pane, find and select `Metric filters`
5. Select `Create metric filter`
6. For the *Filter pattern* enter the pattern from below: [Metric Filter Patter](#metric-filter-pattern)
7. Under the _Test pattern_ section, select your Instance ID from the `Select log data to test` dropdown
8. Select `Test pattern`. You should get filtered results.
9. Click `Next`
10. 


#### Metric Filter Pattern

Use the following text to create a metric filter that matches for any 404 status codes

```bash
%\b404\b%
```

## Guide

### 1. 