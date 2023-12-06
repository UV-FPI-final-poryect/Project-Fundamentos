from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import utils.template_handler


def main_menu_template(dynamic_frame):
    #   Cuarta  Ventana | Menu principal
    lbl_title = ttk.Label(dynamic_frame, text="Bienvenido",
                            font=("default", 12, "bold"))

    button_dish_option = ttk.Button(dynamic_frame, text = "Gestión Platos",
                                    command = lambda frame = dynamic_frame:\
                                        utils.template_handler.templ_handler\
                                            ('dishes_management', frame))
# #pendiente funcion que busque en la base de datos y de acceso
    button_reserve_table_option = ttk.Button(dynamic_frame,
                                            text = "Gestión Mesas",
                                            command = lambda frame = \
                                            dynamic_frame: utils.template_handler.\
                                                templ_handler\
                                                    ('menu_tables', frame))
# command=lambda frame=dynamic_frame :
# utils.template_handler.templ_handler('login', frame)) #pendiente funcion
# que busque en la base de datos y de acceso
    button_order_option = ttk.Button(dynamic_frame,
                                text="Gestión Pedidos")
# command=lambda frame=dynamic_frame :
# utils.template_handler.templ_handler('login', frame)) #pendiente funcion
# que busque en la base de datos y de acceso
    button_logout = ttk.Button(dynamic_frame, 
                            text="Cerrar sesión",
                            style="Accent.TButton")
# command=lambda frame=dynamic_frame :
# utils.template_handler.templ_handler('login', frame)) #pendiente funcion
# que busque en la base de datos y de acceso


    lbl_title.grid(column=0, row=0, pady=10)
    button_dish_option.grid(column=0, row=1, padx=50, pady=5)
    button_reserve_table_option.grid(column=0, row=2, pady=5)
    button_order_option.grid(column=0, row=3, pady=5)
    button_logout.grid(column=0, row=4, pady=(15, 20))
