from kafka import KafkaProducer, KafkaConsumer
import json
import sys
import random,time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    #bootstrap_servers=["192.168.100.168:9092","192.168.100.195:9092","192.168.100.196:9092"],
    bootstrap_servers=["192.168.200.110:9092"],
    api_version=(2, 12)
)

#历史训练检测
data = {
	"requestId": "TRAINING_HISTORY_DETECTION-1646710460885393408",
	"type": 32,
	"requestTime": 1679046105000,
	"mem": 4096,
	"cpu": 1,
	"subId": "1646710460885393409_nginx01#192.168.100.75#cost_time",
	"metric": "nginx01#192.168.100.75#cost_time",
	"trainStartTime": "2023-03-01 00:00:01",
	"trainEndTime": "2023-03-15 00:00:01",
	"detectStartTime": "2023-03-01 00:00:01",
	"detectEndTime": "2023-03-05 00:00:01",
	"algorithmParams": {
    "upperThreshold": 100.0,
    "trainMinData": "3",
    "useLowerBaseline": False,
    "trainIntervalPeriod": 3,
    "upperBaselineConfidence": 43.0,
    "autoTrain": False,
    "holidays": "2022-12-31",
    "granularity": 1,
    "baselineShiftMinutes": 1,
    "trainMaxData": "70",
    "makeupDays": "2023-05-06",
    "lowerBaselineConfidence": 300.0,
    "trainMinDayLength": 14,
    "predDayLength": 7,
    "missingRate": 0.2,
    "lowerThreshold": 20.0,
    "useUpperBaseline": False
  }
}

#离线训练
data1 = {"requestId": "1212434432444434434", "type": 11, "requestTime": 1679043153000, "mem": 4096, "cpu": 1, "subId": "323333333333322332", "metric": "top02##SuccPer_top", "trainStartTime": "2023-03-01 00:00:01", "trainEndTime": "2023-03-05 00:00:01"}
#离线检测
data2 = {
    "requestId":"1223343223322323",
    "type":12,
    "requestTime":1678175409000,
    "mem":4096,
    "cpu":1,
    "subId":"206372129111234076767",
    "metric":"top01##TransCount_top",
    "detectStartTime":"2023-03-01 00:00:00",
    "detectEndTime":"2023-03-03 00:00:00"
}
#模拟训练检测
data3 = {
	"requestId": "2222224121233443434",
	"type": 31,
	"requestTime": 1679294716000,
	"mem": 4096,
	"cpu": 1,
	"subId": "123372444433332222",
	"metric": "top02##ResPer_top",
	"trainStartTime": "2023-03-01 00:00:01",
	"trainEndTime": "2023-03-15 00:00:01",
	"detectStartTime": "2023-03-01 00:00:01",
	"detectEndTime": "2023-03-03 00:00:01",
	"redisKey": "top-sub43433",
	"algorithmParams": {
		"trainMaxData": 35,
		"useUpperBaseline": True,
		"missingRate": 1.0
	}
}

#沙箱训练检测
data4 = {
    "requestId":"2063799111194234002",
    "type":41,
    "requestTime":1678175409000,
    "mem":4096,
    "cpu":1,
    "subId":"20633312323943240923",
    "metric":"top01##SuccPer_top",
    "trainStartTime":"2023-03-01 00:00:00",
    "trainEndTime":"2023-03-15 00:00:00",
    "detectStartTime":"2023-03-01 00:00:00",
    "detectEndTime":"2023-03-03 00:00:00",
    "isolation":1
}

#沙箱训练
data5 = {
    "requestId":"206374222353114234002",
    "type":42,
    "requestTime":1678175409000,
    "mem":4096,
    "cpu":1,
    "subId":"2022211111942340923",
    "metric":"top02##ResTime_top",
    "trainStartTime":"2023-03-01 00:00:00",
    "trainEndTime":"2023-03-15 00:00:00",
    "isolation":0
}


#沙箱检测
data7 ={
    "requestId":"222222129894234002",
    "type":43,
    "requestTime":1678175409000,
    "mem":4096,
    "cpu":1,
    "subId":"20637444442340923",
    "metric":"top01##ResTime_top",
    "detectStartTime":"2023-03-01 00:00:00",
    "detectEndTime":"2023-03-16 17:40:00",
    "isolation":0
}


#模拟训练检测
data8 = {
	"requestId": "323231111133331113333",
	"type": 31,
	"requestTime": 1679397203000,
	"mem": 4096,
	"cpu": 1,
	"subId": "33344344444444333344444333",
	"metric": "top01##ResPer_top",
	"trainStartTime": "2023-03-01 00:00:01",
	"trainEndTime": "2023-03-15 00:00:01",
	"detectStartTime": "2023-03-01 00:00:01",
	"detectEndTime": "2023-03-05 00:00:01",
	"redisKey": "top-sbu-zld1233332323",
	"algorithmParams": {
		"trainMaxData": 35,
		"lowerBaselineConfidence": 0.5,
		"predDayLength": 7
	}
}


data9 = {
  "requestTime": 1679312287000,
  "subId": "163777767175118592_top01##SuccPer_top",
  "mem": 1024,
  "metric": "top01##FailCount_top",
  "requestId": "batch-task-1637777612679266811",
  "detectStartTime": "2023-03-16 00:00:00",
  "cpu": 1,
  "trainEndTime": "2023-03-20 00:00:00",
  "isolation": 0,
  "trainStartTime": "2023-03-16 00:00:00",
  "type": 41,
  "detectEndTime": "2023-03-20 00:00:00"
}

producer.send('DM_Q_DETEST', data)
producer.close()

# st = parse(sys.argv[1])
# tc = relativedelta(minutes=1)
# newtime=st+tc
# print(stringtime[0:10])
# print(stringtime[11:])
'''for i in range(1440*60):
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
        "value": random.random()
    }
    print(data1)
    if st < datenow:
        producer.send('zld', data1)
        #producer.close()
        st += tc
        print(st)
    else:
        time.sleep(60)
        producer.send('zld', data1)
        #producer.close()
        st += tc

producer.close()'''



'''consumer = KafkaConsumer(
    'metric_train_status',
    auto_offset_reset='earliest',
    bootstrap_servers=["192.168.100.194:9092"]
)

for consumername in consumer:
    new = consumername.value.decode()
    dictnew = json.loads(new)
    #print(dictnew)
    if dictnew["instanceId"] == "201##app26_ResPer_top":
        print(dictnew["startTime"], dictnew["message"])'''


#di_aiops_anal_detn3_log_server