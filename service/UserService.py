from flask import flash, Response
from datasource.entity.SimpleUser import SimpleUser as User
from datasource.dto.SimpleUserDto import SimpleUserDto as UserDto
from utils.DBUtil import DBUtil
from main import db
from datetime import datetime as dt
from utils.JSONSerializator import JSONSerializator
from datasource.dto.GenericResponseDto import GenericResponseDto, ResponseMessage, ResponseCode
from datasource.dto.LoginDto import LoginDto
from datasource.entity.SimpleToken import SimpleToken
from service.SimpleTokenService import TokenService
from utils.Utils import Utils

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
            response = GenericResponseDto.createResponse(ResponseMessage.FORBIDDEN, ResponseCode.FORBIDDEN, "Username already exists!")
            return Response(response, ResponseCode.FORBIDDEN.value)



        user = UserService.mapUser(userSerialized)
        status, data = DBUtil.insert(user)
        if not status:
            response = GenericResponseDto.createResponse(ResponseMessage.INTERNAL_SERVER_ERROR, ResponseCode.INTERNAL_SERVER_ERROR, data)
            return Response(response, ResponseCode.INTERNAL_SERVER_ERROR.value)
        else:
            userDto = UserDto.createFromEntity(data)
            response = GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK, userDto.getJson())
            return Response(response, ResponseCode.CREATED.value)


    @staticmethod
    def mapUser(serialized):
        user = User.create(serialized.username, serialized.password, serialized.name,
                           serialized.surname, serialized.email)
        return user


    @staticmethod
    def getUserByUsername(username):
        user = DBUtil.findByUsername(User, username)
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
        status = DBUtil.delete(user)


    @staticmethod
    def checkIfTokenIsValid(token):
        tokenEntity: SimpleToken = DBUtil.findByToken(SimpleToken, token)
        if tokenEntity is None:
            response = GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED, ResponseCode.UNAUTHORIZED,
                                                         "Provided token not valid!")
            return False, Response(response, ResponseCode.UNAUTHORIZED.value)
        else:
            diff = Utils.timestapsDiff(tokenEntity.created)
            sec = int(str(diff.seconds))
            print(f"Seconds elapsed {sec}")
            if sec > 300:
                response = GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED, ResponseCode.UNAUTHORIZED,
                                                             "Token is not valid anymore, please login again")
                return False, Response(response, ResponseCode.UNAUTHORIZED.value)

            else:
                return True, None

    @staticmethod
    def getAllUsers(token):
        if token is None:
            response = GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED, ResponseCode.UNAUTHORIZED,
                                                         "Token is not provided!")
            return False, Response(response, ResponseCode.UNAUTHORIZED.value)
        else:
            result, response = UserService.checkIfTokenIsValid(token)
            if not result:
                return False, response
            else:
                users = DBUtil.findAll(User)
                dtoList = []
                for u in users:
                    dtoList.append(UserDto.createFromEntity(u).getJson())
                response = GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK,
                                                             dtoList)
                return True, Response(response, ResponseCode.OK.value)

    @staticmethod
    def getUserById(token, id):
        if token is None:
            response = GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED, ResponseCode.UNAUTHORIZED,
                                                         "Token is not provided!")
            return False, Response(response, ResponseCode.UNAUTHORIZED.value)
        else:
            result, response = UserService.checkIfTokenIsValid(token)
            if not result:
                return False, response
            else:
                user = DBUtil.findById(User, id)
                response = GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK,
                                                             UserDto.createFromEntity(user).getJson())
                return True, Response(response, ResponseCode.OK.value)

    @staticmethod
    def changeUserPasword(token, id, password):
        if token is None:
            response = GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED, ResponseCode.UNAUTHORIZED,
                                                         "Token is not provided!")
            return False, Response(response, ResponseCode.UNAUTHORIZED.value)
        else:

            result, response = UserService.checkIfTokenIsValid(token)
            if not result:
                return False, response
            else:
                if password is None:
                    response = GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED,
                                                                 ResponseCode.UNAUTHORIZED,
                                                                 "[password] is not provided as query parameter!")
                    return False, Response(response, ResponseCode.UNAUTHORIZED.value)
                else:
                    user = DBUtil.findById(User, id)
                    userToken = TokenService.findTokenByUserId(id)
                    if userToken is None or userToken.token is None:
                        response = GenericResponseDto.createResponse(ResponseMessage.FORBIDDEN, ResponseCode.FORBIDDEN,
                                                                     "It is forbidden to change other users passwords!")
                        return True, Response(response, ResponseCode.FORBIDDEN.value)
                    else:
                        if token == userToken.token:
                            message = "Password not changed because it is same as old one!"
                            if user.pwd != password:
                                message = "Password successfully changed!"
                                user.pwd = password
                                DBUtil.commit()
                            response = GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK, message)
                            return True, Response(response, ResponseCode.OK.value)
                        else:
                            response = GenericResponseDto.createResponse(ResponseMessage.FORBIDDEN, ResponseCode.FORBIDDEN,
                                                                         "It is forbidden to change other users passwords!")
                            return True, Response(response, ResponseCode.FORBIDDEN.value)

    @staticmethod
    def updateUser(token, id, jsonBody):
        if token is None:
            response = GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED, ResponseCode.UNAUTHORIZED,
                                                         "Token is not provided!")
            return False, Response(response, ResponseCode.UNAUTHORIZED.value)
        else:
            result, response = UserService.checkIfTokenIsValid(token)
            if not result:
                return False, response
            else:
                userDto = UserDto().serialize(jsonBody, ignoreProperties=False)
                userToken = TokenService.findTokenByUserId(id)
                if userToken is None or userToken.token is None:
                    response = GenericResponseDto.createResponse(ResponseMessage.FORBIDDEN, ResponseCode.FORBIDDEN,
                                                                 "It is forbidden to change other users passwords!")
                    return True, Response(response, ResponseCode.FORBIDDEN.value)
                else:
                    user = DBUtil.findById(User, id)
                    if token == userToken.token:
                        changed = False
                        if userDto.name is not None:
                            user.name = userDto.name
                            changed = True
                        if userDto.surname is not None:
                            user.surname = userDto.surname
                            changed = True
                        if userDto.email is not None:
                            user.email = userDto.email
                            changed = True

                        if changed:
                            DBUtil.commit()
                        response = GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK,
                                                                     UserDto.createFromEntity(user).getJson())
                        return True, Response(response, ResponseCode.OK.value)
                    else:
                        response = GenericResponseDto.createResponse(ResponseMessage.FORBIDDEN, ResponseCode.FORBIDDEN,
                                                                     "It is forbidden to change other users data!")
                        return True, Response(response, ResponseCode.FORBIDDEN.value)
    @staticmethod
    def checkLoginInformation(loginDto: LoginDto):
        user = DBUtil.findByUsername(User, loginDto.username)
        if user is None:
            response = GenericResponseDto.createResponse(ResponseMessage.NOT_FOUND, ResponseCode.NOT_FOUND, "User not found!")
            return False, Response(response, ResponseCode.NOT_FOUND.value)
        else:
            if loginDto.password == user.pwd:
                userToken = TokenService.findTokenByUserId(user.id)
                if userToken is None:
                    userToken = TokenService.createNewTokenByUserId(user.id)
                else:
                    userToken.token = TokenService.createToken()
                    userToken.created = Utils.getCurrentTimestamp()
                    DBUtil.commit()
                userDto: UserDto = UserDto.createFromEntity(user)
                userDto.addToken(userToken.token)
                response = GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK, userDto.getJson())
                return True, Response(response, ResponseCode.OK.value)
            else:
                response = GenericResponseDto.createResponse(ResponseMessage.UNAUTHORIZED, ResponseCode.UNAUTHORIZED,
                                                                "Password is not correct!")
                return False, Response(response, ResponseCode.UNAUTHORIZED.value)




    @staticmethod
    def login(loginJson):
        loginDto = LoginDto().serialize(loginJson, ignoreProperties=False)
        print(loginDto.dumpModel())
        return UserService.checkLoginInformation(loginDto)


