from tkinter import *
from tkinter import ttk
import textwrap

from PIL import Image, ImageTk
from utils.clean_frame import clean
#from templates.signin_template import signin_template
#from templates.login_template import login_template
from utils.template_handler import templ_handler

def initial_templ(root):
    #   Primera Ventana | Inicio
     clean(root)

     init_templ_content = ttk.Frame(root)
     init_templ_content.grid_rowconfigure(0, weight=1)
     init_templ_content.grid_columnconfigure(0, weight=1)
     init_templ_content.grid_columnconfigure(1, weight=1)
     
     image = Image.open("../multimedia/Logo.png")
     image = image.resize((50, 50))
     img = ImageTk.PhotoImage(image)
     lbl_img = Label(init_templ_content, image = img)
     lbl_ini = Label(init_templ_content, text = "Mi Restaurante",
                     font = "Helvetica 14", anchor="center", justify="center")
     intro_txt = textwrap.dedent( """
                    Nuestro restaurante es un lugar donde ofrecemos
                    una variedad de platos deliciosos y recursos
                    culinarios para el público para satisfacer tus
                    necesidades culinarias y hacerte disfrutar de 
                    una experiencia gastronómica excepcional.
                    """)
     lbl_intro_txt = Label(init_templ_content, text = intro_txt,\
          font = "Helvetica 11", anchor="center", justify="center")
     bttn_signin = Button(init_templ_content, 
                         text = "Registrarse",
                         font = "Helvetica 11", 
                         bg = "gray", 
                         fg = "white", 
                         command = lambda: templ_handler(root, 'signin'))
                         #command = lambda: signin_template(root))
     bttn_login = Button(init_templ_content, 
                         text = "Iniciar Sesion",
                         font = "Helvetica 11", 
                         bg = "gray", 
                         fg = "white", 
                         command = lambda: templ_handler(root, 'login'))
                         #command = lambda: login_template(root))


     init_templ_content.grid(column=0, row=0, padx=10, pady=10,
                                        sticky="nsew")
     lbl_img.grid(column=0, row=0, columnspan=2)
     lbl_ini.grid(column=0, row=1, columnspan=2)
     lbl_intro_txt.grid(column=0, row=2, columnspan=2)
     bttn_signin.grid(column=0, row=3, sticky="nsew", padx=10, pady=10)
     bttn_login.grid(column=1, row=3, sticky="nsew", padx=10, pady=10)

     root.mainloop()