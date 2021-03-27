from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient
from time import sleep

consumer = KafkaConsumer(
    'LogTopic',
     bootstrap_servers=['kafka:9092'],
     api_version=(2, 7, 0),
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('mongodb://root:rootpassword@mongodb:27017/admin')
collection = client.logdb.logcln

while True:
    for message in consumer:
        message = message.value
        print(message)
        splitted = message.split(",")
        print(splitted)
        message_dict = {"method":splitted[0], "response_time": splitted[1], "timestamp": splitted[2]}
        collection.insert_one(message_dict)
        print('{} added to {}'.format(message_dict, collection))