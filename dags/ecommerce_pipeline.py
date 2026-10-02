"""Daily e-commerce pipeline: load raw data -> build models -> test data."""
from datetime import datetime
from pathlib import Path

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

PROJECT_DIR = Path(__file__).resolve().parent.parent
DBT = f"cd {PROJECT_DIR} && {PROJECT_DIR}/.venv/bin/dbt"

with DAG(
    dag_id="ecommerce_elt",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
    default_args={"retries": 1},
) as dag:
    dbt_seed = BashOperator(task_id="dbt_seed", bash_command=f"{DBT} seed")
    dbt_run = BashOperator(task_id="dbt_run", bash_command=f"{DBT} run")
    dbt_test = BashOperator(task_id="dbt_test", bash_command=f"{DBT} test")

    dbt_seed >> dbt_run >> dbt_test
