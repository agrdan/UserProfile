from enum import Enum
import json

class ResponseCode(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    PARTIAL_CONTENT = 206

    MULTIPLE_CHOICES = 300
    FOUND = 302

    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    REQUEST_TIMEOUT = 408
    CONFLICT = 409

    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503


class ResponseMessage(Enum):
    OK = 'OK'
    CREATED = 'CREATED'
    ACCEPTED = 'ACCEPTED'
    NO_CONTENT = 'NO CONTENT'
    PARTIAL_CONTENT = 'PARTIAL CONTENT'

    MULTIPLE_CHOICES = 'MULTIPLE CHOICES'
    FOUND = 'FOUND'

    BAD_REQUEST = 'BAD REQUEST'
    UNAUTHORIZED = 'UNAUTHORIZED'
    PAYMENT_REQUIRED = 'PAYMENT REQUIRED'
    FORBIDDEN = 'FORBIDDEN'
    NOT_FOUND = 'NOT FOUND'
    METHOD_NOT_ALLOWED = 'METHOD NOT ALLOWED'
    NOT_ACCEPTABLE = 'NOT ACCEPTABLE'
    REQUEST_TIMEOUT = 'REQUEST TIMEOUT'
    CONFLICT = 'CONFLICT'

    INTERNAL_SERVER_ERROR = 'INTERNAL SERVER ERROR'
    NOT_IMPLEMENTED = 'NOT IMPLEMENTED'
    BAD_GATEWAY = 'BAD GATEWAY'
    SERVICE_UNAVAILABLE = 'SERVICE UNAVAILABLE'


class GenericResponseDto:

    @staticmethod
    def createResponse(message, code, data):
        response = {
            'data': data,
            'message': message.value,
            'code': code.value,
        }
        return json.dumps(response)
