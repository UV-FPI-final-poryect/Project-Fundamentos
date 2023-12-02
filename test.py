from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from utils.change_path_for_poject import change_path
from utils.template_handler import templ_handler

def center_window(root):
    root.update_idletasks()
    ancho_ventana = root.winfo_width()
    altura_ventana = root.winfo_height()

    x_pos = (root.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y_pos = (root.winfo_screenheight() // 2) - (altura_ventana // 2)

    root.geometry('{}x{}+{}+{}'.format(ancho_ventana, altura_ventana, x_pos, y_pos))


if __name__ == '__main__':
    change_path()
    root = Tk()
    root.title("SSJ Restorant")
    root.resizable(False, False)
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
    frame_container.grid_columnconfigure(0, weight=1, minsize=700)
    frame_container.grid_rowconfigure(0, weight=1, minsize=150)
    frame_container.grid_rowconfigure(1, weight=1, minsize=400)

    static_frame = ttk.Frame(frame_container,style=frame_style)
    image = Image.open("../multimedia/Logo.png")
    image = image.resize((70, 90))
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
    lbl_ini.place(relx=0.5, rely=0.95, anchor=CENTER)

     #! aqui ingresan la opcion en el primer parametro, recuerden agregarla
     #! al diccionario templ_dic en el archivo template_handler.py

    center_window(root)
    templ_handler('update_dish', dynamic_frame)

    root.mainloop()
