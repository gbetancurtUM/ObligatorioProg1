class AventureroInvalido(Exception):
    def __init__(self, mensaje="Aventurero inválido: datos incorrectos o fuera de rango."):
        super().__init__(mensaje)
