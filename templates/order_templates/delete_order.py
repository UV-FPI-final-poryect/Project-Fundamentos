from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import databases.db_tables as tables
import databases.db_dishes as dbdish
from templates.dish_templates.delete_dish_template import columns_names

def warning(dynamic_frame, tree_dish, tree_table):
    try:
        option_dish = tree_dish.selection()
        option_table = tree_table.selection()
        if option_dish and option_table:
            answer = messagebox.askokcancel("Advertencia",
                                            "¿Seguro quieres ELIMINAR este pedido de forma permanente?")
            if answer:
                
                utils.template_handler.templ_handler('del_order',
                                                     dynamic_frame)
        else:
            messagebox.showerror('Cancelado',
                                 "No se pudo realizar el proceso")
    except Exception:
        messagebox.showerror('Incompleto',
                             "Seleccione un pedido para Eliminar")

def delete_order_template(dynamic_frame):
    title_dish = ("Codigo Plato")
    title_tables = ('N. Mesa')
    lbl_title = ttk.Label(dynamic_frame,
                        text="Pedidos",
                        font=("default", 12, "bold"))    
    
    
    list_table = ttk.Treeview(dynamic_frame, columns=title_tables, show="headings")
    list_table.heading(column=9, text=title_tables)
    list_dish = ttk.Treeview(text=title_dish)
    
    for i in tables.tables:
        list_table.insert("", "end", values=(i[0],))
    
    for j in dbdish.db_matrix:
        list_dish.insert("", "end", values=(j[0],))
    
    
    

    
    # if columns_names == 'Código':
    #     tree_dish.heading(text=columns_names)
    # tree_dish.column(0, anchor="center", width=55)
    # tree_table.column(0, anchor="center", width=15)
    
    # list_dishes = 
    # list_tables = 
    
    # for row in list_dishes:
    #     tree_table.insert("", "end", values=row)
    
    # for row in list_tables:
    #     tree_table.insert("", "end", values=row)
    
    # scrollbar_dish = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_dish.yview)
    # tree_dish.configure(yscrollcommand=scrollbar_dish.set)
    # scrollbar_table = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree_table.yview)
    # tree_table.configure(yscrollcommand=scrollbar_table.set)
    
    
    button_del = ttk.Button(dynamic_frame,
                            text="Eliminar",
                            style="Accent.TButton",
                            command=lambda: warning(dynamic_frame,
                                                    list_dish,
                                                    list_table))

    button_back = ttk.Button(dynamic_frame, text="Atrás",
                            command=lambda: utils.template_handler.\
                            templ_handler('order_menu', dynamic_frame))


    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    
    list_dish.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=10)
    list_table.grid(column=2, row=1, columnspan=2, padx=(15, 0), pady=10)
    # scrollbar_dish.grid(row=1, column=1, padx=(0, 15), pady=10, sticky="ns")
    #scrollbar_table.grid(row=1, column=3, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
    button_del.grid(column=1, row=5, sticky="w", padx=(10, 0), pady=15)