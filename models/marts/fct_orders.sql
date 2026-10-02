-- One row per order with its total amount.
with order_totals as (
    select
        order_id,
        count(*)        as item_count,
        sum(quantity)   as units,
        sum(line_total) as order_total
    from {{ ref('stg_order_items') }}
    group by order_id
)

select
    o.order_id,
    o.customer_id,
    o.order_date,
    o.status,
    t.item_count,
    t.units,
    t.order_total
from {{ ref('stg_orders') }} o
join order_totals t on o.order_id = t.order_id
