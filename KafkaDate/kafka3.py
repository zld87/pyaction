from kafka import KafkaProducer
from kafka import KafkaConsumer
from multiprocessing import Process,Pool,Queue
from threading import Thread
import json
import random,time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime

#kafkaip = "192.168.100.181:9092,192.168.100.184:9092,192.168.100.66:9092"
kafkaip = "192.168.100.209:19092,192.168.100.209:19093,192.168.100.209:19094"

#消费者
consumer = KafkaConsumer('jenkin_zld_out1',
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         # bootstrap_servers=["192.168.100.181:9092","192.168.100.184:9092","192.168.100.66:9092"]
                         # bootstrap_servers=["192.168.100.209:19092","192.168.100.209:19093","192.168.100.209:19094"]
                         bootstrap_servers=kafkaip.split(",")
                         )

#生产者
producer = KafkaProducer(
    # value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    # bootstrap_servers=["192.168.100.168:9092","192.168.100.195:9092","192.168.100.196:9092"],
    # bootstrap_servers=["192.168.100.209:19094","192.168.100.209:19093","192.168.100.209:19092"],
    bootstrap_servers=kafkaip.split(","),
    # api_version=(0,11),
    batch_size=131072
)

def consumer_function():
    mum = 0
    for message in consumer:
        '''print("%s:%d:%d: key=%s value=%s time=%s" % (message.topic,
                                             message.partition,
                                             message.offset,
                                             message.key,
                                             message.value,
                                             message.timestamp
                                            ))'''
        time1=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(message.timestamp / 1000))
        #time1 = time.localtime(message.timestamp / 1000)
        time2 = str(time1)
        print(time2)
        mum += 1
        sttmum = str(mum)
        print(mum)
        with open("/Users/zhouliudong/Desktop/grpc.csv", "a+", encoding="utf-8") as f:
            f.write(time2+'   '+sttmum+'\n')

        consumer.commit()



def producer_function():
    spath="/Users/zhouliudong/Desktop/test_data.txt"
    newtopic = "jenkin_zld_in1"
    with open(spath, "r", encoding="utf-8") as fs:
        shijian = time.strftime(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        print("发送时间",shijian)
        for i in fs.readlines():
            #print(i.strip())
            producer.send(newtopic, i.strip().encode())
        producer.close()
    print("生产结束")


if __name__ == "__main__":
    cm = Thread(target=consumer_function)
    time.sleep(1)
    pd = Thread(target=producer_function)
    cm.start()
    pd.start()

