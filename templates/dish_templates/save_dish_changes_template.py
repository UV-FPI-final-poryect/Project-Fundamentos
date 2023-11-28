from tkinter import *
from tkinter import ttk
from tkinter import constants
import utils.template_handler
import templates.dish_templates.MATRIZ_EJEMPLO as MATRIX

def save_process(dynamic_frame, s):
    print(s[1])
    #utils.template_handler.templ_handler('update_dish', dynamic_frame)

def capturar_valor(var, dish_to_update):
    dish_to_update[1] = var
    print("Valor modificado:", dish_to_update[1])

def save_dish_changes_template(dynamic_frame, dish_to_update):
    utils.template_handler.destroy_widgets(dynamic_frame)

    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame,
                          text="Guardar cambios - plato",
                          font=("default",12, "bold"))
    lbl_dish_name = ttk.Label(dynamic_frame,
                              text="Nombre")
    lbl_dish_price = ttk.Label(dynamic_frame,
                               text="Precio")
    lbl_dish_description = ttk.Label(dynamic_frame,
                                     text="Descripción")
    lbl_dish_availability = ttk.Label(dynamic_frame,
                                      text="Disponibilidad")

    #dish_name = StringVar()
    # dish_price = StringVar()
    # dish_description = StringVar()
    # dish_availability = StringVar()
    entry_dish_name = ttk.Entry(dynamic_frame,
                                #textvariable=dish_name,
                                width=entry_box_width,
                                validate="focusout", 
                                validatecommand=(dynamic_frame.register(capturar_valor), '%S', dish_to_update))
    entry_dish_price = ttk.Entry(dynamic_frame,
                                 #textvariable=dish_price,
                                 width=entry_box_width)
    entry_dish_description = ttk.Entry(dynamic_frame,
                                      # textvariable=dish_description,
                                       width=entry_box_width)
    entry_dish_availability = ttk.Entry(dynamic_frame,
                                       # textvariable=dish_availability,
                                        width=entry_box_width)
    
    #dish_name.trace_add('write', actualizar_label)
    
    entry_dish_name.insert(0, dish_to_update[1])
    entry_dish_price.insert(0, dish_to_update[2])
    entry_dish_description.insert(0, dish_to_update[3])
    entry_dish_availability.insert(0, dish_to_update[4])
    
    button_add = ttk.Button(
        dynamic_frame,
        text="Guardar",
        style="Accent.TButton",
        command=lambda frame=dynamic_frame, s=dish_to_update: save_process(frame, s))  # pendiente funcion que guarde en la base de datos

    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'update_dish', frame))

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