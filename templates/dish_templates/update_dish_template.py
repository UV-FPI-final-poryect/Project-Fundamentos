from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import data_access_tools.dishes_da as tools_dishes
from templates.dish_templates.save_dish_changes_template import save_dish_changes_template


"""
This module imports libraries such as tkinter, ttk, and messagebox 
for notifications, as well as widgets and functionalities for table
organization within the dynamic_frame. 
Additionally, it imports modules like 'dishes_da' for dish saving and updating.
"""

def warning(dynamic_frame, tree):
    try:
        selected = tree.selection()
        if selected:
            result = messagebox.askokcancel("Confirmación",
                                            "¿Es este el plato que deseas modificar?")
            if result:
                dish_to_update = tree.item(selected)['values']
                save_dish_changes_template(dynamic_frame, dish_to_update)
        else:
            messagebox.showerror('Sin selección', 'Asegurate de haber seleccionado una fila para modificar.')
    except Exception:

        messagebox.showerror('No se pudo completar la acción',
                             'No se ha logrado realizar el proceso de actualización, llama al proveedor para asesoria')


def update_dish_template(dynamic_frame):
    """This is the main template where we configure all widgets within the frame."""
    lbl_title = ttk.Label(dynamic_frame,
                          text="Actualizar plato",
                          font=("default", 12, "bold"))

    tree = ttk.Treeview(dynamic_frame, columns=tools_dishes.dishes_columns(), show="headings", height=9)

    for col in tools_dishes.dishes_columns():
        tree.heading(col, text=col)
        if col == "Nombre":
            tree.column(col, anchor="center", width=120)
            continue
        if col == "Descripción":
            tree.column(col, anchor="center", width=250)
            continue
        tree.column(col, anchor="center", width=55)
    data_base_for_dishes = tools_dishes.list_dishes()
    for row in data_base_for_dishes:
        tree.insert("", "end", values=row)

    scrollbar_y = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)

    button_update = ttk.Button(
        dynamic_frame,
        text="Actualizar",
        style="Accent.TButton",
        command=lambda: warning(dynamic_frame, tree))
    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler('dishes_management', frame))

    lbl_title.grid(column=0, row=0, columnspan=2, pady=10)
    tree.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=10)
    scrollbar_y.grid(row=1, column=2, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=15)
    button_update.grid(column=1, row=2, sticky="w", padx=(10, 0), pady=15)
