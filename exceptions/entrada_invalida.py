class EntradaInvalida(Exception):
    def __init__(self, mensaje="Entrada inválida. Revise los datos ingresados."):
        super().__init__(mensaje)