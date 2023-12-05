from tkinter import *
from tkinter import ttk
import re
import utils.template_handler
import data_access_tools.tables_adu as tool_table


global table_date
global table_hour
global table_people

table_date = ''
table_hour = ''
table_people = 0


def save_change(frame, upd_table):
    global table_date
    global table_hour
    global table_people

    upd_table[1] = table_date
    upd_table[2] = table_hour
    upd_table[3] = table_people
    
    tool_table.updat_table(upd_table)
    utils.template_handler.templ_handler('upd_table', frame)

def catch_date_table(var):
    if len(var)>10:
        return False
    global table_date
    table_date = str(var)
    return True

#width = entry_box_width, validate="key", validatecommand = (dynamic_frame.register(catch_hour_table), '%P')
def catch_hour_table(var):
    if len(var)>5:
        return False
    global table_hour
    table_hour = var
    return True


def catch_people_table(var):
    global table_people
    pattern = r'\d*'
    if re.fullmatch(pattern, var) is None or len(var)>2:
        return False
    table_people = var
    return True
    

def recharge_table(dynamic_frame, upd_table):
    utils.template_handler.destroy_widgets(dynamic_frame)
    global table_date
    global table_hour
    global table_people
    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame, text = "Guardar Cambios",
                        font=("default", 12, "bold"))
    lbl_date_table = ttk.Label(dynamic_frame, text = "Fecha")
    lbl_hour_table = ttk.Label(dynamic_frame, text = "Hora")
    lbl_people_table = ttk.Label(dynamic_frame,
                                    text = "Número de Personas")


    entry_date_table = ttk.Entry(dynamic_frame, width=entry_box_width,
                                validate="key", validatecommand = \
                                    (dynamic_frame.register(catch_date_table),'%P'))
    entry_hour_table = ttk.Entry(dynamic_frame, width=entry_box_width,
                                validate="key", validatecommand = \
                                    (dynamic_frame.register(catch_hour_table),'%P'))
    entry_people_table = ttk.Entry(dynamic_frame, width=entry_box_width,
                                validate="key", validatecommand = \
                                    (dynamic_frame.register(catch_people_table),'%P'))

    entry_date_table.insert(0, upd_table[1])
    entry_hour_table.insert(0, upd_table[2])
    entry_people_table.insert(0, upd_table[3])
    
    table_date = upd_table[1]
    table_hour = upd_table[2]
    table_people = upd_table[3]
    
    
    button_add = ttk.Button(dynamic_frame, text="Agregar",
        style="Accent.TButton",
        command=lambda frame=dynamic_frame, upd_table = upd_table: save_change(frame, upd_table))

    button_back = ttk.Button(dynamic_frame, text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'upd_table',frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_date_table.grid(column=0, row=1, sticky="w", padx=(20,0), pady=2)
    entry_date_table.grid(column=0, row=2, padx=(20,10), pady=2)
    lbl_hour_table.grid(column=1, row=1, sticky="w", padx=(10,0), pady=2)
    entry_hour_table.grid(column=1, row=2, padx=(10,20), pady=2)
    lbl_people_table.grid(column=0, row=3, sticky="w", padx=(20,0), pady=2)
    entry_people_table.grid(column=0, row=4, padx=(20,10), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0,10), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(10,0), pady=15)
