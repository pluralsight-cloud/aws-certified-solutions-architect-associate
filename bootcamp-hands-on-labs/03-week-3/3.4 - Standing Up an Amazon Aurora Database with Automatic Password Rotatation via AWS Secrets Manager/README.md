# Standing Up an Amazon Aurora Database with Automatic Password Rotatation via AWS Secrets Manager

## Create employees.txt File

> Creates the local file on the EC2 client for importing later

```shell
cat <<EOF > /home/ssm-user/employees.txt
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

## Connecting to Database

> Connect to the MySQL database instance. Mus change the _host_ and and _user_ values

```shell
mysql --host=CHANGE_TO_WRITER_ENDPOINT_NAME --user=CHANGE_TO_ADMIN_USERNAME --password employees_db
```

## Creating Employees Table

> Create the Employees table on the MySQL employees_db database

```mysql
CREATE TABLE Employees
(
    EmployeeId int,
    LastName   varchar(255),
    FirstName  varchar(255),
    Email      varchar(255)
);
```

## Importing/Loading Employees.txt File Data

> Import the employees.txt file data into the **Employees** table

```mysql
LOAD DATA LOCAL INFILE '/home/ssm-user/employees.txt' INTO TABLE Employees
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n';
```

## Rotate Secret Immediately Using AWS CLI

```shell
aws secretsmanager rotate-secret --secret-id 'CHANGE_ME_TO_SECRET_NAME' --region us-east-1
```