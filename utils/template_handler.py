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