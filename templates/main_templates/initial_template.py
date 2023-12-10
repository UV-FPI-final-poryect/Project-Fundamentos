from tkinter import ttk
import textwrap

import utils.template_handler


def initial_template(dynamic_frame):
    # Primera Ventana | Inicio

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
