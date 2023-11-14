import tkinter as tk

#   Opcion Registrarse                          1 Pag
def register_template():
    print("Estas en Registro")

#   Opcion Iniciar Sesion                       1 Pag
def login_template():
    print("Inicio de Sesion")

#   Empezar Registrar Usuario                   2 Pag
def register_user(user_name, user_pass):
    user_name = 'Nombre'
    user_pass = 'Contraseña'
    print(user_name + user_pass)

#   Leer Usuario de Inicio de Sesion            3 Pag
def login_user(user_name, user_pass):
        user_name = 'Nombre'
        user_pass = 'Contraseña'
        print(user_name + user_pass)

#   Gestion de Platos                           4 Pag
def dishes_management_template():
    pass

#   Gestion de Mesas                            4 Pag
def table_management_template():
    pass

#   Gestion de Pedidos                          4 Pag
def deliver_management_template():
    pass

#   Cerrar Sesion                               4 Pag
def logout_user():
    pass

#   Ventana Principal de Inicio                 1 Pag
def ventana_1tkinter():
    #   Primera Ventana | Inicio
    ventana_main = tk.Tk()
    ventana_main.title("Restorant SLP")
    ventana_main.geometry("370x330")
    inicio = tk.Label(ventana_main, text = "Mi Restaurante",\
        font = "Helvetica 14")
    #logo
    intro = tk.Label(ventana_main, text = \
        """
        Nuestro restaurante es un lugar donde ofrecemos
        una variedad de platos deliciosos y recursos
        culinarios para el público para satisfacer tus
        necesidades culinarias y hacewrte disfrutar d una
        experiencia gastronómica excepcional.
        """)
    button_signin = tk.Button(ventana_main, text = "Registrarse",\
        font = "Helvetica 11", command = lambda: register_template())
    button_logout = tk.Button(ventana_main, text = "Iniciar Sesion",\
        font = "Helvetica 11", command = lambda: login_template())
    inicio.pack()
    intro.pack()
    button_signin.pack()
    button_logout.pack()
    ventana_main.mainloop()

#   Ventana de Registro                         2 Pag
def ventana_2tkinter():
    #   Segunda  Ventana | Registro
    ventana_1 = tk.Tk()
    ventana_1.title("Registro")
    ventana_1.geometry("370x330")
    inicio = tk.Label(ventana_1, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    lbl1 = tk.Label(ventana_1, text = "Registrarse",\
        font = "Helvetica 11")
    lbl2 = tk.Label(ventana_1, text = "Email")
    lbl3 = tk.Label(ventana_1, text = "Contraseña")
    lbl4 = tk.Label(ventana_1, text = "Confirmar Contraseña")
    nemail = tk.Entry(ventana_1)
    npassw = tk.Entry(ventana_1)
    npassw1 = tk.Entry(ventana_1)
    button_loged = tk.Button(ventana_1, text = "Registrar",\
        font = "Helvetica 10", command = lambda: register_user())
    inicio.pack()
    lbl1.pack()
    lbl2.pack()
    nemail.pack()
    lbl3.pack()
    npassw.pack()
    lbl4.pack()
    npassw1.pack()
    button_loged.pack()
    ventana_1.mainloop()

#   Ventana de Inicio Sesion                    3 Pag
def ventana_3tkinter():
    #   Tercera  Ventana | Inicio Sesion
    ventana_2 = tk.Tk()
    ventana_2.title("Registro")
    ventana_2.geometry("370x330")
    inicio = tk.Label(ventana_2, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    lbl1 = tk.Label(ventana_2, text = "Inicio Sesión",\
        font = "Helvetica 11")
    lbl2 = tk.Label(ventana_2, text = "Email")
    lbl3 = tk.Label(ventana_2, text = "Contraseña")
    nemail = tk.Entry(ventana_2)
    npassw = tk.Entry(ventana_2)
    button_loged = tk.Button(ventana_2, text = "Iniciar Sesión",\
        font = "Helvetica 10", command = lambda: login_user())
    inicio.pack()
    lbl1.pack()
    lbl2.pack()
    nemail.pack()
    lbl3.pack()
    npassw.pack()
    button_loged.pack()
    ventana_2.mainloop()

#   Ventana de Menu Principal                   4 Pag
def ventana_4tkinter():
    #   Cuarta  Ventana | Main Menu
    ventana_3 = tk.Tk()
    ventana_3.title("Menu Main")
    ventana_3.geometry("370x330")
    inicio = tk.Label(ventana_3, text = "Mi Restaurante",\
        font = "Helvetica 14")
    # logo
    lbl1 = tk.Label(ventana_3, text = "Bienvenido",\
        font = "Helvetica 11")
    lbl2 = tk.Label(ventana_3, text = "Contraseña")
    button_gest_dish = tk.Button(ventana_3, text = "Gestion Platos",\
        font = "Helvetica 10", command = lambda: \
            dishes_management_template())
    button_gest_table = tk.Button(ventana_3, text = "Gestion Mesas",\
        font = "Helvetica 10", command = lambda: \
            table_management_template())
    button_order = tk.Button(ventana_3, text = "Gestion Pedidos",\
        font = "Helvetica 10", command = lambda: \
            deliver_management_template())
    button_close_ss = tk.Button(ventana_3, text = "Cerrar Sesión",\
        font = "Helvetica 10", command = lambda: logout_user())
    inicio.pack()
    lbl1.pack()
    button_gest_dish.pack()
    button_gest_table.pack()
    button_order.pack()
    button_close_ss.pack()
    ventana_3.mainloop()


if __name__ == '__main__':
    ventana_1tkinter()