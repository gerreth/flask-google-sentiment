from flask import request
from models import Entity, Sentiment

class AnalyzeController:

    def __init__(self):
        self.EntityModel = Entity()
        self.SentimentModel = Sentiment()

    def index(self):
        entities, types, sentiments = (None, None, None)

        if request.method == 'POST':
            message = request.form.get('message')

            response = self.EntityModel.getEntities(message)
            sentiments = self.SentimentModel.getSentiment(message)

            entities = {}
            types = []
            for elements in response:
                for entity in elements['entities']:
                    if not entity['name'] in entities:
                        entities[entity['name']] = {}
                        entities[entity['name']]['type'] = entity['type'].lower()
                        if not entity['type'].lower() in types:
                            types.append(entity['type'].lower())
                        if bool(entity['metadata']) and 'wikipedia_url' in entity['metadata']:
                            entities[entity['name']]['wikipedia_url'] = entity['metadata']['wikipedia_url']
                        else:
                            entities[entity['name']]['wikipedia_url'] = {}

            for sentiment in sentiments:
                for sentence in sentiment['sentences']:
                    for entity,values in entities.items():
                        if bool(values['wikipedia_url']):
                            sentence['text']['content'] = str.replace(sentence['text']['content'], entity, '<a href="'+values['wikipedia_url']+'" class="'+values['type']+'">'+entity+'</a>')
                        else:
                            sentence['text']['content'] = str.replace(sentence['text']['content'], entity, '<span class="'+values['type']+'">'+entity+'</span>')

        return entities, types, sentiments
