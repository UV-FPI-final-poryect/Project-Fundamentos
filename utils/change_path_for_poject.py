import os

def change_path():
    # Obtén la ruta del script actual
    script_dir = os.path.dirname(__file__)
    # Cambia el directorio de trabajo actual al directorio del script
    os.chdir(script_dir)