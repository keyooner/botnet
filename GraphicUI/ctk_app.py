import re
import temp
import customtkinter as ctk
import FirebaseFunctions.firebaseDatabase as fdb
import TwitterFunctions.seleniumFunctions as sf
import FirebaseFunctions.firebaseAuthentication as fba
import ctk_app_functions as ctkfun
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

#vpn_switch_var = ctk.StringVar(value="off") #no me funciona la variable

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

def splitEmail(email):
    name, domain = email.split("@")
    return name, domain

def get_driver():
    return webdriver.Chrome(service = Service(ChromeDriverManager().install()))

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
        self.textbox_frame= ctk.CTkFrame(self, fg_color="transparent")
        self.textbox_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox = ctk.CTkTextbox(self.textbox_frame, width=700, state="disabled")
        self.textbox.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.textbox_frame.columnconfigure(0, weight=1)
        self.textbox_frame.rowconfigure(0, weight=1)

        # create main entry and button
        self.entry = ctk.CTkEntry(self, placeholder_text="Entry your text here")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.entry_button = ctk.CTkButton(master=self, fg_color="transparent", text="Send", border_width=2, text_color=("gray10", "#DCE4EE"), command=lambda: ctkfun.input_message_in_textbox(self.textbox, self.entry))
        self.entry_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create profile data frame
        self.profile_frame = ctk.CTkFrame(self)
        self.profile_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_profile_data = ctk.CTkLabel(master=self.profile_frame, text="User Info", font=ctk.CTkFont(size=13, weight="bold"))
        self.label_profile_data.grid(row=0, column=2, padx=20, pady=0, sticky="")
        #! we call the function to obtain name and domain
        name, domain = splitEmail(temp.get_email())
        self.label_profile_user = ctk.CTkLabel(master=self.profile_frame, text=f"User: {name}")
        self.label_profile_user.grid(row=1, column=2, padx=20, pady=0, sticky="")
        self.label_profile_name = ctk.CTkLabel(master=self.profile_frame, text=f"Domain: {domain}")
        self.label_profile_name.grid(row=2, column=2, padx=20, pady=0, sticky="")
        self.label_profile_interactions = ctk.CTkLabel(master=self.profile_frame, text=f"Interactions Available: {fdb.get_values_unlocked(temp.get_email(), temp.get_password())}")
        self.label_profile_interactions.grid(row=3, column=2, padx=20, pady=0, sticky="")
        self.label_profile_vpn_status = ctk.CTkLabel(master=self.profile_frame, text=temp.get_vpn_status())
        self.label_profile_vpn_status.grid(row=4, column=2, padx=20, pady=0, sticky="")
        self.label_profile_vpn_location = ctk.CTkLabel(master=self.profile_frame, text=temp.get_vpn_location())
        self.label_profile_vpn_location.grid(row=5, column=2, padx=20, pady=0, sticky="")
        self.label_profile_vpn_ip = ctk.CTkLabel(master=self.profile_frame, text=temp.get_vpn_ip())
        self.label_profile_vpn_ip.grid(row=6, column=2, padx=20, pady=0, sticky="")

        # create checkbox and switch frame
        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        
        my_image = ctk.CTkImage(light_image=Image.open("GraphicUI/images/botnet_light.png"),
                                dark_image=Image.open("GraphicUI/images/botnet_dark.png"),
                                size=(100, 100))

        image_label = ctk.CTkLabel(self.image_frame, image=my_image, text="")
        image_label.pack(anchor="center", expand=True)

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

        if button == 'accounts':
            self.accounts_option_button_clicked()

        elif button == 'vpn':
            self.vpn_option_button_clicked()

        elif button == 'twitter':
            self.twitter_option_button_clicked()

        elif button == 'logout':
            self.logout_option_button_clicked()

    def accounts_option_button_clicked(self):

        ctkfun.disable_option_button('accounts', self.sidebar_vpn_button, self.sidebar_accounts_button, self.sidebar_twitter_button, self.sidebar_logout_button)
        ctkfun.accounts_option_content(self.options_frame)

    
    def vpn_option_button_clicked(self):
        ctkfun.disable_option_button('vpn', self.sidebar_vpn_button, self.sidebar_accounts_button, self.sidebar_twitter_button, self.sidebar_logout_button)
        ctkfun.vpn_option_content(self.options_frame, self.label_profile_vpn_status, self.label_profile_vpn_location, self.label_profile_vpn_ip)

    def twitter_option_button_clicked(self):
        
        ctkfun.disable_option_button('twitter', self.sidebar_vpn_button, self.sidebar_accounts_button, self.sidebar_twitter_button, self.sidebar_logout_button)

        # label option selected
        self.twitter_label_option = ctk.CTkLabel(self.options_frame, text='Twitter', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        self.twitter_label_option.pack(padx=(10,10), pady=(10,10))

        self.add_entry_valuable_button(0,self.return_available_accounts_twitter())

        # create urls container frame
        urls_container_frame = ctk.CTkFrame(self.options_frame)
        urls_container_frame.pack(fill="x")
        
        # create entry urls
        if temp.get_twitter_url() == None:
            self.entry_twitter_url = ctk.CTkEntry(urls_container_frame, placeholder_text="Entry your twitter url here")
            self.twitter_url_button = ctk.CTkButton(urls_container_frame, text="Check Url", command=lambda:self.verify_twitter_url(self.entry_twitter_url.get()))
            temp.set_twitter_url(None)
        else:
            twitter_url_input_variable = ctk.StringVar()
            twitter_url_input_variable.set(temp.get_twitter_url())
            twitter_placeholder_url_input_variable = ctk.StringVar()
            twitter_placeholder_url_input_variable.set("Entry your twitter url here")
            self.entry_twitter_url = ctk.CTkEntry(urls_container_frame, textvariable=twitter_url_input_variable, placeholder_text=twitter_placeholder_url_input_variable)
            self.twitter_url_button = ctk.CTkButton(urls_container_frame, text="Check Url", command=lambda:self.verify_twitter_url(self.entry_twitter_url.get()))
        
        self.entry_twitter_url.pack(side="left", padx=(20,10), pady=(20,10), fill="x", expand=True)
        self.twitter_url_button.pack(side="left", padx=(20,10), pady=(20,10), fill="x", expand=True)

        # create checkboxes
        checkbox_container_frame = ctk.CTkFrame(self.options_frame)
        checkbox_container_frame.pack(fill="x")

        if temp.get_twitter_actions() == None:
            self.twitter_checkbox_like = ctk.CTkCheckBox(checkbox_container_frame, text='Like', state='disabled')
            self.twitter_checkbox_rt = ctk.CTkCheckBox(checkbox_container_frame, text='Retweet', state='disabled')
            self.twitter_checkbox_cmnt = ctk.CTkCheckBox(checkbox_container_frame, text='Comment', state='disabled')
            temp.set_twitter_actions(None)
        else:
            self.twitter_checkbox_like = ctk.CTkCheckBox(checkbox_container_frame, text='Like', state='normal')
            self.twitter_checkbox_rt = ctk.CTkCheckBox(checkbox_container_frame, text='Retweet', state='normal')
            self.twitter_checkbox_cmnt = ctk.CTkCheckBox(checkbox_container_frame, text='Comment', state='normal')

        self.twitter_checkbox_like.pack(side="left", padx=(20,10), pady=(20,10))
        self.twitter_checkbox_rt.pack(side="left", padx=(20,10), pady=(20,10))
        self.twitter_checkbox_cmnt.pack(side="left", padx=(20,10), pady=(20,10))


        if temp.get_twitter_follow() == None:
            self.twitter_checkbox_follow = ctk.CTkCheckBox(checkbox_container_frame, text='Follow', state='disabled')
            temp.set_twitter_follow(None)
        else:
            self.twitter_checkbox_follow = ctk.CTkCheckBox(checkbox_container_frame, text='Follow', state='normal')

        if ((temp.get_twitter_actions()) == None) and ((temp.get_twitter_follow()) == None):
            self.twitter_button_action = ctk.CTkButton(checkbox_container_frame, text="Do it", state='disabled', command = self.twitter_checkCheckbox)
        else:
            self.twitter_button_action = ctk.CTkButton(checkbox_container_frame, text="Do it", state='normal', command = self.twitter_checkCheckbox)

        self.twitter_checkbox_follow.pack(side="left", padx=(20,10), pady=(20,10))
        self.twitter_button_action.pack(side="left", padx=(20,10), pady=(20,10), fill="x", expand=True)
                
    def return_available_accounts_twitter(self):
        #! CAMBIAR!! POR --> EMAIL, PASSWORD
        return fdb.get_values_unlocked(temp.get_email(), temp.get_password())

    def add_entry_valuable_button(self, min_value, max_value):
        
        def validate_entry(text):
            if (text.isdigit() or text == ""):
                return text == "" or int(text) <= self.return_available_accounts_twitter()
            else:
                return False

        validate_command = self.options_frame.register(validate_entry)

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

        container = ctk.CTkFrame(self.options_frame)
        container.pack(fill="x")

        self.twitter_label_accounts = ctk.CTkLabel(
            container,
            text=f'Max interactions available: {self.return_available_accounts_twitter()}',
        )
        self.twitter_label_accounts.pack(side="top", padx=5, pady=5)

        self.twitter_label_interactions = ctk.CTkLabel(container, text="Select number of interactions: ")
        self.twitter_label_interactions.pack(side="left", padx=5, pady=5, anchor="center")

        self.button_entry = ctk.CTkEntry(container, width=30, validate="key", validatecommand=(validate_command, "%P"))

        self.button_entry.pack(side="left", padx=5, pady=5, anchor="center")

        self.button_increase = ctk.CTkButton(container, text='+', command=lambda:increase(self), width=2)
        self.button_increase.pack(side="left", padx=5, pady=5, anchor="center")

        self.button_decrease = ctk.CTkButton(container, text='-', command=lambda:decrease(self), width=2)
        self.button_decrease.pack(side="left", padx=5, pady=5, anchor="center")

        if fdb.get_values_unlocked(temp.get_email(), temp.get_password()) < 1:
            self.button_entry.configure(state="disabled")
            self.button_increase.configure(state="disabled")
            self.button_decrease.configure(state="disabled")
        else:
            if temp.get_twitter_interactions() != None:
                self.button_entry.insert(temp.get_twitter_interactions(), f"{temp.get_twitter_interactions()}")
            else:
                self.button_entry.insert(1, "1")
    
    def twitter_checkCheckbox(self):
        if self.twitter_url_verified(self.entry_twitter_url.get()) in [
            'actions',
            'follow',
        ]:

            if  self.twitter_checkbox_cmnt.get() == 1:
                self.twitter_popup_comment_window()

            if self.twitter_checkbox_like.get() == 1:
                print(sf.action_n_times(get_driver(), fdb.get_values_for_actions(temp.get_email(), temp.get_password(), int(self.button_entry.get())), self.entry_twitter_url.get(), 
                            self.entry_twitter_url.get(), 2))

    def twitter_popup_comment_window(self):
        entry_value = int(self.button_entry.get())
        popup_comment_window = ctk.CTkToplevel()
        popup_comment_window.title("Comments window")
        popup_comment_window.geometry("250x300")
        popup_comment_window.focus()

        # create scrollable frame
        self.scrollable_popup_frame = ctk.CTkScrollableFrame(popup_comment_window, label_text="Comments")
        self.scrollable_popup_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_popup_frame.grid_columnconfigure(0, weight=2)
        self.scrollable_frame_entries = []
        for i in range(entry_value):
            self.comment_entries = ctk.CTkEntry(master=self.scrollable_popup_frame, placeholder_text=f"Type your comment {i+1}", width=300)
            self.comment_entries.grid(row=i, column=0, padx=10, pady=(0, 20))
            setattr(self, f"comment_entries_{i}", self.comment_entries)
            self.scrollable_frame_entries.append(self.comment_entries)

        popup_comment_window_button = ctk.CTkButton(self.scrollable_popup_frame, text='Go!')
        popup_comment_window_button.grid(row=entry_value, column=0)
        
    def twitter_url_verified(self, url):
        tweet_url = r'^https?://twitter\.com/[A-Za-z0-9_]{1,15}/status/\d+$'
        follow_url = r'^https?://twitter\.com/[A-Za-z0-9_]{1,15}$'
        if re.match(tweet_url, url) and (int(self.button_entry.get()) > 0):
            return "actions"
        elif re.match(follow_url, url) and (int(self.button_entry.get()) > 0):
            return "follow"

    def verify_twitter_url(self, url):

        if self.twitter_url_verified(url) == 'actions':
            self._extracted_from_verify_twitter_url_4('normal')
            self.twitter_checkbox_follow.configure(state='disabled')
            self.twitter_checkbox_follow.deselect()
            self.entry_twitter_url.configure(border_color="green")
            temp.set_twitter_actions(1)
        elif self.twitter_url_verified(url) == 'follow':
            self.twitter_checkbox_follow.configure(state='normal')
            self._extracted_from_verify_twitter_url_4('disabled')
            self.twitter_button_action.configure(state='normal')
            self.twitter_checkbox_like.deselect()
            self.twitter_checkbox_rt.deselect()
            self.twitter_checkbox_cmnt.deselect()
            self.entry_twitter_url.configure(border_color="green")
            temp.set_twitter_follow(1)
        else:
            self._extracted_from_verify_twitter_url_4('disabled')
            self.twitter_checkbox_like.deselect()
            self.twitter_checkbox_rt.deselect()
            self.twitter_checkbox_cmnt.deselect()
            self.twitter_checkbox_follow.configure(state='disabled')
            self.twitter_checkbox_follow.deselect()
            self.entry_twitter_url.configure(border_color="red")
            temp.set_twitter_actions(None)
            temp.set_twitter_follow(None)
        if not self.entry_twitter_url.get():
            temp.set_twitter_url(None)
        else:
            temp.set_twitter_url(self.entry_twitter_url.get())
        temp.set_twitter_interactions(self.button_entry.get())

        

    # TODO Rename this here and in `verify_twitter_url`
    def _extracted_from_verify_twitter_url_4(self, state):
        self.twitter_checkbox_like.configure(state=state)
        self.twitter_checkbox_rt.configure(state=state)
        self.twitter_checkbox_cmnt.configure(state=state)
        self.twitter_button_action.configure(state=state)
                

    def logout_option_button_clicked(self):
        ctkfun.disable_option_button('logout', self.sidebar_vpn_button, self.sidebar_accounts_button, self.sidebar_twitter_button, self.sidebar_logout_button)
        ctkfun.logout_option_content(self.options_frame, self.action_logOut)

    def close_main_window(self):
        self.destroy()

    def action_logOut(self):
        self.close_main_window()
        ctkfun.logout_user()        

if __name__ == "__main__":
    app = App()
    app.mainloop()