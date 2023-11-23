from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from utils.clean_frame import clean
from utils.template_handler import templ_handler

#   Ventana de Inicio Sesion                    3 Pag
def login_template(root):
     #   Tercera  Ventana | Inicio Sesio
     clean(root)

     login_templ_content = ttk.Frame(root)
     login_templ_content.grid_rowconfigure(0, weight=1)
     login_templ_content.grid_columnconfigure(0, weight=1)
     #login_templ_content.grid_columnconfigure(1, weight=1)

     image = Image.open("../multimedia/Logo.png")
     image = image.resize((50, 50))
     img = ImageTk.PhotoImage(image)
     lbl_img = Label(login_templ_content, image = img)
     lbl_ini = Label(login_templ_content, text = "Mi Restaurante",
                    font = "Helvetica 14", anchor="center", justify="center")
     lbl1 = Label(login_templ_content, text = "Inicio Sesión", 
                    font = "Helvetica 11")
     lbl2 = Label(login_templ_content, text = "Email")
     lbl3 = Label(login_templ_content, text = "Contraseña")

     user_email = StringVar()
     user_pass = StringVar()
     nemail = Entry(login_templ_content, textvariable=user_email)
     npassw = Entry(login_templ_content, textvariable=user_pass, show="*")
     button_loged = Button(login_templ_content, text = "Iniciar Sesión",
                         font = "Helvetica 10", bg = "gray", fg = "white",
                         command = lambda:templ_handler(root, 'initial'))#, command = lambda: initial_templ(root))
     
     login_templ_content.grid(column=0, row=0, padx=10, pady=10,
                                        sticky="nsew")
     lbl_img.grid(column=0, row=0, pady=10)
     lbl_ini.grid(column=0, row=1)
     lbl1.grid(column=0, row=2, pady=10)
     lbl2.grid(column=0, row=3)
     nemail.grid(column=0, row=4)
     lbl3.grid(column=0, row=5)
     npassw.grid(column=0, row=6)
     button_loged.grid(column=0, row=7, pady=10)


     #root.mainloop()