from tkinter import ttk
from tkinter import messagebox
import utils.template_handler


def save_order():
    pass


def make_order_template(dynamic_frame):
    
    lbl_title = ttk.Label(dynamic_frame,
                          text="Realizar Pedido",
                          font=("default", 12, "bold"))
    lbl_plate_order = ttk.Label(dynamic_frame, text="N. Plato")
    lbl_table_order = ttk.Label(dynamic_frame, text="N. Mesa")


    
    button_make = ttk.Button(dynamic_frame,
                            text="Realizar",
                            style="Accent.TButton",
                            command=lambda: save_order(dynamic_frame))

    button_back = ttk.Button(dynamic_frame, text="Atrás",
                             command=lambda: utils.template_handler.\
                                 templ_handler('order_menu', dynamic_frame))


    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_plate_order.grid(column=0, row=1, sticky="w", padx=(20, 0), pady=2)
    lbl_table_order.grid(column=1, row=1, sticky="w", padx=(10, 0), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
    button_make.grid(column=1, row=5, sticky="w", padx=(10, 0), pady=15)