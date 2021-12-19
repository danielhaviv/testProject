# Databricks notebook source
import mlflow
with mlflow.start_run():
    mlflow.log_param("x", 3)
    mlflow.log_metric("y", 4)

# COMMAND ----------

# MAGIC %sh
# MAGIC rm -rf /dbfs//tmp/daniel.haviv@databricks.com/copyinto

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists danieldelta;
# MAGIC create table danieldelta (id long)
# MAGIC using delta
# MAGIC location '/tmp/daniel.haviv@databricks.com/copyinto'

# COMMAND ----------

# MAGIC %sql
# MAGIC set spark.databricks.delta.schema.autoMerge.enabled=true;
# MAGIC COPY INTO danieldelta
# MAGIC FROM (SELECT * FROM '/tmp/daniel.haviv@databricks.com/jsondata/')
# MAGIC FILEFORMAT = JSON
# MAGIC FORMAT_OPTIONS ('recursiveFileLookup' = 'true',  'rescuedDataColumn' = '_rescued_data') 

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from danieldelta

# COMMAND ----------

# MAGIC %sql
# MAGIC select exists('yes',) from range(1)

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into table snapshots
# MAGIC select count(*), item_id
# MAGIC from events
# MAGIC group by item_id
