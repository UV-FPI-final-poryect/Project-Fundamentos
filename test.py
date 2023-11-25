from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from utils.change_path_for_img import change_path
from utils.template_handler import templ_handler

if __name__ == '__main__':
    change_path()

    root = Tk()
    root.title("SSJ Restorant")
    root.columnconfigure(0, weight=1, minsize=500)
    root.rowconfigure(0, weight=1, minsize=80)
    root.rowconfigure(1, weight=2, minsize=300)
    root.iconbitmap('../multimedia/forkandknife.ico')

    frame_style = 'My.TFrame'
    style = ttk.Style()
    style.configure(
        frame_style,
        background='gray75',
        borderwidth=2,
        relief="flat")

    static_frame = ttk.Frame(root)
    image = Image.open("../multimedia/Logo.png")
    image = image.resize((50, 50))
    img = ImageTk.PhotoImage(image)
    lbl_img = Label(static_frame,
                    image=img)
    lbl_ini = Label(static_frame,
                    text="Mi Restaurante",
                    font="Helvetica 14",
                    bd=1,
                    anchor="center",
                    justify="center")

    dynamic_content_frame = ttk.Frame(root)

    dynamic_frame = ttk.Frame(dynamic_content_frame, style=frame_style)

    static_frame.grid(column=0, row=0, sticky="nwes")
    dynamic_content_frame.grid(column=0, row=1, sticky="nwes")
    dynamic_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_img.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_ini.place(relx=0.5, rely=0.9, anchor=CENTER)

     #! aqui ingresan la opcion en el primer parametro, recuerden agregarla
     #! al diccionario templ_dic en el archivo template_handler.py

    templ_handler('dishes_management', dynamic_frame)

    root.mainloop()
