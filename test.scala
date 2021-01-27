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

// MAGIC %python
// MAGIC spark.sqlContext.conf.set("spark.redis.host", "server1")
// MAGIC loadedDf = spark.read.option("spark.redis.host", "server1").format("org.apache.spark.sql.redis").option("table", "person").load()

// COMMAND ----------

// MAGIC %python
// MAGIC from pyspark.sql import SparkSession
// MAGIC 
// MAGIC spark2 = SparkSession.builder.config("spark.redis.host", "server2").config("spark.redis.port", "6379").getOrCreate();
// MAGIC             
// MAGIC spark.conf.set("spark.redis.host", "server1")
// MAGIC spark._jsc.getConf().set("spark.redis.host", "server1")
// MAGIC spark.sparkContext.getConf().set("spark.redis.host", "server1")
// MAGIC loadedDf = spark2.read.option("spark.redis.host", "server1").format("org.apache.spark.sql.redis").option("table", "person").load()

// COMMAND ----------

// MAGIC %python
// MAGIC from pyspark.sql import SparkSession
// MAGIC 
// MAGIC spark2 = SparkSession.builder.appName("myApp").config("spark.redis.host", "server9").config("spark.redis.port", "6379").config("spark.redis.auth", "passwd").getOrCreate()
// MAGIC 
// MAGIC 
// MAGIC loadedDf = spark2.read.option("spark.redis.host", "server1").format("org.apache.spark.sql.redis").option("table", "person").load()

// COMMAND ----------

