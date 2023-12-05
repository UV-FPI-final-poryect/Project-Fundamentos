from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import utils.template_handler
import data_access_tools.tables_adu as tool_table

def save_hour():
    global table_date
    global table_hour
    global table_people
    print(type(table_date))
    print(type(table_hour))
    print(type(table_people))
    tool_table.change_format_to_read(table_date, table_hour, table_people)


def warning(dynamic_frame): # Pendiente que verifique si todos los campos estan llenos
    try:
        answer = messagebox.askokcancel("Confirmación",\
        "¿Deseas Agregar Esta Mesa?")
        if answer:
            save_hour()
            utils.template_handler.templ_handler('menu_tables', dynamic_frame)
        else:
            messagebox.showerror('Interrupción',
                'Se ha Cancelado la Operación')
    except Exception as e:
        print(e)
        messagebox.showerror('No se puedo completar la acción',
        'No se ha logrado realizar el proceso de agregación, llama al proveedor para asesoria')


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
    


def create_table(dynamic_frame):
    global table_date
    global table_hour
    global table_people
    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame, text="Agregar Mesas",
                        font=("default",12, "bold"))
    lbl_date_table = ttk.Label(dynamic_frame, text="Fecha")
    lbl_hour_table = ttk.Label(dynamic_frame, text="Hora")
    lbl_people_table = ttk.Label(dynamic_frame, text="N. Personas")


    table_date = StringVar()
    table_hour = StringVar()
    table_people = StringVar()

    entry_date_table = ttk.Entry(dynamic_frame, width=entry_box_width,
                                validate="key", validatecommand = \
                                    (dynamic_frame.register(catch_date_table),'%P'))
    entry_hour_table = ttk.Entry(dynamic_frame, width=entry_box_width,
                                validate="key", validatecommand = \
                                    (dynamic_frame.register(catch_hour_table),'%P'))
    entry_people_table = ttk.Entry(dynamic_frame, width=entry_box_width,
                                validate="key", validatecommand = \
                                    (dynamic_frame.register(catch_people_table),'%P'))

    button_add = ttk.Button(dynamic_frame, text="Agregar",
        style="Accent.TButton",
        command=lambda frame=dynamic_frame: warning(frame))

    button_back = ttk.Button(dynamic_frame, text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'menu_tables',frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_date_table.grid(column=0, row=1, sticky="w", padx=(20,0), pady=2)
    entry_date_table.grid(column=0, row=2, padx=(20,10), pady=2)
    lbl_hour_table.grid(column=1, row=1, sticky="w", padx=(10,0), pady=2)
    entry_hour_table.grid(column=1, row=2, padx=(10,20), pady=2)
    lbl_people_table.grid(column=0, row=3, sticky="w", padx=(20,0), pady=2)
    entry_people_table.grid(column=0, row=4, padx=(20,10), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0,10), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(10,0), pady=15)
