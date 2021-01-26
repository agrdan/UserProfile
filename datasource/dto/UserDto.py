from datasource.entity.User import User
import json

class UserDto:

    def __init__(self):
        self.username = None
        self.name = None
        self.surname = None
        self.address = None
        self.zip = None
        self.city = None
        self.email = None
        self.mobile = None
        self.appId = None
        self.created = None


    @staticmethod
    def createFromEntity(entity: User):
        user = UserDto()
        user.username = entity.username
        user.name = entity.name
        user.surname = entity.surname
        user.address = entity.address
        user.zip = entity.zip
        user.city = entity.city
        user.email = entity.email
        user.mobile = entity.mobile
        user.appId = entity.app_id
        user.created = entity.created
        return user


    def getJson(self):
        user = {
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'address': self.address,
            'zip': self.zip,
            'city': self.city,
            'email': self.email,
            'mobile': self.mobile,
            'appId': self.appId,
            'created': self.created
        }
        return json.dumps(user)