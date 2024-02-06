# Sending VPC Flow Logs to S3 and Parsing the Logs via Amazon Athena

## Create SQL Database

```sql
CREATE
DATABASE vpc_flow_logs_db;
```

---

## SQL Create Table Command

This assumes you use the default version fields (_Version 2_)

> The command below creates a table with Parquet formatted data.
> Change the **BUCKET_NAME** text within the LOCATION portion of the SQL query.
> This also assumes you have enabled Hive-compatible prefixes.

```sql
CREATE
EXTERNAL TABLE IF NOT EXISTS `vpc_flow_logs` (
  version int,
  account_id string,
  interface_id string,
  srcaddr string,
  dstaddr string,
  srcport int,
  dstport int,
  protocol bigint,
  packets bigint,
  bytes bigint,
  start bigint,
  `end` bigint,
  action string,
  log_status string
)
PARTITIONED BY (
  `aws-account-id` string,
  `aws-service` string,
  `aws-region` string,
  `year` string, 
  `month` string, 
  `day` string,
  `hour` string
)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://BUCKET_NAME/AWSLogs/'
TBLPROPERTIES (
  'EXTERNAL'='true', 
  'skip.header.line.count'='1'
  )
```

---

## Repair Table and Update Partitions

```sql
MSCK
REPAIR TABLE `vpc_flow_logs`;
```

---

## Fixing Errors

You may run into errors when running the MSCK command. We need to drop the table and database, and then restart.

### Drop Table

```sql
DROP TABLE vpc_flow_logs;
```

### Drop Datatabase

```sql
DROP
DATABASE vpc_flow_logs_db;
```