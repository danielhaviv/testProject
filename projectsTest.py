# Databricks notebook source


# COMMAND ----------
import mlflow

mlflow.set_experiment("/Users/daniel.haviv@databricks.com/my-experiment")

with mlflow.start_run():
    mlflow.log_param("c", 1)
    mlflow.log_metric("d", 2)
