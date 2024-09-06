from dateutil.parser import parse
import random


def sum_value(value=None):
	succ_count_value = 0
	if value == None:
		src_ip = random.choice(["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"])
		resp_code = random.choice(['200', '304', '400', '402', '502'])
		method_type = random.choice(['get', 'post', 'update', 'delete', 'put'])
		dist_port = random.choice(['8000', '8001', '27001', '34000'])
		src_os = random.choice(
			['Linux; Android 5.1.1"', 'Linux; Android 5.1.2', 'mac; os 5.1.3', 'nginx; Android 5.1.4"'])
		return (src_ip, resp_code, method_type, dist_port, src_os)
	elif value == 2:
		val_float = random.choice([random.random(), random.uniform(0.01, 0.0010)])
		mertic_value = format(val_float, ".3f")
		return float(mertic_value)
	elif value == 2:
		FailCount_value = random.choice([1, 0])
		if FailCount_value == 1:
			succ_count_value = 0
			return succ_count_value

		else:
			succ_count_value = 1
			return succ_count_value
	else:
		print(type(value))
		t_tuple = value.timetuple()
		timestamp = time.mktime(t_tuple)
		value = format(timestamp, '.0f')
		return int(value)


st = parse('2022-12-01')

data = {
    "data_source": "top_zld01",
    "objects": [{
        "id": "top_object01",
        "object_class": "top_object",
        "object_name": "top01",
        "metrics": [{
            "id": "top_object01#resp_time01",
            "metric_class": "RespTime",
            "metric_key": "top_zld01#top_object#resp_time01",
            "metric_name": "top响应时间",
            "value": sum_value(1),
            "dimensions": ["src_ip", "resp_code", "method_type", "dist_port", "src_os"]
        }, {
            "id": "top_object01#TransCount01",
            "metric_class": "TransCount",
            "metric_key": "top_zld01#top_object#TransCount01",
            "metric_name": "top交易量",
            "value": 1,
            "dimensions": ["src_ip", "resp_code", "method_type", "dist_port", "src_os"]
        }, {
            "id": "top_object01#FailCount01",
            "metric_class": "FailCount",
            "metric_key": "top_zld01#top_object#FailCount01",
            "metric_name": "top失败量",
            "value": sum_value(2),
            "dimensions": ["src_ip", "resp_code", "method_type", "dist_port", "src_os"]
        }, {
            "id": "top_object01#succ_count01",
            "metric_class": "succ_count",
            "metric_key": "top_zld01#top_object#succ_count01",
            "metric_name": "top成功量",
            "value": 1,
            "dimensions": ["src_ip", "resp_code", "method_type", "dist_port", "src_os"]
        }]
    }],
    "time": str(st),
    "json": {
        "src_ip": sum_value()[0],
        "resp_code": sum_value()[1],
        "method_type": sum_value()[2],
        "dist_port": sum_value()[3],
        "src_os": sum_value()[4]
    }
}

sum_value()

print(data)
val_float = sum_value(1)
print(val_float)
