from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="retail_etl_pipeline",
    start_date=datetime(2026, 3, 17),
    schedule=None,
    catchup=False,
    tags=["retail", "etl", "spark"],
) as dag:

    # Step 1: Clean raw CSV (Pandas)
    transform_clean = BashOperator(
        task_id="transform_clean",
        bash_command="cd /opt/airflow && python scripts/transform_clean.py",
    )

    # Step 2: Ingest + convert to parquet (Spark)
    ingest_raw = BashOperator(
        task_id="ingest_raw",
        bash_command="cd /opt/airflow && python spark_jobs/ingest_raw.py",
    )

    # Step 3: Build aggregates (Spark)
    build_aggregates = BashOperator(
        task_id="build_aggregates",
        bash_command="cd /opt/airflow && python spark_jobs/build_aggregates.py",
    )

    # Pipeline order
    transform_clean >> ingest_raw >> build_aggregates