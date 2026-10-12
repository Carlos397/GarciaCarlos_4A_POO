"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

print("\033c")
class Coches:
    def __init__(self, color, marca, velocidad, modelo, potencia, plazas):
        self._color = color
        self._marca = marca
        self._velocidad = velocidad
        self._modelo = modelo
        self._potencia = potencia
        self._plazas = plazas

    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1

    def getcolor(self):
        return(self._color)

    def setColor(self, color):
        self._color = color

    def getMarca(self):
        return(self._marca)

    def setMarca(self, marca):
        self._marca = marca

    def getVelocidad(self):
        return self._velocidad

    def setVelocidad(self, velocidad):
        self._velocidad = velocidad

    def getModelo(self):
        return(self._modelo)

    def setModelo(self, modelo):
        self._modelo = modelo    

    def getModelo(self):
        return(self._potencia)

    def setModelo(self, potencia):
        self._plazas = potencia

    def getModelo(self):
        return(self._plazas)

    def setModelo(self, plazas):
        self._plazas = plazas    

class Camiones(Coches):
    def __init__(self, color, marca, velocidad, modelo, potencia, plazas, eje, capacidadCarga):
        super().__init__(color, marca, velocidad, modelo, potencia, plazas)
        self.__eje = eje
        self.__capacidadCarga = capacidadCarga

    def cargar(self, tipo_carga):
        print(f"El tipo de carga es: {tipo_carga}")

    def acelerar(self):
        self._velocidad += 1
        print("Estoy acelerando como una camión")

    def frenar(self):
        self._velocidad -= 1
        print("Estoy frenando como una camión")

    def setEje(self, eje):
        self.__eje = eje

    def getEje(self):
        return self.__eje
    
    def setCapacidadCarga(self, capacidadCarga):
        self.__capacidadCarga = capacidadCarga

    def getEje(self):
        return self.__capacidadCarga
    
class Camionetas(Coches):
    def __init__(self, color, marca, velocidad, modelo, potencia, plazas, traccion, cerrada):
        super().__init__(color, marca, velocidad, modelo, potencia, plazas)
        self.__traccion = traccion
        self.__cerrada = cerrada

    def transoportar(self, num_pasajeros):
        print(f"El numero de pasajeros de la camioneta es: {num_pasajeros}")

    def setTraccion(self):
        return self.__traccion

    def getTraccion(self, traccion):
        self.__traccion = traccion
        
    def setCerrada(self):
        return self.__cerrada

    def getCerrada(self, cerrada):
        self.__cerrada = cerrada
        