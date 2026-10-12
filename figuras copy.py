print("\033c")

class Figuras:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mover(self, x, y):
        self.x = x
        self.y = y

    def calcularArea(self, figura, valor1, valor2):
        if figura == "rectangulo":
            return valor1 * valor2
        elif figura == "circulo":
            return 3.1416 * (valor1 * valor1)

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getVisible(self):
        return self.visible

    def setVisible(self, visible):
        self.visible = visible


class Rectangulos(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.__ancho = ancho
        self.__alto = alto

    def getAlto(self):
        return self.__alto
    
    def setAlto(self, alto):
        self.__alto = alto
    
    def getAncho(self):
        return self.__ancho
    
    def setAncho(self, ancho):
        self.__ancho = ancho

class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.__radio = radio

    def getRadio(self):
        return self.__radio

    def setRadio(self, radio):
        self.__radio = radio

rectangulo1 = Rectangulos(3, 4, True, 10, 20)
circulo1 = Circulos(3, 3, True, 6)

#Metodos Rectangulo 1
print(f"El valor original de visible es: {rectangulo1.getVisible()}")

rectangulo1.ocultar()
print(f"El Rectangulo 1 es visible? {rectangulo1.getVisible()}")
rectangulo1.mostrar()
print(f"El Rectangulo 1 es visible? {rectangulo1.getVisible()}")
print(f"El area del rectangulo es: {rectangulo1.calcularArea('rectangulo', 10, 20)}")

print("-----------------------------------------------------------------------")

#Metodos del Circulo 1
print(f"El valor original de visible es: {circulo1.getVisible()}")

circulo1.ocultar()
print(f"El circulo 1 es visible? {circulo1.getVisible()}")
circulo1.mostrar()
print(f"El circulo 1 es visible? {circulo1.getVisible()}")
print(f"El area del circulo es: {circulo1.calcularArea('circulo', 6, 0)}")
