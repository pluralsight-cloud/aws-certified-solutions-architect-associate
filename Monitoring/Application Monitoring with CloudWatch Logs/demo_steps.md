# Installing and Configuring the Amazon CloudWatch Agent (Linux)

To configure the CloudWatch agent on a Linux instance to send custom application log files to CloudWatch, you need to follow these steps:

1. Create an IAM role with the relevant permissions and attach it to the Linux instance.
2. Install the CloudWatch agent in the instance.
3. Prepare the configuration file in the instance.
4. Start the CloudWatch agent service in the instance.
5. Monitor the logs using CloudWatch web console.

Here is a brief overview of each step:

1. Create an IAM role with relevant permissions and attach it to Linux instance:

   - Create an AWS Role for CloudWatch.
   - Create an AWS Policy of type (Service) "CloudWatch Logs" in the AWS console and add following permissions for all resources:
     - CreateLogStream
     - DescribeLogStreams
     - CreateLogGroup
     - PutLogEvents
   - Name the policy (_Eg. CWPol-LinuxLog_). This is done in the visual editor.
   - Create an AWS Role of type EC2 and name the role Eg, _CWRole-LinuxLog_.
   - Add the above policy _CWPol-LinuxLog_ to Role _CWRole-LinuxLog_.

2. Install the CloudWatch agent in the instance:

   - Install the awslogs package using `sudo yum install awslogs`.
   - Edit file `/etc/awslogs/awscli.conf` and change your AWS Region.

3. Prepare the configuration file in the instance:

   - Edit file `/etc/awslogs/awslogs.conf` and verify following lines:
     ```
     [/var/log/messages]
     datetime_format = %b %d %H:%M:%S
     file = /var/log/messages
     buffer_duration = 5000
     log_stream_name = {instance_id}
     initial_position = start_of_file
     log_group_name = AMZ-2
     ```
   - The above configuration will create a hierarchical structure in the CloudWatch interface with log_group_name AMZ-2 (an arbitrary name) as a container and respective instance id as the object where contents of `/var/log/messages` file is redirected. `buffer_duration` specifies the time duration for batching of log events.

4. Start the CloudWatch agent service in the instance:

   - Run `sudo service awslogs start`.

5. Monitor logs using CloudWatch web console:
   - Go to your AWS Management Console and navigate to **CloudWatch** > **Logs** > **Log groups**.
   - Select your log group from list of groups.
   - Select your log stream from list of streams.

Please note that this is a general overview, and you may need to modify these steps based on your specific use case.
