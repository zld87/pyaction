import redis
from rediscluster import RedisCluster

startup_nodes = [{"host": "192.16.11.10", "port": "6379"}]

# 单节点链接池方式
pool = redis.ConnectionPool(host="192.16.11.10", port=6379, password='xz@2023', db=0, decode_responses=True)
r = redis.Redis(connection_pool=pool)
keys = r.keys()

# 集群链接方式
rc = RedisCluster(startup_nodes=startup_nodes, password='xz@2023', decode_responses=True)
rc_keys = rc.keys()

for key in keys:
    print(key)

