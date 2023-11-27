from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import utils.template_handler


def create_table(dynamic_frame):

    lbl_title = ttk.Label(dynamic_frame, text="Agregar Mesa")
    lbl_date = ttk.Label(dynamic_frame, text="Date")
    date = StringVar()
    entry_date = ttk.Entry(dynamic_frame, textvariable=date)
    lbl_hour = ttk.Label(dynamic_frame, text="Hour")
    hour = StringVar()
    entry_hour = ttk.Entry(dynamic_frame, textvariable=hour)
    lbl_people = ttk.Label(dynamic_frame, text="Numbers of People")
    people = StringVar()
    entry_people = ttk.Entry(dynamic_frame, textvariable=people)
    button_add = ttk.Button(dynamic_frame, text = "Add",
                        command=lambda frame=dynamic_frame :\
            utils.template_handler.templ_handler('menu_tables', frame))

    lbl_title.grid(column=1, row=0, padx=20, pady=10)
    lbl_date.grid(column=0, row=1, padx=10, pady=0)
    entry_date.grid(column=0, row=2, padx=10, pady=10)
    lbl_hour.grid(column=2, row=1, padx=10, pady=0)
    entry_hour.grid(column=2, row=2, padx=10, pady=0)
    lbl_people.grid(column=0, row=3, padx=10, pady=10)
    entry_people.grid(column=0, row=4, padx=10, pady=0)
    button_add.grid(column=1, row=5, pady=10)
