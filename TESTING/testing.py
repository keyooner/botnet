import customtkinter as ctk

def crear_popup():
    popup = ctk.CTkToplevel()
    popup.title("Ventana emergente")
    
    # Agrega widgets y personaliza la ventana emergente aquí
    
    popup.mainloop()

# Crear la ventana principal
ventana = ctk.CTkToplevel()

# Agregar un botón para abrir el popup
boton_popup = ctk.CTkButton(ventana, text="Abrir Popup", command=crear_popup)
boton_popup.pack()

ventana.mainloop()
