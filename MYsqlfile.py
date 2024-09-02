import pymysql
import sys
from deepdiff import grep
# '''你好'''
# #创建数据来源
def dio_app(sql=None):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='test',
        password='12345678',
        database='mitmproxy',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('show databases')
    cursor.execute(sql)
    for x in cursor:
        print(x['Database'])
    conn.commit()
    #print(cursor.fetchone()["id"])
    #print(cursor.scroll(0))

#sql = 'SELECT * FROM mitmproxy.req_info'

#sql1 = "insert into mitmproxy.req_info values (2, "http://www.164.com" "[{\"User-Agent\":\"mitmproxy\"}]", "{id=448}" ,"post")"
#sql2 = "insert into mitmproxy.req_info values (4, "http://www.164.com","[{\"User-Agent\":\"mitmproxy\"}]", "{id=448}" ,"post")"
#sql3 = 'delete from mitmproxy.req_info where id = 3'
sql4 = "update mitmproxy.req_info set url='http://www.zzzz4.com' where id = 1"
sql5 = "insert into mitmproxy.req_info values (2, \"https://www.163.com\",\"[{\"User-Agent\":\"mitmproxy\"}]\",\"{id=448}\",\"post\")"
sql6 = "INSERT INTO mitmproxy.req_info (id, url,parame,method) values (\"9\", \"https://www.123.com\",\"{id=448}\",\"post\")"
sql7 = "INSERT INTO mitmproxy.req_info (id,hearders) values (\"10\", \"\[\{\"User-Agent\":\"mitmproxy\"\}\]\")"
dio_app(sql6)

#\"[{\"User-Agent\":\"mitmproxy\"}]\"
















# class My_Error(Exception):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# try:
#     if a > 0:
#         raise My_Error("name", 18)
# except Exception as zld:
#     print(repr(zld))


# if not {}:
#     print(123)


# obj = {"long": "somewhere", "string": 2, 0: 0, "somewhere": "around", "a": {"b": {"c": {"d": "somewhere1"}}}}
#
# ds1 = obj | grep("somewhere")
#
# print(ds1)
