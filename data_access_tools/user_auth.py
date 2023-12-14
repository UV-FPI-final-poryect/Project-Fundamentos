import hashlib

token = False


"""
This module imports the 'hashlib' library and implements methods
for searching, registering, and confirming users.
It utilizes the library to encrypt passwords and store them in a text file.
"""


def search_user(user_to_verify):
    # Reads the user from the text file to verify if it exists.
    file_regis = open(r"../databases/registro_inicio.txt", "r")
    users_list = file_regis.read().splitlines()
    for user_row in users_list:
        splitted_user_row = user_row.split(",")
        if user_to_verify[0] == splitted_user_row[0]:
            return splitted_user_row
    return None


def signin_user(user_to_create):
    # Checks if the user exists to create it if not registered.
    if search_user(user_to_create) is None:
        encode_pass = hashlib.sha256(user_to_create[1].encode("utf-8"))
        user_row = user_to_create[0] + ',' + user_to_create[1] + "\n"
        file_regis = open(r"../databases/registro_inicio.txt", "a")
        file_regis.write(user_row)
        file_regis.close()
        file_pass = open(r"../databases/password.txt", "a")
        file_pass.write(encode_pass.hexdigest() + "\n")
        file_pass.close()
    else:
        raise FileExistsError


def login_user(user_to_verify):
    global token
    user = search_user(user_to_verify)
    if user is not None and user[1] == user_to_verify[1]:
        token = True
    else:
        raise FileNotFoundError


def logout_user():
    global token
    token = False
