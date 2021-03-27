from kafka import KafkaProducer
import os.path
import time 
from json import dumps
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

index = 0
path = "./log/log.txt"
obspath = "./log"

producer = KafkaProducer(bootstrap_servers=['kafka'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def send(string):
    with open(path) as f:
        global index
        for i, row in enumerate(f):
            if i == index: 
                log_line = row.rstrip("\n")
                index += 1
                producer.send('LogTopic', value = log_line)
                print(string + " " + log_line)

def on_created(event):
    send("Created")

def on_modified(event):
    send("Modified")

if os.path.exists(path) == True:
    send("Exists")

my_event_handler.on_created = on_created
my_event_handler.on_modified = on_modified

go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, obspath, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()