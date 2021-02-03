from utils.JSONSerializator import JSONSerializator


class LoginDto(JSONSerializator):

    def __init__(self):
        self.username = None
        self.password = None
        self.appId = None
        self.token = None
