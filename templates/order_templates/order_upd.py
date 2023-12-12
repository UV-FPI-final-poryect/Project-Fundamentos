import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import databases.db_tables as tables
import databases.db_dishes as dbdish
import databases.db_orders as order
import templates.order_templates.make_order as save


def save_change(dynamic_frame, upd_order):
    global table_order
    global dish_order
    upd_order[1] = 'Mesa'
    upd_order[2] = table_order
    upd_order[3] = 'Plato'
    upd_order[4] = dish_order
    save.actualize_order(upd_order)
    utils.template_handler.templ_handler('upd_order', dynamic_frame)

####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    """
    método save_change(event) cambiar parametro a dynamic_frame y funcionalidad como en la 
    plantilla save_dish_changes_template.py
    
    crear dos funciones como catch_dish_availability(event) para guardar los valores del combobox
    en variables globales para cada uno
    
    """


def catch_table(event):
    global table_order
    table_order = event.widget.get()
    return True


def catch_dish(event):
    global dish_order
    dish_order = event.widget.get()
    return True


def table_id():
    n_table = []
    for row in range(tables.total_tables):
        n_table.append(row + 1)
    return n_table


def dish_id():
    n_dish = []
    for row in dbdish.db_matrix:
        if row[4] == 'Si':  
            n_dish.append(row[0])
    return n_dish


def update_order(dynamic_frame, upd_order):
    utils.template_handler.destroy_widgets(dynamic_frame)
    global table_order
    global dish_order
    lbl_title = ttk.Label(dynamic_frame,
                          text="Guardar Cambios",
                          font=("default", 12, "bold"))
    lbl_tables = ttk.Label(dynamic_frame,
                                      text="Mesas")
    lbl_dishes = ttk.Label(dynamic_frame,
                                      text="Platos")
    
    table_ids = table_id()
    table_option = ttk.Combobox(dynamic_frame, values=table_ids)
    table_option.bind("<<ComboboxSelected>>", catch_table)
    table_option.insert(0, upd_order[2])
    table_order = upd_order[2]
    
    dish_ids = dish_id()
    dish_option = ttk.Combobox(dynamic_frame,  values=dish_ids)
    dish_option.bind("<<ComboboxSelected>>", catch_dish)
    dish_option.insert(0, upd_order[4])
    dish_order = upd_order[4]
    
    button_add = ttk.Button(dynamic_frame,
                            text="Actualizar",
                            style="Accent.TButton",
                            command=lambda: save_change(dynamic_frame, upd_order))

    button_back = ttk.Button(dynamic_frame,
                             text="Atrás",
                             command=lambda: utils.template_handler.templ_handler(
                                 'upd_order', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_tables.grid(column=0, row=2, padx=10)
    lbl_dishes.grid(column=1, row=2, padx=10)
    table_option.grid(column=0, row=3, padx=15, pady=10)
    dish_option.grid(column=1, row=3, padx=15, pady=10)
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 15), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(15, 0), pady=15)
