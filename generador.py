import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def generar_pin(longitud):
    return ''.join(random.choice(string.digits) for _ in range(longitud))