# 🚀 RetailInsight Pipeline Engine

### An End-to-End Retail Data Engineering & Analytics Platform

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img alt="Kafka" src="https://img.shields.io/badge/Streaming-Kafka-black">
  <img alt="Spark" src="https://img.shields.io/badge/Processing-Spark-orange">
  <img alt="Airflow" src="https://img.shields.io/badge/Orchestration-Airflow-red">
  <img alt="Data" src="https://img.shields.io/badge/Data-Pipeline-green">
</p>

---

## ✨ Key Features

- 📥 Multi-source data ingestion  
- ⚡ Real-time streaming using Kafka  
- 🔄 Batch & streaming data processing  
- 🧠 Data transformation using Spark / dbt  
- 🏗️ Data lake and warehouse architecture  
- 📊 Analytics-ready curated datasets  
- 🔁 Workflow orchestration with Airflow  
- 📈 Business intelligence & reporting layer  

---

## 🧭 Why Choose

- Simulates real-world enterprise data platform  
- Combines streaming + batch processing  
- Demonstrates end-to-end data lifecycle  
- Production-style modular architecture  
- Strong showcase of Data Engineering skills  

---

## 🏗️ System Architecture

<p align="center">
  <img src="readme_docs/datainsight_ai.gif" width="900"/>
</p>

---

## 🎬 Demo

<p align="center">
  <img src="readme_docs/datainsight_ai_GIF.gif" width="900"/>
</p>

---

## ⚡ Quick Start

```bash
pip install -r requirements.txt
python main.py
```

---

## 🧩 Simple Example

Data Sources → Ingestion → Streaming (Kafka) → Processing (Spark/dbt) → Data Lake → Warehouse → Analytics

---

## 🗂️ Project Structure

```text
|RetailInsight-Pipeline-Engine/
|
├── Dockerfile
├── Dockerfile.airflow
├── README.md
├── airflow.log
├── airflow_home
│   ├── airflow.cfg
│   ├── airflow.db
│   ├── airflow.db-shm
│   ├── airflow.db-wal
│   ├── logs
│   │   └── dag_processor
│   │       ├── 2026-03-17
│   │       │   └── example_dags
│   │       │       ├── example_asset_alias.py.log
│   │       │       ├── example_asset_alias_with_no_taskflow.py.log
│   │       │       ├── example_asset_decorator.py.log
│   │       │       ├── example_asset_with_watchers.py.log
│   │       │       ├── example_assets.py.log
│   │       │       ├── example_branch_labels.py.log
│   │       │       ├── example_branch_python_dop_operator_3.py.log
│   │       │       ├── example_complex.py.log
│   │       │       ├── example_custom_weight.py.log
│   │       │       ├── example_dag_decorator.py.log
│   │       │       ├── example_display_name.py.log
│   │       │       ├── example_dynamic_task_mapping.py.log
│   │       │       ├── example_dynamic_task_mapping_with_no_taskflow_operators.py.log
│   │       │       ├── example_inlet_event_extra.py.log
│   │       │       ├── example_kubernetes_executor.py.log
│   │       │       ├── example_latest_only_with_trigger.py.log
│   │       │       ├── example_local_kubernetes_executor.py.log
│   │       │       ├── example_nested_branch_dag.py.log
│   │       │       ├── example_outlet_event_extra.py.log
│   │       │       ├── example_params_trigger_ui.py.log
│   │       │       ├── example_params_ui_tutorial.py.log
│   │       │       ├── example_passing_params_via_test_command.py.log
│   │       │       ├── example_setup_teardown.py.log
│   │       │       ├── example_setup_teardown_taskflow.py.log
│   │       │       ├── example_simplest_dag.py.log
│   │       │       ├── example_skip_dag.py.log
│   │       │       ├── example_task_group.py.log
│   │       │       ├── example_task_group_decorator.py.log
│   │       │       ├── example_time_delta_sensor_async.py.log
│   │       │       ├── example_trigger_target_dag.py.log
│   │       │       ├── example_workday_timetable.py.log
│   │       │       ├── example_xcom.py.log
│   │       │       ├── example_xcomargs.py.log
│   │       │       ├── plugins
│   │       │       │   ├── decreasing_priority_weight_strategy.py.log
│   │       │       │   ├── event_listener.py.log
│   │       │       │   ├── listener_plugin.py.log
│   │       │       │   └── workday.py.log
│   │       │       ├── standard
│   │       │       │   ├── example_bash_decorator.py.log
│   │       │       │   ├── example_bash_operator.py.log
│   │       │       │   ├── example_branch_datetime_operator.py.log
│   │       │       │   ├── example_branch_day_of_week_operator.py.log
│   │       │       │   ├── example_branch_operator.py.log
│   │       │       │   ├── example_branch_operator_decorator.py.log
│   │       │       │   ├── example_external_task_child_deferrable.py.log
│   │       │       │   ├── example_external_task_marker_dag.py.log
│   │       │       │   ├── example_external_task_parent_deferrable.py.log
│   │       │       │   ├── example_latest_only.py.log
│   │       │       │   ├── example_python_decorator.py.log
│   │       │       │   ├── example_python_operator.py.log
│   │       │       │   ├── example_sensor_decorator.py.log
│   │       │       │   ├── example_sensors.py.log
│   │       │       │   ├── example_short_circuit_decorator.py.log
│   │       │       │   ├── example_short_circuit_operator.py.log
│   │       │       │   └── example_trigger_controller_dag.py.log
│   │       │       ├── tutorial.py.log
│   │       │       ├── tutorial_dag.py.log
│   │       │       ├── tutorial_objectstorage.py.log
│   │       │       ├── tutorial_taskflow_api.py.log
│   │       │       ├── tutorial_taskflow_api_virtualenv.py.log
│   │       │       └── tutorial_taskflow_templates.py.log
│   │       └── latest -> 2026-03-17
│   └── simple_auth_manager_passwords.json.generated
├── config
├── dags
│   ├── __pycache__
│   │   └── retail_etl_dag.cpython-312.pyc
│   └── retail_etl_dag.py
├── data
│   ├── curated
│   │   ├── category_sales
│   │   │   ├── _SUCCESS
│   │   │   └── part-00000-1d6bab39-41e1-4089-8744-a0970c5a13bc-c000.snappy.parquet
│   │   ├── monthly_sales
│   │   │   ├── _SUCCESS
│   │   │   └── part-00000-e98fbea9-f854-4389-8b57-fab61d8d0cb3-c000.snappy.parquet
│   │   └── region_sales
│   │       ├── _SUCCESS
│   │       └── part-00000-9d80bba1-2c1b-4806-a98b-b46ade58122a-c000.snappy.parquet
│   ├── processed
│   │   ├── cleaned_retail_sales.csv
│   │   ├── retail_sales_clean
│   │   │   ├── _SUCCESS
│   │   │   └── part-00000-fb74d7ec-74d6-4ac8-9e2a-b823097dc00a-c000.snappy.parquet
│   │   └── retail_sales_parquet
│   │       ├── _SUCCESS
│   │       └── part-00000-63be197c-e973-4dde-91db-5b1ba508a87a-c000.snappy.parquet
│   └── raw
│       └── retail_sales.csv
├── docker-compose.yaml
├── logs
│   ├── dag_id=retail_etl_pipeline
│   │   ├── run_id=manual__2026-03-17T20:48:53.384395+00:00
│   │   │   └── task_id=transform_clean
│   │   │       ├── attempt=1.log
│   │   │       └── attempt=2.log
│   │   ├── run_id=manual__2026-03-17T21:12:09.085792+00:00
│   │   │   └── task_id=transform_clean
│   │   │       └── attempt=1.log
│   │   ├── run_id=manual__2026-03-17T21:28:44.739123+00:00
│   │   │   └── task_id=transform_clean
│   │   │       └── attempt=1.log
│   │   ├── run_id=manual__2026-03-17T21:39:03.631183+00:00
│   │   │   └── task_id=transform_clean
│   │   │       └── attempt=1.log
│   │   └── run_id=manual__2026-03-17T21:44:28.261982+00:00
│   │       ├── task_id=build_aggregates
│   │       │   └── attempt=1.log
│   │       ├── task_id=ingest_raw
│   │       │   └── attempt=1.log
│   │       └── task_id=transform_clean
│   │           └── attempt=1.log
│   └── dag_processor
│       ├── 2026-03-17
│       │   └── dags-folder
│       │       └── retail_etl_dag.py.log
│       ├── 2026-03-18
│       │   └── dags-folder
│       │       └── retail_etl_dag.py.log
│       ├── 2026-03-19
│       │   └── dags-folder
│       │       └── retail_etl_dag.py.log
│       ├── 2026-03-20
│       │   └── dags-folder
│       │       └── retail_etl_dag.py.log
│       └── latest -> 2026-03-20
├── plugins
├── readme_docs
│   └── retail-Rag-AI.gif
├── requirements.txt
├── scripts
│   └── transform_clean.py
├── spark_jobs
│   ├── build_aggregates.py
│   └── ingest_raw.py
└── utils
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   └── spark_session.cpython-312.pyc
    └── spark_session.py
```

---

## 📬 Contact

Chandrayee Kumar  
Python Developer | AI/ML Engineer  

---

## 🚀 Future Improvements

- 📊 Real-time dashboards  
- ☁️ Cloud deployment  
- 🔍 Data quality monitoring  
- 🤖 AI anomaly detection  
- 🔗 API integrations  
