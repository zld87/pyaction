import paramiko
# 远程登陆操作系统
def remoteSsh(sys_ip, username, command, password=''):
    try:
        # 创建ssh客户端
        client = paramiko.SSHClient()
        # 第一次ssh远程时会提示输入yes或者no
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if len(password) == 0:
            print('互信方式远程连接')
            key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
            client.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)
        else:
            print('密码方式远程连接') # base64.b64decode(password).decode()
            client.connect(sys_ip, 22, username=username, password=password, timeout=20)
        print(f"开始在远程服务器上执行指令:{command}")
        # 执行查询命令
        stdin, stdout, stderr = client.exec_command(f"""{command}""")
        # 获取查询命令执行结果,返回的数据是一个list
        for i in range(10):
            #result = stdout.channelchannel.setblocking(False)
            #recv = result.recv()
            print(f"{sys_ip}执行结果:", stdout.readline())
        #print(dir(stderr))
        #error = stderr.read()
        #print(type(error))
        #if error != "":
        #    print(f"{sys_ip}错误信息:", error)
        #else:
        #    pass
    except Exception as e:
        print(e)
    finally:
        client.close()

#remoteSsh("192.168.70.28", "root", "cd /python_makedata/log/;tail -200f duowei.log", "dm123456")
remoteSsh("192.168.200.114", "root", "cd /data/dm/di-monitor-3.0.2303/logs;tail -n 1 -f di-monitor.log", "P@ssw0rd")
#remoteSsh("192.168.70.28", "root", "cd /python_makedata/log/", "dm123456")


#remoteSsh("192.168.20.191", "root", "cd /python_makedata/;nohup python kafkazldcopy.py 2023-03-01 S#FC011 &", "ka0@2021")


# with open('./option2.sh', 'a', encoding='utf-8') as fa:
#     for i in range(0, 10000):
#         # print(f"{i:02}")
#         sh = f"nohup python kafkazldcopy.py 2023-03-01 T#TEST{i:04} &"
#         fa.write(f"{sh}\nsleep 3\n")



# with open('metric2.csv', "a+") as 'metric':
#     for i in range(5000, 7000):
#         metric.write(f"\"T#TEST{i:04}\""+",")


# pool1 = redis.ConnectionPool(host='192.168.200.110', port='16379', password='hds2g23453kxsS1', db=0)
# r1 = redis.Redis(connection_pool=pool1)
# for i in r1.keys():
#     if i == b'AlgoDetectMetricList':
#         print(r1.type(i))
#         for i in range(4, 10000):
#             r1.hset("AlgoDetectMetricList", f"T#TEST{i:04}", 1)
#             #print(r1.hmget(i, "T#TEST0000", 'T#TEST0001', 'T#TEST0002', 'T#TEST0003'))
#         #r1.hmget()



class err1(Exception):
    def __init__(self, name, age):
        self.name =name

def zldd(m):
    try:
        if m > 3:
            raise err1("3", 13)
    except err1 as zld_err:
        print(repr(zld_err))
        print(zld_err)
        print(zld_err.name)
    except:
        print(1323)


#zldd(4)


