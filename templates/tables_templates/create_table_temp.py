from tkinter import ttk
from tkinter import messagebox

import datetime as dt
import re
import utils.template_handler
import data_access_tools.tables_adu as tool_table


global table_date
global table_hour
global people


def save_hour(dynamic_frame):
    global table_date
    global table_hour
    global people
    date_today = dt.datetime.now()
    try:
        date = dt.datetime.strptime(table_date, "%d-%m-%Y")
        hour = dt.datetime.strptime(table_hour, "%H:%M")
        if date_today <= date:
            warning(dynamic_frame, date, hour, people)
        else:
            messagebox.showinfo('Actualizar', 'La fecha esta vencida')
    except Exception:
        messagebox.showerror('Error',
                'Formato Fecha u Hora Incorrecto')



def warning(dynamic_frame, date, hour, people): # Pendiente que verifique si todos los campos estan llenos

    try:
        answer = messagebox.askokcancel("Confirmación",
                                        "¿Deseas Agregar Esta Mesa?")
        if answer:
            tool_table.change_format_to_read(date,
                                            hour,
                                            people)
            utils.template_handler.templ_handler('menu_tables',
                                                dynamic_frame)
        else:
            messagebox.showerror('Interrupción',
                                 'Se ha Cancelado la Operación')
    except Exception as e:
        print(e)
        messagebox.showerror('No se puedo completar la acción',
                             'No se ha logrado realizar el proceso de agregación, llama al proveedor para asesoria')


def catch_date_table(var):
    if len(var) > 10:
        return False
    global table_date
    table_date = str(var)
    return True


def catch_hour_table(var):
    if len(var) > 5:
        return False
    global table_hour
    table_hour = var
    return True


def catch_people_table(var):
    global people
    pattern = r'\d*'
    if re.fullmatch(pattern, var) is None or len(var) > 2:
        return False
    people = var
    return True


def create_table(dynamic_frame):
    global table_date
    global table_hour
    global table_people
    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame, text="Agregar Mesas",
                          font=("default", 12, "bold"))
    lbl_date_table = ttk.Label(dynamic_frame, text="Fecha")
    lbl_hour_table = ttk.Label(dynamic_frame, text="Hora")
    lbl_people_table = ttk.Label(dynamic_frame, text="N. Personas")
    ######-------- se elimina asignacion de variables globales con stringvalue() ya que no es necesario
    entry_date_table = ttk.Entry(dynamic_frame,
                                 width=entry_box_width,
                                 validate="key",
                                 validatecommand=(dynamic_frame.register(catch_date_table), '%P'))
    entry_hour_table = ttk.Entry(dynamic_frame,
                                 width=entry_box_width,
                                 validate="key",
                                 validatecommand=(dynamic_frame.register(catch_hour_table), '%P'))
    entry_people_table = ttk.Entry(dynamic_frame,
                                   width=entry_box_width,
                                   validate="key",
                                   validatecommand=(dynamic_frame.register(catch_people_table), '%P'))

    button_add = ttk.Button(dynamic_frame,
                            text="Agregar",
                            style="Accent.TButton",
                            command=lambda: warning(dynamic_frame))

    button_back = ttk.Button(dynamic_frame, text="Atrás",
                             command=lambda: utils.template_handler.templ_handler('menu_tables', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_date_table.grid(column=0, row=1, sticky="w", padx=(20, 0), pady=2)
    entry_date_table.grid(column=0, row=2, padx=(20, 10), pady=2)
    lbl_hour_table.grid(column=1, row=1, sticky="w", padx=(10, 0), pady=2)
    entry_hour_table.grid(column=1, row=2, padx=(10, 20), pady=2)
    lbl_people_table.grid(column=0, row=3, sticky="w", padx=(20, 0), pady=2)
    entry_people_table.grid(column=0, row=4, padx=(20, 10), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(10, 0), pady=15)
