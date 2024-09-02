# 脚本路径：wordpress\common\sql_util.py
import pymysql.cursors
import sys
from wordpress.config import *


def conn(connect_kwargs):
    # 连接数据库
    connection = pymysql.connect(
        host=connect_kwargs.get("host", "localhost"),
        port=connect_kwargs.get("port", 3306),
        user=connect_kwargs.get("user", "test"),
        password=connect_kwargs.get("password", "12345678"),
        database=connect_kwargs.get("database", "mitmproxy"),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection


def do_query_type(select_type, cursor):
    """ 处理查询类型，封装pymysql 中查询函数，
    :param select_type:  处理do_sql中 的查询逻辑。
    :param cursor: pymysql cursor对象
    :return:
    """
    if isinstance(select_type, str):
        if 'one' in select_type.lower():  # 防止其他人传入：One,ONE
            return cursor.fetchone()  # 查询一条数据
        elif 'all' in select_type.lower():
            return cursor.fetchall()  # 查询所有数据
        elif select_type.isdigit():  # 数字类型字符串处理逻辑
            return cursor.fetchmany(eval(select_type))  # 查询多条数据
    if isinstance(select_type, int):  # 整数类型处理逻辑
        return cursor.fetchmany(select_type)


def do_sql(sql_txt, value=None,
           select_type=None, **connect_kwargs):
    """据pymysql官方demo 封装而成，操作SQL的函数。
    :param sql_txt: 具体执行的SQL语句
    :param value: 查询的条件或具体的创建或修改的参数数据
    :param select_type: "one"查询一条数据、"all"查询全部数据、  "int(数字)":提取多行
    :param connect_kwargs: dict 为数据库链接配置信息。
    :return: 查询返回结果数据，如DDL操作（创建、修改、删除）返回无。
    """
    # 连接数据库
    connection = conn(connect_kwargs)

    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql_txt, value)
                if select_type is not None:
                    return do_query_type(select_type, cursor)
            except Exception as e:
                connection.rollback()
                print('出错了要回滚', e)
            else:
                # 连接在默认情况下是不自动提交的。所以你必须提交以保存你的修改。
                connection.commit()


def do_create_sql(db_name=None, table_sql=None,
                  **connect_kwargs):
    """据pymysql官方demo 封装而成，操作SQL的函数。
    :param table_sql: 创建表的字符串
    :param db_name: 数据库名
    """
    # 连接数据库
    connection = conn(connect_kwargs)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            dbs = [x['Database'] for x in cursor]
            # 如果数据库不存在mysql数据中，创建。
            if db_name not in dbs:
                DB = f"CREATE DATABASE {db_name} " \
                     f"CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
                cursor.execute(DB)
            # 使用数据库
            cursor.execute(f"USE {db_name}")
            try:
                cursor.execute(table_sql)  # 创建表语句
            except Exception as e:
                print('出错了要回滚', e)
                connection.rollback()
            else:
                # 默认情况下连接不是自动提交的。所以你必须手动提交保存
                connection.commit()
    print('程序执行完毕！')


if __name__ == '__main__':
    from wordpress.config import Config

    # 简单测试
    # sample_query = do_sql(sql_txt="select * from api_data", select_type="all")
    # sample_query = do_sql(sql_txt="select *from mitmproxy.req_info", select_type="all")
    # print(sample_query)


# # 条件查询
# query_sql = "SELECT * " \
#             "FROM mitmproxy.req_info " \
#             "WHERE url = %s and id = %s"
# query_args = ("https://www.123.com", 3)  # 就在value 元组中添加，对应多个条件字段的值
# # one 查询一条，all:查询所有、2 : 查询两条
# query_res = do_sql(query_sql, value=query_args, select_type="2")
# print(query_res)


# # 修改
# up_sql = "UPDATE mitmproxy.req_info SET " \
#          "url = %s" \
#          "WHERE id = %s"
#
# up_args = ('get', 1)
# do_sql(up_sql, value=up_args)


# 创库库表测试
# table = """
#           CREATE TABLE IF NOT EXISTS api_data (
#               id INT PRIMARY KEY AUTO_INCREMENT,
#               start_time datetime,
#               host VARCHAR (255),
#               status_code float)
#       """
# # 创建api_cc数据库，和创建表
# do_create_sql(db_name='api_info', table_sql=table)


# 插入数据
# Config.MYSQL_CONNECT['database'] = "api_cc"  # 切换数据库api_cc
# insert_sql = "INSERT INTO api_data (start_time,host,status_code) " \
#              "VALUES (%s,%s,%s)"
#
# insert_args = ("2022-11-12 18:34:32", "192.168.1.102", "502")
#
# # do_sql(insert_sql, value=insert_args, **Config.MYSQL_CONNECT)


# # 关键字配置数据库链接
# do_sql(insert_sql, value=insert_args, host='localhost',
#        user='root', passwd='root', database='api_cc')
