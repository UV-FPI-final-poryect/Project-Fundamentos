from tkinter import ttk
from tkinter import messagebox
import re
import data_access_tools.user_auth as tools_users
import utils.template_handler

global user_email
global user_pass


def verify_process():
    global user_email
    global user_pass
    try:
        if (user_email.isspace() or user_email == '' or
                user_pass.isspace() or user_pass == ''):
            raise ValueError
        else:
            user_to_verify = [user_email.lower(),
                              user_pass]
            tools_users.login_user(user_to_verify)
    except ValueError:
        messagebox.showerror('Faltan campos', 'Hay algún camo vacío, por favor verifica.')


def catch_user_email(var):
    global user_email
    pattern = r'[A-Za-z0-9._%+-]+@{1}(gmail|hotmail|yahoo|outlook|correounivalle.edu){1}+\.(com|co){1}'
    if re.fullmatch(pattern, var) is None or len(var) > 50:
        messagebox.showinfo('Correo no valido', 'Verifica que el correo ingresado este sin espacios '
                                                'contenga @, sea partede un dominio válido (gmail, hotmail, yahoo, '
                                                'outlook, correounivalle.edu) y termine con .com o .co')
        user_email = ''
        return False

    user_email = var
    return True


def catch_user_pass(var):
    global user_pass
    if (re.search(r'[a-z]', var) is None or
            re.search(r'[A-Z]', var) is None or
            re.search(r'[0-9]', var) is None or
            re.search(r'[@*$!?\&/]', var) is None or
            re.search(r'[-_.:,;[]{}<>`~=+|\'"]', var) is not None or
            len(var) != 10):
        messagebox.showinfo('Contraseña no valida', 'Verifica que la contraseña ingresada cumpla con:\n'
                                                    '- Al menos una letra minúscula\n'
                                                    '- Al menos una letra mayúscula\n'
                                                    '- Al menos un número\n'
                                                    '- Uno de estos caracteres @*$!?\\&/\n'
                                                    '- No puede contener -_.:,;[]{}<>`~=+|\'"\n'
                                                    '- Longitud exacta de 10 caracteres')
        user_pass = ''
        return False
    user_pass = var
    return True


def login_template(dynamic_frame):
    entry_box_width = 35
    lbl_title = ttk.Label(dynamic_frame,
                          text="Inicio Sesión",
                          font=("default", 12, "bold"))
    lbl_subtitle_email = ttk.Label(dynamic_frame,
                                   text="Email")
    lbl_subtitle_pass = ttk.Label(dynamic_frame,
                                  text="Contraseña")

    entry_email = ttk.Entry(dynamic_frame,
                            width=entry_box_width,
                            validate="focusout",
                            validatecommand=(dynamic_frame.register(catch_user_email), '%P'))
    entry_passw = ttk.Entry(dynamic_frame,
                            width=entry_box_width,
                            validate="focusout",
                            validatecommand=(dynamic_frame.register(catch_user_pass), '%P'),
                            show="*")

    button_login = ttk.Button(dynamic_frame,
                              text="Iniciar Sesión",
                              style="Accent.TButton",
                              command=lambda frame=dynamic_frame:
                              utils.template_handler.templ_handler
                              ('main_menu', frame))
    button_back = ttk.Button(dynamic_frame,
                             text="Atrás",
                             command=lambda: utils.template_handler.templ_handler('initial', dynamic_frame))

    # pendiente funcion que busque en la base de datos y de acceso

    lbl_title.grid(column=0, row=0, columnspan=2, pady=10)
    lbl_subtitle_email.grid(column=0, row=1, columnspan=2, pady=2)
    entry_email.grid(column=0, row=2, columnspan=2, padx=30, pady=2)
    lbl_subtitle_pass.grid(column=0, row=3, columnspan=2, pady=2)
    entry_passw.grid(column=0, row=4, columnspan=2, padx=30, pady=2)
    button_login.grid(column=1, row=5, sticky="w", pady=15)
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
