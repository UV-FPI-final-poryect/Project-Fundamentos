from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk


ventana_main = Tk()
ventana_main.title("Restorant S J y S")
ventana_main.geometry("370x330") # 600x450+350+150


# Obtén la ruta del script actual
script_dir = os.path.dirname(__file__)
# Cambia el directorio de trabajo actual al directorio del script
os.chdir(script_dir)



ventana_main.iconbitmap('../multimedia/forkandknife.ico') # Imagen Arriba
inicio = Label(ventana_main, text = "Mi Restaurante",\
    font = "Helvetica 14")
inicio.pack()
#   Logo
image = Image.open("../multimedia/Logo.png")
image = image.resize((50, 50))
img = ImageTk.PhotoImage(image)
lbl_img = Label(ventana_main, image = img)
lbl_img.pack()
frame = LabelFrame(ventana_main, bd=0, background = "White")
frame.pack()
intro = Label(frame, text = \
    """
    Nuestro restaurante es un lugar donde ofrecemos
    una variedad de platos deliciosos y recursos
    culinarios para el público para satisfacer tus
    necesidades culinarias y hacerte disfrutar de una
    experiencia gastronómica excepcional.
    """)
intro.pack()

ventana_main.mainloop()