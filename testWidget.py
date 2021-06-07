# Databricks notebook source
dbutils.widgets.dropdown("X123", "1", [str(x) for x in range(1, 10)])

# COMMAND ----------

print("hello value is:", dbutils.widgets.get("X123"))

# COMMAND ----------


