import tkinter as tk
from PIL import Image, ImageTk


#   Ventana de Inicio Sesion                    3 Pag
def login_template(root):
    #   Tercera  Ventana | Inicio Sesion
    ventana_2 = tk.Toplevel(root)
    ventana_2.title("Iniciar Sesion")
    ventana_2.geometry("370x330")
    inicio = tk.Label(ventana_2, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    image = Image.open("../multimedia/Logo.png")
    image = image.resize((50, 50))
    img = ImageTk.PhotoImage(image)
    lbl_img = tk.Label(ventana_2, image = img)
    frame = tk.LabelFrame(ventana_2, bd=0, background = "Gray")
    lbl1 = tk.Label(frame, text = "Inicio Sesión",\
        font = "Helvetica 11")
    lbl2 = tk.Label(frame, text = "Email")
    lbl3 = tk.Label(frame, text = "Contraseña")
    nemail = tk.Entry(frame)
    npassw = tk.Entry(frame)
    button_loged = tk.Button(frame, text = "Iniciar Sesión",\
        font = "Helvetica 10", bg = "gray", fg = "white")#,\
            #command = lambda: login_user())
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