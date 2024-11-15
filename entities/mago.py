from entities.aventurero import Aventurero
from exceptions import AventureroInvalido

class Mago(Aventurero):
    def __init__(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mana):
        super().__init__(nombre, id_aventurero, puntos_habilidad, experiencia, dinero)
        self.__mana = self.validar_mana(mana)
        self.__tipo_aventurero = "Mago"

    #getters
    @property
    def mana(self):
        return self.__mana  

    @property
    def tipo_aventurero(self):
        return self.__tipo_aventurero

    #metodos
    @staticmethod
    def validar_mana(mana):
        if not isinstance(mana,int) or not (1 <= mana <= 1000):
            raise AventureroInvalido("El mana debe estar entre 1 y 1000.")
        return mana

    def calcular_habilidad_total(self):
        return self.puntos_habilidad + (self.mana / 10)
