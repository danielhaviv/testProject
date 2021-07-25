// Databricks notebook source
// MAGIC %sql
// MAGIC 
// MAGIC SELECT * FROM cloud_files("/databricks-datasets/retail-org/sales_orders/", "json", map("cloudFiles.inferColumnTypes", "true"))

// COMMAND ----------

// MAGIC %sh nc -zv 10.0.27.111 12222

// COMMAND ----------

// MAGIC %sql
// MAGIC select count(*)
// MAGIC from range(1, 100000)
// MAGIC group by daniel

// COMMAND ----------

print("Hello from databricks")

// COMMAND ----------

print("Hello from databricks")

// COMMAND ----------

// MAGIC %sql
// MAGIC select * from (show tables)

// COMMAND ----------

// MAGIC %python
// MAGIC tables = spark.sql("show tables").collect()
// MAGIC for table in tables:
// MAGIC   ddl = spark.sql("show create table " + table["tableName"]).collect()
// MAGIC   print(ddl)

// COMMAND ----------

spark.sql("show create table " + tables[tableName].tableName)

// COMMAND ----------

// MAGIC %sql
// MAGIC show tables

// COMMAND ----------

// MAGIC %sql
// MAGIC select * from aapl_parquet 

// COMMAND ----------

// MAGIC %sql
// MAGIC create view danieldemoview
// MAGIC as select * From aapl_parquet

// COMMAND ----------

// MAGIC %sql
// MAGIC select * from danieldemoview
// MAGIC where Date='2018-05-04'

// COMMAND ----------

// MAGIC %sql
// MAGIC select * from cloudfiles()

// COMMAND ----------

// MAGIC %scala 
// MAGIC import io.lemonlabs.uri.Url
// MAGIC 
// MAGIC val url = Url.parse("https://www.scala-lang.org")

// COMMAND ----------


