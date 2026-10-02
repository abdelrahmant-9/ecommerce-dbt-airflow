select
    order_date,
    count(*)                   as orders,
    sum(order_total)           as revenue,
    round(avg(order_total), 2) as avg_order_value
from {{ ref('fct_orders') }}
where status in ('completed', 'shipped')
group by order_date
order by order_date
