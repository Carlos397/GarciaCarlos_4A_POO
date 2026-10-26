from conexionBD import *
from coches import coches

class Camiones(coches.Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__eje = eje
        self.__capacidadCarga = capacidadCarga

    @property
    def eje(self):
        return self.__eje

    @eje.setter
    def eje(self, value):
        self.__eje = value

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga

    @capacidadCarga.setter
    def capacidadCarga(self, value):
        self.__capacidadCarga = value

    def cargar(self, tipo_carga):
        print(f"El tipo de carga del camion es: {tipo_carga}")

    def acelerar(self):
        self._velocidad += 1
        print("Estoy acelerando como una camión")

    def frenar(self):
        self._velocidad -= 1
        print("Estoy frenando como una camión")



    def insertar(self):
        try: 
            cursor.execute("insert into camiones VALUES (NULL , %s, %s, %s, %s, %s, %s, %s, %s)", (self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.asientos, self.eje, self.capacidadCarga))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from camiones")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from camiones where id = %s", (id,))
            conexion.commit()
            return True
        except:
            return False

    def actualizar(self, id):
        try:
            cursor.execute("update camiones set marca = %s, color = %s, modelo = %s, velocidad = %s, potencia = %s, asientos = %s, eje = %s, capacidadCarga = %s where id = %s", (self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.asientos, self.eje, self.capacidadCarga, id))
            conexion.commit()
            return True
        except:
            return False
