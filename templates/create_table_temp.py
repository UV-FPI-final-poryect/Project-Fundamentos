from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import utils.template_handler


def create_table(dynamic_frame):
    font = "Helvetica 11"
    title_font = "Helvetica 14"
    background = 'gray75'
    lbl_title = tk.Label(dynamic_frame, text="Agregar Mesa",
                        font=title_font, background=background)
    lbl_date = tk.Label(dynamic_frame, text="Date", font=font,
                        background=background)
    date = StringVar()
    entry_date = Entry(dynamic_frame, textvariable=date)
    lbl_hour = tk.Label(dynamic_frame, text="Hour", font=font,
                        background=background)
    hour = StringVar()
    entry_hour = Entry(dynamic_frame, textvariable=hour)
    lbl_people = tk.Label(dynamic_frame, text="Numbers of People",
                        font=font, background=background)
    people = StringVar()
    entry_people = Entry(dynamic_frame, textvariable=people)
    button_add = Button(dynamic_frame, text = "Add", font = font,
                        bg = "gray", fg = "white",
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
