from services import GoogleAPIHelper, MySQLHelper, RedisHelper
import json

class Index:
    # message = 'Das ist eine schlechte Nachricht! Das ist eine gute Nachricht! Das ist eine Nachricht!'
    # message = 'Mist. Irgendwas mit Käse. Hehe. Was denkst du? Gut oder Schlechte? Schlecht? Gut! Oh nein! Das sieht nicht gut aus! Das ist scheisse! Oh Mist!'

    message = 'In Lauffen am Neckar in Baden-Württemberg ist offenbar ein Brandanschlag auf ein Moscheegebäude verübt worden. Die Brandsätze, sogenannte Molotowcocktails, richteten zwar nur Sachschaden an, die Polizei ermittelt nach eigenen Angaben aber wegen versuchten Mordes, weil sich der Imam zur Tatzeit in dem Gebäude aufhielt. Hinweise auf Täter lagen der Polizei zunächst nicht vor. Ein oder mehrere bislang Unbekannte hatten die Brandsätze in ein Nebengebäude der Moschee geworfen, in dem sich laut Polizei Gemeinschafts- und Fortbildungsräume, aber auch Wohnräume des Imams befinden. In dem Gebäude kam es zu erheblichen Verrußungen, das aufflammende Feuer konnte gelöscht werden. Der Schaden wird auf etwa 5.000 Euro geschätzt. Verletzt wurde niemand. Laut Bundesinnenministerium gab es im vergangenen Jahr knapp 1.000 Angriffe auf Muslime und muslimische Einrichtungen. Dabei wurden 33 Menschen verletzt.'

    colors = {
        'good'      : { 'r': 48,  'g':189, 'b':57 },
        'neutral'   : { 'r': 255 ,  'g':215 ,  'b':0  },
        'bad'       : { 'r': 189, 'g':48,  'b':57 }
    }

    def __init__(self):
        pass

    def getFromGoogle(self):
        g = GoogleAPIHelper()
        response = g.sentiment(self.message)
        response = self.addColorGradient(response)
        return [response]

    def getFromRedis(self):
        r = RedisHelper();
        responses = []
        for key in r.scan('*'):
            response = r.get(key)
            response = self.addColorGradient(response)
            responses.append(response)
        return responses

    def addColor(self,response):
        good    = self.colors['good']
        neutral = self.colors['neutral']
        bad     = self.colors['bad']

        for sentence in response['sentences']:
            if sentence['sentiment']['score'] > 0.25:
                red     = good['r']
                green   = good['g']
                blue    = good['b']
            elif sentence['sentiment']['score'] < -0.25:
                red     = bad['r']
                green   = bad['g']
                blue    = bad['b']
            else:
                red     = neutral['r']
                green   = neutral['g']
                blue    = neutral['b']

            sentence['color'] = {
                'r': red,
                'g': green,
                'b': blue
            }
        return response

    def addColorGradient(self,response):
        good    = self.colors['good']
        bad     = self.colors['bad']
        neutral = self.colors['neutral']

        for sentence in response['sentences']:
            if sentence['sentiment']['polarity'] > 0:
                red     = int( neutral['r'] - (sentence['sentiment']['score'] * (neutral['r'] - good['r'])) )
                green   = int( neutral['g'] - (sentence['sentiment']['score'] * (neutral['g'] - good['g'])) )
                blue    = int( neutral['b'] - (sentence['sentiment']['score'] * (neutral['b'] - good['b'])) )
            else:
                red     = int( neutral['r'] + (sentence['sentiment']['score'] * (neutral['r'] - bad['r'])) )
                green   = int( neutral['g'] + (sentence['sentiment']['score'] * (neutral['g'] - bad['g'])) )
                blue    = int( neutral['b'] + (sentence['sentiment']['score'] * (neutral['b'] - bad['b'])) )

            sentence['color'] = {
                'r': red,
                'g': green,
                'b': blue
            }
        return response
