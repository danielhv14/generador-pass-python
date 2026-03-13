import string

def evaluar_seguridad(clave):

    longitud = len(clave)
    puntaje = 0

    if any(c.islower() for c in clave):
        puntaje += 1

    if any(c.isupper() for c in clave):
        puntaje += 1

    if any(c.isdigit() for c in clave):
        puntaje += 1

    if any(c in string.punctuation for c in clave):
        puntaje += 1

    if longitud >= 12:
        puntaje += 1

    niveles = ["Muy débil", "Débil", "Aceptable", "Fuerte", "Muy fuerte"]

    return niveles[puntaje - 1] if puntaje > 0 else "Muy débil", puntaje