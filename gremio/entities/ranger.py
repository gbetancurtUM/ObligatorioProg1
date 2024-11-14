from entities.aventurero import Aventurero
from entities.mascota import Mascota
from exceptions import AventureroInvalido

class Ranger(Aventurero):
    def _init_(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mascota=None):
        super()._init_(nombre, id_aventurero, puntos_habilidad, experiencia, dinero)
        self.mascota = self.validar_mascota(mascota) #if mascota else None
        self.tipo_aventurero = "Ranger"

    @staticmethod
    def validar_mascota(mascota):
        if mascota is not None and not isinstance(mascota, Mascota):
            raise AventureroInvalido("La mascota debe ser una instancia válida de la clase Mascota.")
        return mascota

    def calcular_habilidad_total(self):
        habilidad_total = self.puntos_habilidad
        if self.mascota and habilidad_total <= 80:   #duda sobre sumar solo en rangos 1 a 4
            habilidad_total += self.mascota.puntos_habilidad
        return habilidad_total
