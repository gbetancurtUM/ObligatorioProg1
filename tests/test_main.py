import unittest
from unittest.mock import patch
from io import StringIO
from gremio import Gremio
from main import registrar_aventurero, registrar_mision, realizar_mision, otras_consultas

class TestMain(unittest.TestCase):

    def setUp(self):
        self.gremio = Gremio()

    @patch('builtins.input', side_effect=[
        '1',             # Opción: Guerrero
        'Arthur',        # Nombre
        '1',             # ID
        '50',            # Puntos de habilidad
        '0',             # Experiencia
        '100.0',         # Dinero
        '80'             # Fuerza
    ])
    def test_registrar_aventurero_guerrero(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            registrar_aventurero(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Registro Guerrero:")
            print(output)  # Mostrar mensaje de registro
            self.assertIn("Se ha registrado exitosamente el guerrero 'Arthur'.", output)
            self.assertEqual(len(self.gremio.aventureros), 1)

    @patch('builtins.input', side_effect=[
        '2',             # Opción: Mago
        'Merlin',        # Nombre
        '2',             # ID
        '70',            # Puntos de habilidad
        '0',             # Experiencia
        '150.0',         # Dinero
        '900'            # Mana
    ])
    def test_registrar_aventurero_mago(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            registrar_aventurero(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Registro Mago:")
            print(output)  # Mostrar mensaje de registro
            self.assertIn("Se ha registrado exitosamente el mago 'Merlin'.", output)
            self.assertEqual(len(self.gremio.aventureros), 1)

    @patch('builtins.input', side_effect=[
        '3',             # Opción: Ranger
        'Robin',         # Nombre
        '3',             # ID
        '60',            # Puntos de habilidad
        '0',             # Experiencia
        '120.0',         # Dinero
        'S',             # Tiene mascota
        'Shadow',        # Nombre de la mascota
        '40'             # Puntos de habilidad de la mascota
    ])
    def test_registrar_aventurero_ranger_con_mascota(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            registrar_aventurero(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Registro Ranger con Mascota:")
            print(output)  # Mostrar mensaje de registro
            self.assertIn("Se ha registrado exitosamente el ranger 'Robin'.", output)
            self.assertEqual(len(self.gremio.aventureros), 1)
            self.assertIsNotNone(self.gremio.aventureros[0].mascota)
            self.assertEqual(self.gremio.aventureros[0].mascota.nombre, "Shadow")

    @patch('builtins.input', side_effect=[
        'Recuperar el amuleto',  # Nombre de la misión
        '2',                     # Rango
        '500.0',                 # Recompensa
        'N'                      # Es misión grupal
    ])
    def test_registrar_mision_individual(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            registrar_mision(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Registro Misión Individual:")
            print(output)  # Mostrar mensaje de registro
            self.assertIn("Se ha registrado exitosamente la misión 'Recuperar el amuleto'.", output)
            self.assertEqual(len(self.gremio.misiones), 1)

    @patch('builtins.input', side_effect=[
        'Derrotar al dragón',  # Nombre de la misión
        '5',                   # Rango
        '10000.0',             # Recompensa
        'S',                   # Es misión grupal
        '3'                    # Mínimo de miembros
    ])
    def test_registrar_mision_grupal(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            registrar_mision(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Registro Misión Grupal:")
            print(output)  # Mostrar mensaje de registro
            self.assertIn("Se ha registrado exitosamente la misión 'Derrotar al dragón'.", output)
            self.assertEqual(len(self.gremio.misiones), 1)

    @patch('builtins.input', side_effect=[
        'Recuperar el amuleto',  # Nombre de la misión
        '1',                     # ID del aventurero
        'N'                      # No registrar otro aventurero
    ])

    def test_realizar_mision_individual(self, mock_input):
        # Preparar datos
        self.gremio.registrar_guerrero("Arthur", 1, 50, 0, 100.0, 80)
        self.gremio.registrar_mision("Recuperar el amuleto", 2, 500.0, "individual", 1)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            realizar_mision(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Realización Misión Individual:")
            print(output)  # Mostrar resultado de la misión completada
            self.assertIn("¡La misión 'Recuperar el amuleto' ha sido completada por los aventureros exitosamente!", output)
            aventurero = self.gremio.buscar_aventurero_por_id(1)
            self.assertEqual(aventurero.dinero, 100.0 + 500.0)
            self.assertEqual(aventurero.experiencia, 0 + self.gremio.buscar_mision_por_nombre("Recuperar el amuleto").obtener_experiencia_por_rango())
            self.assertEqual(aventurero.misiones_completadas, 1)

    @patch('builtins.input', side_effect=[
        'Recuperar el amuleto grupal',  # Nombre de la misión
        '1',                     # ID del aventurero
        'S',                      # No registrar otro aventurero
        '2',                     # ID del aventurero
        'N'                      # No registrar otro aventurero
    ])

    def test_realizar_mision_individual(self, mock_input):
        # Preparar datos
        self.gremio.registrar_guerrero("Arthur", 1, 50, 0, 100.0, 80)
        self.gremio.registrar_guerrero("Tomas", 2, 50, 10, 150.0, 80)
        self.gremio.registrar_mision("Recuperar el amuleto grupal", 2, 500.0, "grupal", 1)

        with patch('sys.stdout', new=StringIO()) as fake_output:
            realizar_mision(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Realización Misión Grupal:")
            print(output)  # Mostrar resultado de la misión completada
            self.assertIn("¡La misión 'Recuperar el amuleto grupal' ha sido completada por los aventureros exitosamente!", output)
            experiencia_mision_rango = self.gremio.buscar_mision_por_nombre("Recuperar el amuleto grupal").obtener_experiencia_por_rango()
            aventurero_uno = self.gremio.buscar_aventurero_por_id(1)
            aventurero_dos = self.gremio.buscar_aventurero_por_id(2)    
            self.assertEqual(aventurero_uno.dinero, 350.0)
            self.assertEqual(aventurero_uno.experiencia, experiencia_mision_rango)
            self.assertEqual(aventurero_uno.misiones_completadas, 1)

            self.assertEqual(aventurero_dos.dinero, 400.0)
            self.assertEqual(aventurero_dos.experiencia, 10 + experiencia_mision_rango)
            self.assertEqual(aventurero_dos.misiones_completadas, 1)


    @patch('builtins.input', side_effect=[ 
        'Misión Secreta',  # Nombre de la misión no existente
    ])
    def test_realizar_mision_no_existente(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            realizar_mision(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Misión No Existente:")
            print(output)  # Mostrar el mensaje de error
            self.assertIn("Error: La misión 'Misión Secreta' no existe.", output)

    @patch('builtins.input', side_effect=[ 
        '5',  # Opción inválida en otras consultas
    ])
    def test_otras_consultas_opcion_invalida(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            otras_consultas(self.gremio)
            output = fake_output.getvalue()
            print("Resultado Opción Inválida en Otras Consultas:")
            print(output)  # Mostrar el mensaje de error
            self.assertIn("Error: El valor debe ser menor o igual a 4.\nVolviendo al menú principal.", output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    #unittest.main()