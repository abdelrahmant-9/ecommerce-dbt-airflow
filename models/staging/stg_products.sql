select
    id                                     as product_id,
    name                                   as product_name,
    category,
    {{ cents_to_currency('price_cents') }} as price
from {{ ref('raw_products') }}
