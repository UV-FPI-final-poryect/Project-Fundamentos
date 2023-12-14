from tkinter import ttk
import utils.template_handler
from tkinter import messagebox
import data_access_tools.tables_da as tables_da
import data_access_tools.dishes_da as dishes_da
import data_access_tools.orders_da as orders_da
import traceback

global table_order
global dish_order


def save_change(dynamic_frame, upd_order):
    global table_order
    global dish_order
    try:
        upd_order[1] = 'Mesa'
        upd_order[2] = table_order
        upd_order[3] = 'Plato'
        upd_order[4] = dish_order
        orders_da.actualize_order(upd_order)
        utils.template_handler.templ_handler('upd_order', dynamic_frame)
    except Exception:
        messagebox.showerror('No se puedo completar la acción', 'No se ha logrado realizar el proceso de '
                                                                'actualización, llama al proveedor para asesoria')
        traceback.print_exc()

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
    for row in range(tables_da.get_total_tables()):
        n_table.append(str(row + 1))
    return n_table


def dish_id():
    n_dish = []
    for row in dishes_da.list_dishes():
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
