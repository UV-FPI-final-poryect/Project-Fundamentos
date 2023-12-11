from tkinter import ttk

import utils.template_handler


def menu_order_template(dynamic_frame):
    lbl_title = ttk.Label(dynamic_frame, text="Gestión de Pedidos",
                          font=("default", 12, "bold"))

    button_make_order = ttk.Button(dynamic_frame, text="Realizar",
                                  command=lambda: utils.template_handler.templ_handler('make_order', dynamic_frame))
    button_del_order = ttk.Button(dynamic_frame, text="Eliminar",
                                  command=lambda: utils.template_handler.templ_handler('del_order', dynamic_frame))
    button_upd_order = ttk.Button(dynamic_frame, text="Actualizar",
                                  command=lambda: utils.template_handler.templ_handler('upd_order', dynamic_frame))
    button_back = ttk.Button(dynamic_frame, text="Atrás",
                             style="Accent.TButton",
                             command=lambda: utils.template_handler.templ_handler('main_menu', dynamic_frame))

    lbl_title.grid(column=0, row=0, padx=50, pady=10)
    button_make_order.grid(column=0, row=1, pady=5)
    button_del_order.grid(column=0, row=2, pady=5)
    button_upd_order.grid(column=0, row=3, pady=5)
    button_back.grid(column=0, row=4, pady=(15, 20))

