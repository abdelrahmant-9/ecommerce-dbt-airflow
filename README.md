# E-commerce Data Pipeline — dbt + DuckDB + Airflow

A beginner data engineering project: raw e-commerce CSV files are loaded into a
database, cleaned and modelled with **dbt**, checked with **tests**, and run
every day by **Apache Airflow**.

Runs locally on **DuckDB** (a database in a single file), so no cloud account is needed.
`profiles.yml` also shows how the same project would connect to **Snowflake**.

## Flow

```
seeds/*.csv  ──dbt seed──►  raw tables
                               │
                           dbt run
                               ▼
                 staging (views)   stg_customers, stg_orders, stg_order_items, stg_products
                               ▼
                 marts (tables)    fct_orders, dim_customers,
                                   mart_daily_revenue, mart_product_performance
                               │
                           dbt test   (23 tests)

Airflow DAG `ecommerce_elt` (daily):  dbt_seed → dbt_run → dbt_test
```

## Folders
```
seeds/        raw CSV data
models/       staging and marts SQL models + tests (.yml)
macros/       cents_to_currency macro
tests/        custom SQL test
dags/         Airflow DAG
scripts/      data generator + Airflow start script
```

## How to run
See [HOW_TO_RUN.md](HOW_TO_RUN.md).
