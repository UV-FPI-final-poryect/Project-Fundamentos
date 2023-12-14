from tkinter import ttk
from tkinter import messagebox
import re
import data_access_tools.user_auth as tools_users
import utils.template_handler


"""
This template is generated to gather and verify the user log in info
before it will be send to the user authentication script (user_auth.py).

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
- Generates the log in template asigned to the dynamic_frame.
- Utilizes 'ttk' for creating graphical elements in the GUI.
- Implements 'templ_handler' for handling the templates in the application.
- Verify that the credentials are right before manage it in the backend.

 Args:
        user_email (String): The verified user email which will be send to
        user_auth.
        user_pass (String): The user password which will be send to
        user_auth.
"""


user_email = ''
user_pass = ''


def verify_process(dynamic_frame):
    """
    Here is where the user executes the verify process for the email and 
    the password entered, first confirms if these variables have some 
    content, and if they have add them to a list which is passed to the
    login_user method of the user_auth module to validate the data given.
    """
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
    """
    Here validates the email entered in the entry_email widget using the 're' library and if everything is ok,
    the entered email is assigned to the user_email global variable.

    Parameters:
        var (String): is the parameter given by the validatecommand to be evaluated.
    """
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
    """
    Just catch the password entered.

    Parameters:
        var (String): is the parameter given by the validatecommand to be evaluated.
    """
    global user_pass
    user_pass = var
    return True


def login_template(dynamic_frame):
    #Generates the structure for the log in template
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
