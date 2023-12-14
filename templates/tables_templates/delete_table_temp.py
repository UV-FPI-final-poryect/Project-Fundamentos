from tkinter import ttk
from tkinter import messagebox
import utils.template_handler
import data_access_tools.tables_da as tool_table


def warning(dynamic_frame, tree):
    try:
        option = tree.selection()
        if option:
            answer = messagebox.askokcancel("Advertencia",
                                            "¿Seguro quieres ELIMINAR esta mesa de forma permanente?")
            if answer:
                del_table = tree.item(option)["values"]  # Guardamos los valores de la seleccion escogida
                tool_table.delet_table(del_table[0])
                utils.template_handler.templ_handler('del_table',
                                                     dynamic_frame)
        else:
            messagebox.showerror('Cancelado',
                                 "No se pudo realizar el proceso")
    except Exception:
        messagebox.showerror('Incompleto',
                             "Seleccione una Mesa para Eliminar")


def delete_table(dynamic_frame):
    lbl_title = ttk.Label(dynamic_frame, text="Mesas",
                          font=("default", 12, "bold"))

    tree = ttk.Treeview(dynamic_frame, columns=tool_table.tables_columns(),
                        show="headings", height=9)

    for col in tool_table.tables_columns():
        tree.heading(col, text=col)
        if col == "Fecha":
            tree.column(col, anchor="center", width=100)
            continue
        if col == "N. Personas":
            tree.column(col, anchor="center", width=100)
            continue
        tree.column(col, anchor="center", width=55)
    data_base_for_tables = tool_table.get_matriz()
    for row in data_base_for_tables:
        tree.insert("", "end", values=row)

    scrollbar_y = ttk.Scrollbar(dynamic_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)

    button_back = ttk.Button(dynamic_frame, text="Atrás",
                             command=lambda frame=dynamic_frame:
                                 utils.template_handler.templ_handler('menu_tables', frame))
    button_del = ttk.Button(dynamic_frame, text="Eliminar",
                            style="Accent.TButton",
                            command=lambda: warning(dynamic_frame, tree))

    lbl_title.grid(column=0, row=0, columnspan=2, pady=10)
    tree.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=10)
    scrollbar_y.grid(row=1, column=2, padx=(0, 15), pady=10, sticky="ns")
    button_back.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=15)
    button_del.grid(column=1, row=2, sticky="w", padx=(10, 0), pady=15)
