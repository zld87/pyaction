import sys, requests, os
import os, json, xlwt
import subprocess, random
import paramiko
import time
from multiprocessing import Process, Pool, Queue
from dateutil.parser import parse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


print(os.getcwd())
if __name__ == '__main__':
    print(__name__)
    print(sys.argv)

print(sys.path)
print(__name__)
a = set()
a.add(1)
a.add(2)
print(a)

url = 'http://192.168.3.16/itsm/itsmboot/user/login'
data = {"login": True, "password": "Password@1", "loginType": "system", "roleLoginType": 0}
json1 = json.dumps(data)
'''for i,x in data.items():
    print(i)
    print(x)
result=requests.post(url=url,json=data)
b=result.text
print(b)

#os.mkdir('zld')
a=os.path.join(os.getcwd(),'zld')
file=os.path.join(a,"request.xls")
os.getcwd()'''
'''#读取jmeter生成的报告文件
f=open('/Users/zhouliudong/Desktop/ruslut.txt')
file=f.readlines()
newfile=[]
for f in range(0,len(file)):
    file[f]=file[f].strip()
    if file[f] != '':
        newfile.append(file[f])
print(newfile)

a=os.path.join(os.getcwd(),'zld')
filepath=os.path.join(a,"request.xls")

for i in newfile:
    if "http://" in i:
        with open(filepath,"a+") as newfile:
            newfile.write(i)
    elif "POST data" in i or "GET data":
        pass






xlwt.Font()
xlwt.XFStyle()'''

a = [1, 2]
b = [1, 2, 3, [1, 2]]

a1 = '123232'
a2 = '123'
a = str(a)
b = str(b)
c = a in b

print(c)


def test():
    print("-------test---------")


def zhou(a, **b):
    print(b)


A = "abcdefg"

print(A[-1::-2])

a = [2 for y in range(10)]
c = type(a)
print(c)


class zhou(object):
    def __call__(self, a):
        print('---call----' + a)


a = zhou()

i = 3
i *= 3
print(i)

i = "测试"
b1 = "zld"
i1 = i.join(b1)
print(i1)

a = 20
if a < 1:
    print(1)
elif a > 1:
    if a == 2:
        print(2)
    else:
        if a == 15:
            print(15)
        elif a == 20:
            print("bingo")

# sub0,sub1=subprocess.getstatusoutput("ls -l")
'''while True:
    sub4=subprocess.getoutput("dir")
    if type(sub4)=="class 'str'":
        break
    print(type(sub4))'''
# print(sub0)
'''ret = os.fork()
print(ret)
if ret == 0:
    f = open("./zld1.log")
    print("循环内----%d--%d--"%(os.getpid(),os.getppid()))
    while True:
        file = f.readline()
        if not file:
            continue
        print(file)'''

# 多线程
# ret=os.fork()
# ret=os.fork()
# print(ret)

print(os.getpid())
# subprocess.run("vim zld1.log",shell=True)
zld1 = subprocess.Popen(["ssh", 'root@192.168.100.186'], stdin=subprocess.PIPE)

print(zld1.returncode)
print(zld1.pid)


def test(*args, **kwargs):
    print(*args)
    print(kwargs)


a = {"name": "zhouludong"}

test(**a)

a = 1, 2, 3
print(a)

print(random.random())


def zld(mm):
    return zld


@zld
def zld123():
    print("zld")


# for i in range(1,30):
#     print (str(i).rjust(5, 0))


a1a = [1, 2, 3, 4, 5, 6]
a2a = ["a", 'b', 'c', 'df']

for x, y in zip(a1a, a2a):
    print(x, y)

a = (123, 323)
c, d = a
print(c, d)

ids = [123, 333]
print(random.choice(ids))

zzl = 22


def zzld():
    global zzl
    zzl += 1
    print(zzl)


zzld()

cc = {'name': 'zhouliuddodng', 'age': 18}


def zldcc(*d, **cc):
    print(cc)
    print(d)


zldcc(**cc)

AA = 15
print(hex(AA))

data = [("p", 1), ("p", 2), ("p", 3),
        ("h", 1), ("h", 2), ("h", 3)]

result = {}
for (key, value) in data:
    if key in result:
        result[key].append(value)
    else:
        result[key] = [value]

print(result)
ee = {'host': '456'}
print(ee.get("host", '123'))

ac = 'abad'
acd = ac.replace('a', 'b', 2)
print(acd)

for z1 in cc.values():
    print(z1)
    print('zldfdf')


if zld33 := ee.get('host3', 3335):
    print(zld33)


n = 2
while (n := n - 1) + 1:
    print(f'a的长度{n}')


print(bin(255))


# requests.request(method='post', )


str_obj = "Hello, world!"
attribute_name = "lower"  # lower()方法用于将字符串转换为小写
attribute_value = getattr(str_obj, attribute_name)
print(str(attribute_value))# 输出：'hello, world!'.lower()

str_obj = "Hello, world!"
attribute_name = "upper"  # isdigit()方法用于检查字符串是否只包含数字字符
has_attribute = hasattr(str_obj, attribute_name)
print(has_attribute)  # 输出：False，因为字符串对象没有isdigit()方法，但有isdigit属性（值为False）和isdecimal属性（值为True）


a = os.path.exists(os.path.join('/Users/zhouliudong/pyaction/', 'display.py'))
print(a)
# while not (a := os.path.exists(os.path.join('/Users/zhouliudong/pyaction/', '*.py'))):
#     print(123)
#     time.sleep(3)


# url = 'https://daas-perf.seazonmotor.com/'
# driver = webdriver.Chrome()
# driver.get(url=url)
# userInput = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入账号/邮箱/手机号"]')
# userInput.send_keys("zld87")
# pwdInput = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入账号密码"]')
# pwdInput.send_keys("123qweASD")
# loginButton = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[5]/div/button')
# loginButton.click()
# smallImage = driver.find_element(By.ID, 'slider-move-btn')
# newDis = int(smallImage.location['x'] - dis * 260 / 590)
#
# print(smallImage.location)
# time.sleep(5)

# a1 = {'name': 'zhouliudong', 'age': 18, 'paly': {'play1': 'dog', 'play2': 'cat'}}
# print(a1.get('paly').get('play1'))

# a = 'RUN'
# PARKING_count = 33
#
# if a == "RUN1" and \
#             (PARKING_count > 3 and PARKING_count <= 33) or \
#             (PARKING_count > 88 and PARKING_count <= 110):
#     print('todo')



str_obj = "Hello, world!"
attribute_name = "upper"  # isdigit()方法用于检查字符串是否只包含数字字符
has_attribute = hasattr(str_obj, attribute_name)
print(has_attribute)

a = {'name': 'zhouliudong', 'age': 18}
b = ('zld', 19)

def zld(*b, **a):
    try:
        print(a)
        # return a
    except Exception as aa:
        print(aa)
    else:
        print('zld')
    finally:
        print(b)

zld(*b, **a)


valid = [True, False]

c = random.choices(valid, weights=[10, 1], k=4)
print(c)


yy = '12323'
print(yy.strip('"'))

# import zmq
#
# context = zmq.Context()
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:8800")
#
# msg1 = {
#             "TYPE": "REP_HMIRunStatus",
#             'time': str(format(time.time(), '.0f')),
#             "DATA": {
#                     # 辅助功能：0为未开启，1为倒垃圾，2为充电，3为加水。
#                     "AUXOPERATE": random.choices([0, 1, 2, 3], weights=[1, 10, 10, 10], k=1)[0],
#                      # 偏航角：范围 -90度到90度
#                      "DirectionAngle": float(format(random.uniform(-90, 90), '.1f')),
#                      # 车辆档位， 0为P档，1为N档，2为R档，3为D档。
#                      "GEAR": random.choices([0, 1, 2, 3], weights=[1, 1, 1, 10], k=1)[0],
#                      # 车辆模式：1 自动驾驶 2 本地驾驶 3 远程遥控。
#                      "MODE": 2,
#                      # 车辆自检状态：0为检测中，1为自检完成。
#                      "RUNSTATE": random.choices([0, 1], weights=[1, 1], k=1)[0],
#                      # 清扫作业启动状态：0为未清扫，1为清扫。（后续细分清扫模式可扩展）
#                      "SWEEP": random.choices([0, 1], weights=[10, 5], k=1)[0],
#                      # 红绿灯识别结果：0为未识别，1为绿灯，2为黄灯，3为红灯。
#                      "TRAFFICLIGHT": random.choices([0, 1, 2, 3], weights=[10, 5, 1, 10], k=1)[0],
#                      # 转向信号，0为直行，1为左转，2为右转。
#                      "TURNROUND": random.choices([0, 1, 2], weights=[10, 1, 1], k=1)[0],
#                      # 车速，单位为km/h
#                      "VCAR": random.randint(10, 30),
#                      # 启/停自动驾驶信号，false为停止，true为启动。
#                      "bStart": 'false',
#                      # 车辆故障的故障码，多个故障码之间用“|”符号隔离。
#                      "ERROR": '',
#                      "OBSTACLES": []
#                      }
#         }
#
#
# newmsg = {
#     'DATA': {
#         'AUXOPERATE': 0,
#         'B': 0.0,
#         'DirectionAngle': 0.0,
#         'GEAR': 0,
#         'L': 0.0,
#         'MODE': 0,
#         'OBSTACLES': [],
#         'RUNSTATE': 0,
#         'SWEEP': 0,
#         'TRAFFICLIGHT': 0,
#         'TURNROUND': 0,
#         'VCAR': 0,
#         'bStart': True,
#         'headingAngle': 0.0
#     },
#     'TYPE': 'REQ_HMIRunStatus'
# }
#
# #客户端必须要先发送消息，然后在接收消息
# if __name__ == '__main__':
#     print('zmq client start....')
#     for i in range(1, 5):
#         socket.send_json(newmsg)
#         message = socket.recv_json()
#         print(message)
#         time.sleep(5)

if is_fault := bool(random.choices([True, False], weights=[1, 10], k=1)[0]):
    print(is_fault)
else:
    print(is_fault)



# 飞书机器人
# url = 'https://open.feishu.cn/open-apis/bot/v2/hook/44155aeb-b5f3-48d1-83d4-bbb846b3db81'
#
# data1 = {"msg_type": "text", "content": {"text": "request example"}}
#
# headers = {"Content-Type": "application/json"}
#
# r = requests.post(url=url, headers=headers, json=data1)
# print(r.text)



i = '77'
print(int(i, 10))


data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data = data[0:10] + 'T' + data[11:19] + 'Z'
print(data)


