from pyspark.sql import SparkSession

from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("MyApp")
sc = SparkContext(conf=conf)

sc.setLogLevel("WARN")  # set the logging level to "WARN"



spark = SparkSession.builder.appName("SparkStreaming").getOrCreate()

spark.sparkContext.setLogLevel('WARN')

lines = spark.readStream\
    .format("socket")\
    .option("host", "localhost")\
    .option("port", 9009) \
    .load()

query = lines.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()