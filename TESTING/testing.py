import tkinter as tk

def crear_popup():
    popup = tk.Toplevel()
    popup.title("Ventana emergente")
    
    # Agrega widgets y personaliza la ventana emergente aquí
    
    popup.mainloop()

# Crear la ventana principal
ventana = tk.Tk()

# Agregar un botón para abrir el popup
boton_popup = tk.Button(ventana, text="Abrir Popup", command=crear_popup)
boton_popup.pack()

ventana.mainloop()
