import sys
import os
from new import xlwt
import urllib.request
import re
import requests
import logging
import datetime

print(__name__)

print(sys.path)


def test3():
    print('----displaytest3-----')


a = 'abc'
b = 'def'
print(a + b)

print(sys.argv[1:])

a = {"name": 'zhouliudong', "age": 18}

b = a.get('name1')
print(b)


class toperror(Exception):
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = 2
b = 4

if a < b:
    try:
        raise toperror(a, b)
    except toperror as zld:
        print(zld)


class zld(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, a, b):
        self.a = a
        self.b = b


zld1 = zld(133, 144)
Z = zld1.a
# zld2=zld()
print(Z)
# print(id(zld2))


a = [[0, 1, 2, 3], [1, 3, 3]]

try:
    print(a[0][3])
except IndexError as zld:
    print(repr(zld))
    raise

a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(a)

aa = {"name": 123, "name": 456}
print(aa)

a = [i for i in range(0, 11) if i % 2 == 0]
print(a)


# 单例模式，只初始化一次对象
class zld1(object):
    __shuxing = None
    __mingzi = None
    mingzi = 12333333

    def __new__(cls, *args, **kwargs):
        if cls.__shuxing == None:
            cls.__shuxing = object.__new__(cls)
            return cls.__shuxing
        else:
            return cls.__shuxing

    def __init__(self, name):
        if zld1.__mingzi == None:
            zld1.__mingzi = True
            self.name = name


zld111 = zld1('1zzzz')
zld222 = zld1(2222)
zld333 = zld1(33333)

print(zld111.name)
print(zld222.name)
print(zld333.name)
print(zld1.mingzi)
pwd = None

if pwd:
    print(1111)
else:
    print(2222)

# 正则匹配
names = ["d3sdfsdsd", "/", "2_name", "__name__"]
for name in names:
    # print(name)
    reslut = re.match("[\w\$]+", name)
    print(reslut)
    if reslut:
        print("是正确的%s" % reslut.group())
    else:
        print("不正确%s" % name)

aaa = {"name": 'zhouliudong', 'age': 18}


def aaa1(*a, **b):
    print(a)
    print(b)


aaa1(1, 3, 3232)

za = [0, 1, 2, 3, 4, 5, 232, 3, 2, 11, 12, 13]
c = za[0:8:2]
print(c)

open(os.path.join(os.getcwd(), 'testreq.py'), "w")


class cuowu(Exception):
    def __init__(self, xinxi):
        self.xinxi = xinxi


try:
    if 1 + 1 == 2:
        raise cuowu("你算错了")
except cuowu as zld:
    print(zld)

a = [i for i in range(1, 100) if i % 2 == 0]

print(a)
'''logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

a={'name':'zhouliudong','age':'18'}

print(type(a.keys()))
print(type(a.items()))
for i,v in a.items():
    print(i)
    print(v)
    logging.info(f'当前工单{i}{v}')'''

name = '【4554545454545】'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)-4s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='2021.08.12.log',
                    filemode='w')

# logging.FileHandler('zld.log',mode='w',encoding='utf-8')

logging.debug("23232")
logging.info(f'当前工单{name}')
logging.warning('This is 12 message')
logging.warning('This is 13 message')

a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)


def func1(index: int, arr: list):
    '''这个是解释说明一个功能发送使用help()方法可以看到此说明'''
    print(index)
    print(arr)


help(func1)

func1(arr=12, index=78)


def funcwaimian(canshu):
    def func(fm):
        print('--------func1----------')

        def func_in(*args, **kwargs):
            print('---------func_in1---------')
            return fm(*args, **kwargs)
            print('---------func_in2----------')

        return func_in

    return func


@funcwaimian(22)
def test1(a, b, c):
    print('-------test1--%d-%d-%d-----' % (a, b, c))


def test2(a, b, c, d):
    print('-------test2--%d-%d-%d--%d---' % (a, b, c, d))


test1(1111, 2222, 3333)

test2(1111, 2222, 3333, 44444)

r = open('2021.12.20.py', mode='w')
