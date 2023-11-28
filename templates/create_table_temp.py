from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import utils.template_handler


def create_table(dynamic_frame):
    lbl_title = ttk.Label(dynamic_frame, text="Agregar Mesa",
                        font=("default",12, "bold"))
    lbl_date = ttk.Label(dynamic_frame, text="Date")
    date = StringVar()
    entry_date = ttk.Entry(dynamic_frame, textvariable=date)
    lbl_hour = ttk.Label(dynamic_frame, text="Hour")
    hour = StringVar()
    entry_hour = ttk.Entry(dynamic_frame, textvariable=hour)
    lbl_people = ttk.Label(dynamic_frame, text="Numbers of People")
    people = StringVar()
    entry_people = ttk.Entry(dynamic_frame, textvariable=people)
    button_add = ttk.Button(dynamic_frame, text = "Add", style="Accent.TButton",
                            command=lambda frame=dynamic_frame :\
                                utils.template_handler.templ_handler('menu_tables', frame))
    button_back = ttk.Button(dynamic_frame, text = "Back",
                        command=lambda frame=dynamic_frame :\
                                utils.template_handler.templ_handler('menu_tables', frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_date.grid(column=0, row=1, sticky="w", padx=(20,0), pady=2)
    entry_date.grid(column=0, row=2, padx=(20,10), pady=2)
    lbl_hour.grid(column=1, row=1, sticky="w", padx=(10,0), pady=2)
    entry_hour.grid(column=1, row=2, padx=(10,20), pady=2)
    lbl_people.grid(column=0, row=3, sticky="w", padx=(20,0), pady=2)
    entry_people.grid(column=0, row=4, padx=(20,10), pady=2)
    button_add.grid(column=1, row=5, sticky="w", padx=(0,10), pady=15)
    button_back.grid(column=0, row=5, sticky="e", padx=(0,10), pady=15)
