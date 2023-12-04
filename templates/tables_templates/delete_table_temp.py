from tkinter import *
import tkinter as tk
import utils.template_handler
from tkinter import messagebox


def warning(dynamic_frame):
    resultado = messagebox.askokcancel("Warning",\
        "Are you sure you want to delete this table permanently?")
    if resultado:
        utils.template_handler.templ_handler('menu_tables', dynamic_frame)
    else:
        print("La acción fue cancelada.")


def delete_table(dynamic_frame):
    font = "Helvetica 11"
    title_font = "Helvetica 14"
    background = 'gray75'

    lbl_title = tk.Label(dynamic_frame, text="Mesas",\
        font=title_font, background=background)
    button_del = Button(dynamic_frame, text = "Eliminar", font = font,\
        bg = "gray", fg = "white", command=lambda:warning(dynamic_frame))
    button_upd = Button(dynamic_frame, text = "Actualizar", font = font,\
        bg = "gray", fg = "white", command=lambda frame=dynamic_frame :\
            utils.template_handler.templ_handler('menu_tables', frame))

    lbl_title.grid(column=1, row=0, padx=20, pady=10)
    button_del.grid(column=0, row=2, padx=20, pady=10)
    button_upd.grid(column=3, row=2, padx=20, pady=10)
