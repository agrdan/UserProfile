from utils.JSONSerializator import JSONSerializator


class LoginDto(JSONSerializator):

    def __init__(self):
        self.username = None
        self.password = None


    def __repr__(self):
        loginJson = {
            'username': self.username,
            'password': self.password
        }
        return loginJson
