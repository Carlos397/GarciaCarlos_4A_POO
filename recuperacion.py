class Productos:
    _nombre = ""
    _precio = 0
    _cantidad = 0

    def mostrarProductos(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
        print(f"El nombre es: {self._nombre}")
        print(f"El precio es: {self._precio}$")
        print(f"La cantidad es: {self._cantidad}")

    def calcularTotal(self, precio, cantidad):
        self._precio = precio
        self._cantidad = cantidad
        total = self._cantidad * self._precio
        return total

producto1 = Productos()
producto2 = Productos()

producto1.mostrarProductos("papas", 10, 2)
print(f"EL total es: {producto1.calcularTotal(1,20)}")

print("---------------------------------\n")

producto2.mostrarProductos("picafresa", 1, 20)
print(f"EL total es: {producto1.calcularTotal(1,20)}")
