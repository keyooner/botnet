import datetime
import customtkinter as ctk
import re
from CTkTable import *
import tkinter

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("BotNet Twitter")
        self.geometry('1100x580')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # label sidebar frame
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Options", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # sidebar buttons
        self.sidebar_accounts_button = ctk.CTkButton(self.sidebar_frame, text="Accounts",command=lambda:self.sidebar_button_clicked('accounts'))
        self.sidebar_accounts_button.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_vpn_button = ctk.CTkButton(self.sidebar_frame, text="VPN",command=lambda:self.sidebar_button_clicked('vpn'))
        self.sidebar_vpn_button.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_twitter_button = ctk.CTkButton(self.sidebar_frame, text="Twitter" ,command=lambda:self.sidebar_button_clicked('twitter'))
        self.sidebar_twitter_button.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_logout_button = ctk.CTkButton(self.sidebar_frame, text="LogOut" ,command=lambda:self.sidebar_button_clicked('logout'))
        self.sidebar_logout_button.grid(row=4, column=0, padx=20, pady=10)
        
        #sidebar appearance mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                        command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                                command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = ctk.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create interactive options frame
        self.options_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.options_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.options_frame.grid_columnconfigure(0, weight=1)
        self.options_frame.grid_rowconfigure(4, weight=1)

        # create radiobutton frame
        self.radiobutton_frame = ctk.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")


        # create checkbox and switch frame
        self.checkbox_slider_frame = ctk.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_2 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("90%")
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_clicked(self, button):

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        if button == 'accounts':
            self.vpn_option_button_clicked()

        elif button == 'vpn':
            self.vpn_option_button_clicked()

        elif button == 'twitter':
            self.twitter_option_button_clicked()

        elif button == 'logout':
            self.logout_option_button_clicked()

    def vpn_option_button_clicked(self):
        self.disable_option_button('vpn')

        self.vpn_label_option = ctk.CTkLabel(self.options_frame, text='Vpn', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        self.vpn_label_option.grid(row=0, column=0, padx=(10,10), pady=(10,10), columnspan=5)

        self.vpn_connect_button = ctk.CTkButton(self.options_frame, text="CONNECT VPN")
        self.vpn_connect_button.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
    
    def twitter_option_button_clicked(self):
        
        self.disable_option_button('twitter')

        #label option selected
        self.twitter_label_option = ctk.CTkLabel(self.options_frame, text='Twitter', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        self.twitter_label_option.grid(row=0, column=0, padx=(10,10), pady=(10,10), columnspan=5)

        self.twitter_label_accounts = ctk.CTkLabel(
            self.options_frame,
            text=f'Max interactions available: {self.return_available_accounts_twitter()}',
            justify='left',
        )
        self.twitter_label_accounts.grid(row=1, column=0, padx=(20,10), pady=(20,10), sticky="w")

        self.add_entry_valuable_button(0,self.return_available_accounts_twitter())

        # create entry urls
        self.entry_twitter_url = ctk.CTkEntry(self.options_frame, placeholder_text="Entry your twitter url here")
        self.entry_twitter_url.grid(row=2, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.twitter_url_button = ctk.CTkButton(self.options_frame, text="Check Url", command=lambda:self.verify_twitter_url(self.entry_twitter_url.get()))
        self.twitter_url_button.grid(row=2, column=1, padx=(20,10), pady=(20,10), sticky='w')

        # create checkboxs
        self.twitter_checkbox_like = ctk.CTkCheckBox(self.options_frame, text='Like', state='disabled')
        self.twitter_checkbox_like.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="e")
        self.twitter_checkbox_rt = ctk.CTkCheckBox(self.options_frame, text='Retweet', state='disabled')
        self.twitter_checkbox_rt.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="w")
        self.twitter_checkbox_cmnt = ctk.CTkCheckBox(self.options_frame, text='Comment', state='disabled')
        self.twitter_checkbox_cmnt.grid(row=3, column=1, pady=(20, 0), padx=20, sticky="nsew")
        self.twitter_button_action = ctk.CTkButton(self.options_frame, text="Do it", state='disabled')
        self.twitter_button_action.grid(row=6, column=0, padx=(20, 10), pady=(10, 10), sticky="nsew")

    def return_available_accounts_twitter(self):
        return 5

    def add_entry_valuable_button(self, min_value, max_value):

        def increase(self):
            value = int(self.button_entry.get())
            if value < max_value:
                self.button_entry.delete(0, ctk.END)
                self.button_entry.insert(0, str(value + 1))

        def decrease(self):
            value = int(self.button_entry.get())
            if value > min_value:
                self.button_entry.delete(0, ctk.END)
                self.button_entry.insert(0, str(value - 1))

        self.button_entry = ctk.CTkEntry(self.options_frame, width=30)
        self.button_entry.insert(0, "0")
        self.button_entry.grid(row=1, column=0, padx=(20,10), pady=(20,10), sticky="e")

        self.button_increase = ctk.CTkButton(self.options_frame, text='+', command=lambda:increase(self), width=2)
        self.button_increase.grid(row=1, column=1, padx=(20,10), pady=(20,10))

        self.button_decrease = ctk.CTkButton(self.options_frame, text='-', command=lambda:decrease(self), width=2)
        self.button_decrease.grid(row=1, column=2, padx=(20,10), pady=(20,10))

    def verify_twitter_url(self, url):
        standard_url = r'^https?://twitter\.com/[A-Za-z0-9_]{1,15}/status/\d+$'
        if re.match(standard_url, url):
            self.twitter_checkbox_like.configure(state='normal')
            self.twitter_checkbox_rt.configure(state='normal')
            self.twitter_checkbox_cmnt.configure(state='normal')
            self.twitter_button_action.configure(state='normal')
        else:
            self.twitter_checkbox_like.configure(state='disabled')
            self.twitter_checkbox_rt.configure(state='disabled')
            self.twitter_checkbox_cmnt.configure(state='disabled')
            self.twitter_button_action.configure(state='disabled')
                

    def logout_option_button_clicked(self):
        self.disable_option_button('logout')

        #label option selected
        self.logout_label_option = ctk.CTkLabel(self.options_frame, text='LogOut', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        self.logout_label_option.grid(row=0, column=0, padx=(10,10), pady=(10,10), columnspan=5)

        self.logout_label_quest = ctk.CTkLabel(self.options_frame, text="Are you sure?", justify="center")
        self.logout_label_quest.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), columnspan=4)

        #button option selected
        self.logout_button_yes = ctk.CTkButton(self.options_frame, text="Yes", anchor='center')
        self.logout_button_yes.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="w")

        self.logout_button_no = ctk.CTkButton(self.options_frame, text="No", anchor='center')
        self.logout_button_no.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="e")

    def disable_option_button(self,button):
        #enable other buttons
        self.sidebar_vpn_button.configure(state='normal')
        self.sidebar_accounts_button.configure(state='normal')
        self.sidebar_twitter_button.configure(state='normal')
        self.sidebar_logout_button.configure(state='normal')
        #disable specific button
        if button == 'twitter':
            self.sidebar_twitter_button.configure(state='disabled')
        elif button == 'vpn':
            self.sidebar_vpn_button.configure(state='disabled')
        elif button == 'accounts':
            self.sidebar_accounts_button.configure(state='disabled')
        elif button == 'logout':
            self.sidebar_logout_button.configure(state='disabled')

if __name__ == "__main__":
    app = App()
    app.mainloop()