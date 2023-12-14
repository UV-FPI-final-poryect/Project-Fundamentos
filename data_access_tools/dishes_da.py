from tkinter import messagebox
import databases.db_dishes as dishes
import data_access_tools.user_auth as tools_users


"""
This module supports data management operations such as saving, updating,
and deleting entries in the dish management database.

It imports libraries like tkinter and its methods, alongside custom
modules such as the general dish database module and the user 
verification check module.
"""


def restricted():
    messagebox.showerror('Faltan permisos', 'No tiene autorización para realizar esta acción, autentiquese primero')


def dishes_columns():
    if tools_users.token:
        return dishes.COLUMNS_NAMES
    else:
        restricted()


def add_dish(dish_to_create):
    """
    This method positions the received elements based on the
    database before appending them.

    Args:
        dish_to_create (list): The elements to be added to the
        general database.
    """
    if tools_users.token:
        new_dish = []
        for i in range(len(dishes.COLUMNS_NAMES)):
            new_dish.append(i)
        dishes.db_id += 1
        new_dish_id = dishes.db_id
        new_dish[0] = new_dish_id
        new_dish[1] = dish_to_create[1]
        new_dish[2] = dish_to_create[2]
        new_dish[3] = dish_to_create[3]
        new_dish[4] = dish_to_create[4]
        dishes.db_matrix.append(new_dish)
    else:
        restricted()


def list_dishes():
    if tools_users.token:
        return dishes.db_matrix
    else:
        restricted()


def actualize_dish(dish_to_update):
    """
    This method arranges the received elements from the database to 
    update them in the array.

    Args:
        dish_to_create (list): Elements intended for updating the 
        general database.
    """
    if tools_users.token:
        database = list_dishes()
        list_index = dish_to_update[0]
        for row in range(len(database)):
            if database[row][0] == list_index:
                dishes.db_matrix[row] = dish_to_update
                break
    else:
        restricted()


def erase_dish(dish_id):
    """
    This method arranges the received elements from the database to 
    erase them in the array.

    Args:
    dish_id (posicion): Elements intended for delete the 
    general database.
    """
    if tools_users.token:
        database = list_dishes()
        for row in database:
            if row[0] == dish_id:
                dishes.db_matrix.remove(row)
                break
    else:
        restricted()
