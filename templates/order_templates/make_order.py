from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import data_access_tools.orders_da as orders_da
import databases.db_tables as tables
import databases.db_dishes as dbdish


"""
This module configures the order creation template by modifying the 
'dynamic_frame'.
It imports libraries such as 'tkinter'-'ttk', the 'orders_da'
module for calling methods that assist in dish creation and updates,
and the 'template_handler' module for configuring the frame.
"""


def check_order(dynamic_frame, tree_dish, tree_table):
    """
    This method prompts the user to confirm their selected option and
    utilizes exceptions to prevent program interruption.

    Args:
        dynamic_frame (frame - widget): The dynamic frame being configured 
        for user interaction.
        tree_dish (treeview - widget): The table with the dish items.
        tree_table (treeview - widget): the table with the table items.
    """
    try:
        option_dish = tree_dish.selection()
        option_table = tree_table.selection()
        if option_dish and option_table:
            answer = messagebox.askokcancel("Advertencia",
                                            "¿Seguro quieres Agregar este pedido?")
            if answer:
                dish = tree_dish.item(option_dish)['values']
                table = tree_table.item(option_table)["values"]
                save_order(dish[0], table[0])
                utils.template_handler.templ_handler('order_menu',
                                                     dynamic_frame)
            else:
                messagebox.showerror('Cancelado',
                                     "No se pudo realizar el proceso")
        else:
            messagebox.showerror('Incompleto',
                                 "Asegurate de haber seleccionado tanto mesa como plato")
    except Exception:
        messagebox.showerror('No se pudo completar la acción', 'No se ha logrado realizar el proceso '
                                                               'de agregación llama al proveedor para asesoria')


def save_order(dish, table):
    #Once the check order is ok, creates a list with the desired elements
    #that are going to append in the database
    new_order = []
    new_order.append(0)
    new_order.append('Mesa')
    new_order.append(table)
    new_order.append("Plato")
    new_order.append(dish)
    orders_da.add_order(new_order)


def make_order_template(dynamic_frame):
    #Generates the structure for the order creation template
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
        if dish_row[4] == 'Si':
            tree_dish.insert('', "end", values=(dish_row[0],))

    for table_row in range(tables.total_tables):
        tree_table.insert('', "end", values=[table_row + 1])

    scrollbar_dish = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_dish.yview)
    scrollbar_table = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_table.yview)
    tree_dish.configure(yscrollcommand=scrollbar_dish.set)
    tree_table.configure(yscrollcommand=scrollbar_table.set)

    button_make = ttk.Button(dynamic_frame,
                             text="Realizar",
                             style="Accent.TButton",
                             command=lambda: check_order(dynamic_frame,
                                                         tree_dish,
                                                         tree_table))

    button_back = ttk.Button(dynamic_frame, text="Atrás",
                             command=lambda: utils.template_handler.
                             templ_handler('order_menu', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=4, padx=40, pady=10)
    tree_dish.grid(column=0, row=1, padx=(15, 0), pady=10)
    tree_table.grid(column=2, row=1, padx=(15, 0), pady=10)
    scrollbar_dish.grid(column=1, row=1, padx=(0, 15), pady=10, sticky="ns")
    scrollbar_table.grid(column=3, row=1, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, columnspan=2, sticky="ew", padx=10, pady=15)
    button_make.grid(column=2, row=2, columnspan=2, sticky="ew", padx=10, pady=15)
