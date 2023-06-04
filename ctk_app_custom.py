import datetime
import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("BotNet Twitter")
        self.geometry('1100x580')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure((2, 3), weight = 0)
        self.grid_rowconfigure((0, 1, 2), weight = 1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        # sidebar label
        self.sidebar_label = ctk.CTkLabel(self.sidebar_frame, text='Options', font=ctk.CTkFont(size=20, weight="bold"))
        self.sidebar_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # sidebar buttons
        self.sidebar_email_button = ctk.CTkButton(self.sidebar_frame, text = 'Emails', command=lambda:self.test_slider_button_clicked('email'))
        self.sidebar_email_button.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_vpn_button = ctk.CTkButton(self.sidebar_frame, text = 'VPN', command=lambda:self.test_slider_button_clicked('vpn'))
        self.sidebar_vpn_button.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_twitter_button = ctk.CTkButton(self.sidebar_frame, text = 'Twitter', command=lambda:self.test_slider_button_clicked('twitter'))
        self.sidebar_twitter_button.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_logout_button = ctk.CTkButton(self.sidebar_frame, text = 'Log Out', command=lambda:self.test_slider_button_clicked('logout'))
        self.sidebar_logout_button.grid(row=5, column=0, padx=20, pady=10)

        # create textbox
        self.textbox = ctk.CTkTextbox(self, width=150)
        self.textbox.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")

        # create options frame
        self.slider_options_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.slider_options_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_options_frame.grid_columnconfigure(0, weight=1)
        self.slider_options_frame.grid_rowconfigure(4, weight=1)

        # create main entry and button
        self.entry = ctk.CTkEntry(self, placeholder_text="Entry your text here")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.entry_button_send = ctk.CTkButton(master=self, text="Send",fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.test_input_message_in_textbox)
        self.entry_button_send.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # appearance mode labels
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                    command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                            command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def test_slider_button_clicked(self, button):

        def increase(self):
            value = int(self.email_entry.get())
            self.email_entry.delete(0, ctk.END)
            self.email_entry.insert(0, str(value + 1))

        def decrease(self):
            value = int(self.email_entry.get())
            self.email_entry.delete(0, ctk.END)
            self.email_entry.insert(0, str(value - 1))

        for widget in self.slider_options_frame.winfo_children():
            widget.destroy()

        if button == 'email':
            #disable and enable other buttons
            self.sidebar_email_button.configure(state='disabled')
            self.sidebar_vpn_button.configure(state='normal')
            self.sidebar_twitter_button.configure(state='normal')
            self.sidebar_logout_button.configure(state='normal')

            self.email_label_option = ctk.CTkLabel(self.slider_options_frame, text='Emails', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
            self.email_label_option.grid(row=0, column=0, padx=(10,10), pady=(10,10), columnspan=5)

            self.email_label_create = ctk.CTkLabel(self.slider_options_frame, text='Create accounts: ', justify='left')
            self.email_label_create.grid(row=1, column=0, padx=(20,10), pady=(20,10), sticky="w")

            self.email_entry = ctk.CTkEntry(self.slider_options_frame, width=30)
            self.email_entry.insert(0, "0")
            self.email_entry.grid(row=1, column=0, padx=(20,10), pady=(20,10), sticky="e")

            self.email_increase_button = ctk.CTkButton(self.slider_options_frame, text='+', command=lambda:increase(self), width=2)
            self.email_increase_button.grid(row=1, column=1, padx=(20,10), pady=(20,10))

            self.email_decrease_button = ctk.CTkButton(self.slider_options_frame, text='-', command=lambda:decrease(self), width=2)
            self.email_decrease_button.grid(row=1, column=2, padx=(20,10), pady=(20,10))

            self.email_create_button = ctk.CTkButton(self.slider_options_frame, text="Create")
            self.email_create_button.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        elif button == 'vpn':
            #disable and enable other buttons
            self.sidebar_vpn_button.configure(state='disabled')
            self.sidebar_email_button.configure(state='normal')
            self.sidebar_twitter_button.configure(state='normal')
            self.sidebar_logout_button.configure(state='normal')

            self.vpn_label_option = ctk.CTkLabel(self.slider_options_frame, text='Vpn', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
            self.vpn_label_option.grid(row=0, column=0, padx=(10,10), pady=(10,10), columnspan=5)

            self.vpn_connect_button = ctk.CTkButton(self.slider_options_frame, text="CONNECT VPN")
            self.vpn_connect_button.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        elif button == 'twitter':
            #disable and enable other buttons
            self.sidebar_twitter_button.configure(state='disabled')
            self.sidebar_vpn_button.configure(state='normal')
            self.sidebar_email_button.configure(state='normal')
            self.sidebar_logout_button.configure(state='normal')

            #label option selected
            self.twitter_label_option = ctk.CTkLabel(self.slider_options_frame, text='Twitter', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
            self.twitter_label_option.grid(row=0, column=0, padx=(10,10), pady=(10,10), columnspan=5)

            self.twitter_label_accounts = ctk.CTkLabel(
                self.slider_options_frame,
                text=f'Available accounts: {self.test_return_available_accounts_twitter()}',
                justify='left',
            )
            self.twitter_label_accounts.grid(row=1, column=0, padx=(20,10), pady=(20,10), sticky="w")

            self.twitter_label_interactions = ctk.CTkLabel(self.slider_options_frame, text='Select interactions: ', justify='right')
            self.twitter_label_interactions.grid(row=1, column=0, padx=(20,10), pady=(20,10), sticky="e")

            self.twitter_button_like = ctk.CTkButton(self.slider_options_frame, text="Like")
            self.twitter_button_like.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.twitter_button_rt = ctk.CTkButton(self.slider_options_frame, text="Retweet",)
            self.twitter_button_rt.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.twitter_button_cmnt = ctk.CTkButton(self.slider_options_frame, text="Comment")
            self.twitter_button_cmnt.grid(row=4, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        elif button == 'logout':
            #disable and enable other buttons
            self.sidebar_logout_button.configure(state='disabled')
            self.sidebar_vpn_button.configure(state='normal')
            self.sidebar_twitter_button.configure(state='normal')
            self.sidebar_email_button.configure(state='normal')

            #label option selected
            self.logout_label_option = ctk.CTkLabel(self.slider_options_frame, text='LogOut', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
            self.logout_label_option.grid(row=0, column=0, padx=(10,10), pady=(10,10), columnspan=5)

            self.logout_label_quest = ctk.CTkLabel(self.slider_options_frame, text="Are you sure?", justify="center")
            self.logout_label_quest.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), columnspan=4)

            #button option selected
            self.logout_button_yes = ctk.CTkButton(self.slider_options_frame, text="Yes", anchor='center')
            self.logout_button_yes.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="w")

            self.logout_button_no = ctk.CTkButton(self.slider_options_frame, text="No", anchor='center')
            self.logout_button_no.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="e")
    
    def test_return_variable(self):
        return 'Testing'

    def test_input_message_in_textbox(self):
        date_time = datetime.datetime.now()
        self.textbox.insert("0.0", f'[{date_time}] $: ' + f'{self.entry.get()} ' + self.test_return_variable() + '\n\n')
        self.entry.delete(0, ctk.END)     

    def test_return_available_accounts_twitter(self):
        return 5   

if __name__ == "__main__":

    # Appearance window tkinter app
    ctk.set_appearance_mode('light') # Modes: system (default), light, dark
    ctk.set_default_color_theme('green') # Themes: blue (default), dark-blue, green

    # Create main window tkinter app
    app_window = App()
    app_window.mainloop()