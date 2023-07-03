import temp
import customtkinter as ctk
import FirebaseFunctions.firebaseDatabase as fdb
import ctk_app_functions as ctkfun
from PIL import Image

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

def splitEmail(email):
    name, domain = email.split("@")
    return name, domain

email_global = temp.get_email()
password_global = temp.get_password()
status_global = temp.get_vpn_status()
location_global = temp.get_vpn_location()
ip_global = temp.get_vpn_ip()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("BotNet Twitter")
        self.geometry('1100x580')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # label sidebar frame
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Options", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # sidebar buttons
        self.sidebar_help_button = ctk.CTkButton(self.sidebar_frame, text="Help", command=lambda:self.sidebar_button_clicked('help'))
        self.sidebar_help_button.grid(row=0, column=0, padx=20, pady=10)
        self.sidebar_accounts_button = ctk.CTkButton(self.sidebar_frame, text="Accounts", command=lambda:self.sidebar_button_clicked('accounts'))
        self.sidebar_accounts_button.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_unlock_button = ctk.CTkButton(self.sidebar_frame, text="Unlock Accounts", command=lambda:self.sidebar_button_clicked('unlock'))
        self.sidebar_unlock_button.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_vpn_button = ctk.CTkButton(self.sidebar_frame, text="VPN", command=lambda:self.sidebar_button_clicked('vpn'))
        self.sidebar_vpn_button.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_twitter_button = ctk.CTkButton(self.sidebar_frame, text="Twitter", command=lambda:self.sidebar_button_clicked('twitter'))
        self.sidebar_twitter_button.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_logout_button = ctk.CTkButton(self.sidebar_frame, text="LogOut", command=lambda:self.sidebar_button_clicked('logout'))
        self.sidebar_logout_button.grid(row=5, column=0, padx=20, pady=10)
        
        #sidebar appearance mode
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

        # create interactive options frame
        self.options_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.options_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.options_frame.grid_columnconfigure(0, weight=1)
        self.options_frame.grid_rowconfigure(4, weight=1)
        
        # welcome image on options frame
        welcome_image = ctk.CTkImage(light_image=Image.open("GraphicUI/images/welmoce_light.png"),
                                dark_image=Image.open("GraphicUI/images/welcome_dark.png"),
                                size=(800, 300))

        welcome_image_label = ctk.CTkLabel(self.options_frame, image=welcome_image, text="")
        welcome_image_label.pack(anchor="center", expand=True)

        # create textbox frame
        ctkfun.setInstance(self)
        ctkfun.create_textbox_entry()

        # create profile data frame
        self.profile_frame = ctk.CTkFrame(self)
        self.profile_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_profile_data = ctk.CTkLabel(master=self.profile_frame, text="User Info", font=ctk.CTkFont(size=13, weight="bold"))
        self.label_profile_data.grid(row=0, column=2, padx=20, pady=0, sticky="")
        #! we call the function to obtain name and domain
        name, domain = splitEmail(email_global)
        self.label_profile_user = ctk.CTkLabel(master=self.profile_frame, text=f"User: {name}")
        self.label_profile_user.grid(row=1, column=2, padx=20, pady=0, sticky="")
        self.label_profile_name = ctk.CTkLabel(master=self.profile_frame, text=f"Domain: {domain}")
        self.label_profile_name.grid(row=2, column=2, padx=20, pady=0, sticky="")
        self.label_profile_interactions = ctk.CTkLabel(master=self.profile_frame, text=f"Interactions Available: {fdb.get_count_values_unlocked(email_global, password_global)}")
        self.label_profile_interactions.grid(row=3, column=2, padx=20, pady=0, sticky="")
        self.label_profile_locked = ctk.CTkLabel(master=self.profile_frame, text=f"Locked accounts: {fdb.get_count_values_locked(email_global, password_global)}")
        self.label_profile_locked.grid(row=4, column=2, padx=20, pady=0, sticky="")
        self.label_profile_vpn_status = ctk.CTkLabel(master=self.profile_frame, text=status_global)
        self.label_profile_vpn_status.grid(row=5, column=2, padx=20, pady=0, sticky="")
        self.label_profile_vpn_location = ctk.CTkLabel(master=self.profile_frame, text=location_global)
        self.label_profile_vpn_location.grid(row=6, column=2, padx=20, pady=0, sticky="")
        self.label_profile_vpn_ip = ctk.CTkLabel(master=self.profile_frame, text=ip_global)
        self.label_profile_vpn_ip.grid(row=7, column=2, padx=20, pady=0, sticky="")

        # create checkbox and switch frame
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 10), sticky="nsew")
        
        my_image = ctk.CTkImage(light_image=Image.open("GraphicUI/images/botnet_light.png"),
                                dark_image=Image.open("GraphicUI/images/botnet_dark.png"),
                                size=(100, 100))

        image_label = ctk.CTkLabel(self.image_frame, image=my_image, text="")
        image_label.pack(anchor="center", expand=True)

        github_image_keyooner = ctk.CTkImage(light_image=Image.open("GraphicUI/images/github_keyooner_light.png"),
                                dark_image=Image.open("GraphicUI/images/github_keyooner_dark.png"),
                                size=(80, 30))
        
        github_image_label_keyooner = ctk.CTkLabel(self.image_frame, image=github_image_keyooner, text="", cursor="hand2")
        github_image_label_keyooner.pack(side="left", expand=True)

        github_image_label_keyooner.bind("<Button-1>", lambda event: ctkfun.open_url("https://github.com/keyooner"))

        github_image_dani5fdez = ctk.CTkImage(light_image=Image.open("GraphicUI/images/github_dani5fdez_light.png"),
                                dark_image=Image.open("GraphicUI/images/github_dani5fdez_dark.png"),
                                size=(80, 30))
        
        github_image_label_dani5fdez = ctk.CTkLabel(self.image_frame, image=github_image_dani5fdez, text="", cursor="hand2")
        github_image_label_dani5fdez.pack(side="right", expand=True)

        github_image_label_dani5fdez.bind("<Button-1>", lambda event: ctkfun.open_url("https://github.com/dani5fdez"))
        

#########################################################################################################################################################
################################################ BASIC FUNCTIONS ########################################################################################
#########################################################################################################################################################

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

        if button == 'help':
            self.help_option_button_clicked()

        elif button == 'accounts':
            self.accounts_option_button_clicked()
        
        elif button == 'unlock':
            self.unlock_option_button_clicked()

        elif button == 'vpn':
            self.vpn_option_button_clicked()

        elif button == 'twitter':
            self.twitter_option_button_clicked()

        elif button == 'logout':
            self.logout_option_button_clicked()

    def help_option_button_clicked(self):
        ctkfun.help_option_content(self.options_frame)
        ctkfun.disable_option_button('help', self.sidebar_help_button, 
                                    self.sidebar_accounts_button, self.sidebar_unlock_button, 
                                    self.sidebar_vpn_button, self.sidebar_twitter_button, 
                                    self.sidebar_logout_button)

    def accounts_option_button_clicked(self):
        ctkfun.accounts_option_content(self.options_frame)
        ctkfun.disable_option_button('accounts', self.sidebar_help_button, 
                                    self.sidebar_accounts_button, self.sidebar_unlock_button, 
                                    self.sidebar_vpn_button, self.sidebar_twitter_button, 
                                    self.sidebar_logout_button)

    def unlock_option_button_clicked(self):
        ctkfun.unlock_option_content(self.options_frame)
        ctkfun.disable_option_button('unlock', self.sidebar_help_button, 
                                    self.sidebar_accounts_button, self.sidebar_unlock_button, 
                                    self.sidebar_vpn_button, self.sidebar_twitter_button, 
                                    self.sidebar_logout_button)  

    def vpn_option_button_clicked(self):
        ctkfun.vpn_option_content(self.options_frame, self.label_profile_vpn_status, self.label_profile_vpn_location, self.label_profile_vpn_ip)
        ctkfun.disable_option_button('vpn', self.sidebar_help_button, 
                                    self.sidebar_accounts_button, self.sidebar_unlock_button, 
                                    self.sidebar_vpn_button, self.sidebar_twitter_button, 
                                    self.sidebar_logout_button)

    def twitter_option_button_clicked(self):
        ctkfun.twitter_option_content(self.options_frame, self)
        ctkfun.disable_option_button('twitter', self.sidebar_help_button, 
                                    self.sidebar_accounts_button, self.sidebar_unlock_button, 
                                    self.sidebar_vpn_button, self.sidebar_twitter_button, 
                                    self.sidebar_logout_button)

    def logout_option_button_clicked(self):
        ctkfun.logout_option_content(self.options_frame, self) 
        ctkfun.disable_option_button('logout', self.sidebar_help_button, 
                                    self.sidebar_accounts_button, self.sidebar_unlock_button, 
                                    self.sidebar_vpn_button, self.sidebar_twitter_button, 
                                    self.sidebar_logout_button)
            

if __name__ == "__main__":
    app = App()
    app.mainloop()