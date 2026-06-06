import redis
from rediscluster import RedisCluster as Rc

startup_nodes = [{"host": "192.16.11.10", "port": "6379"}]

class Redis_Cli(object):
    def __init__(self, startup_nodes=None, host='192.16.11.10', port=6379, password='xz@2023', db=0,
                 decode_responses=True):
        self.startup_nodes = startup_nodes
        self.host = host
        self.port = port
        self.pwd = password
        self.db = db
        self.decode_responses = decode_responses

    def con_type(self, T_type=2):
        # 单节点连接方式
        if T_type == 1:
            pool = redis.ConnectionPool(host=self.host, port=self.port, password=self.pwd, db=self.db,
                                        decode_responses=self.decode_responses)
            r = redis.Redis(connection_pool=pool)
            return r
        # 集群连接方式
        elif T_type == 2:
            rc = Rc(startup_nodes=self.startup_nodes, password=self.pwd,
                    decode_responses=self.decode_responses)
            return rc




# for key in Redis_Cli(startup_nodes=startup_nodes).get_rckey():
#     if '13916843740_LOGIN' in key:
#         val = Redis_Cli(startup_nodes=startup_nodes).get_value(key)
#         print(val)

# for key in r_redis():
#     if '13916843740_LOGIN' in key:
#         print(key)


