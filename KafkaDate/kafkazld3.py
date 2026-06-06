from kafka import KafkaProducer, KafkaConsumer
import json
import sys
import random,time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime


def sum_value(value=None):
    if value == None:
        sum_value = random.choice(["a1", "b2", "c3", "d4", "e5"])
        return sum_value
    elif value == 1:
        val_float = random.uniform(10, 80)
        mertic_value = format(val_float, ".2f")
        return float(mertic_value)
    else:
        print(type(value))
        t_tuple = value.timetuple()
        timestamp = time.mktime(t_tuple)
        value = format(timestamp, '.0f')
        return int(value)


producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    #bootstrap_servers=["192.168.100.168:9092","192.168.100.195:9092","192.168.100.196:9092"],
    bootstrap_servers=["192.168.100.194:9092"],
    api_version=(2, 12)
)

sys.argv[1]
st = parse('2022-12-01')
tc = relativedelta(minutes=1)
#newtime=st+tc
#print(stringtime[0:10])
#print(stringtime[11:])
for i in range(1440*60):
    datenow = datetime.now()
    stringtime = str(st)
    print(type(st))
    data = {
        "system": "PP1A",
        "instanceId": "e856656d55f9467fba6149af922c2d6d",
        "tenantId": "055145",
        "metrics": "cpu",
        "time": stringtime[0:10] + "T" + stringtime[11:] + ".000+08:00",
        "value": str(random.randint(20, 70)),
        "userId": "1502192367004389377"
    }
    if st < datenow:
        for i in range(1, 21):
            data1 = {
                "top_test1": sum_value(),
                "top_test2": sum_value(),
                "top_test3": sum_value(),
                "top_test4": sum_value(),
                "ResPer_top": sum_value(1),
                "ts": sum_value(st),
                "app": "top1",
                "ResTime_top": sum_value(1),
                "SuccPer_top": sum_value(1),
                "TransCount_top": sum_value(1),
            }
            data1["ts"] += i
            print(data1)
            #producer.send('drill_log', data1)
        st += tc
        print(st)
    else:
        for i in range(1, 21):
            data1 = {
                "top_test1": sum_value(),
                "top_test2": sum_value(),
                "top_test3": sum_value(),
                "top_test4": sum_value(),
                "ResPer_top": sum_value(1),
                "ts": sum_value(st),
                "app": "top1",
                "ResTime_top": sum_value(1),
                "SuccPer_top": sum_value(1),
                "TransCount_top": sum_value(1),
            }
            time.sleep(1)
            data1["ts"] += i
            print(data1)
            #producer.send('drill_log', data1)
        time.sleep(40)
        st += tc

producer.close()



'''st = parse("2022-11-01")
print(st.timetuple())
timebew = st.timetuple()
timestamp = time.mktime(timebew)
value = format(timestamp, '.0f')
print(value)'''
