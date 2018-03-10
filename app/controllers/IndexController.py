from flask import request
from models import Index
from services import GoogleAPIHelper, MySQLHelper
import json

class IndexController:
    message = 'Das ist eine gute Nachricht!'

    def __init__(self):
        self.model = Index()

    def index(self):
        g = GoogleAPIHelper()
        response = g.sentiment(self.message)
        return response

    def create(self):
        m = MySQLHelper()
        m.query = ('INSERT INTO user (firstname,lastname) VALUES (%s, %s)')
        m.data = ('First','Last')
        m.save()
