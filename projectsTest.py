# Databricks notebook source
# MAGIC %pip install function-libs==0.0.1

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

# COMMAND ----------
import mlflow

mlflow.set_experiment("/Users/daniel.haviv@databricks.com/my-experiment")

with mlflow.start_run():
    mlflow.log_param("c", 1)
    mlflow.log_metric("d", 2)
