from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import utils.template_handler


def dishes_management_template(dynamic_frame):
    #   Cuarta  Ventana | Menu principal
    font = "Helvetica 11"
    title_font = "Helvetica 14"
    background = 'gray75'
    lbl_title = Label(dynamic_frame,
                      text="Gestión de platos",
                      font=title_font,
                      background=background)

    button_create_dish = Button(dynamic_frame, 
                                text="Agregar",
                                font=font, 
                                bg="gray", 
                                fg="white")
# command=lambda frame=dynamic_frame : templ_handler('create_dish', frame))
# #pendiente funcion que busque en la base de datos y de acceso
    button_delete_dish = Button(dynamic_frame,
                                        text="Eliminar",
                                        font=font,
                                        bg="gray",
                                        fg="white")
# command=lambda frame=dynamic_frame :
# utils.template_handler.templ_handler('delete_dish', frame)) #pendiente funcion
# que busque en la base de datos y de acceso
    button_update_dish = Button(dynamic_frame,
                                 text="Actualizar", 
                                 font=font, 
                                 bg="gray",
                                 fg="white")
# command=lambda frame=dynamic_frame :
# utils.template_handler.templ_handler('update_dish', frame)) #pendiente funcion
# que busque en la base de datos y de acceso
    button_back = Button(dynamic_frame, 
                           text="Atrás",
                           font=font, 
                           bg="gray", 
                           fg="white",
                           command=lambda frame=dynamic_frame : utils.template_handler.templ_handler('main_menu', frame))
    
    lbl_title.grid(column=0, row=0, padx=40, pady=10)
    button_create_dish.grid(column=0, row=1, pady=5)
    button_delete_dish.grid(column=0, row=2, pady=5)
    button_update_dish.grid(column=0, row=3, pady=5)
    button_back.grid(column=0, row=4, pady=5)