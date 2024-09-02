from multiprocessing import Process,Pool,Queue
from threading import Thread as zld
import time
import os,sys


def test():
    time.sleep(5)
    print("---test----%d----%d"%(os.getpid(),os.getppid()))

p = Process(target=test)


'''if __name__ == "__main__":
    p.start()
    p.join()
    print("---ower-----%d"%(os.getpid()))

if 1:
    print("abd%d"%os.getpid())'''

class fulei(object):
    def start(self):
        self.run()


class zilei(fulei):
    def run(self):
        print("333")
        print("testzld123")


p = zilei()
p.start()

for i in range(1001):
    for x in range(1001):
        y=1000-i-x
        if i**2+x**2==y**2:
            print(i,x,y)

a=-2
b=-2
c=a*b
print(a**3)

a={"name":"zhouliudong","age":18}
#判断值类型
for i in a.values():
    if isinstance(i,str):
        print(i)

a=[11,21,31]
def test(zld,zld1,zld2):
    print(zld)
    print(zld1)
    print(zld2)

test(*a)

#open("kafkazld.py","w+")

class zldzld(object):
    def __zldzld(self):
        print("siyoufangfa")

zld = zldzld()
a=0
a +=1
print(a)

tre=[
        {
            "metric_type": "Performance",
            "object_type": "Discovered hosts"
        },
        {
            "metric_type": "resp_rate_avg",
            "object_type": "ip"
        },
        {
            "metric_type": "resp_time_avg",
            "object_type": "ip"
        },
        {
            "metric_type": "succ_rate_avg",
            "object_type": "ip"
        },
        {
            "metric_type": "trans_count_sum",
            "object_type": "ip"
        }
    ]

c =os.getcwd()
print(c)
print(type(c))

f = open"./zld1.log", "r")
print(type(f.readline()))