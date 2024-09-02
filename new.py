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





str_obj = "Hello, world!"
attribute_name = "lower"  # lower()方法用于将字符串转换为小写
attribute_value = getattr(str_obj, attribute_name)
print(str(attribute_value))# 输出：'hello, world!'.lower()

str_obj = "Hello, world!"
attribute_name = "upper"  # isdigit()方法用于检查字符串是否只包含数字字符
has_attribute = hasattr(str_obj, attribute_name)
print(has_attribute)  # 输出：False，因为字符串对象没有isdigit()方法，但有isdigit属性（值为False）和isdecimal属性（值为True）


a = os.path.exists(os.path.join('/Users/zhouliudong/pyaction/', '*.py'))
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