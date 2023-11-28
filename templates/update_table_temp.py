from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import utils.template_handler


def update_table(dynamic_frame):
    lbl_title = ttk.Label(dynamic_frame, text="Mesas",
                        font=("default", 12, "bold"))

    button_back = ttk.Button(dynamic_frame, text = "Back",
                        command=lambda frame=dynamic_frame :\
                                utils.template_handler.templ_handler('menu_tables', frame))
    button_upd = ttk.Button(dynamic_frame, text = "Update", style="Accent.TButton",
                        command=lambda frame=dynamic_frame :\
                                utils.template_handler.templ_handler('menu_tables', frame))

    lbl_title.grid(column=1, row=0, padx=20, pady=10)
    button_back.grid(column=0, row=2, padx=20, pady=10)
    button_upd.grid(column=3, row=2, padx=20, pady=10)

