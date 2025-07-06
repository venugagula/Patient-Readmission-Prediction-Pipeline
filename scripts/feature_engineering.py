from pyspark.sql import SparkSession
from pyspark.sql.functions import datediff, col

def engineer_features(input_path, output_path):
    spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()

    df = spark.read.format("delta").load(input_path)
    df = df.withColumn("length_of_stay", datediff(col("dischargeDate"), col("admissionDate")))

    df.write.format("delta").mode("overwrite").save(output_path)
    print("Feature engineering complete.")

if __name__ == "__main__":
    engineer_features("s3://silver-layer/clean_ehr/", "s3://gold-layer/features/")

