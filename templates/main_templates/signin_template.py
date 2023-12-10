from tkinter import ttk
from tkinter import messagebox
import re
import utils.template_handler
import data_access_tools.user_auth as tools_users

user_email = ''
user_pass = ''
user_confirm_pass = ''


def warning(dynamic_frame):
    try:
        result = messagebox.askokcancel("Confirmación", "¿Son correctos los datos que ingresaste?")
        if result:
            save_process()
            utils.template_handler.templ_handler('initial', dynamic_frame)
    except FileExistsError:
        messagebox.showerror('El usuario ya existe', 'El usuario ya se encuentra registrado en la base'
                                                     'de datos.')
    except ValueError:
        messagebox.showerror('Faltan campos', 'Existen campos que no cumplen con las condiciones, verificalos.')
    except Exception:
        messagebox.showerror('No se pudo completar la acción', 'No se ha logrado realizar el proceso '
                                                               'de registro, llama al proveedor para asesoria.')


def save_process():
    global user_email
    global user_pass
    global user_confirm_pass
    if (user_email.isspace() or user_email == '' or
            user_pass.isspace() or user_pass == '' or
            user_confirm_pass.isspace() or user_confirm_pass == ''):
        raise ValueError
    else:
        user_to_create = [user_email.lower(),
                          user_pass]
        tools_users.signin_user(user_to_create)
        user_to_create.clear()
        user_email = ''
        user_pass = ''
        user_confirm_pass = ''


def catch_user_email(var):
    global user_email
    pattern = r'[A-Za-z0-9._%+-]+@{1}(gmail|hotmail|yahoo|outlook|correounivalle.edu){1}+\.(com|co){1}'
    if re.fullmatch(pattern, var) is None or len(var) > 50:
        messagebox.showinfo('Correo no valido', 'Verifica que el correo ingresado este sin espacios '
                                                'contenga @, sea parte de un dominio válido (gmail, hotmail, yahoo, '
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


def catch_confirm_pass(var):
    global user_confirm_pass
    global user_pass
    if var != user_pass or user_pass == '':
        messagebox.showinfo('No coinciden las contraseñas', 'Verifica que las contraseñas ingresadas coincidan'
                                                            ', o que la contraseña sea válida')
        user_confirm_pass = ''
        return False
    user_confirm_pass = var
    return True


def signin_template(dynamic_frame):
    entry_box_width = 35
    lbl_title = ttk.Label(dynamic_frame,
                          text="Registro nuevo usuario",
                          font=("default", 12, "bold"))
    lbl_subtitle_email = ttk.Label(dynamic_frame,
                                   text="Email")
    lbl_subtitle_pass = ttk.Label(dynamic_frame,
                                  text="Contraseña", )
    lbl_subtitle_confirm_pass = ttk.Label(dynamic_frame,
                                          text="Confirmar Contraseña")

    entry_email = ttk.Entry(dynamic_frame,
                            width=entry_box_width,
                            validate="focusout",
                            validatecommand=(dynamic_frame.register(catch_user_email), '%P'))
    entry_pass = ttk.Entry(dynamic_frame,
                           width=entry_box_width,
                           validate="focusout",
                           validatecommand=(dynamic_frame.register(catch_user_pass), '%P'),
                           show="*")
    entry_confirm_pass = ttk.Entry(dynamic_frame,
                                   width=entry_box_width,
                                   validate="focusout",
                                   validatecommand=(dynamic_frame.register(catch_confirm_pass), '%P'),
                                   show="*")

    button_signin = ttk.Button(dynamic_frame,
                               text="Registrarse",
                               style="Accent.TButton",
                               command=lambda: warning(dynamic_frame))

    button_back = ttk.Button(dynamic_frame,
                             text="Atrás",
                             command=lambda: utils.template_handler.templ_handler('initial', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=60, pady=10)
    lbl_subtitle_email.grid(column=0, row=1, columnspan=2, pady=2)
    entry_email.grid(column=0, row=2, columnspan=2, pady=2)
    lbl_subtitle_pass.grid(column=0, row=3, columnspan=2, pady=2)
    entry_pass.grid(column=0, row=4, columnspan=2, pady=2)
    lbl_subtitle_confirm_pass.grid(column=0, row=5, columnspan=2, pady=2)
    entry_confirm_pass.grid(column=0, row=6, columnspan=2, pady=2)
    button_back.grid(column=0, row=7, sticky="e", padx=(0, 10), pady=15)
    button_signin.grid(column=1, row=7, sticky="w", padx=(10, 0), pady=15)
