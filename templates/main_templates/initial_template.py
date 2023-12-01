from tkinter import *
from tkinter import ttk
import textwrap
from PIL import Image, ImageTk

import utils.template_handler

def initial_template(dynamic_frame):
    # Primera Ventana | Inicio
    font = "Helvetica 11"
    intro_txt = textwrap.dedent( """
                    Nuestro restaurante es un lugar donde ofrecemos
                    una variedad de platos deliciosos y recursos
                    culinarios para el público para satisfacer tus
                    necesidades culinarias y hacerte disfrutar de 
                    una experiencia gastronómica excepcional.
                    """)
    lbl_intro_txt = Label(dynamic_frame, text = intro_txt,\
        font = font, anchor="center", justify="center", background='gray85')
    bttn_signin = Button(dynamic_frame, text = "Registrarse", \
        font = font, bg = "gray", fg = "white", command = lambda frame\
            =dynamic_frame: utils.template_handler.templ_handler\
                ('signin', frame))
    bttn_login = Button(dynamic_frame, text = "Iniciar Sesion", \
        font = font, bg = "gray", fg = "white", command = lambda \
            frame=dynamic_frame: utils.template_handler.templ_handler\
                ('login', frame))
    lbl_intro_txt.grid(column=0, row=0, columnspan=2,padx=20, pady=20)
    bttn_signin.grid(column=0, row=1, sticky="nsew", padx=20, pady=20)
    bttn_login.grid(column=1, row=1, sticky="nsew", padx=20, pady=20)
