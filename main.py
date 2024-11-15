from gremio import Gremio
from entities import Mascota
from exceptions import EntradaInvalida, MisionInvalida, RangoInsuficiente, AventureroInvalido
from utils import calcular_rango

def input_entero(mensaje, minimo=None, maximo=None):
    valor_str = input(mensaje)
    if not valor_str.isdigit():
        raise EntradaInvalida("Error: La entrada debe ser un número entero válido.")
    valor = int(valor_str)
    if minimo is not None and valor < minimo:
        raise EntradaInvalida(f"El valor debe ser mayor o igual a {minimo}.")
    if maximo is not None and valor > maximo:
        raise EntradaInvalida(f"El valor debe ser menor o igual a {maximo}.")
    return valor

def input_decimal(mensaje, minimo=None):
    valor_str = input(mensaje)
    try:
        valor = float(valor_str)
        if minimo is not None and valor < minimo:
            raise EntradaInvalida(f"El valor debe ser mayor o igual a {minimo}.")
        return valor
    except ValueError:
        raise EntradaInvalida("Error: La entrada debe ser un número decimal válido.")

def input_nombre(mensaje):
    nombre = input(mensaje)
    if not nombre: # or any(char.isdigit() for char in nombre):
        raise EntradaInvalida("El nombre no puede contener números y no puede estar vacío.")
    return nombre

def menu_principal():
    gremio = Gremio()
    while True:
        print("Bienvenido al Simulador de Gremio de Aventureros!")
        print("Seleccione una opción:")
        print("1. Registrar Aventurero")
        print("2. Registrar Misión")
        print("3. Realizar Misión")
        print("4. Otras Consultas")
        print("5. Salir")
        
        try:
            opcion = input_entero("Seleccione una opción (1-5): ", 1, 5)
            if opcion == 1:
                registrar_aventurero(gremio)
            elif opcion == 2:
                registrar_mision(gremio)
            elif opcion == 3:
                realizar_mision(gremio)
            elif opcion == 4:
                otras_consultas(gremio)
            elif opcion == 5:
                print("Saliendo del programa. ¡Hasta luego!")
                break
        except (EntradaInvalida, MisionInvalida, RangoInsuficiente, AventureroInvalido) as e:
            print(f"Error: {e}\nVolviendo al menú principal.")

def registrar_aventurero(gremio):
    try:
        print("--- Registro de Aventurero ---")
        print("Elija la clase del aventurero:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Ranger")
        clase_opcion = input_entero("Ingrese una opción (1-3): ", 1, 3)

        nombre = input_nombre("Ingrese el nombre del aventurero: ")

        id_aventurero = input_entero("Ingrese el ID del aventurero (entero no negativo): ", 0)
        gremio.validar_id_unico(id_aventurero)
    
        puntos_habilidad = input_entero("Ingrese los puntos de habilidad (1-100): ", 1, 100)
        experiencia = input_entero("Ingrese la experiencia inicial (entero no negativo): ", 0)
        dinero = input_decimal("Ingrese la cantidad de dinero inicial (decimal, no negativo): ", 0)

        if clase_opcion == 1:
            fuerza = input_entero("Ingrese la fuerza del guerrero (1-100): ", 1, 100)
            gremio.registrar_guerrero(nombre, id_aventurero, puntos_habilidad, experiencia, dinero, fuerza)
        elif clase_opcion == 2:
            mana = input_entero("Ingrese el mana del mago (1-1000): ", 1, 1000)
            gremio.registrar_mago(nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mana)
        elif clase_opcion == 3:
            mascota = None
            mascota_respuesta = input("¿Tiene una mascota? (S/N): ")
            if mascota_respuesta not in ['S', 'N']:
                raise EntradaInvalida("Debe ingresar 'S' o 'N'")
            if mascota_respuesta == 'S':
                mascota_nombre = input_nombre("Ingrese el nombre de la mascota: ")
                puntos_habilidad_mascota = input_entero("Ingrese los puntos de habilidad de la mascota (1-50): ", 1, 50)
                mascota = Mascota(mascota_nombre, puntos_habilidad_mascota)
            gremio.registrar_ranger(nombre, id_aventurero, puntos_habilidad, experiencia, dinero, mascota)
    except (EntradaInvalida, AventureroInvalido) as e:
        print(f"Error: {e}\nVolviendo al menú principal.")

def registrar_mision(gremio):
    try:
        print("--- Registro de Misión ---")
        nombre = input_nombre("Ingrese el nombre de la misión: ")

        rango = input_entero("Ingrese el rango de la misión (1-5): ", 1, 5)
        recompensa = input_decimal("Ingrese la recompensa en dinero (no negativo): ", 0)

        tipo_respuesta = input("¿Es una misión grupal? (S/N): ")
        if tipo_respuesta not in ['S', 'N']:
            raise EntradaInvalida("Debe ingresar 'S' o 'N' para definir el tipo de misión.")
        tipo = 'grupal' if tipo_respuesta == 'S' else 'individual'

        if tipo == 'grupal':
            min_miembros = input_entero("Ingrese la cantidad mínima de miembros para la misión grupal (mínimo 2): ", 2)
        else:
            min_miembros = 1

        gremio.registrar_mision(nombre, rango, recompensa, tipo, min_miembros)

    except (MisionInvalida, EntradaInvalida) as e:
        print(f"Error: {e}\nVolviendo al menú principal.")

def realizar_mision(gremio):
    try:
        print("--- Realizar Misión ---")
        nombre_mision = input_nombre("Ingrese el nombre de la misión a realizar: ")
        mision = gremio.buscar_mision_por_nombre(nombre_mision)
        if not mision:
            raise MisionInvalida(f"La misión '{nombre_mision}' no existe.")

        if mision.completada:
            raise MisionInvalida(f"La misión '{nombre_mision}' ya ha sido completada.")

        print(f"La misión '{nombre_mision}' requiere un mínimo de {mision.min_miembros} aventureros.")
        aventureros = []
        agregar_mas_aventureros = "S"
        while agregar_mas_aventureros == "S":
            id_aventurero = input_entero("Ingrese el ID del aventurero: ", 0)
            aventurero = gremio.buscar_aventurero_por_id(id_aventurero)
            if not aventurero:
                raise EntradaInvalida(f"Error: Aventurero con ID {id_aventurero} no encontrado")
            habilidad_total = aventurero.calcular_habilidad_total()
            rango_aventurero = calcular_rango(habilidad_total)
            if rango_aventurero < mision.rango:
                raise RangoInsuficiente("El aventurero no cumple con el rango requerido para esta misión.")
            aventureros.append(aventurero)
            agregar_mas_aventureros = input("¿Registrar otro aventurero? (S/N): ")
            if agregar_mas_aventureros not in ['S', 'N']:
                raise EntradaInvalida("Debe ingresar 'S' o 'N'")
        #if len(aventureros) < mision.min_miembros:
        #    print(f"La misión '{nombre_mision}' requiere al menos {mision.min_miembros} aventureros.")
        #    return

        mision.completar(aventureros)
        print(f"¡La misión '{mision.nombre}' ha sido completada por los aventureros exitosamente!")

    except (MisionInvalida, RangoInsuficiente, EntradaInvalida) as e:
        print(f"Error: {e}\nVolviendo al menú principal.")

def otras_consultas(gremio):
    try:
        while True:
            print("\n--- Otras Consultas ---")
            print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
            print("2. Ver Top 10 Aventureros por Mayor Habilidad")
            print("3. Ver Top 5 Misiones con Mayor Recompensa")
            print("4. Volver al Menú Principal")

            opcion = input_entero("Seleccione una opción (1-4): ", 1, 4)
            if opcion == 1:
                gremio.ver_top_10_aventureros_misiones()
            elif opcion == 2:
                gremio.ver_top_10_aventureros_habilidad()
            elif opcion == 3:
                gremio.ver_top_5_misiones_recompensa()
            elif opcion == 4:
                break
    except EntradaInvalida as e:
        print(f"Error: {e}\nVolviendo al menú principal.")

if __name__ == "__main__":
    menu_principal()