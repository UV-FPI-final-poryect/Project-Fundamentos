from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from utils.change_path_for_img import change_path
from utils.template_handler import templ_handler

if __name__ == '__main__':
     change_path()

     root = Tk()
     root.title("SSJ Restorant")
     root.columnconfigure(0, weight=1, minsize=250)
     root.rowconfigure(0, weight=1, minsize=100)
     root.iconbitmap('../multimedia/forkandknife.ico')

     static_frame = ttk.Frame(root)
     static_frame.grid(column=0, row=0, sticky="nwes")
     static_frame.grid_rowconfigure(0, weight=1)
     static_frame.grid_columnconfigure(0, weight=1)

     image = Image.open("../multimedia/Logo.png")
     image = image.resize((50, 50))
     img = ImageTk.PhotoImage(image)
     lbl_img = Label(static_frame, 
                     image = img)
     lbl_ini = Label(static_frame, 
                     text = "Mi Restaurante",
                     font = "Helvetica 14", 
                     anchor="center", 
                     justify="center")

     dynamic_frame = ttk.Frame(root)
     dynamic_frame.grid(column=0, row=0, sticky="nwes")

     templ_handler('initial', dynamic_frame)

     root.mainloop()
