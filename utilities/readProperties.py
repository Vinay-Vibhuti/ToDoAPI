import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\arist\\PycharmProjects\\ToDoApi\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getBaseURL():
        BaseURL = config.get('common url', 'baseurl')
        return BaseURL
