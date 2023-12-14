from tkinter import messagebox
import databases.db_tables as tables_matriz
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


def tables_columns():
    if tools_users.token:
        return tables_matriz.name_columns
    else:
        restricted()


def get_total_tables():
    if tools_users.token:
        return tables_matriz.total_tables
    else:
        restricted()


def get_matriz():
    if tools_users.token:
        return tables_matriz.tables_reserves
    else:
        restricted()


def save_data_table(date, hour, people):
    if tools_users.token:
        new_table = []
        for i in range(len(tables_matriz.name_columns)):
            new_table.append(i)
        tables_matriz.id_tables_reserves += 1
        new_index = tables_matriz.id_tables_reserves
        new_table[0] = new_index
        new_table[1] = str(date)
        new_table[2] = str(hour)
        new_table[3] = people
        tables_matriz.tables_reserves.append(new_table)
    else:
        restricted()


def delet_table(index):
    if tools_users.token:
        database = get_matriz()
        for i in database:
            if index == i[0]:
                tables_matriz.tables_reserves.remove(i)
    else:
        restricted()


def updat_table(upd_table):
    if tools_users.token:
        database = get_matriz()
        num_index = upd_table[0]
        for row in range(len(database)):
            if database[row][0] == num_index:
                tables_matriz.tables_reserves[row] = upd_table
                break
    else:
        restricted()
