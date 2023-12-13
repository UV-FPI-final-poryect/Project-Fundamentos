from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import databases.db_tables as tables
import databases.db_dishes as dbdish
import databases.db_orders as order
import data_access_tools.user_auth as tools_users


def restricted():
    messagebox.showerror('Faltan permisos',
                         'No tiene autorización para realizar esta acción, autentiquese primero')


def check_order(dynamic_frame, tree_dish, tree_table):
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
                                 "Seleccione un pedido para Eliminar")
    except Exception:
        messagebox.showerror('Incompleto',
                             "Seleccione un pedido para Eliminar")


def save_order(dish, table):
    new_order = []
    new_order.append(0)
    new_order.append('Mesa')
    new_order.append(table)
    new_order.append("Plato")
    new_order.append(dish)
    add_order(new_order)


def actualize_order(upd_order):
    database = order.orders
    list_index = upd_order[0] - 1
    for row in database:
        if row[0] == list_index:
            order.orders[list_index] = upd_order
            break


def add_order(new_order):
    if tools_users.token:
        order.num_order += 1
        order_position = order.num_order
        new_order[0] = order_position
        order.orders.append(new_order)
    else:
        restricted()


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
                             command=lambda: utils.template_handler. \
                             templ_handler('order_menu', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=4, padx=40, pady=10)
    tree_dish.grid(column=0, row=1, padx=(15, 0), pady=10)
    tree_table.grid(column=2, row=1, padx=(15, 0), pady=10)
    scrollbar_dish.grid(column=1, row=1, padx=(0, 15), pady=10, sticky="ns")
    scrollbar_table.grid(column=3, row=1, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, columnspan=2, sticky="ew", padx=10, pady=15)
    button_make.grid(column=2, row=2, columnspan=2, sticky="ew", padx=10, pady=15)
