#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from kafka import KafkaConsumer

#connect to Kafka server and pass the topic we want to consume
#consumer = KafkaConsumer('mytopictest')

#print "begin"
#for msg in consumer:
#    print msg

#kafka消费者
from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.12.181:9092")
topic = client.topics['mytopictest']
# 获取 consumer 消费者
consumer = topic.get_simple_consumer(consumer_group="test",reset_offset_on_start=True)
for message in consumer:
    print message
    if message is not None:
        print ">>>>>>>>>>",message.offset
        print ">>>>>>>>>>",message.value