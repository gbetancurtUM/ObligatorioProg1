# README

## Simulador de Gremio de Aventureros

Este es un programa que simula un gremio de aventureros al estilo de juegos tipo Dungeons & Dragons. Permite gestionar aventureros, misiones y realizar diversas consultas desde la terminal mediante un menú interactivo.

### Funcionalidades principales

- **Registrar Aventurero**: Permite registrar guerreros, magos y rangers con sus atributos correspondientes.
- **Registrar Misión**: Posibilidad de agregar misiones individuales o grupales al gremio.
- **Realizar Misión**: Asignar misiones a aventureros y completar misiones si cumplen con los requisitos.
- **Otras Consultas**: Acceder a rankings y listados, como el Top 10 de aventureros con más misiones completadas, entre otros.

### Requisitos del sistema

- **Python 3.6 o superior**

### Instalación

1. Clona este repositorio o descarga el código fuente.
2. Asegúrate de tener Python instalado en tu sistema.

### Estructura del proyecto

/ObligatorioProg1
- `main.py`: Programa principal que maneja la interacción con el usuario.
- `gremio.py`: Contiene la clase Gremio y su lógica.
- `entities/`: Directorio con las clases de los aventureros, misiones y mascotas.
  - `__init__.py`
  - `aventurero.py`
  - `guerrero.py`
  - `mago.py`
  - `mascota.py`
  - `mision.py`  
  - `ranger.py`
- `exceptions/`: Directorio con las excepciones personalizadas.
  - `__init__.py`
  - `aventurero_invalido.py`
  - `entrada_invalida.py`
  - `mision_invalida.py`
  - `rango_insuficiente.py`
- `tests/`: Directorio con test del paquete unitest.
  - `__init__.py`
  - `test_gremio.py`
  - `test_main.py`
- `utils.py`: utilidad para calcular rango(no repetir codigo)
- `README.md`
- `DiagramaUML.png` Diagrama UML contienedo las clases, atributos y relaciones. 

### Ejecución del programa

Para ejecutar el programa, abre una terminal en el directorio del proyecto y ejecuta:

```bash
python main.py
```
### Ejecución de los tests
Este proyecto utiliza unittest para realizar pruebas unitarias. Las pruebas se encuentran dentro de la carpeta tests/. Puedes ejecutar todos los tests utilizando el siguiente comando:

python -m unittest -v  tests.test_main     -- para main
python -m unittest -v  tests.test_gremios  -- para gremio 

### Uso del programa

Al iniciar el programa, se mostrará un menú principal con las opciones disponibles. Ingresa el número de la opción que deseas seleccionar y sigue las instrucciones en pantalla.

### Notas importantes

- Asegúrate de ingresar los datos en el formato y rango solicitados. El programa validará las entradas y mostrará mensajes de error en caso de datos inválidos.
- Los nombres de aventureros y misiones no deben contener números y no pueden estar vacíos.
- Los IDs de los aventureros deben ser únicos.

### Ejemplo de interacción

```
Bienvenido al Simulador de Gremio de Aventureros!
Seleccione una opción:
1. Registrar Aventurero
2. Registrar Misión
3. Realizar Misión
4. Otras Consultas
5. Salir
```

### EXPLICACION DIAGRAMA UML

Clase Gremio es la clase principal, con sus atributos que gestionan las misiones y los aventureros. Controla las consultas del menu que se implementó en el main. 
Clase aventurero es abstracta, tiene los atributos comunes a guerrero, mago, y ranger.
Luego cada clase hija(guerrero, mago y ranger) hereda de la clase padre(Aventurero) e implementa los
metodos sobre calcular_habilidad_total de acuerdo a como se calcula en cada clase. 
Un ranger tiene una unica mascota y la instancia mascota depende del ranger, por eso una composicion(sin ranger no hay mascota).
Las exceciones RangoInsuficiente, MisionInvalida, EntradaInvalida y AventureroInvalido heredan de la clase Exception. 
Finalmente una clase utils con calcular_rango para no repetir codigo y reutilizarlo. 




