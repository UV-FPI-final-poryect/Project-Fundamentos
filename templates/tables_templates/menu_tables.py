from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import utils.template_handler

def menu_tables_template(dynamic_frame):
        lbl_title = ttk.Label(dynamic_frame, text="Gestión de Mesas",
                        font=("default", 12, "bold"))

        button_add_table = ttk.Button(dynamic_frame, text = "Agregar",
                                command=lambda frame = dynamic_frame:\
                                utils.template_handler.templ_handler\
                                                ('add_table', frame))
        button_del_table = ttk.Button(dynamic_frame, text = "Eliminar",
                                command = lambda frame = dynamic_frame:\
                                utils.template_handler.templ_handler\
                                        ('del_table', frame))
        button_upd_table = ttk.Button(dynamic_frame, text = "Actualizar",
                                command = lambda frame = dynamic_frame:\
                                utils.template_handler.templ_handler\
                                                ('upd_table', frame)) 
        button_back = ttk.Button(dynamic_frame, text="Atrás",
                        style = "Accent.TButton",
                        command = lambda frame = dynamic_frame:\
                                utils.template_handler.templ_handler\
                                        ('main_menu', frame))

        lbl_title.grid(column=0, row=0, padx=50, pady=10)
        button_add_table.grid(column=0, row=1, pady=5)
        button_del_table.grid(column=0, row=2, pady=5)
        button_upd_table.grid(column=0, row=3, pady=5)
        button_back.grid(column=0, row=4, pady=(15, 20))
