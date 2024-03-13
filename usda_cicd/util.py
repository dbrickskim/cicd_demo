from pyspark.sql import DataFrame, SparkSession

class UsdaUtil(object):
    def __init__(self, market_data_path:str):
        self.spark_session = SparkSession.builder.getOrCreate()
        self.market_data_path = market_data_path

    def get_market_data(self, has_header:bool) -> DataFrame:
        retail_df = self.spark_session.read.option("header", has_header).csv(self.market_data_path)
        return retail_df
    
    def save_as_table(self, data_frame:DataFrame, schema_name:str, table_name:str) -> None:
        self.spark_session.sql(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")
        self.spark_session.sql(f"DROP TABLE IF EXISTS {schema_name}.{table_name}")
        data_frame.write.saveAsTable(f"{schema_name}.{table_name}")