from utils.DBUtil import DBUtil
from datasource.entity.Application import Application
from datasource.dto.ApplicationDto import ApplicationDto
from datasource.dto.GenericResponseDto import GenericResponseDto, ResponseMessage, ResponseCode

class ApplicationService:


    @staticmethod
    def createApplication(name):
        if not ApplicationService.appNameExists(name):
            app = Application.create(name)
            DBUtil.insert(app)
            appDto = ApplicationDto.createFromEntity(app)
            return GenericResponseDto.createResponse(ResponseMessage.CREATED, ResponseCode.CREATED, appDto.getJson())
        else:
            return GenericResponseDto.createResponse(ResponseMessage.CONFLICT, ResponseCode.CONFLICT, None)


    @staticmethod
    def findAppByName(name):
        app = DBUtil.findByName(Application, name)
        return app



    @staticmethod
    def getAppByName(name):
        app = ApplicationService.findAppByName(name)
        if app is None:
            return GenericResponseDto.createResponse(ResponseMessage.NOT_FOUND, ResponseCode.NOT_FOUND, None)
        else:
            appDto = ApplicationDto.createFromEntity(app)
            return GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK, appDto.getJson())


    @staticmethod
    def findAppByToken(token):
        app = DBUtil.findByToken(Application, token)
        return app

    @staticmethod
    def findAppById(id):
        app = DBUtil.findById(Application, id)
        return app


    @staticmethod
    def getAppByToken(token):
        app = ApplicationService.findAppByToken(token)
        if app is None:
            return GenericResponseDto.createResponse(ResponseMessage.NOT_FOUND, ResponseCode.NOT_FOUND, None)
        else:
            appDto = ApplicationDto.createFromEntity(app)
            return GenericResponseDto.createResponse(ResponseMessage.OK, ResponseCode.OK, appDto.getJson())

    @staticmethod
    def appNameExists(name):
        app = ApplicationService.findAppByName(name)
        if app is not None:
            return True
        else:
            return False