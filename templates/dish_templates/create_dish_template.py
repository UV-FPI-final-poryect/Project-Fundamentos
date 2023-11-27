from tkinter import *
from tkinter import ttk
import utils.template_handler


def create_dish_template(dynamic_frame):
    #   Segunda  Ventana | Registro

    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame,
                          text="Agregar platos",
                          font=("default",12, "bold"))
    lbl_dish_name = ttk.Label(dynamic_frame,
                              text="Nombre")
    lbl_dish_price = ttk.Label(dynamic_frame,
                               text="Precio")
    lbl_dish_description = ttk.Label(dynamic_frame,
                                     text="Descripción")
    lbl_dish_availability = ttk.Label(dynamic_frame,
                                      text="Disponibilidad")

    dish_name = StringVar()
    dish_price = StringVar()
    dish_description = StringVar()
    dish_availability = StringVar()

    entry_dish_name = ttk.Entry(dynamic_frame,
                                width=entry_box_width,
                                textvariable=dish_name)
    entry_dish_price = ttk.Entry(dynamic_frame,
                                 textvariable=dish_price,
                                 width=entry_box_width)
    entry_dish_description = ttk.Entry(dynamic_frame,
                                       textvariable=dish_description,
                                       width=entry_box_width)
    entry_dish_availability = ttk.Entry(dynamic_frame,
                                        textvariable=dish_availability,
                                        width=entry_box_width)

    button_add = ttk.Button(
        dynamic_frame,
        text="Agregar",
        style="Accent.TButton",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'dishes_management',
            frame))  # pendiente funcion que guarde en la base de datos

    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'dishes_management',
            frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_dish_name.grid(column=0, row=1, sticky="w", padx=(20,0), pady=2)
    entry_dish_name.grid(column=0, row=2, padx=(20,10), pady=2)
    lbl_dish_price.grid(column=1, row=1, sticky="w", padx=(10,0), pady=2)
    entry_dish_price.grid(column=1, row=2, padx=(10,20), pady=2)
    lbl_dish_description.grid(column=0, row=3, sticky="w", padx=(20,0), pady=2)
    entry_dish_description.grid(column=0, row=4, padx=(20,10), pady=2)
    lbl_dish_availability.grid(column=1, row=3, sticky="w", padx=(10,0), pady=2)
    entry_dish_availability.grid(column=1, row=4, padx=(10,20), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0,10), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(10,0), pady=15)
