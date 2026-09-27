#Programa principal desde la que se manda llamar los objetos de la clase de coches
import coches
from coches import Coches

coche1 = coches.Coches("Blanco", "VW", 220, "2022", 150, 5) 
coche2 = Coches("Azul", "Nissan", 180, "2020", 150, 6)

coche1.acelerar()   
coche1.acelerar()   