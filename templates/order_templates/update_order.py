from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import databases.db_orders as order
#import templates.order_templates.order_upd as change


def warning(dynamic_frame, tree_order):
    try:
        option = tree_order.selection()
        if option:
            answer = messagebox.askokcancel("Advertencia",
                                            "¿Seguro quieres Actualizar este pedido?")
            if answer:
                upd_order = tree_order.item(option)["values"]  # Guardamos los valores de la seleccion escogida
                #change.update_order(dynamic_frame, upd_order[0])
                # Pensando que funcion implementar, en local tengo combobox
                utils.template_handler.templ_handler('upd_order',
                                                     dynamic_frame)
            else:
                messagebox.showerror('Cancelado',
                                    "No se pudo realizar el proceso")
        else:
            messagebox.showerror('Incompleto',
                             "Seleccione un pedido para Actualizar")
    except Exception:
        messagebox.showerror('Incompleto',
                             "Seleccione un pedido para Actualizar")


def update_order_template(dynamic_frame):
    lbl_title = ttk.Label(dynamic_frame,
                        text="Actualizar Pedido",
                        font=("default",12, "bold"))

    tree_order = ttk.Treeview(dynamic_frame, columns=order.title_orders,
                        show="headings", height=9)

    for col in order.title_orders:
        tree_order.heading(col, text=col)
        tree_order.column(col, anchor="center", width=55)
    data_base_for_order = order.orders
    for row in data_base_for_order:
        tree_order.insert("", "end", values=row)

    scrollbar_y = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_order.yview)
    tree_order.configure(yscrollcommand=scrollbar_y.set)
    
    button_del = ttk.Button(
        dynamic_frame,
        text="Actualizar",
        style="Accent.TButton",
        command=lambda :warning(dynamic_frame, tree_order))
    button_back = ttk.Button(
        dynamic_frame,
        text="Atrás",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler('order_menu',frame))

    lbl_title.grid(column=0, row=0, columnspan=2, pady=10)
    tree_order.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=10)
    scrollbar_y.grid(row=1, column=2, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=15)
    button_del.grid(column=1, row=2, sticky="w", padx=(10, 0), pady=15)