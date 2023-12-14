from tkinter import ttk
from tkinter import messagebox
import re
import utils.template_handler
import data_access_tools.user_auth as tools_users


"""
This template is generated to gather and verify the user sign in info
before it will be send to the user authentication script (user_auth.py) 
and save it.

Imports:
- 'ttk' module from the 'tkinter' library for creating the Graphical
User Interface (GUI).
- 'messagebox' module from the 'tkinter' library which creates a focused
top level frame with an advise to the user.
- 're' is the regular expression library for python where we can use 
several methods to verify if a string accomplish a designed pattern.
- 'user_auth' is the module which manage the user credentials.
- 'templ_handler' method from the 'template_handler' module.

Purpose:
- Generates the sign in template asigned to the dynamic_frame.
- Utilizes 'ttk' for creating graphical elements in the GUI.
- Implements 'templ_handler' for handling the templates in the application.
- Verify that the credentials are right before manage it in the backend.

 Args:
        user_email (String): The verified user email which will be send to
        user_auth.
        user_pass (String): The user password which will be send to
        user_auth.
        user_confirm_pass (String): The user confirm password which will be 
        used to validate if the user password is ok.
"""


user_email = ''
user_pass = ''
user_confirm_pass = ''


def warning(dynamic_frame):
    """
    In this function is where the exceptions will be handled when something 
    breaks up and displays a confirm message box before saving the user
    credentials.
    
    Params:
        dynamic_frame (widget): The frame object to receive the 
        selected template.
    """
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
    #Verified if the global variables are ok and creates a list with them 
    #which it will passed to the sign in method of user_auth
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
    """
    Here validates the email entered in the entry_email widget using the 
    're' library and if everything is ok, the entered email is assigned 
    to the user_email global variable.

    Parameters:
        var (String): is the parameter given by the validatecommand to 
        be evaluated.
    """
    global user_email
    pattern = r'[A-Za-z0-9._%+-]+@{1}(gmail|hotmail|yahoo|outlook|correounivalle.edu){1}\.(com|co){1}'
    if re.fullmatch(pattern, var) is None or len(var) > 50:
        messagebox.showinfo('Correo no valido', 'Verifica que el correo ingresado este sin espacios '
                                                'contenga @, sea parte de un dominio válido (gmail, hotmail, yahoo, '
                                                'outlook, correounivalle.edu) y termine con .com o .co')
        user_email = ''
        return False

    user_email = var
    return True


def catch_user_pass(var):
    """
    Here validates the password entered in the entry_pass widget using the 
    're' library and if everything is ok, the entered password is assigned 
    to the user_pass global variable.

    Parameters:
        var (String): is the parameter given by the validatecommand to be
        evaluated.
    """
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
    """
    Here confirms if the password entered in the entry_confirm_pass and
    entry_pass widgets are the same.

    Parameters:
        var (String): is the parameter given by the validatecommand to be 
        evaluated.
    """
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
    #Generates the structure for the sign in template
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
