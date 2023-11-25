
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import utils.template_handler

def main_menu_template(dynamic_frame):
#     Window Menu Main
      font = "Helvetica 11"
      title_font = "Helvetica 14"
      background = 'gray75'
      lbl_title = Label(dynamic_frame,
                        text="Bienvenido",
                        font=title_font, 
                        background=background)
      
      button_dish_option = Button(dynamic_frame, text="Gestión platos",\
            font=font, bg="gray", fg="white")
#     Santiago Anexando la funcion al boton para ir a gestion de mesas
# command=lambda frame=dynamic_frame : utils.template_handler.templ_handler('menu_tables', frame))
      button_table_option = Button(dynamic_frame,\
            text="Gestión mesas",font=font, bg="gray", fg="white",\
                  command = lambda frame=dynamic_frame: \
                        utils.template_handler.templ_handler\
                  ('menu_tables', frame))
      button_order_option = Button(dynamic_frame, \
            text="Gestión pedidos", font=font, bg="gray",\
                  fg="white")
      button_logout = Button(dynamic_frame, text="Cerrar sesión",\
            font=font, fg="white")
      lbl_title.grid(column=0, row=0, pady=10)
      button_dish_option.grid(column=0, row=1, pady=10)
      button_table_option.grid(column=0, row=2, pady=10)
      button_order_option.grid(column=0, row=3, pady=10)
      button_logout.grid(column=0, row=4, pady=10)
