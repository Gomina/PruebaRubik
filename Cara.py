from Arista import Arista
from Esquina import Esquina

class Cara:
    __centro = '0'
    __e1 = Esquina()
    __e2 = Esquina()
    __e3 = Esquina()
    __e4 = Esquina()
    __a1 = Arista()
    __a2 = Arista()
    __a3 = Arista()
    __a4 = Arista()

    def __init__(self, centro):
        self.__centro = centro