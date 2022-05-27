from main import db
from datetime import datetime as dt
import json

class SimpleUser(db.Model):
    __tablename__ = 'simple_user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    created = db.Column(db.String(20))

    @staticmethod
    def create(username, pwd, name, surname, email):
        user = SimpleUser()
        user.username = username
        user.pwd = pwd
        user.name = name
        user.surname = surname
        user.email = email
        user.created = str(int(dt.now().timestamp()))
        return user

    def getJson(self):
        userJson = {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
        }
        return userJson

    def __repr__(self):
        return str(self.__dict__)