import requests
import os
from utils.JSONSerializator import JSONSerializator

class Config(JSONSerializator):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "ad908fa1243151zu3i4g2uzi34g6"

    def __init__(self):
        pass
        # self.appName = None
        # self.endpoint = None
        # self.connectionUrl = None
        #self.readBaseConfig()
        #self.readRemoteConfiguration()


    def readBaseConfig(self):
        with open("config.json", "r") as reader:
            test = reader.readlines()
            print(test[0])
            model = JSONSerializator().serialize(test[0])
            self.baseUrl = model.baseUrl
            self.appName = model.appName
            self.endpoint = model.endpoint
            self.SECRET_KEY = model.secretKey


    def readRemoteConfiguration(self):
        url = "http://{}{}/{}".format(self.baseUrl, self.endpoint, self.appName)
        print(url)
        r = requests.get(url)
        response = JSONSerializator().serialize(r.text)
        self.SQLALCHEMY_DATABASE_URI = response.connectionString