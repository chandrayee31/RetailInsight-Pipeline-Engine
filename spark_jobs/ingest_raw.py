from utils.spark_session import create_spark_session

def main():
    spark = create_spark_session("RetailRawIngestion")
    df = spark.read.csv("data/raw/retail_sales.csv",header=True,inferSchema=True)

    print("Schema")
    df.printSchema()

    print("Sample Rows")
    df.show(5)

    df.write.mode("overwrite").parquet("data/processed/retail_sales_parquet")
    print("Raw data ingested successfully into data/processed/retail_sales_parquet")
    spark.stop()


if __name__=="__main__":
        main()
