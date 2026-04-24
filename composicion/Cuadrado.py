from Coordenada import Coordenada

class Cuadrado:
    # Método constructor
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    def mostrarVertices(self):
        print("El cuadrado está compuesto por los siguientes vértices:")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()

def main():
    v1 = Coordenada(1,1)
    v2 = Coordenada(4,1)
    v3 = Coordenada(4,4)
    v4 = Coordenada(1,4)
    cuadrado = Cuadrado(v1,v2,v3,v4)
    cuadrado.mostrarVertices()

if __name__ == main():
    main()