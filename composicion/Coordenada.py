class Coordenada:
    # Metodo constructor
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    # Metodos de acceso
    def getX(self):
        return self.__X

    def setX(self, x):
        self.__X = x

    def getY(self):
        return self.__Y

    def setY(self, y):
        self.__Y = y

    # Metodo para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(",self.__X,",",self.__Y, ")")