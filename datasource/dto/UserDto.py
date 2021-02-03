from datasource.entity.User import User
import json

class UserDto:

    def __init__(self):
        self.id = None
        self.username = None
        self.name = None
        self.surname = None
        self.address = None
        self.zip = None
        self.city = None
        self.country = None
        self.email = None
        self.mobile = None
        self.appId = None
        self.created = None


    @staticmethod
    def createFromEntity(entity: User):
        user = UserDto()
        user.id = entity.id
        user.username = entity.username
        user.name = entity.name
        user.surname = entity.surname
        user.address = entity.address
        user.zip = entity.zip
        user.city = entity.city
        user.country = entity.country
        user.email = entity.email
        user.mobile = entity.mobile
        user.appId = entity.app_id
        user.created = entity.created
        return user


    def getJson(self):
        userJson = {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'address': self.address,
            'zip': self.zip,
            'city': self.city,
            'country': self.country,
            'mobile': self.mobile,
        }
        return userJson