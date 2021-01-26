from main import db
from datetime import datetime as dt
import json

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    address = db.Column(db.String(70))
    zip = db.Column(db.String(10))
    city = db.Column(db.String(20))
    email = db.Column(db.String(40))
    mobile = db.Column(db.String(15))
    user_type = db.Column(db.Integer(), db.ForeignKey('user_type.type'))
    require_change = db.Column(db.Boolean, default=True)
    app_id = db.Column(db.Integer(), db.ForeignKey('application.id'))
    created = db.Column(db.String(20))


    @staticmethod
    def create(username, pwd, name, surname, type, appId):
        user = User()
        user.username = username
        user.pwd = pwd
        user.name = name
        user.surname = surname
        user.user_type = type
        user.require_change = True
        user.created = str(int(dt.now().timestamp()))
        return user

    def __repr__(self):
        return str(self.__dict__)