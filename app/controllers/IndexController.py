from flask import request
from models import Index

class IndexController:

    def __init__(self):
        self.model = Index()

    def index(self):
        responses = self.model.getFromRedis()
        return responses

    def create(self):
        m = MySQLHelper()
        m.query = ('INSERT INTO user (firstname,lastname) VALUES (%s, %s)')
        m.data = ('First','Last')
        m.save()
