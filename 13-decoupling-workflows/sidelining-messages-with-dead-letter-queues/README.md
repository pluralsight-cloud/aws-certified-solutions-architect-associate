# Sidelining Messages with Dead Letter Queues

Relevant documentation for this lesson.

## Creating the Lambda Function IAM Policy

Let's work on creating the IAM policy for this demo.

1. Navigate to Lambda and create your new function. Select `Author from scratch`

![Creating Function](./images/1-function.png)

2. Under **Permissions**, select `Create a new role from AWS policy templates`, and then provide a name for your IAM
   Role.

![Creating Function Role](./images/2-function.png)

3. Open up the dropdown menu, then find and select `Amazon SQS poller permissions`

![SQS permissions](./images/3-function.png)

4. Navigate to the newly created IAM Role and select it.

6. Find and select the Policy starting with `AWSLambdaSQSPollerExecutionRole-`

![IAM Role](./images/4-function.png)

6. Once within the Policy page, find and select `Edit`

![Editing Policy](./images/5-function.png)

7. Select the `JSON` format editor, and then paste in
   the [sqs_perm_only_lambda_function_iam_policy.json](./sqs_perm_only_lambda_function_iam_policy.json) contents.
   Overwrite the existing contents.

![Pasting Policy](./images/6-function.png)

8. **IMPORTANT**: Change the `<ACCOUNT_ID>` within the policy to match your AWS Account ID number!

![Pasting Policy](./images/7-function.png)

9. Click on `Next`, ensure you have `Set this new version as the default` checkbox selected, and then
   click `Save changes`
10. You are done with the IAM role!