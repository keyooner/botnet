import customtkinter as ctk 
import tkinter.messagebox as tkmb
import re
import FirebaseFunctions.firebaseAuthentication as fba
import GraphicUI.ctk_app as gui_app
import temp

def togglePasswordVisibility():
    if show_password.get():
        password_input.configure(show='')
    else:
        password_input.configure(show='*')

def createWindowRegister():
    def register ():
        
        email = username_input_reg.get()
        password = password_input_reg.get()
        password2 = password_input_reg2.get()
        
        if password != password2:
            tkmb.showerror(title = 'Register failed', message = "Passwords don't match!")
        
        log, verify = fba.createUser(email, password)
        
        if verify == True:
            #print(show_info("info", 'Register Successfully', log, new_window))
            tkmb.showinfo(title = 'Register Successfully', message = log)
            secondPriority()
            close_window()
        else:
            secondPriority()
            #show_info("error", 'Register Failed', log, new_window)
            tkmb.showerror(title = 'Register failed', message = log)
        
        firstPriority()
        
    def close_window():
        new_window.destroy()
        enable_button()
        
    def enable_button():
        register_button.configure(state="normal")
        
    def disable_button():
        register_button.configure(state="disabled")
    
    def secondPriority():
        new_window.attributes('-topmost', 0)
    
    def firstPriority():
        new_window.attributes('-topmost', 1)
    
    def togglePasswordVisibilityForRegister():
        if show_password.get():
            password_input_reg.configure(show='')
            password_input_reg2.configure(show='')
        else:
            password_input_reg.configure(show='*')
            password_input_reg2.configure(show='*')
            
    new_window = ctk.CTkToplevel(main_window)
    # Deshabilitar el botón de maximizar
    new_window.resizable(False, False)
    new_window.attributes('-topmost', 1)
    new_window.title('Register')
    window_width = 400
    window_height = 400

    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)

    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a frame to login method
    register_frame = ctk.CTkFrame(new_window)
    register_frame.pack(pady = 20, padx = 40, fill = 'both', expand = True)

    # Set the login label inside the login frame 
    login_label = ctk.CTkLabel(register_frame, text = 'Create a new user')
    login_label.pack(pady = 12, padx = 10)

    # Create inputs to user and password
    username_input_reg = ctk.CTkEntry(register_frame, placeholder_text = 'Email')
    username_input_reg.pack(pady = 12, padx = 10)

    password_input_reg = ctk.CTkEntry(register_frame, placeholder_text = 'Password', show = '*')
    password_input_reg.pack(pady = 12, padx = 10)
    
    password_input_reg2 = ctk.CTkEntry(register_frame, placeholder_text = 'Confirm Password', show = '*')
    password_input_reg2.pack(pady = 12, padx = 10)
    
    show_password = ctk.BooleanVar()
    show_password_button = ctk.CTkCheckBox(register_frame, text="Mostrar contraseñas", variable=show_password, command=togglePasswordVisibilityForRegister)
    show_password_button.pack()
    
    # Create a register account button
    register_acc_button = ctk.CTkButton(register_frame, text = 'Register', command = register)
    register_acc_button .pack(pady = 12, padx = 10)
    
    # Create a go back button
    go_back_button = ctk.CTkButton(register_frame, text = 'Go back', command = close_window)
    go_back_button.pack(pady = 8, padx = 10)
            
    disable_button()
    new_window.protocol("WM_DELETE_WINDOW", close_window)
    new_window.wait_window()

def createWindowRecover():
    def recover():
        email = username_input_reg.get()
        if checkRequisitesRecover():
            log, verify = fba.recoverPassword(email)
            if verify == True:
                #show_info("info", 'Recover Successfully', log, new_window)
                tkmb.showinfo(title = 'Recover Successfully', message = log)
                secondPriority()
                close_window()
            else:
                #show_info("error", 'Recover failed', log, new_window)
                tkmb.showerror(title = 'Recover failed', message = log)
                secondPriority()
            
            firstPriority()
    
    def close_window():
        new_window.destroy()
        enable_button()
        
    def enable_button():
        recover_button.configure(state="normal")
        
    def disable_button():
        recover_button.configure(state="disabled")
    
    def secondPriority():
        new_window.attributes('-topmost', 0)
    
    def firstPriority():
        new_window.attributes('-topmost', 1)
            
    new_window = ctk.CTkToplevel(main_window)
    # Deshabilitar el botón de maximizar
    new_window.resizable(False, False)
    new_window.attributes('-topmost', 1)
    new_window.title('Recover Password')
    window_width = 400
    window_height = 400

    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)

    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a frame to login method
    recover_frame = ctk.CTkFrame(new_window)
    recover_frame.pack(pady = 20, padx = 40, fill = 'both', expand = True)

    # Set the login label inside the login frame 
    login_label = ctk.CTkLabel(recover_frame, text = 'Recover your password')
    login_label.pack(pady = 12, padx = 10)

    # Create inputs to user and password
    state, email_inserted = getEmail()
    username_input_reg = ctk.CTkEntry(recover_frame, placeholder_text = 'Email')
    username_input_reg.pack(pady = 12, padx = 10)
    if state:
        username_input_reg.insert(0, email_inserted)
    
    def checkRequisitesRecover():
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(regex, username_input_reg.get()):
            #show_info("error", 'Login failed', "Pls, introduce a valid email!!", new_window)
            tkmb.showerror(title = 'Login failed', message = "Pls, introduce a valid email!!")
            new_window.attributes('-topmost', 0)
        else:
            return True
        
    def buttonEnterRecover():
        if checkRequisitesRecover():
            recover()

    def bindButtonEnterRecover(event):
        buttonEnterRecover()

    username_input_reg.bind("<Return>", bindButtonEnterRecover)

    # Create a register account button
    recover_acc_button = ctk.CTkButton(recover_frame, text = 'Recover', command = recover)
    recover_acc_button .pack(pady = 12, padx = 10)
    
    # Create a go back button
    go_back_button = ctk.CTkButton(recover_frame, text = 'Go back', command = close_window)
    go_back_button.pack(pady = 8, padx = 10)
            
    disable_button()
    new_window.protocol("WM_DELETE_WINDOW", close_window)
    new_window.wait_window()

def enable_button():
    register_button.configure(state="normal")

def login():
    email = username_input.get()
    password = password_input.get()
    if checkRequisitesLogin():
        log, verify = fba.loginUser(email, password)
        if verify == True:
            tkmb.showinfo(title = 'Login Successfully', message = log)
            #app.saveData(email, password)
            temp.set_credentials(email, password)
            main_window.destroy()
            app_window = gui_app.App()
            app_window.mainloop()
        else:
            tkmb.showerror(title = 'Login failed', message = log)

def getEmail():
    if username_input.get() != "":
        return True, username_input.get()
    return False, None
        
# Appearance window tkinter app
ctk.set_appearance_mode('light') # Modes: system (default), light, dark
ctk.set_default_color_theme('green') # Themes: blue (default), dark-blue, green

# Create main window tkinter app
main_window = ctk.CTk()
window_width = 400
window_height = 400

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)

main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Deshabilitar el botón de maximizar
main_window.resizable(False, False)
main_window.title('Login')

# Label of Main Window app
main_window_label = ctk.CTkLabel(main_window, text = 'TWITTER BOT CREATOR')
main_window_label.pack(pady = 20)

# Create a frame to login method
login_frame = ctk.CTkFrame(main_window)
login_frame.pack(pady = 20, padx = 40, fill = 'both', expand = True)

# Set the login label inside the login frame 
login_label = ctk.CTkLabel(login_frame, text = 'Login into your account')
login_label.pack(pady = 12, padx = 10)

# Create inputs to user and password
username_input = ctk.CTkEntry(login_frame, placeholder_text = 'Email')
username_input.pack(pady = 12, padx = 10)

password_input = ctk.CTkEntry(login_frame, placeholder_text = 'Password', show = '*')
password_input.pack(pady = 12, padx = 10)

show_password = ctk.BooleanVar()
show_password_button = ctk.CTkCheckBox(login_frame, text="Mostrar contraseña", variable=show_password, command=togglePasswordVisibility)
show_password_button.pack()

# Create a recover password button
recover_button = ctk.CTkButton(login_frame, text = 'Recover Password', command = createWindowRecover)
recover_button.pack(side= 'top', pady = 10, padx = 10)

# Create a login button
login_button = ctk.CTkButton(login_frame, text = 'Login', command = login)
login_button.pack(side='left', pady = 0, padx = 10)

def checkRequisitesLogin():
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(regex, username_input.get()):
            tkmb.showerror(title = 'Login failed', message = "Pls, introduce a valid email!!")
        elif password_input.get() == "":
            tkmb.showerror(title = 'Login failed', message = "Pls, introduce a password!!")
        else:
            return True
        
def buttonEnterLogin():
    if checkRequisitesLogin():
        login()

def bindButtonEnterLogin(event):
    buttonEnterLogin()

username_input.bind("<Return>", bindButtonEnterLogin)
password_input.bind("<Return>", bindButtonEnterLogin)

# Create a register button
register_button = ctk.CTkButton(login_frame, text = 'Register', command = createWindowRegister)
register_button.pack(side='right', pady = 0, padx = 10)

# Launch main window tkinter app
main_window.mainloop()


