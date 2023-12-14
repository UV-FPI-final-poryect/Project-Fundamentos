from tkinter import ttk
import utils.template_handler
import data_access_tools.user_auth as tools_users


"""
This template displays the menu where the user can access to the management
options and log out.

Imports:
- 'ttk' module from the 'tkinter' library for creating the Graphical
User Interface (GUI).
- 'user_auth' is the module which manage the user credentials.
- 'templ_handler' method from the 'template_handler' module.

Purpose:
- Generates the main menu template asigned to the dynamic_frame.
- Utilizes 'ttk' for creating graphical elements in the GUI.
- Implements 'templ_handler' for handling the templates in the application.
- Shows the management and log out options
"""


def logout_action(dynamic_frame):
    #This function allow the user to log out whenever he/she wants
    tools_users.logout_user()
    print(tools_users.token)
    utils.template_handler.templ_handler('initial', dynamic_frame)


def main_menu_template(dynamic_frame):
    #Generates the structure for the main menu template
    lbl_title = ttk.Label(dynamic_frame,
                          text="Bienvenido",
                          font=("default", 12, "bold"))

    button_dish_option = ttk.Button(dynamic_frame,
                                    text="Gestión Platos",
                                    command=lambda: utils.template_handler.templ_handler('dishes_management',
                                                                                         dynamic_frame))
    button_reserve_table_option = ttk.Button(dynamic_frame,
                                             text="Gestión Mesas",
                                             command=lambda: utils.template_handler.templ_handler('menu_tables',
                                                                                                  dynamic_frame))
    button_order_option = ttk.Button(dynamic_frame,
                                     text="Gestión Pedidos",
                                     command=lambda: utils.template_handler.templ_handler('order_menu',
                                                                                          dynamic_frame))
    
    button_logout = ttk.Button(dynamic_frame,
                               text="Cerrar Sesión",
                               style="Accent.TButton",
                               command=lambda: logout_action(dynamic_frame))

    lbl_title.grid(column=0, row=0, pady=10)
    button_dish_option.grid(column=0, row=1, padx=50, pady=5)
    button_reserve_table_option.grid(column=0, row=2, pady=5)
    button_order_option.grid(column=0, row=3, pady=5)
    button_logout.grid(column=0, row=4, pady=(15, 20))
