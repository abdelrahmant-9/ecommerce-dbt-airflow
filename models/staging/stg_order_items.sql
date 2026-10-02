select
    id                                          as order_item_id,
    order_id,
    product_id,
    quantity,
    {{ cents_to_currency('unit_price_cents') }} as unit_price,
    {{ cents_to_currency('unit_price_cents * quantity') }} as line_total
from {{ ref('raw_order_items') }}
