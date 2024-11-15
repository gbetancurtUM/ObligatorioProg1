def calcular_rango(habilidad_total):
    if 1 <= habilidad_total <= 20:
        return 1
    elif 21 <= habilidad_total <= 40:
        return 2
    elif 41 <= habilidad_total <= 60:
        return 3
    elif 61 <= habilidad_total <= 80:
        return 4
    else:
        return 5