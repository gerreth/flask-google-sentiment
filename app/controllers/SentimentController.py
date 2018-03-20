from flask import request
from models import Sentiment

class SentimentController:

    def __init__(self):
        self.SentimentModel = Sentiment()

    def index(self, message):
        responses = self.SentimentModel.getSentiment(message)
        return responses
