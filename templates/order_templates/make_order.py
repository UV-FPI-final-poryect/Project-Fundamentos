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

    tree_dish = ttk.Treeview(dynamic_frame, columns='Platos', show="headings", height=9)
    tree_dish.column('Platos', anchor="center", width=50)
    tree_dish.heading('Platos', text='N. Platos')

    tree_table = ttk.Treeview(dynamic_frame, columns='Mesa', show="headings", height=9)
    tree_table.column('Mesa', anchor="center", width=50)
    tree_table.heading('Mesa', text='N. Mesa')

    for dish_row in dbdish.db_matrix:
        tree_dish.insert('', "end", values=(dish_row[0],))

    for table_row in tables.tables_reserves:
        tree_table.insert('', "end", values=(table_row[0],))

    scrollbar_dish = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_dish.yview)
    scrollbar_table = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_table.yview)
    tree_dish.configure(yscrollcommand=scrollbar_dish.set)
    tree_table.configure(yscrollcommand=scrollbar_table.set)

    button_make = ttk.Button(dynamic_frame,
                             text="Realizar",
                             style="Accent.TButton",
                             command=lambda: save_order(dynamic_frame,
                                                        tree_dish,
                                                        tree_table))

    button_back = ttk.Button(dynamic_frame, text="Atrás",
                             command=lambda: utils.template_handler. \
                             templ_handler('order_menu', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=4, padx=40, pady=10)
    tree_dish.grid(column=0, row=1, padx=(15, 0), pady=10)
    tree_table.grid(column=2, row=1, padx=(15, 0), pady=10)
    scrollbar_dish.grid(column=1, row=1, padx=(0, 15), pady=10, sticky="ns")
    scrollbar_table.grid(column=3, row=1, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, columnspan=2, sticky="ew", padx=10, pady=15)
    button_make.grid(column=2, row=2, columnspan=2, sticky="ew", padx=10, pady=15)
