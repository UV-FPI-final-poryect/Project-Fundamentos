from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import utils.template_handler

def yes(dynamic_frame):
    window.destroy()
    utils.template_handler.templ_handler('menu_tables', dynamic_frame)

def warning(dynamic_frame):
    global window
    window = tk.Tk()
    window.title("Confirm Delete")
    window.geometry("500x200+500+200")
    window.resizable()
    message = tk.Label(window, text = \
        """
        Are you sure you want to delete this table permanently?
        """,
        font = "Helvetica 10")
    message.pack()
    button_no = tk.Button(window, text = "NO",\
        font = "Helvetica 11", bg = "dimgray", fg = "white", \
            command= window.destroy)
    button_yes = tk.Button(window, text = "YES",\
        font = "Helvetica 11", bg = "gray", fg = "white",command= lambda:yes(dynamic_frame))
    button_yes.pack(pady=10)
    button_no.pack(pady=10)
    window.mainloop()



def delete_table(dynamic_frame):
    font = "Helvetica 11"
    title_font = "Helvetica 14"
    background = 'gray75'
    lbl_title = tk.Label(dynamic_frame, text="Mesas",\
        font=title_font, background=background)
    button_del = Button(dynamic_frame, text = "Eliminar", font = font,\
        bg = "gray", fg = "white", command=lambda:warning(dynamic_frame))
    button_upd = Button(dynamic_frame, text = "Actualizar", font = font,\
        bg = "gray", fg = "white", command=lambda frame=dynamic_frame :\
            utils.template_handler.templ_handler('menu_tables', frame))
    lbl_title.grid(column=1, row=0, padx=20, pady=10)
    button_del.grid(column=0, row=2, padx=20, pady=10)
    button_upd.grid(column=3, row=2, padx=20, pady=10)
