from exceptions import AventureroInvalido

class Mascota:
    def __init__(self, nombre, puntos_habilidad):
        self.__nombre = self.validar_nombre(nombre)
        self.__puntos_habilidad = self.validar_puntos_habilidad(puntos_habilidad)

    #getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad

    #metodos
    @staticmethod
    def validar_nombre(nombre):
        if not nombre: #or any(char.isdigit() for char in nombre):
            raise AventureroInvalido("El nombre de la mascota no puede contener números y no puede estar vacío.")
        return nombre

    @staticmethod
    def validar_puntos_habilidad(puntos_habilidad):
        if not isinstance(puntos_habilidad,int) or not (1 <= puntos_habilidad <= 50):
            raise AventureroInvalido("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
        return puntos_habilidad

