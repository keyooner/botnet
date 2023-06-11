import tkinter as tk
from tkinter import ttk

# Datos de ejemplo para la tabla
datos = [
    ("Juan", "Pérez", 25),
    ("María", "López", 30),
    ("Pedro", "Gómez", 35),
    ("Laura", "Rodríguez", 28)
]

# Crear la ventana principal
ventana = tk.Tk()

# Crear el objeto Treeview
tabla = ttk.Treeview(ventana)

# Configurar las columnas de la tabla
tabla["columns"] = ("Nombre", "Apellido", "Edad")
tabla.column("#0", width=0, stretch=tk.NO)  # Columna oculta para índices
tabla.column("Nombre", width=100)
tabla.column("Apellido", width=100)
tabla.column("Edad", width=50)

# Encabezados de las columnas
tabla.heading("#0", text="")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Apellido", text="Apellido")
tabla.heading("Edad", text="Edad")

# Insertar los datos en la tabla
for i, (nombre, apellido, edad) in enumerate(datos, start=1):
    tabla.insert(parent="", index="end", iid=i, text="", values=(nombre, apellido, edad))

# Crear una barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

# Ubicar la barra de desplazamiento y la tabla
tabla.pack(side=tk.LEFT, fill=tk.Y)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
