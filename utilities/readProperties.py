import configparser
import os

config = configparser.RawConfigParser()
# path = os.path.abspath(os.curdir)
# print(path)
# config.read(os.path.abspath(os.curdir) + "\\configurations\\config.ini")
config.read("D:\eCommerceSite_V1\configurations\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        email = config.get('commonInfo', 'email')
        return email
