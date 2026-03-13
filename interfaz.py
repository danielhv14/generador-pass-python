import tkinter as tk
from tkinter import ttk

from generador import generar_contraseña, generar_pin
from seguridad import evaluar_seguridad
from configuracion import configurar_estilo


def iniciar_interfaz():

    ventana = tk.Tk()
    ventana.title("Generador de Contraseña y PIN")
    ventana.geometry("500x450")
    ventana.configure(bg="#f0f4f8")

    configurar_estilo(ventana)

    def actualizar_longitudes(*args):

        tipo = tipo_var.get()

        longitud_combo["values"] = [4, 8, 12, 20]

        longitud_combo.set(12 if tipo == "Contraseña" else 4)


    def generar():

        tipo = tipo_var.get()
        longitud = int(longitud_combo.get())

        if tipo == "Contraseña":

            clave = generar_contraseña(longitud)
            seguridad, nivel = evaluar_seguridad(clave)

            etiqueta_seguridad.config(text=f"Seguridad: {seguridad}")
            barra_seguridad["value"] = nivel * 20

        elif tipo == "PIN":

            clave = generar_pin(longitud)

            etiqueta_seguridad.config(text="PIN generado.")
            barra_seguridad["value"] = 0

        else:

            clave = ""
            etiqueta_seguridad.config(text="")

        resultado_var.set(clave)


    def borrar():

        resultado_var.set("")
        etiqueta_seguridad.config(text="")
        barra_seguridad["value"] = 0


    ttk.Label(
        ventana,
        text="🔐 Generador de Contraseña y PIN",
        font=("Segoe UI", 14, "bold")
    ).pack(pady=10)


    tipo_var = tk.StringVar(value="Contraseña")
    tipo_var.trace_add("write", actualizar_longitudes)


    ttk.Label(ventana, text="¿Qué desea generar?").pack()

    ttk.Radiobutton(
        ventana,
        text="Contraseña",
        variable=tipo_var,
        value="Contraseña"
    ).pack()

    ttk.Radiobutton(
        ventana,
        text="PIN",
        variable=tipo_var,
        value="PIN"
    ).pack()


    ttk.Label(ventana, text="Longitud:").pack(pady=(10, 0))

    longitud_combo = ttk.Combobox(ventana, state="readonly")
    longitud_combo.pack()

    actualizar_longitudes()


    ttk.Button(
        ventana,
        text="GENERAR",
        command=generar
    ).pack(pady=10)

    ttk.Button(
        ventana,
        text="BORRAR",
        command=borrar
    ).pack(pady=(0, 10))


    resultado_var = tk.StringVar()

    entrada_resultado = ttk.Entry(
        ventana,
        textvariable=resultado_var,
        font=("Consolas", 12),
        justify="left",
        width=40
    )

    entrada_resultado.pack(pady=10, fill="x", padx=20)


    etiqueta_seguridad = ttk.Label(
        ventana,
        text="",
        font=("Segoe UI", 10, "italic")
    )

    etiqueta_seguridad.pack(pady=(5, 0))


    barra_seguridad = ttk.Progressbar(
        ventana,
        length=300,
        maximum=100
    )

    barra_seguridad.pack(pady=(5, 20))


    ttk.Label(
        ventana,
        text="Fin",
        font=("Segoe UI", 12, "bold")
    ).pack()


    ventana.mainloop()