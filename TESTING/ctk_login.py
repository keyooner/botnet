import customtkinter as ctk 
import tkinter.messagebox as tkmb

def login ():
    username = 'Test'
    password = '123456'

    if username_input.get() == username and password_input.get() == password:
        tkmb.showinfo(title = 'Login Successfully', message = 'You have logged in successfully')
        new_window = ctk.CTkToplevel(main_window)
        new_window.title('New Window')
        new_window.geometry('350x150')
        ctk.CTkLabel(new_window, text = 'New Window for more functions').pack()
    else:
        tkmb.showerror(title = 'Login failed', message = 'Invalid username or password')

# Appearance window tkinter app
ctk.set_appearance_mode('light') # Modes: system (default), light, dark
ctk.set_default_color_theme('green') # Themes: blue (default), dark-blue, green

# Create main window tkinter app
main_window = ctk.CTk()
main_window.geometry('400x400')
main_window.title('Login')

# Label of Main Window app
main_window_label = ctk.CTkLabel(main_window, text = 'Main UI page')
main_window_label.pack(pady = 20)

# Create a frame to login method
login_frame = ctk.CTkFrame(main_window)
login_frame.pack(pady = 20, padx = 40, fill = 'both', expand = True)

# Set the login label inside the login frame 
login_label = ctk.CTkLabel(login_frame, text = 'Login')
login_label.pack(pady = 12, padx = 10)

# Create inputs to user and password
username_input = ctk.CTkEntry(login_frame, placeholder_text = 'Username')
username_input.pack(pady = 12, padx = 10)

password_input = ctk.CTkEntry(login_frame, placeholder_text = 'Password', show = '*')
password_input.pack(pady = 12, padx = 10)

# Create a login button
login_button = ctk.CTkButton(login_frame, text = 'Login', command = login)
login_button.pack(pady = 12, padx = 10)

# Launch main window tkinter app
main_window.mainloop()


