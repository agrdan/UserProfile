from datasource.entity.Application import Application
import json

class ApplicationDto:

    def __init__(self):
        self.id = None
        self.name = None
        self.created = None

    @staticmethod
    def createFromEntity(app: Application):
        appDto = ApplicationDto()
        appDto.id = app.id
        appDto.name = app.name
        appDto.created = app.created
        return appDto


    def getJson(self):
        application = {
            'id': self.id,
            'name': self.name,
            'created': self.created
        }
        return json.dumps(application)