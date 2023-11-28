from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import utils.template_handler


def dishes_management_template(dynamic_frame):
    #   Cuarta  Ventana | Menu principal
    lbl_title = ttk.Label(dynamic_frame,
                          text="Gestión de platos",
                          font=("default", 12, "bold"))

    button_create_dish = ttk.Button(dynamic_frame, 
                                text="Agregar",
                                command=lambda frame=dynamic_frame : utils.template_handler.templ_handler('create_dish', frame))
    button_delete_dish = ttk.Button(dynamic_frame,
                                        text="Eliminar",
                                        command=lambda frame=dynamic_frame :utils.template_handler.templ_handler('delete_dish', frame))
    button_update_dish = ttk.Button(dynamic_frame,
                                 text="Actualizar", command=lambda frame=dynamic_frame :utils.template_handler.templ_handler('update_dish', frame)) 
    button_back = ttk.Button(dynamic_frame, 
                            text="Atrás",
                            style="Accent.TButton",
                            command=lambda frame=dynamic_frame : utils.template_handler.templ_handler('main_menu', frame))
    
    lbl_title.grid(column=0, row=0, padx=50, pady=10)
    button_create_dish.grid(column=0, row=1, pady=5)
    button_delete_dish.grid(column=0, row=2, pady=5)
    button_update_dish.grid(column=0, row=3, pady=5)
    button_back.grid(column=0, row=4, pady=(15, 20))