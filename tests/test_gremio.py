import unittest
from gremio import Gremio
from entities.guerrero import Guerrero
from entities.mago import Mago
from entities.ranger import Ranger
from entities.mascota import Mascota
from entities.mision import Mision
from exceptions import AventureroInvalido, MisionInvalida, RangoInsuficiente
from utils import calcular_rango

class TestGremio(unittest.TestCase):

    def setUp(self):
        self.gremio = Gremio()

    def test_registrar_guerrero(self):
        self.gremio.registrar_guerrero("Arthur", 1, 50, 0, 100.0, 80)
        print(f"Guerrero registrado: {self.gremio.aventureros[0].nombre}, ID: {self.gremio.aventureros[0].id}")
        self.assertEqual(len(self.gremio.aventureros), 1)
        self.assertIsInstance(self.gremio.aventureros[0], Guerrero)
        self.assertEqual(self.gremio.aventureros[0].nombre, "Arthur")

    def test_registrar_mago(self):
        self.gremio.registrar_mago("Merlin", 2, 70, 0, 150.0, 900)
        print(f"Mago registrado: {self.gremio.aventureros[0].nombre}, ID: {self.gremio.aventureros[0].id}")
        self.assertEqual(len(self.gremio.aventureros), 1)
        self.assertIsInstance(self.gremio.aventureros[0], Mago)
        self.assertEqual(self.gremio.aventureros[0].nombre, "Merlin")

    def test_registrar_ranger_con_mascota(self):
        mascota = Mascota("Shadow", 40)
        self.gremio.registrar_ranger("Robin", 3, 10, 0, 120.0, mascota)
        print(f"Ranger registrado: {self.gremio.aventureros[0].nombre}, Mascota: {self.gremio.aventureros[0].mascota.nombre}")
        self.assertEqual(len(self.gremio.aventureros), 1)
        self.assertIsInstance(self.gremio.aventureros[0], Ranger)
        self.assertEqual(self.gremio.aventureros[0].nombre, "Robin")
        self.assertEqual(self.gremio.aventureros[0].calcular_habilidad_total(), 50)
        self.assertIsNotNone(self.gremio.aventureros[0].mascota)
        self.assertEqual(self.gremio.aventureros[0].mascota.nombre, "Shadow")

    def test_registrar_ranger_sin_mascota(self):
        self.gremio.registrar_ranger("Luca", 3, 60, 0, 120.0, None)
        print(f"Ranger registrado: {self.gremio.aventureros[0].nombre}, Mascota: {self.gremio.aventureros[0].mascota}")
        self.assertEqual(len(self.gremio.aventureros), 1)
        self.assertIsInstance(self.gremio.aventureros[0], Ranger)
        self.assertEqual(self.gremio.aventureros[0].nombre, "Luca")
        self.assertEqual(self.gremio.aventureros[0].calcular_habilidad_total(), 60)
        self.assertIsNone(self.gremio.aventureros[0].mascota)

    def test_registrar_mision_individual(self):
        self.gremio.registrar_mision("Recuperar el amuleto", 2, 500.0, "individual", 1)
        print(f"Misión registrada: {self.gremio.misiones[0].nombre}, Tipo: {self.gremio.misiones[0].tipo}")
        self.assertEqual(len(self.gremio.misiones), 1)
        self.assertEqual(self.gremio.misiones[0].nombre, "Recuperar el amuleto")
        self.assertEqual(self.gremio.misiones[0].tipo, "individual")

    def test_registrar_mision_grupal(self):
        self.gremio.registrar_mision("Derrotar al dragón", 5, 10000.0, "grupal", 3)
        print(f"Misión registrada: {self.gremio.misiones[0].nombre}, Tipo: {self.gremio.misiones[0].tipo}, Mínimo de miembros: {self.gremio.misiones[0].min_miembros}")
        self.assertEqual(len(self.gremio.misiones), 1)
        self.assertEqual(self.gremio.misiones[0].nombre, "Derrotar al dragón")
        self.assertEqual(self.gremio.misiones[0].tipo, "grupal")
        self.assertEqual(self.gremio.misiones[0].min_miembros, 3)

    def test_verificar_id_unico(self):
        self.gremio.registrar_guerrero("Arthur", 1, 50, 0, 100.0, 80)
        print(f"Guerrero registrado con ID: {self.gremio.aventureros[0].id}")
        with self.assertRaises(AventureroInvalido):
            self.gremio.registrar_mago("Merlin", 1, 70, 0, 150.0, 900)  # ID duplicado

    def test_buscar_aventurero_por_id(self):
        self.gremio.registrar_guerrero("Arthur", 1, 50, 0, 100.0, 80)
        aventurero = self.gremio.buscar_aventurero_por_id(1)
        print(f"Aventurero encontrado: {aventurero.nombre}, ID: {aventurero.id}")
        self.assertIsNotNone(aventurero)
        self.assertEqual(aventurero.nombre, "Arthur")

    def test_buscar_mision_por_nombre(self):
        self.gremio.registrar_mision("Recuperar el amuleto", 2, 500.0, "individual", 1)
        mision = self.gremio.buscar_mision_por_nombre("Recuperar el amuleto")
        print(f"Misión encontrada: {mision.nombre}, Tipo: {mision.tipo}")
        self.assertIsNotNone(mision)
        self.assertEqual(mision.nombre, "Recuperar el amuleto")

    def test_completar_mision_individual(self):
        self.gremio.registrar_guerrero("Arthur", 1, 50, 0, 100.0, 80)
        self.gremio.registrar_mision("Recuperar el amuleto", 2, 500.0, "individual", 1)
        aventurero = self.gremio.buscar_aventurero_por_id(1)
        mision = self.gremio.buscar_mision_por_nombre("Recuperar el amuleto")

        habilidad_total = aventurero.calcular_habilidad_total()
        rango_aventurero = calcular_rango(habilidad_total)
        print(f"Rango del aventurero: {rango_aventurero}")
        self.assertTrue(rango_aventurero >= mision.rango)

        mision.completar([aventurero])
        print(f"Dinero del aventurero: {aventurero.dinero}, Experiencia: {aventurero.experiencia}, Misiones completadas: {aventurero.misiones_completadas}")
        self.assertTrue(mision.completada)
        self.assertEqual(aventurero.dinero, 100.0 + 500.0)
        self.assertEqual(aventurero.experiencia, 0 + mision.obtener_experiencia_por_rango())
        self.assertEqual(aventurero.misiones_completadas, 1)

    def test_ver_top_10_aventureros_misiones(self):
        # Registrar aventureros con misiones completadas
        for i in range(15):
            nombre_aventurero = f"Guerrero_{chr(65 + i)}"  # Genera nombres como Guerrero_A, Guerrero_B, etc.
            self.gremio.registrar_guerrero(nombre_aventurero, i+1, 50, 0, 100.0, 80)
            self.gremio.aventureros[i].misiones_completadas = i

        top_aventureros = self.gremio.ordenar_aventureros_por_misiones()
        print("Top 10 Aventureros con más misiones completadas:")
        for aventurero in top_aventureros[:10]:
            print(f"{aventurero.nombre}: {aventurero.misiones_completadas} misiones")
        self.assertEqual(len(top_aventureros), 15)
        self.assertEqual(top_aventureros[0].misiones_completadas, 14)  # Mayor número de misiones

    def test_ver_top_5_misiones_recompensa(self):
        # Registrar misiones con diferentes recompensas
        for i in range(10):
            nombre_mision = f"Mision_{chr(65 + i)}"  # Genera nombres como Mision_A, Mision_B, etc.
            self.gremio.registrar_mision(nombre_mision, 2, 1000.0 * i, "individual", 1)

        top_misiones = self.gremio.ordenar_misiones_por_recompensa()
        print("Top 5 misiones con mayor recompensa:")
        for mision in top_misiones[:5]:
            print(f"{mision.nombre}: {mision.recompensa} de recompensa")
        self.assertEqual(len(top_misiones), 10)
        self.assertEqual(top_misiones[0].recompensa, 9000.0)  # Mayor recompensa

    def test_mision_con_aventurero_rango_insuficiente(self):
        self.gremio.registrar_guerrero("Lancelot", 1, 10, 0, 100.0, 20)  # Habilidad total baja
        self.gremio.registrar_mision("Mision Difícil", 5, 5000.0, "individual", 1)
        aventurero = self.gremio.buscar_aventurero_por_id(1)
        mision = self.gremio.buscar_mision_por_nombre("Mision Difícil")

        with self.assertRaises(RangoInsuficiente):
            mision.completar([aventurero])  # Debería fallar por rango insuficiente

    def test_registrar_mision_con_datos_invalidos(self):
        with self.assertRaises(MisionInvalida):
            self.gremio.registrar_mision("Mision123", 6, -500.0, "desconocido", 0)  # Datos inválidos

    def test_ordenar_aventureros_por_misiones(self):
        # Registrar aventureros con mismo número de misiones
        self.gremio.registrar_guerrero("Arthur", 1, 50, 0, 100.0, 80)
        self.gremio.registrar_mago("Merlin", 2, 70, 0, 150.0, 900)
        self.gremio.aventureros[0].misiones_completadas = 5
        self.gremio.aventureros[1].misiones_completadas = 5

        top_aventureros = self.gremio.ordenar_aventureros_por_misiones()
        print("Top Aventureros ordenados por misiones completadas:")
        for aventurero in top_aventureros:
            print(f"{aventurero.nombre}: {aventurero.misiones_completadas} misiones")
        self.assertEqual(top_aventureros[0].nombre, "Arthur")  # Debe estar antes por orden alfabético

    def test_ordenar_aventureros_por_habilidad(self):
        # Registrar aventureros con misma habilidad
        self.gremio.registrar_guerrero("Arthur", 1, 50, 0, 100.0, 80)
        self.gremio.registrar_mago("Albus", 2, 50, 0, 150.0, 800)
        top_aventureros = self.gremio.ordenar_aventureros_por_habilidad()
        print("Top Aventureros ordenados por habilidad:")
        for aventurero in top_aventureros:
            print(f"{aventurero.nombre}: {aventurero.calcular_habilidad_total()} habilidad")
        self.assertEqual(top_aventureros[0].nombre, "Albus")  # Debe estar antes por orden alfabético

if __name__ == '__main__':
    unittest.main()
