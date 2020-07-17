class Aristas:
    __color1 = '0'
    __color2 = '0'

    def __init__(self):
        self.__color1 = 0
        self.__color2 = 0

    def __init__(self, color1, color2):
        self.__color1 = color1
        self.__color2 = color2

    def setColor1(self, color1):
        self.__color1 = color1

    def setColor2(self, color2):
        self.__color2 = color2

    def getColor1(self):
        return self.__color1

    def getColor2(self):
        return self.__color2
