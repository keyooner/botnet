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
        self.sidebar_email_button = ctk.CTkButton(self.sidebar_frame, text = 'Emails', command=self.sidebar_button_event)
        self.sidebar_email_button.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_vpn_button = ctk.CTkButton(self.sidebar_frame, text = 'VPN', command=self.sidebar_button_event)
        self.sidebar_vpn_button.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_twitter_button = ctk.CTkButton(self.sidebar_frame, text = 'Twitter', command=self.sidebar_button_event)
        self.sidebar_twitter_button.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_logout_button = ctk.CTkButton(self.sidebar_frame, text = 'Log Out', command=self.sidebar_button_event)
        self.sidebar_logout_button.grid(row=5, column=0, padx=20, pady=10)

        # create textbox
        self.textbox = ctk.CTkTextbox(self, width=150)
        self.textbox.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")

        # create options frame
        self.slider_options_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.slider_options_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_options_frame.grid_columnconfigure(0, weight=1)
        self.slider_options_frame.grid_rowconfigure(4, weight=1)

        def option_twitter(self):
            self.seg_button_1 = ctk.CTkSegmentedButton(self.slider_options_frame)
            self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.progressbar_1 = ctk.CTkProgressBar(self.slider_options_frame)
            self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.progressbar_2 = ctk.CTkProgressBar(self.slider_options_frame)
            self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.slider_1 = ctk.CTkSlider(self.slider_options_frame, from_=0, to=1, number_of_steps=4)
            self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.slider_2 = ctk.CTkSlider(self.slider_options_frame, orientation="vertical")
            self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
            self.progressbar_3 = ctk.CTkProgressBar(self.slider_options_frame, orientation="vertical")
            self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        def option_emails(self):
            self.seg_button_1 = ctk.CTkButton(self.slider_options_frame, text="Text Here")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.seg_button_2 = ctk.CTkButton(self.slider_options_frame, text="Text Here")
            self.seg_button_2.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.seg_button_3 = ctk.CTkButton(self.slider_options_frame, text="Text Here",)
            self.seg_button_3.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
            self.seg_button_4 = ctk.CTkButton(self.slider_options_frame, text="Text Here")
            self.seg_button_4.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        option_twitter(self)
        #option_emails(self)

        # create main entry and button
        self.entry = ctk.CTkEntry(self, placeholder_text="Entry your text here")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(master=self, text="Send",fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.test_input_message_in_textbox)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

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

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def test_return_variable(self):
        return 'Testing'

    def test_input_message_in_textbox(self):
        date_time = datetime.datetime.now()
        self.textbox.insert("0.0", f'[{date_time}] $: ' + f'{self.entry.get()} ' + self.test_return_variable() + '\n\n')
        self.entry.delete(0, ctk.END)

if __name__ == "__main__":

    # Appearance window tkinter app
    ctk.set_appearance_mode('light') # Modes: system (default), light, dark
    ctk.set_default_color_theme('green') # Themes: blue (default), dark-blue, green

    # Create main window tkinter app
    app_window = App()
    app_window.mainloop()