from abc import ABC, abstractmethod
from exceptions import AventureroInvalido, EntradaInvalida

class Aventurero(ABC):
    def __init__(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero):
        self.__nombre = self.validar_nombre(nombre)
        self.__id = self.validar_id(id_aventurero)
        self.__puntos_habilidad = self.validar_puntos_habilidad(puntos_habilidad)
        self.__experiencia = self.validar_experiencia(experiencia)
        self.__dinero = self.validar_dinero(dinero)
        self.__misiones_completadas = 0
        #self.tipo_aventurero = self.__class__.__name__


    #getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def id(self):
        return self.__id

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad

    @property
    def experiencia(self):
        return self.__experiencia

    @property
    def dinero(self):
        return self.__dinero

    @property
    def misiones_completadas(self):
        return self.__misiones_completadas
    
    #setters
    @experiencia.setter
    def experiencia(self, valor):
        if valor < 0:
            raise EntradaInvalida("La experiencia no puede ser negativa.")
        self.__experiencia = valor 

    @dinero.setter
    def dinero(self, valor):
        if valor < 0:
            raise EntradaInvalida("El dinero no puede ser negativo.")
        self.__dinero = valor 

    @misiones_completadas.setter
    def misiones_completadas(self, valor):
        if valor < 0:
            raise EntradaInvalida("Las misiones completadas no pueden ser un valor negativo.")
        self.__misiones_completadas = valor 

    #metodos
    @staticmethod
    def validar_nombre(nombre):
        if not nombre: #or any(char.isdigit() for char in nombre)
            raise AventureroInvalido("El nombre no puede contener números y no puede estar vacío.")
        return nombre

    @staticmethod
    def validar_id(id_aventurero):
        if not isinstance(id_aventurero, int) or id_aventurero <= 0:
            raise AventureroInvalido("El ID debe ser un número entero positivo.")
        return id_aventurero

    @staticmethod
    def validar_puntos_habilidad(puntos_habilidad):
        if not isinstance(puntos_habilidad,int) or not (1 <= puntos_habilidad <= 100):
            raise AventureroInvalido("Puntos de habilidad fuera de rango (1-100).")
        return puntos_habilidad
    
    @staticmethod
    def validar_experiencia(experiencia):
        if not isinstance(experiencia,int) or experiencia < 0:
            raise AventureroInvalido("Experiencia debe ser un numero entero positivo.")
        return experiencia
    
    @staticmethod
    def validar_dinero(dinero):
        if not isinstance(dinero,float) or dinero < 0:
            raise AventureroInvalido("Dinero debe ser un numero decimal positivo.")
        return dinero

    @abstractmethod
    def calcular_habilidad_total(self):
        pass

    def incrementar_experiencia(self, cantidad):
        if cantidad < 0:
            raise EntradaInvalida("La cantidad de experiencia no puede ser negativa.")
        self.experiencia += cantidad

    def agregar_dinero(self, cantidad):
        if cantidad < 0:
            raise EntradaInvalida("La cantidad de dinero a agregar no puede ser negativa.")
        self.dinero += cantidad
