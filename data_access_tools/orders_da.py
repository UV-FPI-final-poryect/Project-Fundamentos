from tkinter import messagebox
import databases.db_orders as orders
import data_access_tools.user_auth as tools_users


def restricted():
    messagebox.showerror('Faltan permisos', 'No tiene autorización para realizar esta acción, autentiquese primero')


def get_orders_columns():
    if tools_users.token:
        return orders.title_orders
    else:
        restricted()


def list_orders():
    if tools_users.token:
        return orders.orders
    else:
        restricted()


def add_order(new_order):
    if tools_users.token:
        orders.num_order += 1
        order_position = orders.num_order
        new_order[0] = order_position
        orders.orders.append(new_order)
    else:
        restricted()


def actualize_order(upd_order):
    if tools_users.token:
        database = list_orders()
        order_id = upd_order[0]
        for row in range(len(database)):
            if database[row][0] == order_id:
                orders.orders[row] = upd_order
                break
    else:
        restricted()


def delete_order(index):
    if tools_users.token:
        database = list_orders()
        for i in database:
            if index == i[0]:
                orders.orders.remove(i)
    else:
        restricted()
