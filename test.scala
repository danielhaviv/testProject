// Databricks notebook source
print("Hello")

// COMMAND ----------

// MAGIC %sh nc -zv 10.0.27.111 12222

// COMMAND ----------

// MAGIC %sql
// MAGIC select count(*)
// MAGIC from range(1, 100000)
// MAGIC group by id 

// COMMAND ----------

print("Hello from databricks")

// COMMAND ----------

print("Hello from databricks2")

// COMMAND ----------

// MAGIC %python
// MAGIC spark.conf.set("spark.sql.shuffle.partitions", "1024")

// COMMAND ----------

// MAGIC %python
// MAGIC df = spark.range(1,1000000).repartition(1024)

// COMMAND ----------

// MAGIC %python
// MAGIC spark.conf.set("spark.sql.adaptive.enabled", "false")

// COMMAND ----------

// MAGIC %python
// MAGIC df.join(df).count()

// COMMAND ----------

// MAGIC %python
// MAGIC display(dbutils.fs.mounts())

// COMMAND ----------

// MAGIC %fs ls /mnt/yan-data

// COMMAND ----------

// MAGIC %python
// MAGIC dbutils.widgets.dropdown("X123", "1", [str(x) for x in range(1, 10)])

// COMMAND ----------

