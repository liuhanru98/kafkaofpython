#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from kafka import SimpleProducer, KafkaClient

#kafka生产者
#  connect to Kafka
kafka = KafkaClient('192.168.12.181:9092')
producer = SimpleProducer(kafka)
# Assign a topic
topic = 'mytopictest'

def test():
    print('begin')
    n = 1
    i = 1
    while (i):
        producer.send_messages(topic, str(n))
        print "send" + str(n)
        n += 1
        time.sleep(0.5)
    print('done')

if __name__ == '__main__':
    test()
