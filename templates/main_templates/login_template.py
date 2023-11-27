from tkinter import *
from tkinter import ttk

import utils.template_handler


def login_template(dynamic_frame):
    #   Tercera  Ventana | Inicio Sesion 
    lbl_title = ttk.Label(dynamic_frame,
                        text="Inicio Sesión",
                        font=("default", 12, "bold"))
    lbl_subtitle_email = ttk.Label(dynamic_frame,
                            text="Email")
    lbl_subtitle_pass = ttk.Label(dynamic_frame,
                            text="Contraseña")

    user_email = StringVar()
    user_pass = StringVar()

    entry_email = ttk.Entry(dynamic_frame, textvariable=user_email)
    entry_passw = ttk.Entry(dynamic_frame, textvariable=user_pass,
                        show="*")
    button_login = ttk.Button(dynamic_frame, 
                            text="Iniciar Sesión",
                            style="Accent.TButton",
                            command=lambda frame=dynamic_frame:
                            utils.template_handler.templ_handler
                            ('main_menu', frame))
# pendiente funcion que busque en la base de datos y de acceso

    lbl_title.grid(column=0, row=0, pady=10)
    lbl_subtitle_email.grid(column=0, row=1, pady=2)
    entry_email.grid(column=0, row=2, padx=30, pady=2)
    lbl_subtitle_pass.grid(column=0, row=3, pady=2)
    entry_passw.grid(column=0, row=4, padx=30, pady=2)
    button_login.grid(column=0, row=5, pady=15)
