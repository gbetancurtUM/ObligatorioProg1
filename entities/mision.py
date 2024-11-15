from exceptions import MisionInvalida, RangoInsuficiente
from utils import calcular_rango

class Mision:
    def __init__(self, nombre, rango, recompensa, tipo, min_miembros):
        self.__nombre = self.validar_nombre(nombre)
        self.__rango = self.validar_rango(rango)
        self.__recompensa = self.validar_recompensa(recompensa)
        self.__tipo = self.validar_tipo(tipo)
        self.__min_miembros = self.validar_min_miembros(min_miembros)
        self.__completada = False

    
    #getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def rango(self):
        return self.__rango

    @property
    def recompensa(self):
        return self.__recompensa

    @property
    def tipo(self):
        return self.__tipo

    @property
    def min_miembros(self):
        return self.__min_miembros

    @property
    def completada(self):
        return self.__completada
    
    #setters
    @completada.setter
    def completada(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El valor de 'completada' debe ser un valor booleano.")
        self.__completada = valor

    #metodos
    @staticmethod
    def validar_nombre(nombre):
        if not nombre: # or any(char.isdigit() for char in nombre):
            raise MisionInvalida("El nombre de la misión no puede contener números y no puede estar vacío.")
        return nombre

    @staticmethod
    def validar_rango(rango):
        if not isinstance(rango, int) or not (1 <= rango <= 5):
            raise MisionInvalida("El rango de la misión debe ser un entero entre 1 y 5.")
        return rango

    @staticmethod
    def validar_recompensa(recompensa):
        if not isinstance(recompensa,float) or recompensa < 0:
            raise MisionInvalida("La recompensa debe ser un número no negativo.")
        return recompensa

    @staticmethod
    def validar_tipo(tipo):
        if tipo not in ["grupal", "individual"]:
            raise MisionInvalida("El tipo de misión debe ser 'grupal' o 'individual'.")
        return tipo

    @staticmethod
    def validar_min_miembros(miembros):
        if not isinstance(miembros,int) or miembros < 0:
            raise MisionInvalida("La cantidad minima de miembros debe ser mayor o igual a 1.")
        return miembros
    
    def obtener_experiencia_por_rango(self):
        experiencia_por_rango = {1: 5, 2: 10, 3: 20, 4: 50, 5: 100}
        return experiencia_por_rango.get(self.rango, 0)

    def completar(self, aventureros):
        if self.completada:
            raise MisionInvalida(f"La misión '{self.nombre}' ya ha sido completada.")

        for aventurero in aventureros:
            habilidad_total = aventurero.calcular_habilidad_total()
            rango_aventurero = calcular_rango(habilidad_total)
            if rango_aventurero < self.rango:
                raise RangoInsuficiente(f"El aventurero '{aventurero.nombre}' no cumple con el rango requerido para esta misión.")

        if self.tipo == "grupal" and len(aventureros) < self.min_miembros:
            raise MisionInvalida(f"La misión grupal '{self.nombre}' requiere al menos {self.min_miembros} miembros.")

        recompensa_individual = self.recompensa / len(aventureros)
        experiencia_por_rango = self.obtener_experiencia_por_rango()

        for aventurero in aventureros:
            aventurero.incrementar_experiencia(experiencia_por_rango)
            aventurero.agregar_dinero(recompensa_individual)
            aventurero.misiones_completadas += 1

        self.completada = True
