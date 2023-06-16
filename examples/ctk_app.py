import customtkinter as ctk
import ctk_radiobuttonframe as ctkrb
import ctk_loginframe as ctklg
import ctk_textboxframe as ctktb
import ctk_vpnframe as ctkvpn

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title('Twitter BotNet App')
        self.geometry('1000x600')

        # create radio button frame to choose between different options
        self.radio_button_frame_options = ctkrb.RadioButtonFrame(self, header_name = 'Choose one option')
        self.radio_button_frame_options.grid(row = 0, column = 0, padx = 20, pady = 20)

        # create login frame for radio button option 1
        self.login_frame = ctklg.LoginFrame(self, header_name = 'Login')
        self.login_frame.grid(row = 0, column = 1, padx = 20, pady = 20)

        # create vpn frame to connect vpn
        self.vpn_frame = ctkvpn.VpnFrame(self, header_name = 'VPN')
        self.vpn_frame.grid(row = 1, column = 1, padx = 20, pady = 20)        

        # create textbox to see the terminal commands in real time
        self.textbox_frame = ctktb.TextBoxFrame(self,  header_name = 'Text Box Area')
        self.textbox_frame.grid(row = 0, column = 2, padx = 20, pady = 20)

if __name__ == '__main__':

    # Appearance window tkinter app
    ctk.set_appearance_mode('light') # Modes: system (default), light, dark
    ctk.set_default_color_theme('green') # Themes: blue (default), dark-blue, green

    # Create main window tkinter app
    app_window = App()
    app_window.mainloop()