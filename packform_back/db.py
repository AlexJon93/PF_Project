import psycopg2
import os
import json

from pymongo import MongoClient
from psycopg2 import extras

def get_customer(id):
    """Returns given customer object from the mongo db based on id"""
    mongo = MongoClient()
    collection = mongo.packform.customers
    return collection.find_one({'user_id': id}, projection={'_id': False, 'credit_cards': False, "login": False, "password": False})

def get_orders():
    """Gets all orders from postgres db"""
    try:
        conn = psycopg2.connect(f"dbname={os.getenv('DBNAME')} user={os.getenv('DBUSER')}")
        curr = conn.cursor(cursor_factory=extras.RealDictCursor)

        curr.execute(
            '''
            SELECT orders.order_name, orders.customer_id, orders.created_at, 
            sum(orderItems.price_per_unit * deliveries.delivered_quantity) as delivered_amount, 
            sum(orderItems.price_per_unit * orderItems.quantity) as total_amount
                from orders, orderItems
                left join deliveries on deliveries.order_item_id = orderItems.id
                where orders.id = orderItems.order_id
                group by orders.id, orderItems.order_id;
            '''
        )
        
        # fetches all rows from query execution
        orders = []
        for row in curr.fetchall():
            # casting values in json serializable forms
            row['total_amount'] = 0 if row['total_amount'] is None else str(row['total_amount'])
            row['delivered_amount'] = '-' if row['delivered_amount'] is None else str(row['delivered_amount'])
            row['created_at'] = str(row['created_at'])

            # add customer details from mongodb into row dict
            customer = get_customer(row.pop('customer_id'))
            row['customer_company'] = customer['company']['company_name']
            row['customer_name'] = customer['name']
            orders.append(dict(row))
        return orders
    except psycopg2.Error as err:
        print(err)