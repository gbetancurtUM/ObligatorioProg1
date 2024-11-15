class MisionInvalida(Exception):
    def __init__(self, mensaje="Misión inválida: los datos de la misión no son correctos."):
        super().__init__(mensaje)