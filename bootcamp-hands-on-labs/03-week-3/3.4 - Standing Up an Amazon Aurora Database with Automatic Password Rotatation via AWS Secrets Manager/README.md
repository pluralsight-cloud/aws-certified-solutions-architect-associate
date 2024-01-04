# Deploying a Serverless Application Using AWS Lambda, API Gateway, and DynamoDB

---

## Load the File for Import via User Data

```bash
#!/bin/bash

sudo dnf update
sudo dnf install mariadb105 python python-pip -y

pip install boto3 mysql.connector 

touch /home/ec2-user/employees.txt

cat <<EOF > /home/ec2-user/employees.txt
1,Smith,John,john.smith@email.com
2,Doe,Jane,jane.doe@email.com
3,Brown,Sam,sam.brown@email.com
4,Johnson,Pat,pat.johnson@email.com
5,White,Terry,terry.white@email.com
6,Taylor,Alex,alex.taylor@email.com
7,Moore,Linda,linda.moore@email.com
8,Jackson,Ricky,ricky.jackson@email.com
9,Lee,Wendy,wendy.lee@email.com
10,Garcia,Carlos,carlos.garcia@email.com
11,Miller,Zack,zack.miller@email.com
12,Davis,Lucy,lucy.davis@email.com
13,Martinez,Miguel,miguel.martinez@email.com
14,Robinson,Neil,neil.robinson@email.com
15,Clark,Ruby,ruby.clark@email.com
16,Rodriguez,José,jose.rodriguez@email.com
17,Lewis,Grace,grace.lewis@email.com
18,Lee,Brian,brian.lee@email.com
19,Walker,Paul,paul.walker@email.com
20,Hall,Emma,emma.hall@email.com
21,Allen,Gary,gary.allen@email.com
22,Young,Donna,donna.young@email.com
23,Hernandez,Joan,joan.hernandez@email.com
24,King,Larry,larry.king@email.com
25,Wright,Laura,laura.wright@email.com
26,Lopez,Charles,charles.lopez@email.com
27,Hill,Jessica,jessica.hill@email.com
28,Scott,Earl,earl.scott@email.com
29,Green,Andrea,andrea.green@email.com
30,Adams,Shirley,shirley.adams@email.com
EOF
```

## Install MySQL/MariaDB Client

1. sudo dnf install mariadb105
2. mysql --version

## Export DB_HOSTNAME

```bash
export DB_HOST='REPLACE_ME'
```

## Connect to MySQL Amazon Aurora DB

```bash
mysql -h ${DB_HOST} -P 3306 -u %ADMIN_USERNAME% -p
```

## Create Demo Database

```mysql
CREATE DATABASE employeeDB; 
```

## Use the Employee Database

```mysql
USE employeeDB;
```

## Create Demo Table

```mysql
CREATE TABLE Employees
(
    EmployeeId int,
    LastName   varchar(255),
    FirstName  varchar(255),
    Email      varchar(255)
);
```

## Show Tables

```mysql
SHOW TABLES;
```

## Describe Employees Table

```mysql
DESCRIBE Employees;
```

## Import the Data from the local file

```bash
LOAD DATA LOCAL INFILE '/home/ec2-user/employees.txt' INTO TABLE Employees
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
```

## Export DB_PASSWORD, DB_USERNAME on EC2 & Connect to Aurora DB

```bash
python get_secret.py

mysql -h ${DB_HOST} -P 3306 -u ${DB_USERNAME} -p${DB_PASSWORD}
```

## Delete All From Table

```mysql
DELETE
FROM Employees;
```
