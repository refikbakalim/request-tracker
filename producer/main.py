from kafka import KafkaProducer
import os.path
from time import sleep
from json import dumps

index = 1
length = 0
path = "log/log.txt"

while os.path.exists(path) == False:
    sleep(1)

producer = KafkaProducer(bootstrap_servers=['kafka'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
while True:
    with open(path) as f:
        for i, row in enumerate(f):
            if i == index: 
                log_line = row.rstrip("\n")
                index += 1
                producer.send('LogTopic', value = log_line)
                print(log_line) #send to kafka instead
    sleep(1)