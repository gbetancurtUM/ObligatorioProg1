from entities.aventurero import Aventurero
from exceptions import AventureroInvalido

class Guerrero(Aventurero):
    def __init__(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero, fuerza):
        super().__init__(nombre, id_aventurero, puntos_habilidad, experiencia, dinero)
        self.__fuerza = self.validar_fuerza(fuerza)
        self.__tipo_aventurero = "Guerrero"

    #getters
    @property
    def fuerza(self):
        return self.__fuerza
    
    @property
    def tipo_aventurero(self):
        return self.__tipo_aventurero
    
    #metodos
    @staticmethod
    def validar_fuerza(fuerza):
        if not isinstance(fuerza,int) or not (1 <= fuerza <= 100):
            raise AventureroInvalido("La fuerza debe estar entre 1 y 100.")
        return fuerza

    def calcular_habilidad_total(self):
        return self.puntos_habilidad + (self.fuerza / 2)
