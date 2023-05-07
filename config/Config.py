import requests
import os
from utils.JSONSerializator import JSONSerializator
import json

class Config(JSONSerializator):

    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = None

    def __init__(self):

        self.appName = None
        self.endpoint = None
        self.connectionUrl = None
        self.readBaseConfig()
        # self.readRemoteConfiguration()


    def readBaseConfig(self):
        f = open("config.json", "r")
        test = json.load(f)
        print(json.dumps(test, indent=4))
        model = JSONSerializator().serialize(test)
        self.SQLALCHEMY_DATABASE_URI = model.dbUri
        self.SECRET_KEY = model.secretKey
        """
        with open("config.json", "r") as reader:
            test = reader.readlines()
            test = json.loads(test)
            print(json.dumps(test, indent=4))
            model = JSONSerializator().serialize(test)
            #self.baseUrl = model.baseUrl
            #self.appName = model.appName
            #self.endpoint = model.endpoint
            self.SQLALCHEMY_DATABASE_URI = model.dbUri
            self.SECRET_KEY = model.secretKey
        """

    def readRemoteConfiguration(self):
        url = "http://{}{}/{}".format(self.baseUrl, self.endpoint, self.appName)
        print(url)
        r = requests.get(url)
        response = JSONSerializator().serialize(r.text)
        self.SQLALCHEMY_DATABASE_URI = response.connectionString