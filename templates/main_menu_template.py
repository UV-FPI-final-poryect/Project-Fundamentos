
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import utils.template_handler

def main_menu_template(dynamic_frame):
     #   Cuarta  Ventana | Menu principal
     font = "Helvetica 11"
     title_font = "Helvetica 14"
     lbl_title = Label(dynamic_frame, 
                       text="Bienvenido",
                       font=title_font)
     
     button_dish_option = Button(dynamic_frame,
                                 text="Gestión platos",
                                 font=font, 
                                 bg="gray", 
                                 fg="white")#,
                           #command=lambda frame=dynamic_frame : templ_handler('login', frame)) #pendiente funcion que busque en la base de datos y de acceso
     button_reserve_table_option = Button(dynamic_frame,
                                          text="Gestión mesas",
                                          font=font, 
                                          bg="gray", 
                                          fg="white")#,
                           #command=lambda frame=dynamic_frame : utils.template_handler.templ_handler('login', frame)) #pendiente funcion que busque en la base de datos y de acceso
     button_order_option = Button(dynamic_frame, 
                                  text="Gestión pedidos",
                                  font=font,
                                  bg="gray", 
                                  fg="white")#,
                           #command=lambda frame=dynamic_frame : utils.template_handler.templ_handler('login', frame)) #pendiente funcion que busque en la base de datos y de acceso
     button_logout = Button(dynamic_frame, 
                            text="Cerrar sesión",
                            font=font, 
                            fg="white")#,
                           #command=lambda frame=dynamic_frame : utils.template_handler.templ_handler('login', frame)) #pendiente funcion que busque en la base de datos y de acceso
     

     lbl_title.grid(column=0, row=0, pady=10)
     button_dish_option.grid(column=0, row=1, pady=10)
     button_reserve_table_option.grid(column=0, row=2, pady=10)
     button_order_option.grid(column=0, row=3, pady=10)
     button_logout.grid(column=0, row=4, pady=10)
