import customtkinter as ctk

class LoginFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name="Login Frame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = ctk.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=2, padx=10, pady=10)

        self.login_username_var = ctk.StringVar(value="")
        self.login_password_var = ctk.StringVar(value="")

        self.login_username_input = ctk.CTkEntry(self, placeholder_text = 'Username')
        self.login_username_input.grid(row=1, column = 2, padx = 10, pady = 10)

        self.login_password_input = ctk.CTkEntry(self, placeholder_text = 'Password', show = '*')
        self.login_password_input.grid(row=2, column = 2, padx = 10, pady = 10)

        self.login_frame_button = ctk.CTkButton(self, text = 'Login')
        self.login_frame_button.grid(row = 3, column = 2, padx = 10, pady = 10)

    def get_value(self):
        return (self.login_username_var.get(), self.login_password_var.get())

    def set_value(self):
        self.login_username_var.set()
        self.login_password_var.set()