from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import databases.db_tables as tables
import databases.db_dishes as dbdish

def save_order(dynamic_frame, tree_dish, tree_table):
    try:
        option_dish = tree_dish.selection()
        option_table = tree_table.selection()
        if option_dish and option_table:
            answer = messagebox.askokcancel("Advertencia",
                                            "¿Seguro quieres Agregar este pedido?")
            if answer:
                # Funcion para guardar
                utils.template_handler.templ_handler('del_order',
                                                     dynamic_frame)
            else:
                messagebox.showerror('Cancelado',
                                    "No se pudo realizar el proceso")
        else:
            messagebox.showerror('Incompleto',
                                "Seleccione un pedido para Eliminar")
    except Exception:
        messagebox.showerror('Incompleto',
                             "Seleccione un pedido para Eliminar")


def make_order_template(dynamic_frame):
    
    lbl_title = ttk.Label(dynamic_frame,
                          text="Realizar Pedido",
                          font=("default", 12, "bold"))
    lbl_plate_order = ttk.Label(dynamic_frame, text="N. Plato")
    lbl_table_order = ttk.Label(dynamic_frame, text="N. Mesa")


    
    tree_dish = ttk.Treeview(dynamic_frame, columns='Codigo')
    tree_dish.heading('#0', text="Platos")
    
    tree_table = ttk.Treeview(dynamic_frame, columns='Mesa')
    tree_table.heading('#0', text="Mesa")
    tree_table.column('#0', anchor="center", width=(100))
    
    for i in dbdish.db_matrix:
        tree_dish.insert('', "end", values=(i[0],))
    
    for i in tables.tables:
        tree_table.insert('', "end", values=(i[0],))
    
    scrollbar_dish = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_dish.yview)
    scrollbar_table = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_table.yview)
    
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
    tree_dish.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=10)
    tree_table.grid(column=2, row=1, columnspan=2, padx=(15, 0), pady=10)
    scrollbar_table.grid(row=1, column=3, padx=(0, 15), pady=10, sticky="ns")
    scrollbar_dish.grid(row=1, column=1, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
    button_make.grid(column=1, row=5, sticky="w", padx=(10, 0), pady=15)