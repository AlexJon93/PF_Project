# Have placed table queries for postgres in seperate file to enhance readability of main script
table_queries = [
    '''
    CREATE TABLE IF NOT EXISTS orders(
        id integer PRIMARY KEY,
        created_at timestamptz,
        order_name text,
        customer_id text
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS orderItems(
        id integer PRIMARY KEY,
        order_id integer references orders(id),
        price_per_unit decimal,
        quantity integer,
        product text
        
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS deliveries(
        id integer PRIMARY KEY,
        order_item_id integer references orderItems(id),
        delivered_quantity integer
    )
    '''
]