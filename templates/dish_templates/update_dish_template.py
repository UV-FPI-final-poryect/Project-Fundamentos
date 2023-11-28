from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import templates.dish_templates.MATRIZ_EJEMPLO as MATRIX
from templates.dish_templates.save_dish_changes_template import save_dish_changes_template


columns_names = ["Código", "Nombre", "Precio", "Descripción", "Disponible"] 

def warning(dynamic_frame, tree):
    result = messagebox.askokcancel("Confirmación",\
        "¿Es este el plato que deseas modificar?")
    if result:
        selected = tree.selection()
        if selected:
            dish_to_update = tree.item(selected)['values']

        save_dish_changes_template(dynamic_frame, dish_to_update)
    else:
        print("La acción fue cancelada.")


def update_dish_template(dynamic_frame):
    lbl_title = ttk.Label(dynamic_frame,
                          text="Actualizar plato",
                          font=("default",12, "bold"))
    
    tree = ttk.Treeview(dynamic_frame, columns=columns_names, show="headings", height=9)
    
    for col in columns_names:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=(len(col)*10))
    for row in MATRIX.matriz_ejemplo:
        tree.insert("", "end", values=row)

    scrollbar_y = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)

    button_update = ttk.Button(
        dynamic_frame,
        text="Actualizar",
        style="Accent.TButton",
        command=lambda :warning(dynamic_frame, tree))
    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler('dishes_management',frame))

    lbl_title.grid(column=0, row=0, columnspan=2, pady=10)
    tree.grid(column=0, row=1, columnspan=2, padx=(15,0), pady=10)
    scrollbar_y.grid(row=1, column=2, padx=(0,15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, sticky="e", padx=(0,10), pady=15)
    button_update.grid(column=1, row=2, sticky="w", padx=(10,0), pady=15)