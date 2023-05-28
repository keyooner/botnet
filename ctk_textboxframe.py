import customtkinter as ctk

class TextBoxFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name = 'TextBoxFrame', **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = ctk.CTkLabel(self, text = self.header_name)
        self.header.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.textbox_var = ctk.StringVar(value = 'Some test text!')

        self.textbox_frame = ctk.CTkTextbox(self, width = 300, corner_radius = 0)
        self.textbox_frame.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = 'nsew')
        self.textbox_frame.insert('0.0', self.textbox_var)

    def get_value(self):
        return self.textbox_var.get()

    def set_value(self):
        self.textbox_var.set()