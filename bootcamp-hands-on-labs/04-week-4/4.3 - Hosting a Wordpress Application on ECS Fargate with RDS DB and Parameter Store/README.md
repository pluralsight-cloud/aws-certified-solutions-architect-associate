# Hosting a Wordpress Application on ECS Fargate with RDS DB and Parameter Store

## Logging in to ECR

> We use the cloud_user profile via access keys to avoid invalid security token errors

```shell
aws ecr get-login-password --region us-east-1 --profile cloud_user | docker login --username AWS --password-stdin
{ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/wordpress
```

## Pull Wordpress Official Image

```shell
docker pull wordpress
```

## Tag Image

```shell
docker tag wordpress {ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/wordpress:latest
```

## Push Image to ECR

```shell
docker push {ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/wordpress:latest
```