from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def run_etl(input_path, output_path):
    spark = SparkSession.builder.appName("ETL_Pipeline").getOrCreate()

    df_raw = spark.read.json(input_path)
    df_clean = df_raw.dropna(subset=["patientId", "admissionDate", "dischargeDate"])

    df_clean.write.format("delta").mode("overwrite").save(output_path)
    print("ETL completed successfully.")

if __name__ == "__main__":
    run_etl("s3://bronze-layer/ehr_data/", "s3://silver-layer/clean_ehr/")


