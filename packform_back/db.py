import psycopg2
import os
import json
import math

from pymongo import MongoClient
from psycopg2 import extras

PAGE_SIZE = 5

def get_customer(id):
    """Returns given customer object from the mongo db based on id"""
    mongo = MongoClient()
    collection = mongo.packform.customers
    return collection.find_one({'user_id': id}, projection={'_id': False, 'credit_cards': False, "login": False, "password": False})

def get_orders(page, search=None, from_date=None, to_date=None):
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
                where   (orders.id = orderItems.order_id) and 
                        ((orders.order_name like %(search_like)s or %(search)s is NULL) or (orderItems.product like %(search_like)s or %(search)s is NULL)) and
                        ((orders.created_at > %(from_date)s or %(from_date)s is NULL) and (orders.created_at < %(to_date)s or %(to_date)s is NULL))
                group by orders.id, orderItems.order_id
                order by orders.order_name
                limit %(limit)s offset %(offset)s;
            ''', dict(search=search, search_like=f'%{search}%', from_date=from_date, to_date=to_date, limit=PAGE_SIZE, offset=page*PAGE_SIZE)
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

def get_pages():
    """gets count of orders in db and returns number of pages from that count"""
    try:
        conn = psycopg2.connect(f"dbname={os.getenv('DBNAME')} user={os.getenv('DBUSER')}")
        curr = conn.cursor()
        curr.execute('select count(*) from orders;')
        return math.ceil(curr.fetchone()[0]/PAGE_SIZE)
    except psycopg2.Error as err:
        print(err)