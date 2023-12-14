from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import data_access_tools.orders_da as orders_da


"""
This module serves as a template where all the widgets allowing order
deletion are added to the dynamic_frame.
It utilizes libraries such as 'tkinter' and methods like 'ttk' and 
'messagebox', alongside modules like 'template handler' and 'orders_da'.
"""


def warning(dynamic_frame, tree_order):
    """
    This method asks the user to confirm his selected option to be 
    deleted and uses exceptions to avoid program interruption.
    
    Params:
        dynamic_frame (frame): The dynamic frame being configured for
        user interaction.
        tree_order (treeview - widget): the table with the order items.
    """
    try:
        option = tree_order.selection()
        if option:
            answer = messagebox.askokcancel("Advertencia",
                                            "¿Seguro quieres ELIMINAR este"
                                            " pedido de forma permanente?")
            if answer:
                del_order = tree_order.item(option)["values"]  # Guardamos los valores de la seleccion escogida
                orders_da.delete_order(del_order[0])
                utils.template_handler.templ_handler('del_order',
                                                     dynamic_frame)
            else:
                messagebox.showerror('Cancelado',
                                     "Se ha cancelado el proceso")
        else:
            messagebox.showerror('Incompleto',
                                 "Seleccione un pedido para Eliminar")
    except Exception:
        messagebox.showerror('No se pudo completar la acción', 'No se ha logrado realizar el proceso '
                                                               'de eliminación llama al proveedor para asesoria')


def delete_order_template(dynamic_frame):
    #Generates the structure for the order delete template
    lbl_title = ttk.Label(dynamic_frame,
                          text="Eliminar Pedido",
                          font=("default", 12, "bold"))

    tree_order = ttk.Treeview(dynamic_frame, columns=orders_da.get_orders_columns(),
                              show="headings", height=9)

    for col in orders_da.get_orders_columns():
        tree_order.heading(col, text=col)
        tree_order.column(col, anchor="center", width=55)
    data_base_for_order = orders_da.list_orders()
    for row in data_base_for_order:
        tree_order.insert("", "end", values=row)

    scrollbar_y = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_order.yview)
    tree_order.configure(yscrollcommand=scrollbar_y.set)

    button_del = ttk.Button(
        dynamic_frame,
        text="Eliminar",
        style="Accent.TButton",
        command=lambda: warning(dynamic_frame, tree_order))
    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler('order_menu', frame))

    lbl_title.grid(column=0, row=0, columnspan=2, pady=10)
    tree_order.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=10)
    scrollbar_y.grid(row=1, column=2, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=15)
    button_del.grid(column=1, row=2, sticky="w", padx=(10, 0), pady=15)
