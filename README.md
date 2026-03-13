# Generador de Contraseñas en Python

Proyecto en Python para generar contraseñas seguras y PINs aleatorios, con evaluación de la seguridad de cada contraseña.

---

## Descripción

Este proyecto permite al usuario:

- Generar **contraseñas aleatorias** de cualquier longitud, usando letras mayúsculas, minúsculas, números y símbolos.  
- Generar **PINs numéricos** de longitud personalizada.  
- Evaluar la **seguridad** de las contraseñas (Alta, Media o Baja) según su longitud y complejidad.

Es ideal para practicar seguridad de contraseñas y automatizar la creación de claves seguras.

---

## Cómo funciona

1. Ejecuta el programa desde la terminal o consola con:
2. Ingresa la longitud de la contraseña o PIN que deseas generar.

El programa genera aleatoriamente la contraseña o PIN.

Si se trata de una contraseña, se evalúa su seguridad según:

Longitud

Inclusión de mayúsculas y minúsculas

Uso de números y símbolos

Se muestra al usuario la contraseña/PIN generado junto con su nivel de seguridad.
Ejemplo de uso
Contraseña
Ingrese la longitud de la contraseña: 12
Contraseña generada: Xy9!pQ2#kLm$
Nivel de seguridad: Alta
PIN
Ingrese la longitud del PIN: 6
PIN generado: 482915

===========================================================================
Archivos principales

generador.py → Funciones para generar contraseñas y PINs.

seguridad.py → Evalúa la fuerza de la contraseña.

interfaz.py → Interfaz gráfica del generador.

main.py → Archivo principal que inicia la aplicación.

configuracion.py → Configuraciones adicionales del proyecto.

Requisitos

Python 3.12 o superior

Librerías estándar de Python (Tkinter para la interfaz)

Tecnologías

Python 3.12

Tkinter para interfaz gráfica

Autor

Daniel Hidalgo Velásquez
GitHub: danielhv14

```bash
python main.py
