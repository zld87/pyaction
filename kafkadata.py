import sys, time, json, re
from datetime import datetime
print(datetime.now())
print(sys.path)

if time.time() < 1659000382:
    print("1111zld")

print(time.time())
class zld(object):
    def __str__(self):
        return "zld"
    def __call__(self, *args, **kwargs):
        print("这是call")

z1 = zld()
print(z1)
z1()


c = "1".ljust(5, "0")
print(c)

#f = open('/Users/zhouliudong/Desktop/xingnengtest/requset_data.json', 'r+')
#content = f.read()

#第一行为key，第二行以及以后为数据value
'''with open("/Users/zhouliudong/Desktop/zld123.csv", "a+") as f:
    f.seek(0)
    for i in f.readlines()[0:1]:
        with open("/Users/zhouliudong/Desktop/zld124.csv", "a+") as f1:
            f1.write(i)
        print(f.tell())
        f.seek(0)
        for y in f.readlines()[1:]:
            print(y[1:27])
            if y[1:27] == "106##test16.succ_count_sum":
                with open("/Users/zhouliudong/Desktop/zld124.csv", "a+") as f1:
                    f1.write("\"app26_TransCount_top\""+y[28:])'''




#正则匹配带冒号""的字符串数据
with open("/Users/zhouliudong/Desktop/zld123.csv", "a+") as f:
    f.seek(0)
    for i in f.readlines()[1:]:
        print(i)
        new = re.match(r"\".+?\"", i)
        if new.group() == '\"106##test16.succ_count_sum\"':
            print(123)
        #if i[1:27] == "106##test16.succ_count_sum":
         #   with open("/Users/zhouliudong/Desktop/zld124.csv", "a+") as f1:
           #     f1.write("\"101##server26_ResPer_top\""+i[28:])