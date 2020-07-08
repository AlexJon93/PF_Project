import psycopg2
import pymongo
import csv
import os

from pymongo import MongoClient
from pymongo import errors
from dotenv import load_dotenv
load_dotenv()

postgres_files = {
    'orders': 'db_scripts/data_files/Test task - Postgres - orders.csv',
    'orderItems': 'db_scripts/data_files/Test task - Postgres - order_items.csv',
    'deliveries': 'db_scripts/data_files/Test task - Postgres - deliveries.csv'
}

mongo_files = {
    'customers': 'db_scripts/data_files/Test task - Mongo - customers.csv',
    'companies': 'db_scripts/data_files/Test task - Mongo - customer_companies.csv'
}

def run_exports():
    """entry point for the script, calls all the various export methods"""
    from postgres_tables import table_queries

    print('Exporting to postgres')
    init_postgres(table_queries)
    for key in postgres_files:
        if not export_postgres(postgres_files[key], key):
            print(f'Issue with populating table: {key}')
    print('Done!')

    print('Exporting to MongoDB')
    if not export_mongo_customers(mongo_files['customers']):
        print(f'Issue with populating mongodb')
    else:
        if not export_mongo_companies(mongo_files['companies']):
            print(f'Issue with fitting company data onto customer collection')
    print('Done!')

    print('All DBs succesfully exported')


def export_postgres(file, table):
    """
    Exports data from the given csv file to the given table.

    Args:
        file (str): Name of the data file to export
        table (str): Name of the table to export to

    Returns:
        bool: True for successful run, else False
    """
    with open(file, 'r') as data:
        try:
            print(f'loading file {file} into postgres table {table}')
            next(data)
            conn = psycopg2.connect(f"dbname={os.getenv('DBNAME')} user={os.getenv('DBUSER')}")

            curr = conn.cursor()
            curr.copy_from(data, table, sep=',', null='')
            conn.commit()
        except psycopg2.Error as err:
            print(err)
            conn.close()
            return False
        finally:
            conn.close()
    return True    
    

def init_postgres(queries):
    """
    Initialises the tables for the postgresql DB

    Args:
        queries (list): List of all initialising queries
    
    Returns:
        bool: True for successful run, else False
    """
    try:
        print('creating postgres tables...')
        conn = psycopg2.connect(f"dbname={os.getenv('DBNAME')} user={os.getenv('DBUSER')}")

        curr = conn.cursor()
        for query in queries:
            curr.execute(query)
        conn.commit()
        curr.close()
        
    except psycopg2.Error as err:
        print(err)
        conn.close()
        return False
    finally:
        conn.close()
    return True

def export_mongo_customers(file):
    """
    Exports data from the given csv file to a MongoDB collection

    Returns:
        bool: True for successful run, else False
    """
    try:
        mongo = MongoClient()
        collection = mongo.packform.customers
        with open(file, 'r') as csv_file:
            data = csv.DictReader(csv_file)
            for row in data:
                # casting non-string values to respective types
                row['company_id'] = int(row['company_id'])
                row['credit_cards'] = eval(row['credit_cards'])
                collection.insert_one(row)
            collection.create_index([('user_id', pymongo.DESCENDING)], unique=True)
    except errors.PyMongoError as err:
        print(err)
        return False
    return True

def export_mongo_companies(file):
    """
    Replaces simple company_id with further details in user collection

    Returns:
        bool: True for successful run, else False
    """
    try:
        mongo = MongoClient()
        collection = mongo.packform.customers
        with open(file, 'r') as csv_file:
            data = csv.DictReader(csv_file)
            for row in data:
                row['company_id'] = int(row['company_id'])
                collection.update_many({ 'company_id': row['company_id'] }, { '$rename': { 'company_id': 'company' } })
                collection.update_many({ 'company': row['company_id'] }, { '$set': { 'company': row } })
    except errors.PyMongoError as err:
        print(err)
        return False
    return True


if __name__ == "__main__":
    run_exports()