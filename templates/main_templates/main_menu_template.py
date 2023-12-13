from tkinter import ttk
import utils.template_handler
import data_access_tools.user_auth as tools_users


def logout_action(dynamic_frame):
    tools_users.logout_user()
    print(tools_users.token)
    utils.template_handler.templ_handler('initial', dynamic_frame)


def main_menu_template(dynamic_frame):
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
