# Databricks notebook source
dbutils.widgets.dropdown("X123", "1", [str(x) for x in range(1, 10)])

# COMMAND ----------

print("hello value is:", dbutils.widgets.get("X123"))

# COMMAND ----------

# MAGIC %sh
# MAGIC curl http://169.254.169.254/latest/dynamic/instance-identity/document

# COMMAND ----------

import boto3
client = boto3.client('ec2', "us-west-2")

client.describe_tags()

# COMMAND ----------


