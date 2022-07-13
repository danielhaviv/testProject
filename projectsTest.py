# Databricks notebook source
print("Goodbye Kenshoo")

# COMMAND ----------

print("Hello")



# COMMAND ----------

print("Hello from github")

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC select * from table

# COMMAND ----------

# MAGIC %sh ls -ld /mnt/driver-deamon/*

# COMMAND ----------

import mlflow

with mlflow.start_run():
    mlflow.log_param("x", 1)
    mlflow.log_metric("y", 2)
