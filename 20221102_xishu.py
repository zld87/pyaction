from kafka import KafkaProducer, KafkaConsumer
import json
import random,time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers=["192.168.70.29:9092"],
    api_version=(0, 11)
)

#producer.send('my_topic', 'raw_bytes')
#producer.close()



consumer = KafkaConsumer(
    'di_aiops_anal_detn3_log_server',
    auto_offset_reset="earliest",
    bootstrap_servers=["192.168.70.29:9092"],
    #bootstrap_servers=["192.168.20.188:9092"]
)

for message in consumer:
    print(message.timestamp)



