import tkinter as tk

def clean(root):
    # Elmina todos los widgets de la pantalla
    for widget in root.winfo_children():
        widget.destroy()  