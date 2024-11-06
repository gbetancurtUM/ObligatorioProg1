from gremio.entities.gremio import Gremio
from gremio.entities.guerrero import Guerrero
from gremio.entities.mago import Mago
from gremio.entities.ranger import Ranger
from gremio.entities.mision import Mision
from gremio.entities.mascota import Mascota

def main():
    gremio = Gremio()
    
    while True:
        print("\nBienvenido al Simulador de Gremio de Aventureros")
        opcion = input("Seleccione una opción: ")
        print("1. Registrar Aventurero")
        print("2. Registrar Misión")
        print("3. Realizar Misión")
        print("4. Otras Consultas")
        print("5. Salir")
        
        if opcion == "1":
            try:
                clase_opcion = input("Elija la clase del aventurero:\n1. Guerrero\n2. Mago\n3. Ranger: ")
                if clase_opcion not in ["1", "2", "3"]:
                    print("Clase de aventurero inválida. Volviendo al menú principal.")
                    continue
    
                nombre = input("Nombre del aventurero: ")
                if not isinstance(nombre, str) or not nombre.strip():
                    print("El nombre del aventurero debe ser un texto no vacío.")
                    continue

                id = int(input("ID: "))
                if not gremio.id_unico(id):
                    print(f"El ID {id} ya está en uso. Debe ser único.")
                    continue

                puntos_habilidad = int(input("Puntos de habilidad (entre 0 y 100): "))
                if not 0 <= puntos_habilidad <= 100:
                    print("Puntos de habilidad fuera de rango.")
                    continue

                experiencia = int(input("Experiencia: "))
                dinero = float(input("Dinero: "))

                if clase_opcion == "1":
                    fuerza = int(input("Fuerza (entre 0 y 100): "))
                    if not 0 <= fuerza <= 100:
                        print("Fuerza fuera de rango.")
                        continue
                    aventurero = Guerrero(nombre, id, puntos_habilidad, experiencia, dinero, fuerza)

                elif clase_opcion == "2":
                    mana = int(input("Mana (entre 0 y 100): "))
                    if not 0 <= mana <= 100:
                        print("Mana fuera de rango.")
                        continue
                    aventurero = Mago(nombre, id, puntos_habilidad, experiencia, dinero, mana)

                elif clase_opcion == "3":
                    tiene_mascota = input("¿Tiene mascota? (S/N): ").strip().upper()
                    if tiene_mascota not in ["S", "N"]:
                        print("Entrada inválida. Volviendo al menú principal.")
                        continue
                    
                    mascota = None
                    if tiene_mascota == "S":
                        mascota_nombre = input("Nombre de la mascota: ")
                        if not isinstance(mascota_nombre, str) or not mascota_nombre.strip():
                            print("El nombre de la mascota debe ser un texto no vacío.")
                            continue
                        mascota_habilidad = int(input("Puntos de habilidad de la mascota (entre 1 y 50): "))
                        if not 1 <= mascota_habilidad <= 50:
                            print("Puntos de habilidad de la mascota fuera de rango.")
                            continue
                        mascota = Mascota(mascota_nombre, mascota_habilidad)
                    aventurero = Ranger(nombre, id, puntos_habilidad, experiencia, dinero, mascota)

                gremio.registrar_aventurero(aventurero)
                print("Aventurero registrado con éxito.")
                
            except (ValueError, TypeError):
                print("Error: Entrada inválida. Volviendo al menú principal.")
                continue  

        elif opcion == "2":
            try:
                nombre_mision = input("Nombre de la misión: ")
                if not isinstance(nombre_mision, str) or not nombre_mision.strip():
                    print("El nombre de la misión debe ser un texto no vacío.")
                    continue

                rango = int(input("Rango de la misión (entre 1 y 5): "))
                if not 1 <= rango <= 5:
                    print("Rango fuera de rango.")
                    continue

                recompensa = float(input("Recompensa: "))

                tipo = input("¿Es una misión grupal? (S/N): ").strip().upper()
                if tipo not in ["S", "N"]:
                    print("Entrada inválida. Volviendo al menú principal.")
                    continue
                
                min_miembros = 1
                if tipo == "S":
                    min_miembros = int(input("Cantidad mínima de miembros: "))

                mision = Mision(nombre_mision, rango, recompensa, tipo="grupal" if tipo == "S" else "individual", min_miembros=min_miembros)
                gremio.registrar_mision(mision)
                print("Misión registrada con éxito.")

            except (ValueError, TypeError):
                print("Error: Entrada inválida. Volviendo al menú principal.")
                continue  
        
        elif opcion == "3":
            try:
                mision_nombre = input("Nombre de la misión a realizar: ")
                if not isinstance(mision_nombre, str) or not mision_nombre.strip():
                    print("El nombre de la misión debe ser un texto no vacío.")
                    continue

                mision = gremio.buscar_mision_por_nombre(mision_nombre)
                if not mision:
                    print("Misión no encontrada. Volviendo al menú principal.")
                    continue

                aventurero_ids = []
                while True:
                    entrada = input("Ingrese el ID del aventurero o escriba 'fin' para terminar: ").strip()
                    if entrada.lower() == "fin":
                        break

                    if not entrada.isdigit():
                        print("Entrada inválida. Debe ser un número entero o 'fin' para terminar.")
                        continue 

                    aventurero_id = int(entrada)
                    aventurero = gremio.buscar_aventurero_por_id(aventurero_id)
                    if not aventurero:
                        print(f"Aventurero con ID {aventurero_id} no encontrado.")
                        continue  

            
                    if aventurero.calcular_rango() < mision.rango:
                        print(f"El aventurero {aventurero.nombre} no cumple con el rango de la misión. Volviendo al menú principal.")
                        continue 
                    aventurero_ids.append(aventurero_id)
                    
                    agregar_otro = input("¿Registrar otro aventurero? (S/N): ").strip().upper()
                    if agregar_otro not in ["S", "N"]:
                        print("Entrada inválida. Volviendo al menú principal.")
                        continue
                    
                    if agregar_otro == "N":
                        break  

                if not aventurero_ids:
                    print("No se seleccionaron aventureros para la misión. Volviendo al menú principal.")
                    continue

                participantes = [a for a in gremio.aventureros if a.id in aventurero_ids]
                if mision.tipo == "grupal" and len(participantes) < mision.min_miembros:
                    print("No hay suficientes miembros para la misión grupal. Volviendo al menú principal.")
                    continue

                mision.completar()
                recompensa_por_aventurero = mision.recompensa / len(participantes)
                experiencia_por_rango = {1: 5, 2: 10, 3: 20, 4: 50, 5: 100}
                experiencia_ganada = experiencia_por_rango.get(mision.rango, 0)

                for aventurero in participantes:
                    aventurero.dinero += recompensa_por_aventurero
                    aventurero.experiencia += experiencia_ganada
                    aventurero.agregar_mision(mision)

                print("Misión completada con éxito.")
                
            except (ValueError, TypeError):
                print("Error: Entrada inválida. Volviendo al menú principal.")
                continue  

        elif opcion == "4":
            print("\nSubmenú de Consultas:")
            print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
            print("2. Ver Top 10 Aventureros por Experiencia")
            print("3. Ver Top 5 Misiones con Mayor Recompensa")
            print("4. Volver al Menú Principal")

            consulta_opcion = input("Seleccione una opción: ")
            
            if consulta_opcion == "1":
                print("Top 10 aventureros con más misiones resueltas:")
                for i, aventurero in enumerate(gremio.top_aventureros_misiones(), start=1):
                    print(f"{i}. {aventurero.nombre} - Misiones completadas: {len(aventurero.misiones)}")
            
            elif consulta_opcion == "2":
                print("Top 10 aventureros por experiencia:")
                for i, aventurero in enumerate(gremio.top_aventureros_experiencia(), start=1):
                    print(f"{i}. {aventurero.nombre} - Experiencia: {aventurero.experiencia}")
            
            elif consulta_opcion == "3":
                print("Top 5 misiones con mayor recompensa:")
                for i, mision in enumerate(gremio.top_misiones_recompensa(), start=1):
                    print(f"{i}. {mision.nombre} - Recompensa: {mision.recompensa}")
            
            elif consulta_opcion == "4":
                print("Volviendo al menú principal.")
                continue
            else:
                print("Opción de consulta inválida. Volviendo al menú principal.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Volviendo al menú principal.")

if __name__ == "__main__":
    main()