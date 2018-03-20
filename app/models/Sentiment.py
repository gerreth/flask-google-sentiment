from services import GoogleAPIHelper, MySQLHelper, RedisHelper
import json
import logging

class Sentiment:
    colors = {
        'good'      : { 'r': 48,  'g':189, 'b':57 },
        'neutral'   : { 'r': 255 ,  'g':215 ,  'b':0  },
        'bad'       : { 'r': 189, 'g':48,  'b':57 }
    }

    def __init__(self):
        pass

    def getSentiment(self, message):
        g = GoogleAPIHelper()
        response = g.sentiment(message)
        response = self.addColor(response)
        return [response]

    def addColor(self,response):
        # add color to document sentiment
        response = self.addColorSteps(response,'documentSentiment')
        # add color to each sentence
        for sentence in response['sentences']:
            sentence = self.addColorSteps(sentence,'sentiment')

        return response

    def addColorSteps(self,content,field):
        good    = self.colors['good']
        neutral = self.colors['neutral']
        bad     = self.colors['bad']

        if content[field]['score'] > 0:
            red     = good['r']
            green   = good['g']
            blue    = good['b']
        elif content[field]['score'] < -0:
            red     = bad['r']
            green   = bad['g']
            blue    = bad['b']
        else:
            red     = neutral['r']
            green   = neutral['g']
            blue    = neutral['b']

        content['color'] = {
            'r': red,
            'g': green,
            'b': blue
        }

        return content

    def addColorGradient(self,content,field):
        good    = self.colors['good']
        bad     = self.colors['bad']
        neutral = self.colors['neutral']

        if content[field]['polarity'] > 0:
            red     = int( neutral['r'] - (content[field]['score'] * (neutral['r'] - good['r'])) )
            green   = int( neutral['g'] - (content[field]['score'] * (neutral['g'] - good['g'])) )
            blue    = int( neutral['b'] - (content[field]['score'] * (neutral['b'] - good['b'])) )
        else:
            red     = int( neutral['r'] + (content[field]['score'] * (neutral['r'] - bad['r'])) )
            green   = int( neutral['g'] + (content[field]['score'] * (neutral['g'] - bad['g'])) )
            blue    = int( neutral['b'] + (content[field]['score'] * (neutral['b'] - bad['b'])) )

        content['color'] = {
            'r': red,
            'g': green,
            'b': blue
        }

        return content
