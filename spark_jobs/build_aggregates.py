from pyspark.sql.functions import month, sum as spark_sum
from utils.spark_session import create_spark_session


def main():
    print("Starting aggregate build job...")

    spark = create_spark_session("RetailAggregateBuild")

    df = spark.read.parquet("data/processed/retail_sales_clean")

    monthly_sales = (
        df.withColumn("month_num", month("order_date"))
          .groupBy("month_num")
          .agg(
              spark_sum("sales").alias("total_sales"),
              spark_sum("profit").alias("total_profit"),
              spark_sum("quantity").alias("total_quantity")
          )
          .orderBy("month_num")
    )

    category_sales = (
        df.groupBy("category")
          .agg(
              spark_sum("sales").alias("total_sales"),
              spark_sum("profit").alias("total_profit"),
              spark_sum("quantity").alias("total_quantity")
          )
          .orderBy("category")
    )

    region_sales = (
        df.groupBy("region")
          .agg(
              spark_sum("sales").alias("total_sales"),
              spark_sum("profit").alias("total_profit"),
              spark_sum("quantity").alias("total_quantity")
          )
          .orderBy("region")
    )

    print("Monthly sales:")
    monthly_sales.show()

    print("Category sales:")
    category_sales.show()

    print("Region sales:")
    region_sales.show()

    monthly_sales.write.mode("overwrite").parquet("data/curated/monthly_sales")
    category_sales.write.mode("overwrite").parquet("data/curated/category_sales")
    region_sales.write.mode("overwrite").parquet("data/curated/region_sales")

    print("Curated aggregate tables written to data/curated/")

    spark.stop()


if __name__ == "__main__":
    main()