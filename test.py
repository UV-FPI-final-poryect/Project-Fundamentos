from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from utils.change_path_for_img import change_path
from utils.template_handler import templ_handler

if __name__ == '__main__':
    change_path()
    root = Tk()
    root.title("SSJ Restorant")
    root.iconbitmap('../multimedia/forkandknife.ico')

    #Se importa y aplica tema forest-dark
    root.tk.call('source', '../resources/Forest-ttk-theme-master/forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')

    last_plain_bg="#858585"

    frame_style = 'My.TFrame'
    style = ttk.Style()
    style.configure(
        frame_style,
        background=last_plain_bg)

    frame_container = ttk.Frame(root)
    frame_container.grid_columnconfigure(0, weight=1, minsize=500)
    frame_container.grid_rowconfigure(0, weight=1, minsize=110)
    frame_container.grid_rowconfigure(1, weight=1, minsize=400)

    static_frame = ttk.Frame(frame_container,style=frame_style)
    image = Image.open("../multimedia/Logo.png")
    image = image.resize((50, 50))
    img = ImageTk.PhotoImage(image)
    lbl_img = ttk.Label(static_frame,
                    image=img,
                    background=last_plain_bg)
    lbl_ini = ttk.Label(static_frame,
                    text="SSJ Restaurant",
                    font=("default",14, "bold"),
                    background=last_plain_bg)

    dynamic_content_frame = ttk.Frame(frame_container,
                                      style=frame_style)

    dynamic_frame = ttk.Frame(dynamic_content_frame, style="Card")

    frame_container.grid(column=0, row=0, sticky="nwes")
    static_frame.grid(column=0, row=0, sticky="nwes")
    dynamic_content_frame.grid(column=0, row=1, sticky="nwes")
    dynamic_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_img.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_ini.place(relx=0.5, rely=0.9, anchor=CENTER)

     #! aqui ingresan la opcion en el primer parametro, recuerden agregarla
     #! al diccionario templ_dic en el archivo template_handler.py

    templ_handler('delete_dish', dynamic_frame)

    root.mainloop()
