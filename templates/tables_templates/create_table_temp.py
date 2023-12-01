import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import utils.template_handler
import re


def warning(dynamic_frame): # Pendiente que verifique si todos los campos estan llenos
    try:
        answer = messagebox.askokcancel("Confirmación",\
        "¿Deseas Agregar Esta Mesa?")
        if answer:
            utils.template_handler.templ_handler('menu_tables', dynamic_frame)
        else:
            messagebox.showerror('Interrupción',
                'Se ha Cancelado la Operación')
    except Exception:
        messagebox.showerror('No se puedo completar la acción',
        'No se ha logrado realizar el proceso de agregación, llama al proveedor para asesoria')


def catch_date_table(var):
    global table_date
    if len(var)>25:
        return False
    table_date = var
    return True

    # global table_date
    # pattern = r'\d*'
    # if re.fullmatch(pattern, var) is None or len(var)>2:
    #     return False
    # table_date = var
    # return True


def catch_hour_table(var):
    global table_hour
    pattern = r'\d*'
    if re.fullmatch(pattern, var) is None or len(var)>4:
        return False
    table_hour = var
    return True


def catch_people_table(var):
    global table_people
    pattern = r'\d*'
    if re.fullmatch(pattern, var) is None or len(var)>2:
        return False
    table_people = var
    return True


def create_table(dynamic_frame):
    
    global table_date
    global table_hour
    global table_people
    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame, text = "Agregar platos",
                        font=("default", 12, "bold"))
    lbl_dish_name = ttk.Label(dynamic_frame, text = "Fecha")
    lbl_dish_price = ttk.Label(dynamic_frame, text = "Hora")
    lbl_dish_description = ttk.Label(dynamic_frame,
                                    text = "Número de Personas")

    table_date = StringVar()
    table_hour = StringVar()
    table_people = StringVar()

    entry_date_table = ttk.Entry(dynamic_frame, width = entry_box_width,
                                validate="key", validatecommand = \
                                    (dynamic_frame.register(catch_date_table), ''))
    entry_hour_table = ttk.Entry(dynamic_frame, width = entry_box_width,
                                validate="key", validatecommand = 
                                (dynamic_frame.register(catch_hour_table), '%P'))
    entry_people_table = ttk.Entry(dynamic_frame, width = entry_box_width,
                                validate = "key", validatecommand = 
                                (dynamic_frame.register(catch_people_table), '%P'))

    button_add = ttk.Button(
        dynamic_frame,
        text="Agregar",
        style="Accent.TButton",
        command=lambda frame=dynamic_frame: warning(frame))

    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'dishes_management',
            frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_dish_name.grid(column=0, row=1, sticky="w", padx=(20,0), pady=2)
    entry_date_table.grid(column=0, row=2, padx=(20,10), pady=2)
    lbl_dish_price.grid(column=1, row=1, sticky="w", padx=(10,0), pady=2)
    entry_hour_table.grid(column=1, row=2, padx=(10,20), pady=2)
    lbl_dish_description.grid(column=0, row=3, sticky="w", padx=(20,0), pady=2)
    entry_people_table.grid(column=0, row=4, padx=(20,10), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0,10), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(10,0), pady=15)
