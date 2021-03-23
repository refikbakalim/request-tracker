#!/bin/bash

docker-compose build && docker-compose up -d


docker exec -it kafka bash -c '$KAFKA_HOME/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --topic test -partitions 1 --replication-factor 1'
