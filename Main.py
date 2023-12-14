from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from utils.change_path_for_project import change_path
from utils.template_handler import templ_handler


"""
Autors: Juan David Cifuentes Florez
        Santiago Lopez Ramirez

This is the main module responsible for generating the project's
primary interface.

Imports:
- 'ttk' module from the 'tkinter' library for creating the Graphical
User Interface (GUI).
- 'Image' and 'ImageTk' modules from the 'PIL' 
(Python Imaging Library) for image handling.
- 'change_path' method from the 'change_path_for_project' module for
path manipulation.
- 'templ_handler' method from the 'template_handler' module.

Purpose:
- Generates the primary interface used throughout the project.
- Utilizes 'ttk' for creating graphical elements in the GUI.
- Handles image-related tasks using 'Image' and 'ImageTk' from 'PIL'.
- Uses 'change_path' for managing and manipulating paths as required.
- Implements 'templ_handler' for handling templates or related 
functionalities.
"""


def center_window(root):
    """
    Centers the main interface window on the user's screen.

    The 'update_idletasks()' method ensures that tkinter has executed
    all pending tasks to properly define the window size and prevent 
    misplacement.

    :param root: is the main window for the project.
    """
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    x = (root.winfo_screenwidth() // 2) - (window_width // 2)
    y = (root.winfo_screenheight() // 2) - (window_height // 2)

    root.geometry('{}x{}+{}+{}'.format(window_width,
                                       window_height,
                                       x,
                                       y))


if __name__ == '__main__':
    change_path()
    root = Tk()
    root.title("SJ Restorant")
    root.resizable(False, False)
    root.iconbitmap('../multimedia/forkandknife.ico')

    # Forest-dark theme is called and applied to the GUI.
    root.tk.call('source',
                 '../resources/Forest-ttk-theme-master/forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')

    last_plain_bg = "#858585"

    frame_style = 'TFrame'
    style = ttk.Style()
    style.configure(frame_style,
                    background=last_plain_bg)

    frame_container = ttk.Frame(root)
    frame_container.grid_columnconfigure(0, weight=1, minsize=700)
    frame_container.grid_rowconfigure(0, weight=1, minsize=150)
    frame_container.grid_rowconfigure(1, weight=1, minsize=400)

    static_frame = ttk.Frame(frame_container, style=frame_style)
    image = Image.open("../multimedia/Logo.png")
    image = image.resize((70, 90))
    img = ImageTk.PhotoImage(image)
    lbl_img = ttk.Label(static_frame,
                        image=img,
                        background=last_plain_bg)
    lbl_ini = ttk.Label(static_frame,
                        text="SJ Restorant",
                        font=("default", 14, "bold"),
                        background=last_plain_bg)
    dynamic_content_frame = ttk.Frame(
        frame_container, style=frame_style)

    dynamic_frame = ttk.Frame(dynamic_content_frame, style="Card")
    frame_container.grid(column=0, row=0, sticky="nwes")
    static_frame.grid(column=0, row=0, sticky="nwes")
    dynamic_content_frame.grid(column=0, row=1, sticky="nwes")
    dynamic_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_img.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_ini.place(relx=0.5, rely=0.95, anchor=CENTER)

    center_window(root)
    templ_handler('initial', dynamic_frame)

    root.mainloop()
