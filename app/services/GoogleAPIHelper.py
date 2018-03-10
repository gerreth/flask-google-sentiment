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
        response    = self.r.get(message)
        if response == None:
            response = service.documents().analyzeSentiment(
                body = {
                    'document': {
                    'type': 'PLAIN_TEXT',
                    'content': message
                }
            }).execute()
        self.r.set(message,response)
        return response
