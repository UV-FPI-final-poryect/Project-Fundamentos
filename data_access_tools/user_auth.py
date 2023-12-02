import hashlib

token = False
def signin_user(user_name, user_pass):
    encode_pass = hashlib.sha256(user_pass.encode("utf-8"))
    user_row = user_name + ',' + encode_pass.hexdigest() + "\n"
    File_object = open(r"/content/drive/MyDrive/Proyecto final FPI/user.txt","a")
    File_object.write(user_row)
    File_object.close()

    file1 = open(r"/content/drive/MyDrive/Proyecto final FPI/user.txt","r")
    print("Output of Readlines after appending")
    print(file1.read().splitlines())
    print()
    file1.close()


def login_user(user_name, user_pass):
    print(user_name)
    file1 = open(r"/content/drive/MyDrive/Proyecto final FPI/user.txt","r")
    print("Output of Readlines after reading")
    users_list = file1.read().splitlines()
    user_matrix = []
    print(users_list)
    print()
    for user_row in users_list:
        splited_row = user_row.split(",")
        user_matrix.append(splited_row)

    print(user_matrix)
    print()
    file1.close()

def logout_user():
    print("chao")