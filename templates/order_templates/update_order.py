from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import data_access_tools.user_auth as tools_users


def warning(dynamic_frame):
    pass

def update_order_template(dynamic_frame):
    lbl_title = ttk.Label(dynamic_frame,
                          text="Pedidos",
                          font=("default", 12, "bold"))    
    
    #tree = ttk.Treeview(dynamic_frame, columns=tables.name_columns,
    #                   show="headings", height=9)
    
    # scrollbar_y = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree.yview)
    # tree.configure(yscrollcommand=scrollbar_y.set)
    
    button_upd = ttk.Button(dynamic_frame,
                            text="Actualizar",
                            style="Accent.TButton",
                            command=lambda: warning(dynamic_frame))

    button_back = ttk.Button(dynamic_frame, text="Atrás",
                            command=lambda: utils.template_handler.\
                            templ_handler('order_menu', dynamic_frame))


    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    # tree.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=10)
    # scrollbar_y.grid(row=1, column=2, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
    button_upd.grid(column=1, row=5, sticky="w", padx=(10, 0), pady=15)