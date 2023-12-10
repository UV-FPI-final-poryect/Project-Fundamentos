from tkinter import ttk
from tkinter import messagebox
import re
import data_access_tools.user_auth as tools_users
import utils.template_handler


user_email = ''
user_pass = ''


def verify_process(dynamic_frame):
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
            user_to_verify.clear()
            user_email = ''
            user_pass = ''
            utils.template_handler.templ_handler('main_menu', dynamic_frame)
    except ValueError:
        messagebox.showerror('Faltan campos', 'Hay algún campo vacío, por favor verifica.')
    except FileNotFoundError:
        messagebox.showerror('Validación no completada', 'El usuario ingresado no existe o la contraseña es '
                                                         'incorrecta, verifica e intenta de nuevo.')
    except Exception:
        messagebox.showerror('No se pudo completar la acción', 'No se ha logrado realizar el proceso '
                                                               'de validación, llama al proveedor para asesoria.')


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
                              command=lambda: verify_process(dynamic_frame))
    button_back = ttk.Button(dynamic_frame,
                             text="Atrás",
                             command=lambda: utils.template_handler.templ_handler('initial', dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=2, pady=10)
    lbl_subtitle_email.grid(column=0, row=1, columnspan=2, pady=2)
    entry_email.grid(column=0, row=2, columnspan=2, padx=30, pady=2)
    lbl_subtitle_pass.grid(column=0, row=3, columnspan=2, pady=2)
    entry_passw.grid(column=0, row=4, columnspan=2, padx=30, pady=2)
    button_login.grid(column=1, row=5, sticky="w", pady=15)
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
