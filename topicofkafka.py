from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.12.181:9092")
for topic in client.topics:
    print topic