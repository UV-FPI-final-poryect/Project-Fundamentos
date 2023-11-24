from templates.initial_template import initial_template
from templates.login_template import login_template
from templates.signin_template import signin_template
from templates.main_menu_template import main_menu_template


templ_dic = {'initial':initial_template,
            'login':login_template,
            'signin':signin_template,
            'main_menu':main_menu_template
            }

def grid_rows_columns_config(dynamic_frame, ratio):
     columns, rows = dynamic_frame.grid_size()
     for i in range(rows):
          dynamic_frame.grid_rowconfigure(i, weight=ratio)
     for j in range(columns):
          dynamic_frame.grid_columnconfigure(j, weight=ratio)


def templ_handler(choice, dynamic_frame):
     

     for widget in dynamic_frame.winfo_children():
          widget.destroy()
     grid_rows_columns_config(dynamic_frame, 0)
     
     temp_chosen = templ_dic[choice]
     temp_chosen(dynamic_frame)

     grid_rows_columns_config(dynamic_frame, 1)


