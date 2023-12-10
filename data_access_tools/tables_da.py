import databases.db_tables as tables_matriz


def get_matriz():
    return tables_matriz.tables


def save_data_table(date, hour, people):
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


def delet_table(index):
    database = get_matriz()
    for i in database:
        if index == i[0]:
            tables_matriz.tables.remove(i)


def updat_table(index):
    database = get_matriz()
    num_index = index[0] - 1
    for i in database:
        if i[0] == num_index:
            tables_matriz.tables[num_index] = index
            break
