from templates.initial_template import initial_template
from templates.login_template import login_template
from templates.signin_template import signin_template
from templates.main_menu_template import main_menu_template


templ_dic = {'initial':initial_template,
             'login':login_template,
             'signin':signin_template,
             'main_menu':main_menu_template
             }

def templ_handler(choice, dynamic_frame):
  for widget in dynamic_frame.winfo_children():
    widget.destroy()
  
  temp_chosen = templ_dic[choice]
  temp_chosen(dynamic_frame)

 
