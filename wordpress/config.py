class Config(object):
    # mysql 数据库链接配置
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_NAME = 'test'
    MYSQL_PASS = '12345678'
    DATABAASE_NAME = 'mitmproxy'

    MYSQL_CONNECT = {
        'host': MYSQL_HOST,
        'port': MYSQL_PORT,
        'user': MYSQL_NAME,
        'password': MYSQL_PASS,
        'database': DATABAASE_NAME
    }