from kafka import KafkaProducer
import random, time
import json

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers = ["192.168.70.29:9092"],
    api_version=(2, 12),
    batch_size=131072
)

idNew = 1
metricItem = ["cpu", "memory", 'disk']
topicId = "di_aiops_anal_detn3_log_server"

def Producer():
    global idNew
    while True:
        for i in metricItem:
            newData = {"id": idNew, "createdTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "metricItem": i, "value": random.randint(1, 500)}
            print(newData)
            producer.send(topicId, newData)
            idNew += 1
        time.sleep(1)
        producer.close()





def Producer1():
    while True:
        newData = {"createdTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "metricItem": '102##app14.trans_count_sum', "value": random.randint(1, 500)}
        print(newData)
        producer.send(topicId, newData)
        time.sleep(10)
    producer.close()

if __name__ == "__main__":
    Producer1()

