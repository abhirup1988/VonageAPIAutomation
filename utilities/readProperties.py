import configparser

config=configparser.RawConfigParser()
config.read("..//Configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getserver():
        server = config.get('common info', 'server')
        return server

    @staticmethod
    def getJWTToken():
        token = config.get('JWT Token', 'Token')
        return token

if __name__ == '__main__':
    print(ReadConfig.getJWTToken())