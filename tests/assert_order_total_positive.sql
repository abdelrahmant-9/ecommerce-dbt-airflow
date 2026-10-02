-- Fails if any order has a zero or negative total.
select * from {{ ref('fct_orders') }} where order_total <= 0
