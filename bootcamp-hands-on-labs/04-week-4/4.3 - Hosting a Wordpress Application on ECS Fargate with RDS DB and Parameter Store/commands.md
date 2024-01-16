# Commands used in this week's demo

## Image and ECR

### Logging in to ECR

```shell
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin
{ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/wordpress
```

### Pull Wordpress Official Image

```shell
docker pull wordpress
```

### Tag and Push Image to ECR

```shell
docker tag wordpress {ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/wordpress:latest
docker push {ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/wordpress:latest
```