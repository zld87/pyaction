import redis
pool = redis.ConnectionPool(host="192.168.3.19", port=6379, db=0)
r = redis.Redis(connection_pool=pool)
r.set('top', "123")
keys = r.keys()
for key in keys:
    print(key)

