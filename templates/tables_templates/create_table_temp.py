from tkinter import ttk
from tkinter import messagebox

import datetime as dt
import re
import utils.template_handler
import data_access_tools.tables_da as tool_table

table_date = ''
table_hour = ''
people = ''


def save_hour():
    global table_date
    global table_hour
    global people
    if (table_date == '' or
            table_hour == '' or
            people == ''):
        raise ValueError
    else:
        tool_table.save_data_table(table_date, table_hour, people)


def warning(dynamic_frame):
    global table_date
    global table_hour
    global people

    try:
        answer = messagebox.askokcancel("Confirmación",
                                        "¿Deseas Agregar Esta Mesa?")
        if answer:
            save_hour()
            utils.template_handler.templ_handler('menu_tables',
                                                 dynamic_frame)
        else:
            messagebox.showerror('Interrupción',
                                 'Se ha Cancelado la Operación')

    except ValueError:
        messagebox.showerror('Falta alguno de los campos',
                             'Revisa que todos los campos esten correctos y se hayan guardado bien, e intenta '
                             'nuevamente')

    except Exception as e:
        print(e)
        messagebox.showerror('No se puedo completar la acción',
                             'No se ha logrado realizar el proceso de agregación, llama al proveedor para asesoria')


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
                             'El formato de fecha no es aceptado, recuerda que debe ser aaaa-mm-dd'
                             ' y que no sea una fecha anterior al día presente')
        return False


def catch_hour_table(var):
    global table_date
    global table_hour
    try:
        datetime_format = str(table_date) + ' ' + var
        pending_hour = dt.datetime.strptime(datetime_format, "%Y-%m-%d %H:%M")
        if len(var) != 5 or pending_hour < dt.datetime.now():
            table_hour = ""
            raise ValueError
        else:
            table_hour = pending_hour.time().strftime('%H:%M')
            return True
    except ValueError:
        messagebox.showerror('Hora no válida',
                             'El formato de hora no es aceptado, recuerda que debe ser hh:mm'
                             ' y que no sea una hora anterior al día presente, ten en cuenta que se maneja'
                             ' hora militar de las 00:00 hasta las 23:59 horas y que debes de ingresar primero'
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


def create_table(dynamic_frame):
    global table_date
    global table_hour
    global people
    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame,
                          text="Agregar Mesas",
                          font=("default", 12, "bold"))
    lbl_date_table = ttk.Label(dynamic_frame, text="Fecha")
    lbl_hour_table = ttk.Label(dynamic_frame, text="Hora")
    lbl_people_table = ttk.Label(dynamic_frame, text="N. Personas")

    entry_date_table = ttk.Entry(dynamic_frame,
                                 width=entry_box_width,
                                 validate="focusout",
                                 validatecommand=(dynamic_frame.register(catch_date_table), '%P'))
    entry_hour_table = ttk.Entry(dynamic_frame,
                                 width=entry_box_width,
                                 validate="focusout",
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
