from tkinter import messagebox
import databases.db_dishes as dishes
import data_access_tools.user_auth as tools_users


def restricted():
    messagebox.showerror('Faltan permisos', 'No tiene autorización para realizar esta acción, autentiquese primero')


def add_dish(dish_to_create):
    if tools_users.token:
        dishes.db_id += 1
        new_dish_id = dishes.db_id
        dish_to_create[0] = new_dish_id
        dishes.db_matrix.append(dish_to_create)
    else:
        restricted()


def list_dishes():
    if tools_users.token:
        return dishes.db_matrix
    else:
        restricted()


def actualize_dish(dish_to_update):
    if tools_users.token:
        database = list_dishes()
        list_index = dish_to_update[0]-1
        for row in database:
            if row[0] == list_index:
                dishes.db_matrix[list_index] = dish_to_update
                break
    else:
        restricted()


def erase_dish(dish_id):
    if tools_users.token:
        database = list_dishes()
        for row in database:
            if row[0] == dish_id:
                dishes.db_matrix.remove(row)
                break
    else:
        restricted()
    
    