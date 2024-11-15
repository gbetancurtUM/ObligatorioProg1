class RangoInsuficiente(Exception):
    def __init__(self, mensaje="El aventurero no cumple con el rango requerido para esta misión."):
        super().__init__(mensaje)