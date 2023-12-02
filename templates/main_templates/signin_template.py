from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import utils.template_handler

global user_name
global user_pass
global user_cofirm_pass

user_name = ''
user_pass = ''
user_cofirm_pass = ''


def signin_template(dynamic_frame):

    lbl_title = ttk.Label(dynamic_frame,
                          text="Registro nuevo usuario",
                          font=("default", 12, "bold"))
    lbl_subtitle_email = ttk.Label(dynamic_frame,
                                  text="Email")
    lbl_subtitle_pass = ttk.Label(dynamic_frame,
                                 text="Contraseña",)
    lbl_subtitle_confirm_pass = ttk.Label(dynamic_frame,
                                         text="Confirmar Contraseña")
    user_email = StringVar()
    user_pass = StringVar()
    user_confirm_pass = StringVar()

    entry_email = ttk.Entry(dynamic_frame,
                        textvariable=user_email)
    entry_passw = ttk.Entry(dynamic_frame,
                        textvariable=user_pass,
                        show="*")
    entry_confirm_pass = ttk.Entry(dynamic_frame,
                               textvariable=user_confirm_pass,
                               show="*")
    button_signin = ttk.Button(
        dynamic_frame,
        text="Registrarse",
        style="Accent.TButton",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'initial',
            frame))  # pendiente funcion que guarde en la base de datos

    lbl_title.grid(column=0, row=0, padx=40, pady=10)
    lbl_subtitle_email.grid(column=0, row=1, pady=2)
    entry_email.grid(column=0, row=2, pady=2)
    lbl_subtitle_pass.grid(column=0, row=3, pady=2)
    entry_passw.grid(column=0, row=4, pady=2)
    lbl_subtitle_confirm_pass.grid(column=0, row=5, pady=2)
    entry_confirm_pass.grid(column=0, row=6, pady=2)
    button_signin.grid(column=0, row=7, pady=15)
