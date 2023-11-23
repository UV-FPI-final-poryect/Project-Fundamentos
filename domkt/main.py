from tkinter import *
from tkinter import ttk

import handler

if __name__ == '__main__':

     root = Tk()
     root.title("Feet to Meters")
     root.columnconfigure(0, weight=1)
     root.rowconfigure(0, weight=1)

     frame1 = ttk.Frame(root)
     frame1.grid(column=0, row=0, sticky="nwes")
     ttk.Label(frame1, text="imagen-logo").grid(column=0, row=0,)

     frame2 = ttk.Frame(root)
     frame2.grid(column=0, row=1, sticky="nwes")

     handler.handy("t1", frame2)



     root.mainloop()

