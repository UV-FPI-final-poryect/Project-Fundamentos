from tkinter import *
from tkinter import ttk
import handler

def templ3(frame):

     ttk.Label(frame, text="plantilla 3").grid(column=0, row=0, columnspan=2)

     ttk.Button(frame, text="t1", command=lambda frame=frame: \
          handler.handy('t1', frame)).grid(column=0, row=1)
     ttk.Button(frame, text="t2", command=lambda frame=frame: \
          handler.handy('t2', frame)).grid(column=1, row=1)
