from tkinter import messagebox
import data_access_tools.user_auth as tools_users

from templates.main_templates.initial_template import initial_template
from templates.main_templates.login_template import login_template
from templates.main_templates.signin_template import signin_template
from templates.main_templates.main_menu_template import main_menu_template
from templates.dish_templates.dishes_management_template import dishes_management_template
from templates.dish_templates.create_dish_template import create_dish_template
from templates.dish_templates.delete_dish_template import delete_dish_template
from templates.dish_templates.update_dish_template import update_dish_template
from templates.tables_templates.menu_tables import menu_tables_template
from templates.tables_templates.create_table_temp import create_table
from templates.tables_templates.delete_table_temp import delete_table
from templates.tables_templates.update_table_temp import update_table
from templates.order_templates.order_menu import menu_order_template
from templates.order_templates.make_order import make_order_template
from templates.order_templates.delete_order import delete_order_template
from templates.order_templates.update_order import update_order_template


"""
This module retrieves the required template by utilizing two
dictionaries within all imported template modules.
The first dictionary comprises modules for freely accessible templates,
such as user verification, registration, and validation.
The second dictionary holds modules for templates that can be accessed
through functions if the user has the required permissions.

The module's purpose is to locate and retrieve the specified template
from these dictionaries as per the user's access level.

Usage:
- Utilize this module to find and access the necessary template based
on user permissions and requirements.
- The dictionaries categorize templates into freely accessible and
function-accessible categories for ease of retrieval.
"""


NORMAL_ACCESS_TEMPL_DIC = {'initial': initial_template,
                           'login': login_template,
                           'signin': signin_template}

TEMPL_DIC = {'main_menu': main_menu_template,
             'dishes_management': dishes_management_template,
             'create_dish': create_dish_template,
             'delete_dish': delete_dish_template,
             'update_dish': update_dish_template,
             'menu_tables': menu_tables_template,
             'add_table': create_table,
             'del_table': delete_table,
             'upd_table': update_table,
             'order_menu': menu_order_template,
             'make_order': make_order_template,
             'del_order': delete_order_template,
             'upd_order': update_order_template
             }


def grid_rows_columns_config(dynamic_frame, ratio):
    """
    This method configures the rows and columns within a frame to
    modify their proportion.
    """
    columns, rows = dynamic_frame.grid_size()
    for i in range(rows):
        dynamic_frame.grid_rowconfigure(i, weight=ratio)
    for j in range(columns):
        dynamic_frame.grid_columnconfigure(j, weight=ratio)


def destroy_widgets(dynamic_frame):
    """This method removes all widgets from the frame."""
    for widget in dynamic_frame.winfo_children():
        widget.destroy()


def templ_handler(choice, dynamic_frame):
    """
    Selects the template from the dictionary.

    Args:
        choice (str): The key of the dictionary to be accessed.
        dynamic_frame (widget): The frame object to receive the 
        selected template.
    """
    destroy_widgets(dynamic_frame)
    grid_rows_columns_config(dynamic_frame, 0)
    # Check if the key is in the dictionary.
    if choice in TEMPL_DIC:
        # Check if the user has permissions
        if tools_users.token:
            temp_chosen = TEMPL_DIC[choice]
            temp_chosen(dynamic_frame)
        else:
            messagebox.showerror('Faltan permisos',
                                 'No tiene autorización para realizar esta'
                                 'acción, autentiquese primero.')
            temp_chosen = NORMAL_ACCESS_TEMPL_DIC['initial']
            temp_chosen(dynamic_frame)
    else:
        temp_chosen = NORMAL_ACCESS_TEMPL_DIC[choice]
        temp_chosen(dynamic_frame)

    grid_rows_columns_config(dynamic_frame, 1)
