from tkinter import *
from tkinter import ttk
import textwrap
from PIL import Image, ImageTk

from utils.template_handler import templ_handler

def initial_templ(dinamic_frame):
    # Primera Ventana | Inicio
     font = "Helvetica 11"
     intro_txt = textwrap.dedent( """
                    Nuestro restaurante es un lugar donde ofrecemos
                    una variedad de platos deliciosos y recursos
                    culinarios para el público para satisfacer tus
                    necesidades culinarias y hacerte disfrutar de 
                    una experiencia gastronómica excepcional.
                    """)
     lbl_intro_txt = Label(dinamic_frame, 
                           text = intro_txt,
                           font = font, 
                           anchor="center", 
                           justify="center")
     bttn_signin = Button(dinamic_frame,
                          text = "Registrarse",
                          font = font, 
                          bg = "gray", 
                          fg = "white", 
                          command = lambda frame=dinamic_frame: templ_handler('signin', frame))
     bttn_login = Button(dinamic_frame, 
                         text = "Iniciar Sesion",
                         font = font, 
                         bg = "gray", 
                         fg = "white", 
                         command = lambda frame=dinamic_frame: templ_handler('login', frame))
     lbl_intro_txt.grid(column=0, row=0, columnspan=2)
     bttn_signin.grid(column=0, row=1, sticky="nsew", padx=10, pady=10)
     bttn_login.grid(column=1, row=1, sticky="nsew", padx=10, pady=10)

     
