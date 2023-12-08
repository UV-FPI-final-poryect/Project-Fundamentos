from templates.main_templates.initial_template import initial_template
from templates.main_templates.login_template import login_template
from templates.main_templates.signin_template import signin_template
from templates.main_templates.main_menu_template import main_menu_template
# Juan David anexando modulo de gestion de platos
from templates.dish_templates.dishes_management_template import dishes_management_template
from templates.dish_templates.create_dish_template import create_dish_template
from templates.dish_templates.delete_dish_template import delete_dish_template
from templates.dish_templates.update_dish_template import update_dish_template
# Santiago anexando modulo de gestion de mesas
from templates.tables_templates.menu_tables import menu_tables_template
from templates.tables_templates.create_table_temp import create_table
from templates.tables_templates.delete_table_temp import delete_table
from templates.tables_templates.update_table_temp import update_table


templ_dic = {'initial':initial_template,
            'login':login_template,
            'signin':signin_template,
            'main_menu':main_menu_template,
            # Juan David Anexando Opcion de gestion de los platos
            'dishes_management':dishes_management_template,
            'create_dish':create_dish_template,
            'delete_dish':delete_dish_template,
            'update_dish':update_dish_template,
            # Santiago Anexando Opcion de gestion de las mesas
            'menu_tables':menu_tables_template,
            'add_table':create_table,
            'del_table':delete_table,
            'upd_table':update_table
            }


def grid_rows_columns_config(dynamic_frame, ratio):
    columns, rows = dynamic_frame.grid_size()
    for i in range(rows):
        dynamic_frame.grid_rowconfigure(i, weight=ratio)
    for j in range(columns):
        dynamic_frame.grid_columnconfigure(j, weight=ratio)

def destroy_widgets(dynamic_frame):
    for widget in dynamic_frame.winfo_children():
            widget.destroy()

def templ_handler(choice, dynamic_frame):

    destroy_widgets(dynamic_frame)
    grid_rows_columns_config(dynamic_frame, 0)

    temp_chosen = templ_dic[choice]
    temp_chosen(dynamic_frame)

    grid_rows_columns_config(dynamic_frame, 1)