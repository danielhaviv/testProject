# Databricks notebook source
import mlflow
with mlflow.start_run():
    mlflow.log_param("x", 2)
    mlflow.log_metric("y", 1)

# COMMAND ----------


