#Programa principal desde la que se manda llamar los objetos de la clase de coches
import coches
from coches import Coches, Camiones, Camionetas 

coche1 = Coches("Blanco", "VW", 220, "2022", 150, 5) 
coche2 = Coches("Azul", "Nissan", 180, "2020", 150, 6)

camion1 = Camiones("Negro", "Dina", 180, "2020", 300, 12, 8, 2500)
camion2 = Camiones("Azul", "Star", 180, "2019", 300, 12, 8, 2500)

camioneta1 = Camionetas("Amarrillo", "Renault", 240, "2025", 250, 8, "delantera", True)
camioneta2 = Camionetas("Blanca", "Nissan", 180, "2020", 150, 6, "trasera", False)


for i in range(100):
    coche1.acelerar()   

print(coche1.getVelocidad())

coche1.setVelocidad(400)
print(coche1.getVelocidad())