# 4.4 - Hosting a Wordpress Application on ECS Fargate with RDS DB and Parameter Store

> WORK IN PROGRESS. LIKELY TO BE REMOVED OR CHANGED.

## Create the RDS Database

1. Navigate to the Amazon RDS service.
2. Under **Databases** find and select `Create database`.
3. Select `MySQL` from the list of engine types.
4. Leave the default _Edition_ selected, which should be `MySQL Community`.
5. For _Engine version_ select version `MySQL 8.0.35`.
5. Under **Templates** select `Free Tier`.
7. Move to **Settings**. For _DB cluster identifier_ optionally change the name for the cluster or leave the default.
7. Leave the _Master username_ set to `admin`.
8. Check the box for the option to `Manage master credentials in AWS Secrets Manager`
9. Leave the default encryption key for the Secrets Manager credentials
10. Move to **Instance configuration**. For _DB instance class_, under _Standard classes_ select `db.t4g.micro`.
11. For the **Storage** section, set the _Storage type_ to `gp3`.
12. Change the allocate storage to `20 GiB`.
13. Select `Don’t connect to an EC2 compute resource`
14. Place the database in the custom VPC, **NOT** the default VPC.
15. Choose the _DB subnet group_.
16. Set _Public access_ to `No`.
18. For _VPC security group (firewall)_ select `Create new`. Provide a name of your choosing (Example: _DatabaseSG_).
21. SKip down to the **Additional configuration** dropdown menu. Within the _Database options_ set the _Initial database name_ to `WordpressDB`.
21. Leave the rest of the options set to the defaults.
22. Find and select `Create database`.

> Creation of the DB cluster could take several minutes. In the meantime, move onto creating the SSM parameters and ECR/ECS resources.

## SSM Parameter Store Steps here

## ECS and ECR Steps here