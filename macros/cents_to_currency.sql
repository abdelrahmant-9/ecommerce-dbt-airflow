{% macro cents_to_currency(column_name, decimals=2) -%}
    round({{ column_name }} / 100.0, {{ decimals }})
{%- endmacro %}
