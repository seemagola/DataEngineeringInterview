from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Interview Demo")
    .getOrCreate()
)

# Reduce Spark logs
spark.sparkContext.setLogLevel("ERROR")

print("Spark Version:", spark.version)

data = [
    (1, "Alice", 60000),
    (2, "Bob", 70000),
    (3, "Charlie", 80000)
]

df = spark.createDataFrame(data, ["ID", "Name", "Salary"])

df.show()

spark.stop()