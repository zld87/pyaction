import redis
from rediscluster import RedisCluster as Rc

startup_nodes = [{"host": "192.16.11.10", "port": "6379"}]

# 单节点连接方式
# def r_redis():
#     pool = redis.ConnectionPool(host="192.16.11.10", port=6379, password='xz@2023', db=0,
#                                 decode_responses=True)
#     r = redis.Redis(connection_pool=pool)
#     keys = r.keys()
#     return keys


# 集群连接方式
# def rc_redis():
#     rc = Rc(startup_nodes=startup_nodes, password='xz@2023', decode_responses=True)
#     rc_keys = rc.keys()
#     return rc_keys


class Redis_Cli(object):
    def __init__(self, startup_nodes, host='192.16.11.10', port=6379, password='xz@2023', db=0,
                 decode_responses=True):
        self.startup_nodes = startup_nodes
        self.host = host
        self.port = port
        self.pwd = password
        self.db = db
        self.decode_responses = decode_responses

    # 集群连接方式
    def get_rckey(self):
        rc = Rc(startup_nodes=self.startup_nodes, password=self.pwd,
                decode_responses=self.decode_responses)
        rc_keys = rc.keys()
        return rc_keys

    # 单节点连接方式
    def get_rkey(self):
        pool = redis.ConnectionPool(host=self.host, port=self.port, password=self.pwd, db=self.db,
                                    decode_responses=self.decode_responses)
        r = redis.Redis(connection_pool=pool)
        r_keys = r.keys()
        return r_keys

    def get_value(self, key):
        rc = Rc(startup_nodes=self.startup_nodes, password=self.pwd,
                decode_responses=self.decode_responses)
        str_val = rc.get(key)
        return str_val


# for key in Redis_Cli(startup_nodes=startup_nodes).get_rckey():
#     if '13916843740_LOGIN' in key:
#         val = Redis_Cli(startup_nodes=startup_nodes).get_value(key)
#         print(val)

# for key in r_redis():
#     if '13916843740_LOGIN' in key:
#         print(key)


