import tkinter as tk
from PIL import Image, ImageTk

def signin_template(root):
    #   Segunda  Ventana | Registro
    ventana_1 = tk.Toplevel(root)
    ventana_1.title("Registro")
    ventana_1.geometry("370x330")
    inicio = tk.Label(ventana_1, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    image = Image.open("../multimedia/Logo.png")
    image = image.resize((50, 50))
    img = ImageTk.PhotoImage(image)
    lbl_img = tk.Label(ventana_1, image = img)
    frame = tk.LabelFrame(ventana_1, bd=0, background = "White")
    lbl1 = tk.Label(frame, text = "Registrarse",\
        font = "Helvetica 11")
    lbl2 = tk.Label(frame, text = "Email")
    lbl3 = tk.Label(frame, text = "Contraseña")
    lbl4 = tk.Label(frame, text = "Confirmar Contraseña")
    nemail = tk.Entry(frame)
    npassw = tk.Entry(frame)
    npassw1 = tk.Entry(frame)
    button_loged = tk.Button(frame, text = "Registrar",\
        font = "Helvetica 10") #command = lambda: register_user()
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