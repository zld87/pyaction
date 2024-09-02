import pymysql
import redis
import re,gzip
from rediscluster import RedisCluster

#连接数据库
'''coon1=pymysql.connect(
    host='mysql.lcbtest.cn',
    port=3306,
    user='lcb_dev',
    password='@,ue"L&5WylnK$GRb&ms',
    database='lcb_mic_user_db',
    charset='utf8mb4'
)


zldcursor=coon1.cursor(pymysql.cursors.DictCursor)
#sql="SELECT *,AES_DECRYPT(UNHEX(mobile_encry),"9dc5d8e623ca4fb6a91266ddf0f17180") FROM lcb_mic_user_db.us_micro_user WHERE id = 5023264"
sql1="SELECT * FROM lcb_sms_db.sms_biz_template"
sql2="SELECT * FROM lcb_mic_user_db.us_micro_user WHERE AES_DECRYPT(UNHEX(mobile_encry)) = 13916843740;"
zldcursor.execute(sql1)
print(zldcursor.fetchmany(100))
#print(zldcursor.fetchone())
#print(zldcursor.fetchone())
zldcursor.scroll(2,mode='absolute')
#print(zldcursor.fetchall())
#print(zldcursor.fetchone())'''

#正则
'''a="new-day"
reslut=re.match("[-\w]+",a)
print(reslut.group())'''


#连接reids
# pool=redis.ConnectionPool(host='192.168.200.110', port=6379, db=0)
# r=redis.StrictRedis(connection_pool=pool)
# print (r.get('test'))
#
# keys=r.scan_iter("*")
# for key in keys:
#     if b'LCB_API_user_sendSmsIpCount' in key:
#         print(key)
#         del key

#连接redis集群
'''startup_nodes = [{"host": "192.168.100.168", "port": "6380"},
                 {"host": "192.168.100.168", "port": "6381"},
                 {"host": "192.168.100.195", "port": "6380"},
                 {"host": "192.168.100.195", "port": "6381"},
                 {"host": "192.168.100.196", "port": "6380"},
                 {"host": "192.168.100.196", "port": "6381"}]'''

startup_nodes = [{"host": "192.168.100.181","port": "6380"},
                {"host": "192.168.100.181","port": "6379"}]

startup_nodes1 = [{"host": "192.168.200.110", "port": "16379"}]

#rc = RedisCluster(startup_nodes=startup_nodes1, password="hds2g23453kxsS1", decode_responses=True)

#rc.set("foo", "bar")
# for key in rc.keys():
#     Type = rc.type(key)
#     if Type == "hash":
#         print(key)
#         #print(userInfo.decode('unicode_escape'))






