from tkinter import *

#from templates.initial_template import initial_templ
from utils.change_path_for_img import change_path
from utils.template_handler import templ_handler

if __name__ == '__main__':
     change_path()

     root = Tk()
     root.title("SSJ Restorant")
     root.columnconfigure(0, weight=1, minsize=250)
     root.rowconfigure(0, weight=1, minsize=100)
     root.iconbitmap('../multimedia/forkandknife.ico')
     templ_handler(root, 'initial')

     #initial_templ(root)