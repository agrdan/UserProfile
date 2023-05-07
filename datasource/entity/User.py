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
    country = db.Column(db.String(40))
    email = db.Column(db.String(40), nullable=False)
    mobile = db.Column(db.String(15))
    user_type = db.Column(db.Integer(), db.ForeignKey('user_type.type'))
    require_change = db.Column(db.Boolean, default=True)
    image = db.Column(db.Text)
    app_id = db.Column(db.Integer(), db.ForeignKey('application.id'))
    active = db.Column(db.Boolean, default=True)
    created = db.Column(db.String(20))


    @staticmethod
    def create(username, pwd, name, surname, type, email, appId=None, address=None, zip=None, city=None, country=None, mobile=None, image=None):
        user = User()
        user.username = username
        user.pwd = pwd
        user.name = name
        user.surname = surname
        user.user_type = type
        user.app_id = appId
        user.email = email
        user.address = address
        user.zip = zip
        user.city = city
        user.country = country
        user.mobile = mobile
        user.image = image
        user.active = True
        user.require_change = True
        user.created = str(int(dt.now().timestamp()))
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

    def __repr__(self):
        return str(self.__dict__)