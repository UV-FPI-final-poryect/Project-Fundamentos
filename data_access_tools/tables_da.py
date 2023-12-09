import databases.db_tables as tables_matriz


def get_matriz():
    return tables_matriz.tables


# def change_format_to_read(userdate, userhour, people):
#
#     caracter = '/', '-', ';'
#     new_date = ''
#     new_hour = ''
#     for i in userdate:  # Creamos un ciclo para recorrer la cadena
#         if i in caracter:  # Si encuentra un caracter distinto, lo cambia
#             new_date += '/'
#             continue
#         new_date += i  # Guardamos en una variable los cambios
#     print(new_date)
#     for j in userhour:  # Creamos un ciclo para recorrer la cadena
#         if j in caracter:
#             new_hour += ':'
#             continue
#         new_hour += j  # Guardamos en una variable los cambios
#
#     new_date = userdate.strftime("%d-%m-%Y")
#     new_hour = userhour.strftime("%H:%M")
#     save_data_table(new_date, new_hour, people)


def save_data_table(date, hour, people):
    new_table = []  # Creamos la lista de la nueva mesa
    for i in range(len(tables_matriz.name_columns)):
        new_table.append(i)  # Agregamos la cantidad de columnas
    tables_matriz.num_tables += 1
    new_index = tables_matriz.num_tables
    new_table[0] = new_index
    new_table[1] = str(date)
    new_table[2] = str(hour)
    new_table[3] = people
    #############//////////////????????????????/////////////
    print(new_table)
    tables_matriz.tables.append(new_table)


def delet_table(index):
    database = get_matriz()  # Llamamos la matriz
    for i in database:  # Recorremos la matriz
        if index == i[0]:  # Buscamos el valor del indice
            tables_matriz.tables.remove(i)  # Eliminamos ese indice


def updat_table(index):
    database = get_matriz()  # Llamamos la matriz
    num_index = index[0] - 1
    for i in database:  # Recorremos la matriz
        if i[0] == num_index:  # Buscamos el valor del indice
            tables_matriz.tables[num_index] = index
            break
