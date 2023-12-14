from tkinter import messagebox
import databases.db_orders as orders
import data_access_tools.user_auth as tools_users

"""
This module supports data management operations such as saving,
updating, and deleting entries in the tables management database.

It imports libraries like tkinter and its methods, alongside custom
modules such as the general table database module and the user 
verification check module.

"""
def restricted():
    messagebox.showerror('Faltan permisos',
                         'No tiene autorización para realizar esta '
                         'acción, autentiquese primero')


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
    """
    This method positions the received elements based on the
    database before appending them.

    Args:
        new_order (list): The elements to be added to the
        general database.
    """
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
