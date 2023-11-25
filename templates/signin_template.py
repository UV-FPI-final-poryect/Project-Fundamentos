from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import utils.template_handler
def signin_template(dynamic_frame):
    #   Segunda  Ventana | Registro
    font = "Helvetica 11"
    title_font = "Helvetica 14"
    background = 'gray75'
    lbl_title = tk.Label(dynamic_frame,
                        text="Registro nuevo usuario",
                        font=title_font,
                        background=background)
    lbl_subtitle_email = tk.Label(dynamic_frame,
                                text="Email",
                                font=font,
                                background=background)
    lbl_subtitle_pass = tk.Label(dynamic_frame, 
                                text="Contraseña",
                                font=font,
                                background=background)
    lbl_subtitle_confirm_pass = tk.Label(dynamic_frame, 
                                        text="Confirmar Contraseña",
                                        font=font,
                                        background=background)
    user_email = StringVar()
    user_pass = StringVar()
    user_confirm_pass = StringVar()
    
    entry_email = Entry(dynamic_frame, 
                        textvariable=user_email)
    entry_passw = Entry(dynamic_frame, 
                        textvariable=user_pass, 
                        show="*")
    entry_confirm_pass = Entry(dynamic_frame,
                            textvariable=user_confirm_pass,
                            show="*")
    button_signin = Button(dynamic_frame,
                        text="Registrarse",
                        font=font, 
                        bg="gray", 
                        fg="white",
                        command=lambda frame=dynamic_frame : utils.template_handler.templ_handler('initial', frame)) #pendiente funcion que guarde en la base de datos
    
    lbl_title.grid(column=0, row=0,  padx=40, pady=10)
    lbl_subtitle_email.grid(column=0, row=1, pady=2)
    entry_email.grid(column=0, row=2, pady=2)
    lbl_subtitle_pass.grid(column=0, row=3, pady=2)
    entry_passw.grid(column=0, row=4, pady=2)
    lbl_subtitle_confirm_pass.grid(column=0, row=5, pady=2)
    entry_confirm_pass.grid(column=0, row=6, pady=2)
    button_signin.grid(column=0, row=7, pady=15)
