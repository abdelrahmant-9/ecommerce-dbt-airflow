select
    p.product_id,
    p.product_name,
    p.category,
    sum(i.quantity)   as units_sold,
    sum(i.line_total) as revenue
from {{ ref('stg_order_items') }} i
join {{ ref('stg_orders') }} o   on i.order_id = o.order_id
join {{ ref('stg_products') }} p on i.product_id = p.product_id
where o.status in ('completed', 'shipped')
group by p.product_id, p.product_name, p.category
order by revenue desc
