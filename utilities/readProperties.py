import configparser
import os

config = configparser.RawConfigParser()
config.read("C://Users//HP//PycharmProjects//pythonFrameWork//configuration//config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get("common info", 'baseUrl')
        return url

    @staticmethod
    def getUserEmail():
        user = config.get("common info", 'username')
        return user

    @staticmethod
    def getUserPassword():
        pwd = config.get("common info", 'password')
        return pwd
