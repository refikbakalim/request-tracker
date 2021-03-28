from kafka import KafkaProducer
import time 
import os.path
from json import dumps
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

index = 0
path = "./log/log.txt"
obspath = "./log"

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         api_version=(2, 7, 0),
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
def send():
    with open(path,"r") as f:
        global index
        log_line = ""   
        f.seek(index)
        byte = f.read(1) 
        while byte != "": 
            if byte != "\n":
                log_line = log_line + byte
            else:
                producer.send('LogTopic', value = log_line)
                log_line = ""
            index += 1    
            f.seek(index)
            byte = f.read(1)  

def on_created(event):
    send()

def on_modified(event):
    send()

if os.path.exists(path) == True:
    send()

my_event_handler.on_created = on_created
my_event_handler.on_modified = on_modified

go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, obspath, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()