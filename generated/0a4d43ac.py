# PySpark Data Processing Script
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("DataProcessor").getOrCreate()
    print("hello")
    spark.stop()