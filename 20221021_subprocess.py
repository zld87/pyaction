#from subprocess import Popen as popen
import subprocess
import os, time
import random, sys
c = subprocess.Popen("df -lh", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#print(c.stdout.read())
#while True:
for i in range(20):
    c = subprocess.Popen("df -lh", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #c.stdout.seek(0, io.BytesIO)
    print(c.stdout.readline())
    print(111)
    print(c.stderr.read().decode())
    print(222)
    #out, err = c.communicate(input="print(\"zld\") \n".encode())
    #print(out)
    #print(err)


# #while True:
#     #print("zhuxianc")
# tre_timeArray = time.localtime(1666593545000/1000)
# tre_otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S.%f", tre_timeArray)
# print(tre_otherStyleTime)
# #print(c.stdout.readline())
