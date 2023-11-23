from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from utils.template_handler import templ_handler

def login_template(dinamic_frame):
     #   Tercera  Ventana | Inicio Sesion
     font = "Helvetica 11"
     title_font = "Helvetica 14"
     lbl_title = Label(dinamic_frame, 
                       text = "Inicio Sesión",
                       font = title_font)
     lbl_subtitle_email = Label(dinamic_frame, 
                                text = "Email",
                                font = font)
     lbl_subtitle_pass = Label(dinamic_frame,
                                text = "Contraseña",
                                font = font)

     user_email = StringVar()
     user_pass = StringVar()
     
     entry_email = Entry(dinamic_frame, 
                    textvariable=user_email)
     entry_passw = Entry(dinamic_frame, 
                    textvariable=user_pass, 
                    show="*")
     button_login = Button(dinamic_frame, 
                           text = "Iniciar Sesión",
                           font = font, 
                           bg = "gray", 
                           fg = "white",
                           command = lambda frame=dinamic_frame: templ_handler('login', frame)) #pendiente funcion que busque en la base de datos y de acceso
     

     lbl_title.grid(column=0, row=0, pady=10)
     lbl_subtitle_email.grid(column=0, row=1)
     entry_email.grid(column=0, row=2)
     lbl_subtitle_pass.grid(column=0, row=3)
     entry_passw.grid(column=0, row=4)
     button_login.grid(column=0, row=5, pady=10)


