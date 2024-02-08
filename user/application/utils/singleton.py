# singleton.py
class Singleton:
    _instance = None
    usuarios_temporales = {}

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("Esta clase es un singleton!")
        else:
            Singleton._instance = self