# -*- coding: utf8 -*-

# -*- coding: utf8 -*-

import pymysql
from random import Random

from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

database_info = {
    "host": "106.55.168.100",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "edge_test",
    "charset": "utf8"
}


def get_data():
    http_codes = [{'code': '100', 'message': 'Continue', 'data': '继续。客户端应继续其请求'},
                  {'code': '101', 'message': 'Switching Protocols',
                   'data': '切换协议。服务器根据客户端的请求切换协议。只能切换到更高级的协议，例如，切换到HTTP的新版本协议'},
                  {'code': '200', 'message': 'OK', 'data': '请求成功。一般用于GET与POST请求'},
                  {'code': '201', 'message': 'Created', 'data': '已创建。成功请求并创建了新的资源'},
                  {'code': '202', 'message': 'Accepted', 'data': '已接受。已经接受请求，但未处理完成'},
                  {'code': '203', 'message': 'Non-Authoritative Information',
                   'data': '非授权信息。请求成功。但返回的meta信息不在原始的服务器，而是一个副本'},
                  {'code': '204', 'message': 'No Content', 'data': '无内容。服务器成功处理，但未返回内容。在未更新网页的情况下，可确保浏览器继续显示当前文档'},
                  {'code': '205', 'message': 'Reset Content',
                   'data': '重置内容。服务器处理成功，用户终端（例如：浏览器）应重置文档视图。可通过此返回码清除浏览器的表单域'},
                  {'code': '206', 'message': 'Partial Content', 'data': '部分内容。服务器成功处理了部分GET请求'},
                  {'code': '300', 'message': 'Multiple Choices',
                   'data': '多种选择。请求的资源可包括多个位置，相应可返回一个资源特征与地址的列表用于用户终端（例如：浏览器）选择'},
                  {'code': '301', 'message': 'Moved Permanently',
                   'data': '永久移动。请求的资源已被永久的移动到新URI，返回信息会包括新的URI，浏览器会自动定向到新URI。今后任何新的请求都应使用新的URI代替'},
                  {'code': '302', 'message': 'Found', 'data': '临时移动。与301类似。但资源只是临时被移动。客户端应继续使用原有URI'},
                  {'code': '303', 'message': 'See Other', 'data': '查看其它地址。与301类似。使用GET和POST请求查看'},
                  {'code': '304', 'message': 'Not Modified',
                   'data': '未修改。所请求的资源未修改，服务器返回此状态码时，不会返回任何资源。客户端通常会缓存访问过的资源，通过提供一个头信息指出客户端希望只返回在指定日期之后修改的资源'},
                  {'code': '305', 'message': 'Use Proxy', 'data': '使用代理。所请求的资源必须通过代理访问'},
                  {'code': '306', 'message': 'Unused', 'data': '已经被废弃的HTTP状态码'},
                  {'code': '307', 'message': 'Temporary Redirect', 'data': '临时重定向。与302类似。使用GET请求重定向'},
                  {'code': '400', 'message': 'Bad Request', 'data': '客户端请求的语法错误，服务器无法理解'},
                  {'code': '401', 'message': 'Unauthorized', 'data': '请求要求用户的身份认证'},
                  {'code': '402', 'message': 'Payment Required', 'data': '保留，将来使用'},
                  {'code': '403', 'message': 'Forbidden', 'data': '服务器理解请求客户端的请求，但是拒绝执行此请求'},
                  {'code': '404', 'message': 'Not Found',
                   'data': '服务器无法根据客户端的请求找到资源（网页）。通过此代码，网站设计人员可设置"您所请求的资源无法找到"的个性页面'},
                  {'code': '405', 'message': 'Method Not Allowed', 'data': '客户端请求中的方法被禁止'},
                  {'code': '406', 'message': 'Not Acceptable', 'data': '服务器无法根据客户端请求的内容特性完成请求'},
                  {'code': '407', 'message': 'Proxy Authentication Required',
                   'data': '请求要求代理的身份认证，与401类似，但请求者应当使用代理进行授权'},
                  {'code': '408', 'message': 'Request Time-out', 'data': '服务器等待客户端发送的请求时间过长，超时'},
                  {'code': '409', 'message': 'Conflict', 'data': '服务器完成客户端的 PUT 请求时可能返回此代码，服务器处理请求时发生了冲突'},
                  {'code': '410', 'message': 'Gone',
                   'data': '客户端请求的资源已经不存在。410不同于404，如果资源以前有现在被永久删除了可使用410代码，网站设计人员可通过301代码指定资源的新位置'},
                  {'code': '411', 'message': 'Length Required', 'data': '服务器无法处理客户端发送的不带Content-Length的请求信息'},
                  {'code': '412', 'message': 'Precondition Failed', 'data': '客户端请求信息的先决条件错误'},
                  {'code': '413', 'message': 'Request Entity Too Large',
                   'data': '由于请求的实体过大，服务器无法处理，因此拒绝请求。为防止客户端的连续请求，服务器可能会关闭连接。如果只是服务器暂时无法处理，则会包含一个Retry-After的响应信息'},
                  {'code': '414', 'message': 'Request-URI Too Large', 'data': '请求的URI过长（URI通常为网址），服务器无法处理'},
                  {'code': '415', 'message': 'Unsupported Media Type', 'data': '服务器无法处理请求附带的媒体格式'},
                  {'code': '416', 'message': 'Requested range not satisfiable', 'data': '客户端请求的范围无效'},
                  {'code': '417', 'message': 'Expectation Failed', 'data': '服务器无法满足Expect的请求头信息'},
                  {'code': '500', 'message': 'Internal Server Error', 'data': '服务器内部错误，无法完成请求'},
                  {'code': '501', 'message': 'Not Implemented', 'data': '服务器不支持请求的功能，无法完成请求'},
                  {'code': '502', 'message': 'Bad Gateway', 'data': '作为网关或者代理工作的服务器尝试执行请求时，从远程服务器接收到了一个无效的响应'},
                  {'code': '503', 'message': 'Service Unavailable',
                   'data': '由于超载或系统维护，服务器暂时的无法处理客户端的请求。延时的长度可包含在服务器的Retry-After头信息中'},
                  {'code': '504', 'message': 'Gateway Time-out', 'data': '充当网关或代理的服务器，未及时从远端服务器获取请求'},
                  {'code': '505', 'message': 'HTTP Version not supported', 'data': '服务器不支持请求的HTTP协议的版本，无法完成处理'}]
    return Random().choice(http_codes)


def log(message):
    print("%s  %s" % (datetime.now(), message))


def clear_data():
    connect = pymysql.connect(**database_info)
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""SELECT count(1) as count FROM test""")
    row = cursor.fetchone()
    count = row["count"]
    log("clear_data 当前数据：%s" % count)
    if count >= 100000:
        log("clear_data 清理数据")
        cursor.execute("DELETE FROM test ORDER BY create_time  LIMIT 99900 ")
        connect.commit()
    cursor.close()
    connect.close()


def add():
    connect = pymysql.connect(**database_info)
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    sql = """
        INSERT INTO test(`message`,`code`,`data`,`create_time`) 
        VALUES(%(message)s,%(code)s,%(data)s,%(create_time)s)
    """
    args = get_data()
    args["create_time"] = datetime.now()

    row = cursor.execute(sql, args)
    if row <= 0:
        log("add 添加数据失败")
        cursor.close()
        return
    connect.commit()
    log("add  添加数据成功 %s"%args)
    cursor.close()
    connect.close()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(clear_data, 'cron', next_run_time=datetime.now(), minute="*/1")
    scheduler.add_job(add, 'cron', next_run_time=datetime.now(), second="*/5")
    scheduler.start()