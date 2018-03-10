import json
import os
import redis

REDIS_HOST  = os.environ['REDIS_HOST']
REDIS_DB    = os.environ['REDIS_DB']

class RedisHelper():
    def __init__(self):
        self.r = redis.StrictRedis(host=REDIS_HOST, port=6379, db=REDIS_DB)
    def get(self,key):
        value = self.r.get(key)
        return value == None and value or json.loads(value)
    def set(self,key,value):
        self.r.set(key, json.dumps(value))
