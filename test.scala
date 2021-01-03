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

