# 脚本路径：wordpress\common\proxy_util.py
from datetime import datetime
from mitmproxy import ctx

# 防止引入报错
try:
    from wordpress.common.sql_util import do_create_sql, do_sql
except:
    from wordpress.common.sql_util import do_create_sql, do_sql

# step1 : 定义好创建表语句,body如果是媒体文件，可以换成long blob ,或者把图片存成图片
table = """
CREATE TABLE IF NOT EXISTS api_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    start_time datetime,
    host VARCHAR (255),
    url text,
    method VARCHAR (255),
    headers LONGTEXT,
    body LONGTEXT,
    response LONGTEXT,
    duration float,
    status_code float)
"""

# step2：定义好收集API数据的全局字典
api_data = {}


# step3: 实现request、response数据收集存入api_data
def request(flow):
    if 'www.ztloo.com/wp-json/' in flow.request.url:
        api_data['host'] = flow.request.host  # 存储请求主机名
        api_data['url'] = flow.request.url  # 存储请求的url
        api_data['method'] = flow.request.method  # 存储请求的方法

        headers_dict = {}
        headers = flow.request.headers
        for key, value in headers.items():  # 生成标准典样式的header
            headers_dict[key] = value
        api_data['headers'] = str(headers_dict)  # 存储请求的headers

        if flow.request.method == 'POST':
            api_data['body'] = flow.request.get_text()  # 存储请求body


def response(flow):
    if 'www.ztloo.com/wp-json/' in flow.request.url:
        api_data['response'] = flow.response.text  # 存储返回的response

        # 请求开始时间
        req_start_time = flow.request.timestamp_start
        start_time = datetime.fromtimestamp(req_start_time).strftime('%Y-%m-%d %H:%M:%S')
        ctx.log.info(start_time)  # 控制台打印
        api_data['start_time'] = start_time  # 存储请求开始时间

        # 响应结束时间
        res_end_time = flow.response.timestamp_end

        # 从请求到响应的持续时间
        api_data['duration'] = float(res_end_time) - float(req_start_time)

        # 请求的状态码
        api_data['status_code'] = float(flow.response.status_code)

        # 命令输出窗口的日志打印调试
        ctx.log.info(api_data['duration'])
        ctx.log.info(api_data['status_code'])

        # 把交互的API数据进行存入api_dd 数据库中，table为建表语句
        save_api_table('api_dd', table)


# step4 :把api_data 收集好的数据，进行入库操作
def save_api_table(db_name, table_sql):
    do_create_sql(db_name, table_sql)  # 创建数据库和表

    insert_sql = "INSERT INTO `api_data`" \
                 " (`start_time`, `host`,`url`,`method`," \
                 " `headers`,`body`,`response`," \
                 "`duration`,`status_code`) " \
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    insert_values = (
        api_data.get('start_time'),
        api_data.get('host'),
        api_data.get('url'),
        api_data.get('method'),
        api_data.get('headers'),
        api_data.get('body'),
        api_data.get('response'),
        api_data.get('duration'),
        api_data.get('status_code'),
    )

    # 把api_data全局字典中的请求和返回数据，通过sql插入到对应的库表。
    do_sql(insert_sql, value=insert_values, database=db_name)
