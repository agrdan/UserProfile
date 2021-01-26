from flask import flash
from datasource.entity.User import User
from utils.DBUtil import DBUtil
from main import db
from datetime import datetime as dt

now = dt.now()
year = now.year


class UserService:


    def __init__(self):
        pass


    @staticmethod
    def create(name, surname, username, type, appId):
        user = DBUtil.findByUsername(User, username)
        if user is not None:
            flash("Username already exists", 'fail')
            return False
        pwd = '!{}{}123!'.format(username, year)
        user = User.create(username, pwd, name, surname, type, appId)
        DBUtil.insert(user)
        return True

    @staticmethod
    def updateUser(user):
        update = DBUtil.findById(User, user.id)
        update.require_change = user.require_change
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False


    @staticmethod
    def getUserByUsername(username):
        user = DBUtil.findByUsername(User, username)
        return user

    @staticmethod
    def getAllUsers():
        return DBUtil.findAll(User)


    @staticmethod
    def getUserById(id):
        user = DBUtil.findById(User, id)
        return user

    @staticmethod
    def changeUserPassword(username, password):
        try:
            user = DBUtil.findByUsername(User, username)
            user.pwd = password
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False


    @staticmethod
    def deleteUserById(id):
        user = DBUtil.findById(User, id)
        if user.username == 'admin':
            flash("Admin cannot be deleted!")
        else:
            status = DBUtil.delete(user)
            if status:
                flash("User successfully deleted!", "success")
            else:
                flash("Error occurred!", "error")

