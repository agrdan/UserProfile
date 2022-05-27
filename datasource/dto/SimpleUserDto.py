from datasource.entity.SimpleUser import SimpleUser
from utils.JSONSerializator import JSONSerializator

class SimpleUserDto(JSONSerializator):

    def __init__(self):
        self.id = None
        self.username = None
        self.password = None
        self.name = None
        self.surname = None
        self.email = None
        self.token = None


    @staticmethod
    def createFromEntity(entity: SimpleUser):
        dto = SimpleUserDto()
        dto.id = entity.id
        dto.username = entity.username
        dto.password = entity.pwd
        dto.name = entity.name
        dto.surname = entity.surname
        dto.email = entity.email
        return dto

    def addToken(self, token):
        self.token = token

    def getJson(self):
        user = {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            "token": self.token
        }
        return user
