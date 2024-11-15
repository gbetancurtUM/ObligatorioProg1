from entities.aventurero import Aventurero
from entities.mascota import Mascota
from exceptions import AventureroInvalido

class Ranger(Aventurero):
    def __init__(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mascota=None):
        super().__init__(nombre, id_aventurero, puntos_habilidad, experiencia, dinero)
        self.__mascota = self.validar_mascota(mascota) #if mascota else None
        self.__tipo_aventurero = "Ranger"

    #getters
    @property
    def mascota(self):
        return self.__mascota 
    
    @property
    def tipo_aventurero(self):
        return self.__tipo_aventurero

    #metodos
    @staticmethod
    def validar_mascota(mascota):
        if mascota is not None and not isinstance(mascota, Mascota):
            raise AventureroInvalido("La mascota debe ser una instancia válida de la clase Mascota.")
        return mascota

    def calcular_habilidad_total(self):
        habilidad_total = self.puntos_habilidad
        if self.mascota and self.mascota.puntos_habilidad + habilidad_total <= 80:   #duda sobre sumar solo en rangos 1 a 4
            habilidad_total += self.mascota.puntos_habilidad
        return habilidad_total
