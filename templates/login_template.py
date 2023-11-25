from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import utils.template_handler

def login_template(dynamic_frame):
     #   Tercera  Ventana | Inicio Sesion
     font = "Helvetica 11"
     title_font = "Helvetica 14"
     background = 'gray75'
     lbl_title = Label(dynamic_frame,
                         text="Inicio Sesión",
                         font=title_font,
                         background=background)
     lbl_subtitle_email = Label(dynamic_frame,
                              text="Email",
                              font=font,
                              background=background)
     lbl_subtitle_pass = Label(dynamic_frame,
                               text="Contraseña", 
                               font=font, 
                               background=background)

     user_email = StringVar()
     user_pass = StringVar()
     
     entry_email = Entry(dynamic_frame, textvariable=user_email)
     entry_passw = Entry(dynamic_frame, textvariable=user_pass,\
          show="*")
     button_login = Button(dynamic_frame, text="Iniciar Sesión",\
          font=font, bg="gray", fg="white",\
               command=lambda frame=dynamic_frame : \
                    utils.template_handler.templ_handler\
                         ('main_menu', frame))
#pendiente funcion que busque en la base de datos y de acceso

     lbl_title.grid(column=0, row=0, padx=20, pady=10)
     lbl_subtitle_email.grid(column=0, row=1,pady=2)
     entry_email.grid(column=0, row=2, pady=2)
     lbl_subtitle_pass.grid(column=0, row=3, pady=2)
     entry_passw.grid(column=0, row=4, pady=2)
     button_login.grid(column=0, row=5, pady=15)


