from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import utils.template_handler
import templates.Tables as matriz

columns_names = ["Mesa", "Date", "Hour", "N. People"] 

def warning(dynamic_frame):
    resultado = messagebox.askokcancel("Warning",\
        "Are you sure you want to delete this table permanently?")
    if resultado:
        utils.template_handler.templ_handler('menu_tables', dynamic_frame)
    else:
        print("La acción fue cancelada.")


def delete_table(dynamic_frame):

    lbl_title = ttk.Label(dynamic_frame, text="Mesas",
                        font=("default", 12, "bold"))

    tree = ttk.Treeview(dynamic_frame, columns=columns_names, show="headings", height=9)
    
    for col in columns_names:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=(len(col)*10))
    for row in matriz.mesas:
        tree.insert("", "end", values=row)
    
    scrollbar_y = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)

    button_del = ttk.Button(dynamic_frame, text = "Delete", 
                            style="Accent.TButton",
                        command=lambda:warning(dynamic_frame))
    button_back = ttk.Button(dynamic_frame, text = "Back",
                        command=lambda frame=dynamic_frame :\
            utils.template_handler.templ_handler('menu_tables', frame))
    
    lbl_title.grid(column=1, row=0, padx=20, pady=10)
    tree.grid(column=0, row=1, columnspan=2, padx=(15,0), pady=10)
    scrollbar_y.grid(row=1, column=2, padx=(0,15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, padx=20, pady=10)
    button_del.grid(column=3, row=2, padx=20, pady=10)
