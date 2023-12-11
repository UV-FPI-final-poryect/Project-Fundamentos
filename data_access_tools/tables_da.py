from tkinter import messagebox
import databases.db_tables as tables_matriz
import data_access_tools.user_auth as tools_users


def restricted():
    messagebox.showerror('Faltan permisos', 'No tiene autorización para realizar esta acción, autentiquese primero')


def get_matriz():
    if tools_users.token:
        return tables_matriz.tables
    else:
        restricted()


def save_data_table(date, hour, people):
    if tools_users.token:
        new_table = []
        for i in range(len(tables_matriz.name_columns)):
            new_table.append(i)
        tables_matriz.num_tables += 1
        new_index = tables_matriz.num_tables
        new_table[0] = new_index
        new_table[1] = str(date)
        new_table[2] = str(hour)
        new_table[3] = people
        tables_matriz.tables.append(new_table)
    else:
        restricted()


def delet_table(index):
    if tools_users.token:
        database = get_matriz()
        for i in database:
            if index == i[0]:
                tables_matriz.tables.remove(i)
    else:
        restricted()


def updat_table(index):
    if tools_users.token:
        database = get_matriz()
        num_index = index[0] - 1
        for i in database:
            if i[0] == num_index:
                tables_matriz.tables[num_index] = index
                break
    else:
        restricted()
