# Databricks notebook source
import mlflow
with mlflow.start_run():
    mlflow.log_param("x", 1)
    mlflow.log_metric("y", 2)

# COMMAND ----------


