# Databricks notebook source
import sys
sys.path.append("/Workspace/Repos/donghwa.kim@databricks.com/cicd_demo/")

# COMMAND ----------

from usda_cicd.util import UsdaUtil

# COMMAND ----------

market_data_path = "/FileStore/uploads/MNRetailDatasetCSV2014.csv"
market_util = UsdaUtil(market_data_path)

# COMMAND ----------

retail_df = market_util.get_market_data(has_header=True)

# COMMAND ----------

market_util.save_as_table(retail_df, "dkim_usda", "market_data")

# COMMAND ----------


