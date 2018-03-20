from services import GoogleAPIHelper, MySQLHelper, RedisHelper
import json
import logging

class Entity:
    def __init__(self):
        pass

    def getEntities(self, message):
        g = GoogleAPIHelper()
        entities = g.entities(message)
        return [entities]
