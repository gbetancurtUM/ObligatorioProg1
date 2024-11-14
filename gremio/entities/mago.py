from entities.aventurero import Aventurero
from exceptions import AventureroInvalido

class Mago(Aventurero):
    def _init_(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mana):
        super()._init_(nombre, id_aventurero, puntos_habilidad, experiencia, dinero)
        self.mana = self.validar_mana(mana)
        self.tipo_aventurero = "Mago"

    @staticmethod
    def validar_mana(mana):
        if not isinstance(mana,int) or not (1 <= mana <= 1000):
            raise AventureroInvalido("El mana debe estar entre 1 y 1000.")
        return mana

    def calcular_habilidad_total(self):
        return self.puntos_habilidad + (self.mana / 10)
