from conexionBD import *

class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._color = color
        self._marca = marca
        self._velocidad = velocidad
        self._modelo = modelo
        self._potencia = potencia
        self._asientos = asientos

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, value):
        self._velocidad = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, value):
        self._potencia = value

    @property
    def asientos(self):
        return self._asientos

    @asientos.setter
    def asientos(self, value):
        self._asientos = value


    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1

    def insertar(self):
        try: 
            cursor.execute("insert into coches VALUES (NULL , %s, %s, %s, %s, %s, %s)", (self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.asientos))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from coches where id = %s", (id,))
            conexion.commit()
            return True
        except:
            return False

    def actualizar(self, id):
        try:
            cursor.execute("update coches set marca = %s, color = %s, modelo = %s, velocidad = %s, potencia = %s, asientos = %s where id = %s", (self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.asientos, id))
            conexion.commit()
            return True
        except:
            return False
