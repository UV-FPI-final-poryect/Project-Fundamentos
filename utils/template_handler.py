from templates.initial_template import initial_templ
from templates.login_template import login_template
from templates.signin_template import signin_template

#from utils.clean_frame import clean -  ELIMINAR script

templ_dic = {'initial':initial_templ,
             'login':login_template,
             'signin':signin_template
             }

def templ_handler(choice, dynamic_frame):
  for widget in dynamic_frame.winfo_children():
    widget.destroy()
  
  temp_chosen = templ_dic[choice]
  temp_chosen(dynamic_frame)

 
