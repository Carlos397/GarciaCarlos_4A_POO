"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

print("\033c")
class Coches:
    def __init__(self, color, marca, velocidad, modelo, potencia, plazas):
        self.__color = color
        self.__marca = marca
        self.__velocidad = velocidad
        self.__modelo = modelo
        self.__potencia = potencia
        self.__plazas = plazas

    def acelerar(self):
        self.__velocidad += 1

    def frenar(self):
        self.__velocidad -= 1

    def getcolor(self):
        return(self.__color)

    def setColor(self, color):
        self.__color = color

    def getMarca(self):
        return(self.__marca)

    def setMarca(self, marca):
        self.__marca = marca

    def getVelocidad(self):
        return self.__velocidad

    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    def getModelo(self):
        return(self.__modelo)

    def setModelo(self, modelo):
        self.__modelo = modelo    

    def getModelo(self):
        return(self.__potencia)

    def setModelo(self, potencia):
        self.__plazas = potencia

    def getModelo(self):
        return(self.__plazas)

    def setModelo(self, plazas):
        self.__plazas = plazas    