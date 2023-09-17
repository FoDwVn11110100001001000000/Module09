import configparser
import logging

from pymongo import MongoClient
from mongoengine import connect

from utils import setup_log

def connector():
    connect(host=f'mongodb+srv://{user}:{password}@{domain}/{db_name}', ssl=True)

def configurate():
    config = configparser.ConfigParser()
    config.read('config.ini')

    password = config.get('DATABASE', 'PASSWORD')
    user = config.get('DATABASE', 'USER')
    domain = config.get('DATABASE', 'DOMAIN')
    db_name = config.get('DATABASE', 'DB_NAME')
    return password, user, domain, db_name


password, user, domain, db_name = configurate()


def connect_to_mongodb():
    URI = f'mongodb+srv://{user}:{password}@{domain}/{db_name}'
    # Підключення до сервера MongoDB
    client = MongoClient(URI)
    return client

def choose_db(database_name: str):
    client = connect_to_mongodb()
    # Вибір бази даних (або створення нової)
    db = client['module08']
    # Вибір колекції (або створення нової)
    collection = db[database_name]
    return collection


def fill_data(data: list, database: str):
    setup_log()
    
    if data:
        collection = choose_db(database)
        result = collection.insert_many(data)
        logging.info(f"Inserted document IDs: {result.inserted_ids}")