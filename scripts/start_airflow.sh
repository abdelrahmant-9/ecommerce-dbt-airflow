#!/usr/bin/env bash
# Start Airflow locally (UI + scheduler) pointing at this project's dags/ folder.
set -euo pipefail
cd "$(dirname "$0")/.."
export AIRFLOW_HOME="$PWD/airflow_home"
export AIRFLOW__CORE__DAGS_FOLDER="$PWD/dags"
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__CORE__SIMPLE_AUTH_MANAGER_ALL_ADMINS=True   # local demo: no login screen
export PATH="$PWD/.venv-airflow/bin:$PATH"   # standalone spawns `airflow` subprocesses
exec airflow standalone
