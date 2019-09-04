from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.12.181:9092")
print client.brokers

for n in client.brokers:
    host = client.brokers[n].host
    port = client.brokers[n].port
    id = client.brokers[n].id
    print "host=%s | port=%s | broker.id=%s " %(host,port,id)