from flask import flash
from datasource.entity.User import User
from datasource.dto.UserDto import UserDto
from utils.DBUtil import DBUtil
from main import db
from datetime import datetime as dt
from utils.JSONSerializator import JSONSerializator
from datasource.dto.GenericResponseDto import GenericResponseDto, ResponseMessage, ResponseCode
from datasource.dto.LoginDto import LoginDto
from service.ApplicationService import ApplicationService

now = dt.now()
year = now.year


class UserService:


    def __init__(self):
        pass


    @staticmethod
    def create(userJson):
        userSerialized = JSONSerializator().serialize(userJson, ignoreProperties=True)
        print(userSerialized.dumpModel())
        user = DBUtil.findByUsername(User, userSerialized.username)
        if user is not None:
            return GenericResponseDto.createResponse(ResponseMessage.FORBIDDEN, ResponseCode.FORBIDDEN, "Username already exists!")

        app = ApplicationService.findAppById(userSerialized.appId)
        if app is None:
            return GenericResponseDto.createResponse(ResponseMessage.NOT_FOUND,
                                                     ResponseCode.NOT_FOUND, "Application with ID=[{}] not found!".format(userSerialized.appId))
        user = UserService.mapUser(userSerialized)
        status, data = DBUtil.insert(user)
        if not status:
            return GenericResponseDto.createResponse(ResponseMessage.INTERNAL_SERVER_ERROR, ResponseCode.INTERNAL_SERVER_ERROR, data)
        else:
            userDto = UserDto.createFromEntity(data)
            return GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK, userDto.getJson())


    @staticmethod
    def mapUser(serialized):
        user = User.create(serialized.username, serialized.password, serialized.name,
                           serialized.surname, serialized.type, serialized.appId,
                           serialized.email, serialized.address, serialized.zip,
                           serialized.city, serialized.country, serialized.mobile,
                           serialized.image)
        return user



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



    @staticmethod
    def checkLoginInformation(loginDto: LoginDto):
        user = DBUtil.findByUsername(User, loginDto.username)
        if user is None:
            return False, GenericResponseDto.createResponse(ResponseMessage.NOT_FOUND, ResponseCode.NOT_FOUND, "User not found!")
        else:
            if loginDto.password == user.pwd:
                app = ApplicationService.findAppByToken(loginDto.token)
                if app is None:
                    return False, GenericResponseDto.createResponse(ResponseMessage.NOT_FOUND,
                                                                    ResponseCode.NOT_FOUND,
                                                                    "Invalid application token!")
                if app.id == user.app_id:
                    return True, GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK,
                                                                UserDto.createFromEntity(user).getJson())
                else:
                    return False, GenericResponseDto.createResponse(ResponseMessage.NOT_ACCEPTABLE, ResponseCode.NOT_ACCEPTABLE,
                                                                    "Invalid application token!")
            else:
                return False, GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED, ResponseCode.UNAUTHORIZED,
                                                                "Password is not correct!")




    @staticmethod
    def login(loginJson):
        loginDto = LoginDto().serialize(loginJson, ignoreProperties=False)
        print(loginDto.dumpModel())
        return UserService.checkLoginInformation(loginDto)


