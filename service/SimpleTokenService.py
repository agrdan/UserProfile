from datasource.entity.SimpleToken import SimpleToken
from datasource.dto.SimpleUserDto import SimpleUserDto
from utils.DBUtil import DBUtil
from utils.Utils import Utils
import uuid


class TokenService:

    @staticmethod
    def findTokenByUserId(userId):
        simpleToken: SimpleToken = DBUtil.findTokenByUserID(SimpleToken, userId)
        return simpleToken

    @staticmethod
    def findTokenByToken(token):
        simpleToken: SimpleToken = DBUtil.findByToken(SimpleToken, token)
        return simpleToken


    @staticmethod
    def createNewTokenByUserId(userId):
        token = SimpleToken()
        token.token = TokenService.createToken()
        token.created = Utils.getCurrentTimestamp()
        token.user_id = userId
        DBUtil.insert(token)
        return token


    @staticmethod
    def createToken():
        return str(uuid.uuid4())