from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
import time

kafkainip = "192.168.100.181:9092,192.168.100.184:9092,192.168.100.66:9092"
kafkainip1 = "192.168.20.188:9092"
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    #bootstrap_servers=["192.168.100.168:9092","192.168.100.195:9092","192.168.100.196:9092"],
    #bootstrap_servers=["192.168.100.209:19094","192.168.100.209:19093","192.168.100.209:19092"],
    #bootstrap_servers=kafkainip.split(","),
    bootstrap_servers=kafkainip1,
    #api_version=(0,11),
    batch_size=131072
    #linger_ms=5000
)

spath="/Users/zhouliudong/Desktop/5week_train.csv"
newtopic = "di_aiops_anal_detn3_log_server_zld"
z = 2
c = 1
# while z <= 2:
#     with open(spath, "r", encoding="utf-8") as fs:
#         #shijian = time.strftime(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
#         #print(shijian)
#         for i in fs.readlines()[1:]:
#             newDate = i.strip().split(",")
#             #print(newDate)
#             sendDate = {"time": newDate[0], "instance_id": "101##UM"+f"{z:05}", "value": float(newDate[2])}
#             print(sendDate)
#             producer.send(newtopic, sendDate)
#             c += 1
#             print(c)
#     z += 1
# producer.close()
# print("over")



#消费者对象
consumer = KafkaConsumer('di_aiops_anal_detn_abnormal_point',
    #auto_offset_reset='earliest',
    #bootstrap_servers=["192.168.100.168:9092","192.168.100.195:9092","192.168.100.196:9092"]
    bootstrap_servers=["192.168.200.110:9092"]
)


#数据
'''data = {
    "system": "PP1A",
    "instanceId": "ee5fbab7f5414990ab4acd907a070253",
    "tenantId": "055145",
    "metrics": "throughput",
    "time": "2021-10-16T15:46:00.000+08:00",
    "value": str(random.randint(1,100)),
    "userId": "1502192367004389377"
}'''


#消费kafka数据
mum = 0
for message in consumer:
    # print("%s:%d:%d: key=%s value=%s time=%s" % (message.topic,
    #                                      message.partition,
    #                                      message.offset,
    #                                      message.key,
    #                                      message.value,
    #                                      message.timestamp
    #                                     ))
    mum += 1
    print(message.timestamp)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(message.timestamp / 1000)))
    print(mum)

   # print(message.timestamp.strftime('%Y-%m-%d %H:%M:%S.%f'))
    # time1=str(time.strftime('%Y-%m-%d %H:%M:%S.%f',time.localtime(message.timestamp / 1000)))
    # print(time1)
    # mum=+1
    # print(mum)




#time1=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(message.timestamp / 1000)))
#rint(time)
#str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(message.timestamp/1000)))
#print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1654669740911/1000))))
