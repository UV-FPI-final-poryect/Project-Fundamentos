from templates.initial_template import initial_templ
from templates.login_template import login_template
from templates.signin_template import signin_template

from utils.clean_frame import clean

templ_dic = {'initial':initial_templ,
             'login':login_template,
             'signin':signin_template
             }

def templ_handler(root, selected_templ):
     
     selected_func = templ_dic[selected_templ]
     selected_func(root)



#      from tkinter import *
# from tkinter import ttk

# from temp.t1 import templ1
# from temp.t2 import templ2
# from temp.t3 import templ3

# temp_choices = {'t1': templ1, 't2': templ2, 't3': templ3}



# def handy(choice, frame):

#      for widget in frame.winfo_children():
#           widget.destroy()

#      temp_chosen = temp_choices[choice]
#      temp_chosen(frame)


 