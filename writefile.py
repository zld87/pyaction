import os,xlrd,sys,codecs,xlwt
# from imp import reload
'''reload(sys)
print(sys.getdefaultencoding())
#读取jmeter生成的请求和响应
requestruslut=open('/Users/zhouliudong/Desktop/jmeterdata/requestruslut.txt')
responseruslut=open('/Users/zhouliudong/Desktop/jmeterdata/responseruslut.txt')
#生成用于保存接口测试结果的文件
dirpath=os.path.join(os.getcwd(),'jmeterdata')
#os.mkdir(dirpath)
filepath=os.path.join(dirpath,"request1.xls")
#读取请求数据
requestDatas=requestruslut.readlines()
new_requestruslut=[]
for requestData in range(0,len(requestDatas)):
    requestDatas[requestData]=requestDatas[requestData].strip()
    if requestDatas[requestData] != '':
        new_requestruslut.append(requestDatas[requestData])
print(new_requestruslut)

#写入请求数据到文件
for reqdata in new_requestruslut:
    print(reqdata)
    if "POST http://" in reqdata:
        with codecs.open(filepath,"a+") as caselist:
            caselist.write(reqdata+"\n")
            caselist.write("POST"+"\n")
    elif "GET http://" in reqdata:
        with codecs.open(filepath,"a+") as caselist:
            caselist.write(reqdata+"\n")
            caselist.write("GET"+"\n")
    elif "POST data" in reqdata or "GET data" in reqdata or "no cookies" in reqdata:
        pass
    else:
        with codecs.open(filepath,"a+") as caselist:
            caselist.write(reqdata+"\n")

#读取响应数据
responseDatas=responseruslut.readlines()
#写入请求数据
for resdata in responseDatas:
    resdata=resdata.strip()
    with codecs.open(filepath,"a+",encoding='utf-8') as caselist:
        caselist.write(resdata)'''

#f=codecs.open("/Users/zhouliudong/Desktop/responseruslut.txt","w+")
#f.write("zldtt")


open("20221102_xishu.py", "w+")

class zld(Exception):
    def __init__(self, info=2):
        self.name = info
    def __str__(self):
        return self.name


def excee():
    try:
        raise zld('这是1个错误')
    except zld as reslut:
        print(repr(reslut))


excee()



a = "5"

print(a.rjust(4, "0"))
