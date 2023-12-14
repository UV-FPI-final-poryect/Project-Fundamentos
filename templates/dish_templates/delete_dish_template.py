from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import data_access_tools.dishes_da as tools_dishes

"""
This module serves as a template where all the widgets allowing dish
deletion are added to the dynamic_frame.
It utilizes libraries such as 'tkinter' and methods like 'ttk' and 
'messagebox', alongside modules like 'template handler' and 'dishes_da'.
"""


def warning(dynamic_frame, tree):
    """
    This method asks the user to confirm his selected option to be 
    deleted and uses exceptions to avoid program interruption.
    
    Args:
        dynamic_frame (frame): The dynamic frame being configured for
        user interaction.
    """
    try:
        selected = tree.selection()
        if selected:
            result = messagebox.askokcancel("Confirmación",
                                            "¿Deseas elminar este plato?")
            if result:
                dish_to_del = tree.item(selected)['values']
                tools_dishes.erase_dish(dish_to_del[0])
                utils.template_handler.templ_handler('delete_dish', dynamic_frame)
        else:
            messagebox.showerror('Sin selección', 'Asegurate de haber seleccionado una fila para eliminar.')
    except Exception:
        messagebox.showerror('No se pudo completar la acción',
                             'No se ha logrado realizar el proceso de eliminación, llama al proveedor para asesoria')


def delete_dish_template(dynamic_frame):
    """
    This method receives the frame and configures it to display the GUI. 
    GUI 'Remove Dishes'.
    
    Args:
        dynamic_frame (widget): The frame widget to be configured for 
        displaying the 'Eliminar Platos' interface.
    """
    lbl_title = ttk.Label(dynamic_frame,
                          text="Eliminar plato",
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

    button_delete = ttk.Button(dynamic_frame,
                               text="Eliminar",
                               style="Accent.TButton",
                               command=lambda: warning(dynamic_frame, tree))
    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda: utils.template_handler.templ_handler('dishes_management', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=2, pady=10)
    tree.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=10)
    scrollbar_y.grid(row=1, column=2, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=15)
    button_delete.grid(column=1, row=2, sticky="w", padx=(10, 0), pady=15)
