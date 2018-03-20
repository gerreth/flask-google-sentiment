from flask import request
from models import Entity

class EntityController:

    def __init__(self):
        self.EntityModel = Entity()

    def index(self, message):
        responses = self.EntityModel.getEntities(message)
        return responses
