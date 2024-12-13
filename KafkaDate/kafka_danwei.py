from kafka import KafkaProducer, KafkaConsumer
import json
import sys
import random,time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime



st = parse('2022-12-01')
print(type(str(st)))

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    #bootstrap_servers=["192.168.100.168:9092","192.168.100.195:9092","192.168.100.196:9092"],
    bootstrap_servers=["192.168.20.213:9092"],
    api_version=(2, 12)
)



