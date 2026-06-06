from kafka import KafkaProducer
import json
import sys
import random, time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    #bootstrap_servers=["192.168.100.168:9092","192.168.100.195:9092","192.168.100.196:9092"],
    bootstrap_servers=["192.168.200.110:9092"],
    api_version=(2, 12),
    acks='all'
)

st = parse(sys.argv[1])
tc = relativedelta(minutes=1)
#
# producer.send('di_aiops_anal_detn3_log_server', "3232")

#newtime=st+tc
#print(stringtime[0:10])
#print(stringtime[11:])
for i in range(1440*60):
    datenow = datetime.now()
    stringtime = str(st)
    data = {
        "system": "PP1A",
        "instanceId": "e856656d55f9467fba6149af922c2d6d",
        "tenantId": "055145",
        "metrics": "cpu",
        "time": stringtime[0:10] + "T" + stringtime[11:] + ".000+08:00",
        "value": str(random.randint(20, 70)),
        "userId": "1502192367004389377"
    }
    data1 = {
        "instance_id": sys.argv[2],
        "time": stringtime,
        "value": random.randint(1, 100)
    }
    print(data1)
    if st < datenow:
        producer.send('di_aiops_anal_detn3_log_server', data1)
        #producer.close()
        st += tc
        print(st)
    else:
        time.sleep(60)
        producer.send('di_aiops_anal_detn3_log_server', data1)
        #producer.close()
        st += tc

producer.close()






'''data = {
    "system": "PP1A",
    "instanceId": "ee5fbab7f5414990ab4acd907a070253",
    "tenantId": "055145",
    "metrics": "throughput",
    "time": "2021-10-16T15:46:00.000+08:00",
    "value": str(random.randint(1,100)),
    "userId": "1502192367004389377"
}'''

# spath = "/Users/zhouliudong/Desktop/333th_ts_train.csv"
# topic1 = "testIntopic123"
# topic2 = "aiops_anal_detn3_log_server"
# num = 0
# with open(spath, encoding="utf-8") as f:
#     f.seek(0)
#     for i in f.readlines()[1:]:
#         dataArrey = i.split(",")
#         dataDict = {"instance_id": "101##UM3027", "time": dataArrey[0].strip(), "value": dataArrey[2].strip()}
#         producer.send(topic2, dataDict)
#         num += 1
#     producer.close()
#     print(num)
# print("over")
