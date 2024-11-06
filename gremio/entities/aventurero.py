#clase abstracta, metodo calcular rango abstracto. 
from abc import ABC, abstractmethod
class Aventurero(ABC):
    def __init__(self, habilidad):
        self.habilidad = habilidad

    @abstractmethod
    def calcular_rango(self):
        """Calcula el rango del aventurero."""
        pass

class Guerrero(Aventurero):
    def calcular_rango(self):
        return self.habilidad // 20 + 1

# INPUT y validar que ingrese un numero
try:
    habilidad = int(input("Ingrese la habilidad del guerrero: "))
    guerrero = Guerrero(habilidad=habilidad)
    print(f"Rango del guerrero: {guerrero.calcular_rango()}")
except ValueError:
    print("Ingrese un número válido para la habilidad.")
