from pyspark.sql import SparkSession

from pyspark.sql.functions import *


spark = (
    SparkSession.builder
    .appName("Interview Demo")
    .config("spark.sql.legacy.parquet.nanosAsLong", "true")
    .getOrCreate()
)











spark = (
    SparkSession.builder
    .appName("ParquetToSQLite")
    # Fetches the SQLite JDBC artifact dynamically from Maven
    .config("spark.jars.packages", "org.xerial:sqlite-jdbc:3.45.1.0")
    # Keeping your previous timestamp error fix intact
    .config("spark.sql.legacy.parquet.nanosAsLong", "true")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

# 2. Read the Parquet table
sales_df = spark.read.parquet("data/Sales.parquet")

# 3. Define your SQLite database configurations
sqlite_db_path = "data/my_database.db"  # Path to your local .db file
target_table = "sales_table"             # Name of the table inside SQLite

# 4. Write the DataFrame directly into SQLite using JDBC
(
    sales_df.write
    .format("jdbc")
    .option("url", f"jdbc:sqlite:{sqlite_db_path}")
    .option("dbtable", target_table)
    .option("driver", "org.sqlite.JDBC")
    # Modes: "overwrite" (replace table) or "append" (add to table)
    .mode("overwrite") 
    .save()

)    