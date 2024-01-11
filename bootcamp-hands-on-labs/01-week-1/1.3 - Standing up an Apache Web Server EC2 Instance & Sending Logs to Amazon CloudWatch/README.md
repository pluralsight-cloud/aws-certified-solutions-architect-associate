# 1.3 Standing up Single EC2 Apache Web Server Instance & Sending Logs to Amazon CloudWatch

## Steps

### 1 - Install and Test the CloudWatch Agent

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

### 2 - Setting up the CloudWatch Metric Filter

Now let us st up a metric filter within CloudWatch using this new log stream!

1. First, navigate to a fake page within the Apache Web Server in your browser (**Example**: http://3.87.13.214/fake.html)
2. Navigate back to the CloudWatch Log Stream and view the tailing session. You should see an entry with a `404` in there. We will use this `404` status to create a metric filter and an alarm.
3. End the tailing session, and navigate to the `Apache-Access-Logs` Log Group.
4. On the bottom pane, find and select `Metric filters`
5. Select `Create metric filter`
6. For the *Filter pattern* enter the pattern from below: [Metric Filter Patter](#metric-filter-pattern)
7. Under the _Test pattern_ section, select your Instance ID from the `Select log data to test` dropdown
8. Select `Test pattern`. You should get filtered results.
9. Click `Next`
10. For _Filter name_ enter: `404`
11. Under _Metric details_, for _Metric namespace_ enter `Apache`. Ensure that `Create new` is enabled.
12. For _Metric name_ enter `404`
13. Under _Metric value_ enter the number `1`
14. Leave _Default value_ blank
15. For _Unit_ select `Count` from the dropdown menu
16. Click `Next`
17. Review and then select `Create metric filter`


#### Metric Filter Pattern

Use the following text to create a metric filter that matches for any 404 status codes

```bash
%\b404\b%
```

---

### 3 - Alerting Using the CloudWatch Metric Filter

Now let us set up and alarm based on our recent metric filter.

1. Navigate to the newly created metric filter within the `Apache-Access-Logs` Log Group
2. Select the `404` metric from the metric filter list (_Note: It is the Apache/404 link. Not the first one_). This will bring you to the CloudWatch metrics screen.
3. Click the calendar button and select `5 minutes` from the dropdown. This narrows down the time viewed on the graph.
4. Next, click on the down arrow by the refresh button and select `10 seconds`. This will automatically refresh the graph every 10 seconds for you.
5. Navigate to the web server URL again, and then navigate to the same made up page as before (**Example**: http://3.87.13.214/fake.html)
6. After a bit of time you should begin to see metrics appear on the graph (_This could take up to 5 minutes_)
7. From here, select `Create alarm`
8. Only change two settings from the _Metric_ pane. The first is the **Period**. Change that to `1 minute`.
9. The second setting to change is **Statistic** should be `Sum`.
9. For the _Conditions_ leave the **Threshold Type** on `Static`
10. Set the **Whenever 404 is...** to `Greater/Equal`
11. Set the **than** value to `0`
12. Click `Next`
13. For _Notification_, set **Alarm state trigger** to `In alarm`
14. Under _Send a notification to the following SNS topic_ select `Create new topic`
15. Give your topic a name of `404-Alerts`
16. Add an email for the _Email endpoints that will receive the notification…_ input
17. Click `Create topic`
18. You will need to confirm the subscription in you inbox before continuing
19. Click on `Next`
20. For **Alarm name** enter `404-Detections`
21. Click `Next`
22. Review the settings and then click `Create alarm`
23. Wait a few minutes for the data to get out of an _Insufficient data_ state. Then begin to generate 404 status codes via the made up URL used before. This should trigger your Alarm, sending an SNS message to your email address subscribed to the topic!