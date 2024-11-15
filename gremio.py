from entities import Guerrero
from entities import Mago
from entities import Ranger
from entities import Mision
from exceptions import MisionInvalida, RangoInsuficiente, AventureroInvalido, EntradaInvalida

class Gremio:
    def __init__(self):
        self.aventureros = []
        self.misiones = []

    def buscar_mision_por_nombre(self, nombre_mision):
        for mision in self.misiones:
            if mision.nombre == nombre_mision:
                return mision
        return None

    def buscar_aventurero_por_id(self, id_aventurero):
        for aventurero in self.aventureros:
            if aventurero.id == id_aventurero:
                return aventurero
        return None
    
    def validar_id_unico(self, id_aventurero):
        if self.buscar_aventurero_por_id(id_aventurero):
            raise AventureroInvalido(f"El ID {id_aventurero} ya está en uso.")
        

    def registrar_guerrero(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero, fuerza):
        self.validar_id_unico(id_aventurero)
        aventurero = Guerrero(nombre, id_aventurero, puntos_habilidad, experiencia, dinero, fuerza)
        self.aventureros.append(aventurero)
        print(f"Se ha registrado exitosamente el guerrero '{aventurero.nombre}'.")

    def registrar_mago(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mana):
        self.validar_id_unico(id_aventurero)
        aventurero = Mago(nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mana)
        self.aventureros.append(aventurero)
        print(f"Se ha registrado exitosamente el mago '{aventurero.nombre}'.")

    def registrar_ranger(self, nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mascota=None):
        self.validar_id_unico(id_aventurero)
        aventurero = Ranger(nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mascota)
        self.aventureros.append(aventurero)
        print(f"Se ha registrado exitosamente el ranger '{aventurero.nombre}'.")

    def registrar_mision(self, nombre, rango, recompensa, tipo, min_miembros):
        #if  not nombre: #any(char.isdigit() for char in nombre)
        #    raise MisionInvalida("El nombre de la misión no puede estar vacío.")

        #if not isinstance(rango,int) or not (1 <= rango <= 5):
        #    raise MisionInvalida("El rango de la misión debe ser un número entre 1 y 5.")

        #if recompensa < 0:
        #    raise MisionInvalida("La recompensa debe ser un número no negativo.")

        mision = Mision(nombre, rango, recompensa, tipo, min_miembros)
        self.misiones.append(mision)
        print(f"Se ha registrado exitosamente la misión '{mision.nombre}'.")

    def ver_top_10_aventureros_misiones(self):
        top_aventureros = self.ordenar_aventureros_por_misiones()
        print("\nTop 10 Aventureros con Más Misiones Resueltas:")
        for idx, aventurero in enumerate(top_aventureros[:10], 1):
            print(f"{idx}. {aventurero.nombre} - Misiones completadas: {aventurero.misiones_completadas}")

    def ver_top_10_aventureros_habilidad(self):
        top_aventureros = self.ordenar_aventureros_por_habilidad()
        print("\nTop 10 Aventureros por Mayor Habilidad:")
        for idx, aventurero in enumerate(top_aventureros[:10], 1):
            print(f"{idx}. {aventurero.nombre} - Habilidad Total: {aventurero.calcular_habilidad_total()}")

    def ver_top_5_misiones_recompensa(self):
        top_misiones = self.ordenar_misiones_por_recompensa()
        print("\nTop 5 Misiones con Mayor Recompensa:")
        for idx, mision in enumerate(top_misiones[:5], 1):
            print(f"{idx}. {mision.nombre} - Recompensa: {mision.recompensa}")

    def ordenar_aventureros_por_misiones(self):
        return sorted(self.aventureros, key=lambda a: (-a.misiones_completadas, a.nombre.upper()))

    def ordenar_aventureros_por_habilidad(self):
        return sorted(self.aventureros, key=lambda a: (-a.calcular_habilidad_total(), a.nombre.upper()))

    def ordenar_misiones_por_recompensa(self):
        return sorted(self.misiones, key=lambda m: (-m.recompensa, m.nombre.upper()))