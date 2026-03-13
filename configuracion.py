import tkinter as tk
from tkinter import ttk

def configurar_estilo(ventana):

    estilo = ttk.Style(ventana)
    estilo.theme_use("clam")

    estilo.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
    estilo.configure("TLabel", background="#f0f4f8", font=("Segoe UI", 10))
    estilo.configure("TCombobox", font=("Segoe UI", 10))