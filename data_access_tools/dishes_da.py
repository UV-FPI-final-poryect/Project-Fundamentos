
import databases.db_dishes as db_dishes


def read_dishes():
    return db_dishes.db_matrix

def delete_dish(index_dish_to_del):
    database = read_dishes()

    for row in database:
        if row[0] == index_dish_to_del:
            print(row)
            break

    
    db_dishes.db_matrix.remove(row)