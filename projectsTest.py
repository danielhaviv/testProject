# Databricks notebook source


# COMMAND ----------

print("Goodbye!!")

# COMMAND ----------

print("Hello")

# COMMAND ----------

# Hi Similarweb

# COMMAND ----------

# MAGIC %pip install boto3

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from table

# COMMAND ----------

# MAGIC %sh ls -ld /mnt/driver-deamon/*

# COMMAND ----------

import mlflow

with mlflow.start_run():
    mlflow.log_param("c", 1)
    mlflow.log_metric("d", 2)

# COMMAND ----------



