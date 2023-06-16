import customtkinter as ctk
import ctk_app as ctkapp

class RadioButtonFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name="RadioButtonFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = ctk.CTkLabel(self, text=self.header_name)
        self.header.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.radio_button_var = ctk.IntVar(value = 0)

        self.radio_button_1 = ctk.CTkRadioButton(self, text = 'Login ', value = 0, variable = self.radio_button_var)
        self.radio_button_1.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.radio_button_2 = ctk.CTkRadioButton(self, text = 'Emails', value = 1, variable = self.radio_button_var)
        self.radio_button_2.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.radio_button_3 = ctk.CTkRadioButton(self, text = 'VPN  ', value= 2, variable = self.radio_button_var)
        self.radio_button_3.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.radio_button_4 = ctk.CTkRadioButton(self, text = 'Twitter', value = 3, variable = self.radio_button_var)
        self.radio_button_4.grid(row = 4, column = 0, padx = 10, pady = 10)

        self.radio_button_frame_button = ctk.CTkButton(self, text = 'Select Option')
        self.radio_button_frame_button.grid(row = 5, column = 0, padx = 10, pady = 10)

    def get_value(self):
        """ returns selected value as a int, returns 0 (login) if nothing selected """
        return self.radio_button_var.get()

    def set_value(self, selection):
        """ selects the corresponding radio button, selects nothing if no corresponding radio button """
        self.radio_button_var.set(selection)

