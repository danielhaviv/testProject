# Databricks notebook source
dbutils.widgets.dropdown("X123", "1", [str(x) for x in range(1, 10)])

dbutils.widgets.dropdown("1", "1", [str(x) for x in range(1, 10)], "hello this is a widget")

dbutils.widgets.dropdown("x123123", "1", [str(x) for x in range(1, 10)], "hello this is a widget")

dbutils.widgets.dropdown("x1232133123", "1", [str(x) for x in range(1, 10)], "hello this is a widget 2")


# COMMAND ----------

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

params = list([1,2,5,10])
rdd = sc.parallelize(params)
spark.createDataFrame(params, "int").createOrReplaceTempView("join_params")


# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT OVERWRITE partitiontest2 partition (id = getArgument("X123"))
# MAGIC select * from range(100)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * 
# MAGIC from range(100)
# MAGIC -- join join_params on (id=value)
# MAGIC -- where id in (select value from join_params)
# MAGIC -- where id = getArgument("X123")

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC show partitions partitiontest2

# COMMAND ----------

# MAGIC %sql
# MAGIC create table partitiontest2 (name string, id int)
# MAGIC partitioned by (id)
# MAGIC location '/tmp/danieltestpartitions'

# COMMAND ----------

# MAGIC %sql
# MAGIC insert overwrite partitiontest2 
# MAGIC select 'daniel', 6

# COMMAND ----------

spark.conf.set("Amos", "Itai")

# COMMAND ----------

# MAGIC %scala
# MAGIC spark.conf.get("Amos")

# COMMAND ----------

# MAGIC %sh find / -mount -name "conf"  

# COMMAND ----------


