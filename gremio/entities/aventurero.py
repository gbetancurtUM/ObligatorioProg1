from abc import ABC, abstractmethod
from entities.mision import Mision

class Aventurero(ABC):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float):
        self.nombre = nombre
        self.id = id
        self.puntos_habilidad = puntos_habilidad
        self.experiencia = experiencia
        self.dinero = dinero
        self.misiones = [] 

    @abstractmethod
    def calcular_rango(self)-> int:
        pass

    def _calcular_rango_base(self, habilidad_total: int) -> int:
        if habilidad_total <= 20:
            return 1
        elif habilidad_total <= 40:
            return 2
        elif habilidad_total <= 60:
            return 3
        elif habilidad_total <= 80:
            return 4
        else:
            return 5

    def calcular_rango(self) -> int:
        habilidad_total = self.calcular_habilidad_total()
        return self._calcular_rango_base(habilidad_total)

    def incrementar_experiencia(self, puntos: int):
        self.experiencia += puntos

    def agregar_mision(self, mision: Mision):
        self.misiones.append(mision)