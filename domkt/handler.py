from tkinter import *
from tkinter import ttk

from temp.t1 import templ1
from temp.t2 import templ2
from temp.t3 import templ3

temp_choices = {'t1': templ1, 't2': templ2, 't3': templ3}



def handy(choice, frame):

     for widget in frame.winfo_children():
          widget.destroy()

     temp_chosen = temp_choices[choice]
     temp_chosen(frame)


 
     
