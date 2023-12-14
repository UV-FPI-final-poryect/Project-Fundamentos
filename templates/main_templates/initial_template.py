from tkinter import ttk
import textwrap
import utils.template_handler

"""
This module is the first template that appears when the user executes the aplication.

Imports:
- 'ttk' module from the 'tkinter' library for creating the Graphical
User Interface (GUI).
- 'textwrap' is used to dedent large strings.
- 'templ_handler' method from the 'template_handler' module.

Purpose:
- Generates the primary template asigned to the dynamic_frame.
- Utilizes 'ttk' for creating graphical elements in the GUI.
- Implements 'templ_handler' for handling the templates in the application.
"""

def initial_template(dynamic_frame):
    """
    Create the widgets for the initial_template

    Args:
        dynamic_frame (widget): The frame object to receive the 
        selected template.
    """
    intro_txt = textwrap.dedent("""
                    Nuestro restaurante es un lugar donde ofrecemos
                    una variedad de platos deliciosos y recursos
                    culinarios para el público para satisfacer tus
                    necesidades culinarias y hacerte disfrutar de
                    una experiencia gastronómica excepcional.
                    """)
    lbl_intro_txt = ttk.Label(
        dynamic_frame,
        text=intro_txt,
        anchor="center",
        justify="center")
    bttn_signin = ttk.Button(
        dynamic_frame,
        text="Registrarse",
        style="Accent.TButton",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'signin',frame))
    bttn_login = ttk.Button(
        dynamic_frame,
        text="Iniciar Sesion",
        style="Accent.TButton",
        command=lambda frame=dynamic_frame: utils.template_handler.templ_handler(
            'login', frame))
    lbl_intro_txt.grid(column=0, row=0, columnspan=2, padx=20, pady=20)
    bttn_signin.grid(column=0, row=1, sticky="nsew", padx=20, pady=20)
    bttn_login.grid(column=1, row=1, sticky="nsew", padx=20, pady=20)
