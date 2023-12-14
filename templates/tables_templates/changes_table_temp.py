from tkinter import ttk
from tkinter import messagebox
import datetime as dt
import re
import utils.template_handler
import data_access_tools.tables_da as tool_table


"""
This module imports essential libraries such as tkinter, datetime, and
re, utilizing methods like ttk and messagebox.
It also imports two custom modules: 'template_handler' and 'tables_da'.
The primary purpose of this module is to facilitate the saving of 
modified tables.
"""


table_date = ''
table_hour = ''
people = ''


def save_change(frame, upd_table):
    """This function verifies, processes, and saves the new changes."""
    global table_date
    global table_hour
    global people
    try:
        if (table_date == '' or
                table_hour == '' or
                people == ''):
            raise ValueError
        else:

            upd_table[1] = table_date
            upd_table[2] = table_hour
            upd_table[3] = people

            tool_table.updat_table(upd_table)
            utils.template_handler.templ_handler('upd_table', frame)
    except ValueError:
        messagebox.showerror('Falta alguno de los campos',
                             'Revisa que todos los campos esten '
                             'correctos y se hayan guardado bien,'
                             'e intenta nuevamente')

    except Exception as e:
        print(e)
        messagebox.showerror('No se puedo completar la acción',
                             'No se ha logrado realizar el proceso '
                             'de actualización, llama al proveedor para '
                             'asesoria')


def catch_date_table(var):
    global table_date
    try:
        pending_date = dt.datetime.strptime(var, "%Y-%m-%d")
        if len(var) != 10 or pending_date.date() < dt.datetime.today().date():
            table_date = ""
            raise ValueError
        else:
            table_date = pending_date.date()
            return True
    except ValueError:
        messagebox.showerror('Fecha no válida',
                             'El formato de fecha no es aceptado, '
                             'recuerda que debe ser aaaa-mm-dd'
                             ' y que no sea una fecha anterior al día '
                             'presente')
        return False


def catch_hour_table(var):
    global table_date
    global table_hour
    try:
        datetime_format = str(table_date) + ' ' + var
        pending_hour = dt.datetime.strptime(datetime_format,
                                            "%Y-%m-%d %H:%M")
        if len(var) != 5 or pending_hour < dt.datetime.now():
            table_hour = ""
            raise ValueError
        else:
            table_hour = pending_hour.time().strftime('%H:%M')
            return True
    except ValueError:
        messagebox.showerror('Hora no válida',
                             'El formato de hora no es aceptado, '
                             'recuerda que debe ser hh:mm'
                             'y que no sea una hora anterior al día '
                             'presente, ten en cuenta que se maneja'
                             ' hora militar de las 00:00 hasta las 23:59 '
                             'horas y que debes de ingresar primero'
                             ' la fecha')
        return False


def catch_people_table(var):
    global people
    people = ''
    pattern = r'\d*'
    if re.fullmatch(pattern, var) is None:
        return False
    else:
        people = var
        return True


def recharge_table(dynamic_frame, upd_table):
    utils.template_handler.destroy_widgets(dynamic_frame)
    global table_date
    global table_hour
    global people
    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame,
                          text="Guardar Cambios",
                          font=("default", 12, "bold"))
    lbl_date_table = ttk.Label(dynamic_frame,
                               text="Fecha")
    lbl_hour_table = ttk.Label(dynamic_frame,
                               text="Hora")
    lbl_people_table = ttk.Label(dynamic_frame,
                                 text="Número de Personas")

    entry_date_table = ttk.Entry(dynamic_frame,
                                 width=entry_box_width,
                                 validate="focusout",
                                 validatecommand=(dynamic_frame.register\
                                     (catch_date_table), '%P'))
    entry_hour_table = ttk.Entry(dynamic_frame,
                                 width=entry_box_width,
                                 validate="focusout",
                                 validatecommand=(dynamic_frame.register\
                                     (catch_hour_table), '%P'))
    entry_people_table = ttk.Entry(dynamic_frame,
                                   width=entry_box_width,
                                   validate="key",
                                   validatecommand=(dynamic_frame.register\
                                       (catch_people_table), '%P'))

    entry_date_table.insert(0, upd_table[1])
    entry_hour_table.insert(0, upd_table[2])
    entry_people_table.insert(0, upd_table[3])

    table_date = upd_table[1]
    table_hour = upd_table[2]
    people = upd_table[3]

    button_add = ttk.Button(dynamic_frame,
                            text="Actualizar",
                            style="Accent.TButton",
                            command=lambda: save_change(dynamic_frame,
                                                        upd_table))

    button_back = ttk.Button(dynamic_frame,
                             text="Atrás",
                             command=lambda: utils.template_handler.\
                                 templ_handler('upd_table', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_date_table.grid(column=0, row=1, sticky="w", padx=(20, 0), pady=2)
    entry_date_table.grid(column=0, row=2, padx=(20, 10), pady=2)
    lbl_hour_table.grid(column=1, row=1, sticky="w", padx=(10, 0), pady=2)
    entry_hour_table.grid(column=1, row=2, padx=(10, 20), pady=2)
    lbl_people_table.grid(column=0, row=3, sticky="w", padx=(20, 0), pady=2)
    entry_people_table.grid(column=0, row=4, padx=(20, 10), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(10, 0), pady=15)
