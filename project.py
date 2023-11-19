#   Project Final Course Fundamentos

#   Authors:
#   Juan David Cifuentes
#   Santiago Echeverri Torres
#   Santiago Lopez Ramirez

# python version 3.12
# pillow version 10.1

import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk

#   Opcion Registrarse                          1 Pag
def register_template():
    print("Estas en Registro")

#   Opcion Iniciar Sesion                       1 Pag
def login_template():
    print("Inicio de Sesion")

#   Empezar Registrar Usuario                   2 Pag
def register_user(user_name, user_pass):
    user_name = 'Nombre'
    user_pass = 'Contraseña'
    print(user_name + user_pass)

#   Leer Usuario de Inicio de Sesion            3 Pag
def login_user(user_name, user_pass):
        user_name = 'Nombre'
        user_pass = 'Contraseña'
        print(user_name + user_pass)

#   Gestion de Platos                           4 Pag
def dishes_management_template():
    pass

#   Gestion de Mesas                            4 Pag
def table_management_template():
    pass

#   Gestion de Pedidos                          4 Pag
def deliver_management_template():
    pass

#   Cerrar Sesion                               4 Pag
def logout_user():
    pass

#   Agregar Platos                              5 Pag
def create_dish_template():
    pass

#   Eliminar Platos                             5 Pag
def delete_dish_template():
    pass

#   Actualizar Platos                           5 Pag
def update_dish_template():
    pass

#   Ventana Principal de Inicio                 1 Pag
def ventana_1tkinter():
    #   Primera Ventana | Inicio
    ventana_main = tk.Tk()
    ventana_main.title("Restorant S J y S")
    ventana_main.geometry("370x330") # 600x450+350+150

    ventana_main.iconbitmap(bitmap='forkandknife.ico') # Imagen Arriba
    inicio = tk.Label(ventana_main, text = "Mi Restaurante",\
        font = "Helvetica 14")
    inicio.pack()
    #   Logo
    image = Image.open("Logo.png")
    image = image.resize((50, 50))
    img = ImageTk.PhotoImage(image)
    lbl_img = Label(ventana_main, image = img)
    lbl_img.pack()
    frame = LabelFrame(ventana_main, bd=0, background = "White")
    frame.pack()
    intro = tk.Label(frame, text = \
        """
        Nuestro restaurante es un lugar donde ofrecemos
        una variedad de platos deliciosos y recursos
        culinarios para el público para satisfacer tus
        necesidades culinarias y hacerte disfrutar de una
        experiencia gastronómica excepcional.
        """)
    intro.pack()
    button_signin = tk.Button(ventana_main, text = "Registrarse",\
        font = "Helvetica 11", bg = "gray", fg = "white", \
            command = lambda: ventana_2tkinter())
    button_signin.pack()
    button_logout = tk.Button(ventana_main, text = "Iniciar Sesion",\
        font = "Helvetica 11", bg = "gray", fg = "white", \
            command = lambda: ventana_3tkinter())
    button_logout.pack()
    ventana_main.mainloop()

#   Ventana de Registro                         2 Pag
def ventana_2tkinter():
    #   Segunda  Ventana | Registro
    ventana_1 = tk.Toplevel()
    ventana_1.title("Registro")
    ventana_1.geometry("370x330")
    inicio = tk.Label(ventana_1, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    image = Image.open("Logo.png")
    image = image.resize((50, 50))
    img = ImageTk.PhotoImage(image)
    lbl_img = Label(ventana_1, image = img)
    frame = LabelFrame(ventana_1, bd=0, background = "White")
    lbl1 = tk.Label(frame, text = "Registrarse",\
        font = "Helvetica 11")
    lbl2 = tk.Label(frame, text = "Email")
    lbl3 = tk.Label(frame, text = "Contraseña")
    lbl4 = tk.Label(frame, text = "Confirmar Contraseña")
    nemail = tk.Entry(frame)
    npassw = tk.Entry(frame)
    npassw1 = tk.Entry(frame)
    button_loged = tk.Button(frame, text = "Registrar",\
        font = "Helvetica 10", command = lambda: register_user())
    inicio.pack()
    lbl_img.pack()
    frame.pack()
    lbl1.pack()
    lbl2.pack()
    nemail.pack()
    lbl3.pack()
    npassw.pack()
    lbl4.pack()
    npassw1.pack()
    button_loged.pack()
    ventana_1.mainloop()

#   Ventana de Inicio Sesion                    3 Pag
def ventana_3tkinter():
    #   Tercera  Ventana | Inicio Sesion
    ventana_2 = tk.Toplevel()
    ventana_2.title("Iniciar Sesion")
    ventana_2.geometry("370x330")
    inicio = tk.Label(ventana_2, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    image = Image.open("Logo.png")
    image = image.resize((50, 50))
    img = ImageTk.PhotoImage(image)
    lbl_img = Label(ventana_2, image = img)
    frame = LabelFrame(ventana_2, bd=0, background = "Gray")
    lbl1 = tk.Label(frame, text = "Inicio Sesión",\
        font = "Helvetica 11")
    lbl2 = tk.Label(frame, text = "Email")
    lbl3 = tk.Label(frame, text = "Contraseña")
    nemail = tk.Entry(frame)
    npassw = tk.Entry(frame)
    button_loged = tk.Button(frame, text = "Iniciar Sesión",\
        font = "Helvetica 10", bg = "gray", fg = "white",\
            command = lambda: login_user())
    inicio.pack()
    lbl_img.pack()
    frame.pack()
    lbl1.pack()
    lbl2.pack()
    nemail.pack()
    lbl3.pack()
    npassw.pack()
    button_loged.pack()
    ventana_2.mainloop()

#   Ventana de Menu Principal                   4 Pag
def ventana_4tkinter():
    #   Cuarta  Ventana | Main Menu
    ventana_3 = tk.Tk()
    ventana_3.title("Menu Main")
    ventana_3.geometry("370x330")
    inicio = tk.Label(ventana_3, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    lbl1 = tk.Label(ventana_3, text = "Bienvenido",\
        font = "Helvetica 11")
    lbl2 = tk.Label(ventana_3, text = "Contraseña")
    button_gest_dish = tk.Button(ventana_3, text = "Gestion Platos",\
        font = "Helvetica 10", command = lambda: \
            dishes_management_template())
    button_gest_table = tk.Button(ventana_3, text = "Gestion Mesas",\
        font = "Helvetica 10", command = lambda: \
            table_management_template())
    button_order = tk.Button(ventana_3, text = "Gestion Pedidos",\
        font = "Helvetica 10", command = lambda: \
            deliver_management_template())
    button_close_ss = tk.Button(ventana_3, text = "Cerrar Sesión",\
        font = "Helvetica 10", command = lambda: logout_user())
    inicio.pack()
    lbl1.pack()
    button_gest_dish.pack()
    button_gest_table.pack()
    button_order.pack()
    button_close_ss.pack()
    ventana_3.mainloop()


if __name__ == '__main__':
    ventana_1tkinter()