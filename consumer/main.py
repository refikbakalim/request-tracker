from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient

consumer = KafkaConsumer(
    'LogTopic',
     bootstrap_servers=['kafka'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

#client = MongoClient('localhost:27017')
client = MongoClient('mongodb://user:password@127.0.0.1:27017/datab')
collection = client.log_database.log_collection

while True:
    for message in consumer:
        message = message.value
        collection.insert_one(message)
        print('{} added to {}'.format(message, collection))