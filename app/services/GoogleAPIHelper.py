from googleapiclient.discovery import build
from services import RedisHelper
import os

APIKEY  = os.environ['APIKEY']

class GoogleAPIHelper:
    def __init__(self):
        self.r = RedisHelper()
    def sentiment(self,message):
        """
        Args:
        message (str): Sentence to analyze
        """
        service     = build('language', 'v1beta1', developerKey = APIKEY, cache_discovery = False)
        response    = self.r.get('sentiment_' + message)
        if response == None:
            response = service.documents().analyzeSentiment(
                body = {
                    'document': {
                    'type': 'PLAIN_TEXT',
                    'content': message
                }
            }).execute()
        self.r.set('sentiment_' + message,response)
        return response

    def entities(self, message):
        """
        Detects entities in the message.
        """
        service     = build('language', 'v1beta1', developerKey = APIKEY, cache_discovery = False)
        response    = self.r.get('entitites_' + message)
        if response == None:
            response = service.documents().analyzeEntities(
                body = {
                    'document': {
                    'type': 'PLAIN_TEXT',
                    'content': message
                }
            }).execute()
        self.r.set('entitites_' + message,response)

        return response
