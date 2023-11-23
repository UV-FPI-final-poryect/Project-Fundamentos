from tkinter import *
from tkinter import ttk
import handler

def templ1(frame):

     ttk.Label(frame, text="plantilla 1").grid(column=0, row=0, columnspan=2)

     ttk.Button(frame, text="t2", command=lambda frame=frame: 
                             handler.handy('t2', frame)).grid(column=0, row=1)
     ttk.Button(frame, text="t3", command=lambda frame=frame: 
                             handler.handy('t3', frame)).grid(column=1, row=1)
     

     