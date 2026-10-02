-- One row per customer with how much they bought.
-- Only completed and shipped orders count as revenue.
with customer_orders as (
    select
        customer_id,
        min(order_date)  as first_order_date,
        max(order_date)  as last_order_date,
        count(*)         as total_orders,
        sum(order_total) as lifetime_value
    from {{ ref('fct_orders') }}
    where status in ('completed', 'shipped')
    group by customer_id
)

select
    c.customer_id,
    c.full_name,
    c.email,
    c.city,
    c.signup_date,
    co.first_order_date,
    co.last_order_date,
    coalesce(co.total_orders, 0)   as total_orders,
    coalesce(co.lifetime_value, 0) as lifetime_value,
    case
        when co.lifetime_value >= 120000 then 'gold'
        when co.lifetime_value >= 55000  then 'silver'
        else 'bronze'
    end as tier
from {{ ref('stg_customers') }} c
left join customer_orders co on c.customer_id = co.customer_id
