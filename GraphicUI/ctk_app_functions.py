import io
import re
import sys
import temp
import datetime
import webbrowser
import customtkinter as ctk
import TwitterFunctions.twitterActions as sf
import FirebaseFunctions.firebaseFaster as ff
import requests
import EmailFunctions.createEmail as ce
from PIL import Image
from time import sleep
from CTkTable import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN

instance = None
instance_2 = None
scrollable_frame_entries = []
comments_list = []
email_global_user = temp.get_email()
password_global_user = temp.get_password()

def get_driver():
        return webdriver.Chrome(service = Service(ChromeDriverManager().install()))

def setInstance(instance_new):
        global instance
        instance = instance_new
        
def getInstance():
        return instance

def set_scrollable_frame_entries(scrollable_frame_entries_new):
        global scrollable_frame_entries
        scrollable_frame_entries = scrollable_frame_entries_new

def get_scrollable_frame_entries():
        return scrollable_frame_entries

def set_comments_list(comments_list_new):
        global comments_list
        comments_list = comments_list_new

def get_comments_list():
        return comments_list

def create_textbox_entry():
        instance = getInstance()
        textbox_frame = ctk.CTkFrame(instance, fg_color="transparent")
        textbox_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        textbox = ctk.CTkTextbox(textbox_frame, width=700, state="disabled")
        textbox.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")
        
        textbox_frame.columnconfigure(0, weight=1)
        textbox_frame.rowconfigure(0, weight=1)
        
        setInstance(textbox)

def input_message_in_textbox(message):
        self = getInstance()
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.configure(state="normal")
        self.insert("0.0", f"[{date_time}] $:" + f" {message}" "\n\n")
        self.configure(state="disabled")
        
        return message

############################################### HELP ##################################################

def open_url(url):
        webbrowser.open(url)

def help_label(options_frame):
        label_option = ctk.CTkLabel(options_frame, text='Help', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        label_option.pack(padx=(10,10), pady=(10,10))

def help_label_explain(options_frame):
        label_explain_1 = ctk.CTkLabel(options_frame, text='You can see a demo tutorial if you do click on the image', justify='center')
        label_explain_1.pack(padx=(10,10), pady=(10,10))

def help_image(options_frame):
        youtube_image = ctk.CTkImage(light_image=Image.open("GraphicUI/images/Tutorial_youtube_light.png"),
                                dark_image=Image.open("GraphicUI/images/Tutorial_youtube_dark.png"),
                                size=(200, 75))

        youtube_image = ctk.CTkButton(options_frame, corner_radius=0, height=40, border_spacing=10, text="",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=youtube_image, anchor="w", command=lambda:open_url("https://youtu.be/E7b5wbdzx6M"))
        youtube_image.pack(padx=(10,10), pady=(10,10))

def help_label_explain_2(options_frame):
        label_explain_2 = ctk.CTkLabel(options_frame, text='You can download a pdf tutorial if you do click on the document', justify='center')
        label_explain_2.pack(padx=(10,10), pady=(10,10))

def help_button_pdf_image(options_frame):
        pdf_image = ctk.CTkImage(light_image=Image.open("GraphicUI/images/pdf.png"),
                                dark_image=Image.open("GraphicUI/images/pdf.png"),
                                size=(20, 20))
        label_button_explain_2 = ctk.CTkButton(options_frame, corner_radius=0, height=40, border_spacing=10, text="Demo botnet twitter.pdf",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=pdf_image, anchor="w", command=lambda:open_url("https://github.com/keyooner/botnet/blob/main/Documentation/botnet_twitter_manual.pdf"))
        label_button_explain_2.pack(padx=(10,10), pady=(10,10))

def help_option_content(options_frame):
        
        help_label(options_frame)
        help_label_explain(options_frame)
        help_image(options_frame)
        help_label_explain_2(options_frame)
        help_button_pdf_image(options_frame)
        input_message_in_textbox("Opened help menu!")

############################################### ACCOUNTS ##################################################

def accounts_option_content(options_frame, label_profile_interactions, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        #create scrollable frame for table
        scrollable_table_frame = ctk.CTkScrollableFrame(options_frame, fg_color="transparent", label_text="Accounts")
        scrollable_table_frame.pack(side="top", padx=(20, 0), pady=(20, 0), fill="both", expand=True)
        scrollable_table_frame.grid_rowconfigure(0, weight=0)
        scrollable_table_frame.grid_columnconfigure(0, weight=1)
        scrollable_table_frame_values = []

        data = ff.update_values_unlocked_ff()
        header_values = [['             EMAIL            ', ' PASSWORD ', '      USERNAME      ']]
        header_table = CTkTable(scrollable_table_frame, row=1, column=3, values=header_values, header_color="#8370F7", hover=True)
        header_table.grid(row=0 % 3, column=0, padx=10, pady=(0, 20), sticky="ew")
        if data != 0:
                for i, key in enumerate(data.keys()):
                        account_data = data[key]
                        table_values = [[account_data['email'], [account_data['password']], account_data['user']]]
                        table_accounts_available = CTkTable(scrollable_table_frame, row=1, column=3, values=table_values, header_color="#2cc985", hover=True)
                        table_accounts_available.grid(row=i+1 % 3, column=0, padx=10, pady=(0, 20), sticky="ew")
                        scrollable_table_frame_values.append(table_accounts_available)

        # Adjust scrollable size
        scrollable_table_frame.update()

        #create frame for the button
        button_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        button_frame.pack(side="top", fill="x")

        #create button to create account
        create_account_button = ctk.CTkButton(button_frame, text="Create Account", command=lambda:createAccount(options_frame, label_profile_interactions, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip))
        create_account_button.pack(side="left", padx=(20, 10), pady=(10, 10), fill="x", expand=True)
        
        input_message_in_textbox("Opened unlocked accounts menu!")

def createAccount(options_frame, label_profile_interactions, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        try:
                actions_if_vpn(ff.get_preferences(), label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                while_check_internet()
                driver = get_driver()
                input_message_in_textbox("We are creating your account...")
                sleep(1)
                register = input_message_in_textbox(sf.registerUserTwitter(driver, email_global_user, password_global_user))
                driver.close()
                if register == "Create User! Ok!":
                        input_message_in_textbox(f"User: '{ff.get_last_user_create()}'. Has been created!")
                updateProfileInteractionsAvailable(label_profile_interactions)
                destroy_options(options_frame)
                accounts_option_content(options_frame, label_profile_interactions, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
        except TimeoutError:
                deleteAccountError()
        except requests.exceptions.Timeout:
                input_message_in_textbox("Error: Connection timed out.")
        except requests.exceptions.RequestException as e:
                input_message_in_textbox(f"Error: {e}")

def deleteAccountError():
        input_message_in_textbox("Something has failed with IMAP Server!")
        input_message_in_textbox("Deleting last account created...")
        email_delete = ff.get_last_email_create()
        ce.deleteMail(email_delete)
        ff.deleteValues()
        input_message_in_textbox("Account has been deleted!")               

def updateProfileInteractionsAvailable(label_profile_interactions):
        ff.set_values_unlocked_ff()
        label_profile_interactions.configure(text=f"Avaliable accounts: {ff.get_count_values_unlocked_ff()}")

def updateLockedAccounts(label_profile_locked):
        ff.set_values_locked_ff()
        label_profile_locked.configure(text = f"Locked accounts: {ff.get_count_values_locked_ff()}")

######################################## UNLOCK ACCOUNTS #############################################

def unlock_option_content(options_frame, label_profile_interactions, label_profile_locked, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        #create scrollable frame for table
        scrollable_table_frame = ctk.CTkScrollableFrame(options_frame, fg_color="transparent", label_text="Unlock Accounts")
        scrollable_table_frame.pack(side="top", padx=(20, 0), pady=(20, 0), fill="both", expand=True)
        scrollable_table_frame.grid_rowconfigure(0, weight=0)
        scrollable_table_frame.grid_columnconfigure(0, weight=1)
        scrollable_table_frame_values = []

        #accounts available
        ff.set_values_locked_ff()
        data = ff.get_values_locked_ff()
        header_values = [['             EMAIL            ', ' PASSWORD ', '      USERNAME      ']]
        header_table = CTkTable(scrollable_table_frame, row=1, column=3, values=header_values, header_color="#8370F7", hover=True)
        header_table.grid(row=0 % 3, column=0, padx=10, pady=(0, 20), sticky="ew")
        
        if data != 0:
                for i, key in enumerate(data.keys()):
                        account_data = data[key]
                        table_values = [[account_data['email'], [account_data['password']], account_data['user']]]
                        table_accounts_available = CTkTable(scrollable_table_frame, row=1, column=3, values=table_values, header_color="#2cc985", hover=True)
                        table_accounts_available.grid(row=i+1 % 3, column=0, padx=10, pady=(0, 20), sticky="ew")
                        scrollable_table_frame_values.append(table_accounts_available)

        # Adjust scrollable size
        scrollable_table_frame.update()

        #create frame for the button
        button_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        button_frame.pack(side="top", fill="x")

        #create button to unlock account
        create_account_button = ctk.CTkButton(button_frame, text="Check unlock accounts", command = lambda:twitter_check_unlocked_accounts(label_profile_interactions, label_profile_locked, options_frame, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip))
        create_account_button.pack(side="left", padx=(20, 10), pady=(10, 10), fill="x", expand=True)
        
        input_message_in_textbox("Opened locked accounts menu!")

############################################### VPN ##################################################

def vpn_first_frame_creation(options_frame):
        vpn_label_option = ctk.CTkLabel(options_frame, text='Vpn', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        vpn_label_option.pack(padx=(10,10), pady=(10,10))

        vpn_container_frame = ctk.CTkFrame(options_frame)
        vpn_container_frame.pack(fill="x", expand=True)

        vpn_switch_label = ctk.CTkLabel(master=vpn_container_frame, text="Do you want to use VPN?")
        vpn_switch_label.pack(side="left", padx=(10,10), pady=(10,10), fill="both", expand=True)
        
        return vpn_container_frame

def handle_vpn_switch(vpn_switch_var):
        if vpn_switch_var.get() == 'on':
                _extracted_from_handle_vpn_switch_3('on')
        else:
                _extracted_from_handle_vpn_switch_3('off')

# TODO Rename this here and in `handle_vpn_switch`
def _extracted_from_handle_vpn_switch_3(arg0):
        temp.set_vpn_mode(arg0)
        temp.set_preferences_user(arg0)
        ff.set_preferences(arg0)
        
def vpn_switch_creation(vpn_container_frame):
        vpn_switch_var = ctk.StringVar(value=ff.get_preferences())
        
        temp.set_vpn_mode(ff.get_preferences())
        
        vpn_switch = ctk.CTkSwitch(master=vpn_container_frame, 
                                        text="Vpn OFF/ON", 
                                        command=lambda:[handle_vpn_switch(vpn_switch_var)], variable=vpn_switch_var, onvalue='on', offvalue='off')
        vpn_switch.pack(side="left", padx=(20, 10), pady=(10, 10), fill="both", expand=True)

def vpn_switch_status_label_creation(vpn_container_frame_2):
        vpn_switch_status_label = ctk.CTkLabel(vpn_container_frame_2, text=temp.get_vpn_status(), justify='center')
        vpn_switch_status_label.pack(padx=(10,10), pady=(10,10))
        return vpn_switch_status_label

def vpn_second_frame_creation(options_frame):
        vpn_container_frame_2 = ctk.CTkFrame(options_frame)
        vpn_container_frame_2.pack(fill="x", expand=True)

        vpn_container_frame_3 = ctk.CTkFrame(options_frame)
        vpn_container_frame_3.pack(fill="x", expand=True)
        
        return vpn_container_frame_2, vpn_container_frame_3

def vpn_label_second_frame(vpn_container_frame_3):
        vpn_switch_location_label = ctk.CTkLabel(master=vpn_container_frame_3, text=temp.get_vpn_location())
        vpn_switch_location_label.pack(side="left", padx=(10,10), pady=(10,10), fill="both", expand=True)

        vpn_switch_ip_label = ctk.CTkLabel(master=vpn_container_frame_3, text=temp.get_vpn_ip())
        vpn_switch_ip_label.pack(side="left", padx=(10,10), pady=(10,10), fill="both", expand=True)
        
        return vpn_switch_location_label, vpn_switch_ip_label

def vpn_option_content(options_frame):
        
        vpn_container_frame = vpn_first_frame_creation(options_frame)
        
        vpn_container_frame_2, vpn_container_frame_3 = vpn_second_frame_creation(options_frame)
        
        vpn_switch_status_label = vpn_switch_status_label_creation(vpn_container_frame_2)

        vpn_switch_location_label, vpn_switch_ip_label = vpn_label_second_frame(vpn_container_frame_3)
        
        temp.set_vpn_values(vpn_switch_status_label, vpn_switch_location_label, vpn_switch_ip_label)
        
        vpn_switch_creation(vpn_container_frame)
        
        input_message_in_textbox("Opened VPN menu!")
        
def values_for_first_condition():
        stdout = sys.stdout
        exit_prints = io.StringIO()
        sys.stdout = exit_prints
        initialize_VPN(stored_settings=1)
        rotate_VPN()
        sys.stdout = stdout
        prints_exits = exit_prints.getvalue()
        vpn_location = re.search(r'Connecting you to\s*(.*?)\s*\.{3}', prints_exits)
        vpn_ip = re.search(r'your new ip-address is:\s*(.*)', prints_exits)
        
        return vpn_location, vpn_ip

def check_status_first_condition(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location,
                        vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):

        vpn_location, vpn_ip = values_for_first_condition()
        vpn_labels_on(
                vpn_location[1],
                vpn_ip[1],
                label_profile_vpn_status,
                vpn_switch_status_label,
                label_profile_vpn_location,
                vpn_switch_location_label,
                label_profile_vpn_ip,
                vpn_switch_ip_label,
        )

def check_status_second_condition(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location,
                        vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):
        terminate_VPN()
        vpn_labels_off(
                label_profile_vpn_status,
                vpn_switch_status_label,
                label_profile_vpn_location,
                vpn_switch_location_label,
                label_profile_vpn_ip,
                vpn_switch_ip_label,
        )
                
def check_status_vpn_mode(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location,
                        vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):
        if temp.get_vpn_mode() == 'on':
                check_status_first_condition(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location,
                        vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label)
        else:
                check_status_second_condition(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location,
                        vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label)
                
def vpn_connect_clicked(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location,
                        vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):
        temp.set_vpn_mode('on')
        temp.set_vpn_status('Connected')
        check_status_vpn_mode(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location,
                        vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label)
        
def vpn_labels_on(vpn_location, vpn_ip, label_profile_vpn_status, vpn_switch_status_label,
                label_profile_vpn_location, vpn_switch_location_label, label_profile_vpn_ip,
                vpn_switch_ip_label):
        
        temp.set_vpn_location(vpn_location)
        temp.set_vpn_ip(vpn_ip)
        vpn_configure(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location, vpn_switch_location_label,
                        label_profile_vpn_ip, vpn_switch_ip_label)        

def setVPN():
        temp.set_vpn_mode('off')
        temp.set_vpn_status("Disconnected")
        temp.set_vpn_location('')
        temp.set_vpn_ip('')

def getVPN():
        status = temp.get_vpn_status()
        location = temp.get_vpn_location()
        ip = temp.get_vpn_ip()
        return status, location, ip 

def vpn_labels_off(label_profile_vpn_status, 
                vpn_switch_status_label, label_profile_vpn_location, 
                vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):
        setVPN()
        vpn_configure(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location, vpn_switch_location_label,
                        label_profile_vpn_ip, vpn_switch_ip_label)

def vpn_configure(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location, vpn_switch_location_label,
                        label_profile_vpn_ip, vpn_switch_ip_label):
        status, location, ip = getVPN()
        get_status_color(status, label_profile_vpn_status)
        input_message_in_textbox(f"{status}")
        set_status(location, ip, label_profile_vpn_location, label_profile_vpn_ip)
        input_message_in_textbox(f"VPN {location}")
        input_message_in_textbox(f"VPN {ip}")

def set_status(location, ip, label_profile_vpn_location,label_profile_vpn_ip,):
        label_profile_vpn_location.configure(text=location)
        label_profile_vpn_ip.configure(text=ip)
        
def get_status_color(status, label_profile_vpn_status):
        if status == "VPN Status: Disconnected":
                label_profile_vpn_status.configure(text=status, text_color="#ff0000")
        else:
                label_profile_vpn_status.configure(text=status, text_color="#00bb2d")
        
############################################### TWITTER ##################################################

def create_label_interactions(entry_button_frame):
        twitter_label_interactions = ctk.CTkLabel(entry_button_frame, text="Select number of interactions: ")
        twitter_label_interactions.pack(side="left", padx=5, pady=5, anchor="center")

        return twitter_label_interactions

def create_label_accounts(entry_button_frame, avaliable_accounts):
        twitter_label_accounts = ctk.CTkLabel(
                entry_button_frame,
                text=f'Max interactions available: {avaliable_accounts}',
                )
        
        twitter_label_accounts.pack(side="top", padx=5, pady=5)
        temp.set_label_accounts(twitter_label_accounts)
        return twitter_label_accounts

def check_interactions(button_entry, button_increase, button_decrease):
        if ff.get_count_values_unlocked_ff() < 1:
                button_dissable(button_entry, button_increase, button_decrease)
        else:
                interactions = temp.get_button_status()
                if interactions != None:
                        button_entry.insert(interactions, f"{interactions}")
                else:
                        button_entry.insert(1, "1")

def get_url_twitter_option_content(options_frame):
        urls_container_frame = ctk.CTkFrame(options_frame)
        urls_container_frame.pack(fill="x")
        url = temp.get_twitter_url()
        return url, urls_container_frame

def create_entry_url(url, urls_container_frame, button_entry, twitter_checkbox_like, twitter_checkbox_rt, 
                twitter_checkbox_cmnt, twitter_checkbox_follow, twitter_button_action, twitter_label_accounts):
        if url == None:
                entry_twitter_url = ctk.CTkEntry(urls_container_frame, placeholder_text="Entry your twitter url here")
                twitter_url_button = ctk.CTkButton(urls_container_frame, text="Check Url", command =
                                                lambda:twitter_url_actions(entry_twitter_url.get(), entry_twitter_url, button_entry, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_checkbox_follow, twitter_button_action, twitter_label_accounts))
                temp.set_twitter_url(None)
        else:
                twitter_url_input_variable = ctk.StringVar()
                twitter_url_input_variable.set(url)
                twitter_placeholder_url_input_variable = ctk.StringVar()
                twitter_placeholder_url_input_variable.set("Entry your twitter url here")
                entry_twitter_url = ctk.CTkEntry(urls_container_frame, textvariable=twitter_url_input_variable, placeholder_text=twitter_placeholder_url_input_variable)
                twitter_url_button = ctk.CTkButton(urls_container_frame, text="Check Url", command=lambda:twitter_url_actions(entry_twitter_url.get(), entry_twitter_url, button_entry, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_checkbox_follow, twitter_button_action, twitter_label_accounts))
        
        entry_twitter_url.pack(side="left", padx=(20,10), pady=(20,10), fill="x", expand=True)
        twitter_url_button.pack(side="left", padx=(20,10), pady=(20,10), fill="x", expand=True)
        
        return entry_twitter_url

def check_actions_in_twitter_option_content(checkbox_container_frame):
        actions = temp.get_twitter_actions()
        
        if actions == None:
                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt = checkbox_disable(checkbox_container_frame)
        else:
                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt = checkbox_normal(checkbox_container_frame)
        
        return twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, actions

def check_follow_in_twitter_option_content(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, checkbox_container_frame):
        follow = checkbox_pack(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt)
        
        if follow == None:
                twitter_checkbox_follow = ctk.CTkCheckBox(checkbox_container_frame, text='Follow', state='disabled')
                temp.set_twitter_follow(None)
        else:
                twitter_checkbox_follow = ctk.CTkCheckBox(checkbox_container_frame, text='Follow', state='normal')
        
        return twitter_checkbox_follow

def increase(button_entry, avaliable_accounts):
        value = int(button_entry.get())
        if value < avaliable_accounts:
                button_entry.delete(0, ctk.END)
                button_entry.insert(0, str(value + 1))

def decrease(button_entry):
        value = int(button_entry.get())
        if value > 0:
                button_entry.delete(0, ctk.END)
                button_entry.insert(0, str(value - 1))


def twitter_option_content(options_frame, instance, label_profile_vpn_status, label_profile_vpn_location, label_profile_vpn_ip):
        
        # label option selected
        twitter_label_pack(options_frame)
        
        avaliable_accounts = return_available_accounts_twitter()
        
        def validate_entry(text):
                if (text.isdigit() or text == ""):
                        return text == "" or int(text) <= avaliable_accounts
                else:
                        return False

        validate_command = options_frame.register(validate_entry)

        entry_button_frame = ctk.CTkFrame(options_frame)
        entry_button_frame.pack(fill="x")
        
        twitter_label_accounts = create_label_accounts(entry_button_frame, avaliable_accounts)

        twitter_label_interactions = create_label_interactions(entry_button_frame)

        button_entry = create_button_entry(entry_button_frame, validate_command)
        button_increase = create_button_increase(entry_button_frame, button_entry, avaliable_accounts)
        button_decrease = create_button_decrease(entry_button_frame, button_entry)

        check_interactions(button_entry, button_increase, button_decrease)

        # create urls container frame
        url, urls_container_frame = get_url_twitter_option_content(options_frame)
        # create checkboxes
        checkbox_container_frame = ctk.CTkFrame(options_frame)
        checkbox_container_frame.pack(fill="x")
        twitter_button_action = ctk.CTkButton(checkbox_container_frame, text="Do it", state='normal')
        
        twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, actions = check_actions_in_twitter_option_content(checkbox_container_frame)
        
        follow = checkbox_pack(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt)
                
        if (actions == None) and (follow == None):
                twitter_button_action = ctk.CTkButton(checkbox_container_frame, text="Do it", state='disabled', command=lambda: twitter_checkCheckbox(entry_twitter_url, button_entry, twitter_checkbox_cmnt, lambda: twitter_popup_comment_window(button_entry, instance, entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip), twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_follow, twitter_label_accounts, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip))
        else:
                twitter_button_action = ctk.CTkButton(checkbox_container_frame, text="Do it", state='normal', command=lambda: twitter_checkCheckbox(entry_twitter_url, button_entry, twitter_checkbox_cmnt, lambda: twitter_popup_comment_window(button_entry, instance,  entry_twitter_url,  twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip), twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_follow, twitter_label_accounts, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip))
        
        
        twitter_checkbox_follow = check_follow_in_twitter_option_content(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, checkbox_container_frame)
        
        entry_twitter_url = create_entry_url(url, urls_container_frame, button_entry, twitter_checkbox_like, twitter_checkbox_rt, 
                twitter_checkbox_cmnt, twitter_checkbox_follow, twitter_button_action, twitter_label_accounts)

        # twitter_button_action = check_follow_actions_in_twitter_option_content(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, checkbox_container_frame, actions, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, instance)
        
        twitter_pack(twitter_checkbox_follow, twitter_button_action)
        
        input_message_in_textbox("Opened Twitter menu!")

def twitter_label_pack(options_frame):
        twitter_label_option = ctk.CTkLabel(options_frame, text='Twitter', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        twitter_label_option.pack(padx=(10,10), pady=(10,10))
        
def twitter_pack(twitter_checkbox_follow, twitter_button_action):
        twitter_checkbox_follow.pack(side="left", padx=(20,10), pady=(20,10))
        twitter_button_action.pack(side="left", padx=(20,10), pady=(20,10), fill="x", expand=True)
        
def button_dissable(button_entry, button_increase, button_decrease):
        button_entry.configure(state="disabled")
        button_increase.configure(state="disabled")
        button_decrease.configure(state="disabled")
        
def checkbox_pack(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt):
        twitter_checkbox_like.pack(side="left", padx=(20,10), pady=(20,10))
        twitter_checkbox_rt.pack(side="left", padx=(20,10), pady=(20,10))
        twitter_checkbox_cmnt.pack(side="left", padx=(20,10), pady=(20,10))
        return temp.get_twitter_follow()

def checkbox_normal(checkbox_container_frame):
        twitter_checkbox_like = ctk.CTkCheckBox(checkbox_container_frame, text='Like', state='normal')
        twitter_checkbox_rt = ctk.CTkCheckBox(checkbox_container_frame, text='Retweet', state='normal')
        twitter_checkbox_cmnt = ctk.CTkCheckBox(checkbox_container_frame, text='Comment', state='normal')
        return twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt

def checkbox_disable(checkbox_container_frame):  
        twitter_checkbox_like = ctk.CTkCheckBox(checkbox_container_frame, text='Like', state='disabled')
        twitter_checkbox_rt = ctk.CTkCheckBox(checkbox_container_frame, text='Retweet', state='disabled')
        twitter_checkbox_cmnt = ctk.CTkCheckBox(checkbox_container_frame, text='Comment', state='disabled')
        temp.set_twitter_actions(None)
        return twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt

def create_button_entry(entry_button_frame, validate_command):
        button_entry = ctk.CTkEntry(entry_button_frame, width=30, validate="key", validatecommand=(validate_command, "%P"))
        button_entry.pack(side="left", padx=5, pady=5, anchor="center")
        return button_entry

def create_button_increase(entry_button_frame, button_entry, avaliable_accounts):
        button_increase = ctk.CTkButton(entry_button_frame, text='+', command=lambda:increase(button_entry, avaliable_accounts), width=2)
        button_increase.pack(side="left", padx=5, pady=5, anchor="center")
        temp.set_button_increase(button_increase)
        return button_increase

def create_button_decrease(entry_button_frame, button_entry):
        button_decrease = ctk.CTkButton(entry_button_frame, text='-', command=lambda:decrease(button_entry), width=2)
        button_decrease.pack(side="left", padx=5, pady=5, anchor="center")
        temp.set_button_decrease(button_decrease)
        return button_decrease

def twitter_url_check(url, button_entry):
        tweet_url = r'^https?://twitter\.com/[A-Za-z0-9_]{1,15}/status/\d+$'
        follow_url = r'^https?://twitter\.com/[A-Za-z0-9_]{1,15}$'
        button_entry_get = int(button_entry.get())
        if re.match(tweet_url, url) and (button_entry_get > 0):
                return "actions"
        elif re.match(follow_url, url) and (button_entry_get > 0):
                return "follow"

def twitter_checkCheckbox(entry_twitter_url, button_entry, twitter_checkbox_cmnt, twitter_popup_comment_window,
                        twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_follow, twitter_label_accounts, 
                        twitter_button_action, label_profile_vpn_status, label_profile_vpn_location, label_profile_vpn_ip):
        
        if twitter_url_check(entry_twitter_url.get(), button_entry) in ['actions','follow',]:
                driver_twitter = get_driver()
                
                checkbox_follow = twitter_checkbox_follow.get()
                checkbox_cmnt = twitter_checkbox_cmnt.get()
                checkbox_like = twitter_checkbox_like.get()
                checkbox_rt = twitter_checkbox_rt.get()
                
                if (checkbox_like == 1 and checkbox_rt == 1 and checkbox_cmnt== 1):
                        twitter_popup_comment_window()
                        twitter_give_like(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        twitter_give_rt(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        driver_twitter.close()
                elif (checkbox_like == 1 and checkbox_rt == 1):
                        twitter_give_like(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        twitter_give_rt(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        driver_twitter.close()
                elif (checkbox_like == 1 and checkbox_cmnt == 1):
                        twitter_popup_comment_window()
                        twitter_give_like(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        driver_twitter.close()
                elif (checkbox_rt == 1 and checkbox_cmnt == 1):  
                        twitter_popup_comment_window()     
                        twitter_give_rt(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        driver_twitter.close()
                elif checkbox_follow == 1:
                        twitter_give_follow(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        driver_twitter.close()
                elif checkbox_cmnt == 1:
                        twitter_popup_comment_window()
                        
                elif checkbox_like == 1:
                        twitter_give_like(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        driver_twitter.close()
                elif checkbox_rt== 1:
                        twitter_give_rt(driver_twitter, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        driver_twitter.close()
        else:
                input_message_in_textbox("Something has failed! Retry!")

def twitter_check_unlocked_accounts(label_profile_interactions, label_profile_locked, options_frame, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        
        driver = get_driver()
        data = ff.update_values_locked_ff()
        if data == 0:
                input_message_in_textbox("You need to create accounts first or have some accounts locked!")
        else:
                user_try = 1
                count = 0
                input_message_in_textbox(f"Users that are going to be checked: {len(data)}")
                for key, value in data.items():
                        # Variables para almacenar los valores
                        actions_if_vpn(ff.get_preferences(), label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        while_check_internet()
                        id_value = key
                        email_value = value['email']
                        password_value = value['password']
                        user_value = value['user']
                        input_message_in_textbox(f"User try: {user_try}")
                        input_message_in_textbox(f"Actions for user {user_value}")
                        result = input_message_in_textbox(sf.loginUserTwitterLocked(driver, email_value, password_value, user_value))
                        if result != "Your account is still locked!":
                                count = count + 1
                                sleep(1)
                                input_message_in_textbox(sf.closeSession(driver))
                        sleep(1)
                        if result == "Your account is still locked!":
                                driver.close()
                                driver = get_driver()
                        user_try = user_try + 1
                locked = (user_try - 1 - count)        
                input_message_in_textbox(f"{count} account/s has been unlocked with success!")
                input_message_in_textbox(f"{locked} account/s hasn't been unlocked!")
                updateProfileInteractionsAvailable(label_profile_interactions)
                updateLockedAccounts(label_profile_locked)
                destroy_options(options_frame)
                unlock_option_content(options_frame, label_profile_interactions, label_profile_locked)

def destroy_options(options_frame):
        for widget in options_frame.winfo_children():
                widget.destroy()

#################################################################################################################################

def values_action_comment(button_entry, entry_twitter_url):
        driver = get_driver()
        button_entry_get = int(button_entry.get())
        url = entry_twitter_url.get()
        data = ff.update_values_comment(url, button_entry_get)
        return_accounts = (url)
        comments = get_comments_list()
        return driver, button_entry_get, url, data, return_accounts, comments

def step_action_comment(user_try, user_value, driver, email_value, password_value, url, count, comments, i):
        input_message_in_textbox(f"User try: {user_try}")
        input_message_in_textbox(f"Actions for user {user_value}")
        result = input_message_in_textbox(sf.loginUserTwitter(driver, email_value, password_value, user_value))
        if result != "Your account is locked!":
                comment = input_message_in_textbox(sf.comment_tweet(driver, url, url, comments[i], user_value))
                if comment == "Comment Twitter! Ok!" or "Comment Tweet! Fail because you already comment this tweet!":
                        count = count +1
                        check3 = True
                        input_message_in_textbox("Inserting data to the database...")
                        loadActions(email_value, False, False, check3, url, user_value)
                sleep(1)
                input_message_in_textbox(sf.closeSession(driver))
                
        return count

def update_label_action_comment(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, 
                        twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action):
        return_accounts = return_avaliable_accounts_for_actions(entry_twitter_url.get())
        twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts}')
        if return_accounts == 0:
                twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts} \n You cannot make interactions in this tweet!!')
                twitter_widgets_configures('invalid', entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
                temp.set_twitter_actions(None)
                
def twitter_give_comment(entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        # driver.close()
        try:
                driver, button_entry_get, url, data, return_accounts, comments = values_action_comment(button_entry, entry_twitter_url)
                user_try = 1
                count = 0
                i = 0
                input_message_in_textbox(f"Users selected : {button_entry_get}")
                for key, value in data.items():
                        # Variables para almacenar los valores
                        actions_if_vpn(ff.get_preferences(), label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        while_check_internet()
                        id_value = key
                        email_value = value['email']
                        password_value = value['password']
                        user_value = value['user']
                        count = step_action_comment(user_try, user_value, driver, email_value, password_value, url, count, comments, i)
                        user_try = user_try + 1
                        i = i+1
                input_message_in_textbox(f"Successfully completed {count} comments out of {user_try-1}")
                update_label_action_comment(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, 
                                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        except TimeoutError:
                input_message_in_textbox("Something has failed with IMAP Server!")
        except requests.exceptions.Timeout:
                input_message_in_textbox("Error: Connection timed out.")
        except requests.exceptions.RequestException as e:
                input_message_in_textbox(f"Error: {e}")

#################################################################################################################################
def step_action_rt(user_try, user_value, driver, email_value, password_value, url, count):
        input_message_in_textbox(f"User try: {user_try}")
        input_message_in_textbox(f"Actions for user {user_value}")
        result = input_message_in_textbox(sf.loginUserTwitter(driver, email_value, password_value, user_value))
        if result != "Your account is locked!":
                rt = input_message_in_textbox(sf.retweet_tweet(driver, url, url))
                if rt == "Retweet Twitter! Ok!" or "Retweet Tweet! Fail because you already retweet this tweet!":
                        count = count +1
                        check2 = True
                        input_message_in_textbox("Inserting data to the database...")
                        loadActions(email_value, False, check2, False, url, user_value)
                #! Antes de cerrar la sesion debemos comprobar que no ha aparecido
                input_message_in_textbox(sf.get_unlock_more_twitter(driver))
                input_message_in_textbox(sf.closeSession(driver))
                sleep(1)
        return count

def values_action_rt(button_entry, entry_twitter_url):
        button_entry_get = int(button_entry.get())
        url = entry_twitter_url.get()
        data = ff.update_values_rt(url, button_entry_get)
        return_accounts = return_avaliable_accounts_for_actions(url)
        return button_entry_get, url, data, return_accounts

def update_label_action_rt(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, 
                        twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action):
        return_accounts = return_avaliable_accounts_for_actions(entry_twitter_url.get())
        twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts}')
        if return_accounts == 0:
                twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts} \n You cannot make interactions in this tweet!!')
                twitter_widgets_configures('invalid', entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
                temp.set_twitter_actions(None)
        
def twitter_give_rt(driver, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, 
                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        try:
                button_entry_get, url, data, return_accounts = values_action_rt(button_entry, entry_twitter_url)
                user_try = 1
                count = 0
                input_message_in_textbox(f"Users selected : {button_entry_get}")
                for key, value in data.items():
                        # Variables para almacenar los valores
                        actions_if_vpn(ff.get_preferences(), label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        while_check_internet()
                        id_value = key
                        email_value = value['email']
                        password_value = value['password']
                        user_value = value['user']
                        count = step_action_rt(user_try, user_value, driver, email_value, password_value, url, count)
                        user_try = user_try + 1
                        
                input_message_in_textbox(f"Successfully completed {count} retweets out of {user_try-1}")
                update_label_action_rt(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, 
                                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        except TimeoutError:
                input_message_in_textbox("Something has failed with IMAP Server!")
        except requests.exceptions.Timeout:
                input_message_in_textbox("Error: Connection timed out.")
        except requests.exceptions.RequestException as e:
                input_message_in_textbox(f"Error: {e}")

########

def step_action_like(user_try, user_value, driver, email_value, password_value, url, count):
        input_message_in_textbox(f"User try: {user_try}")
        input_message_in_textbox(f"Actions for user {user_value}")
        result = input_message_in_textbox(sf.loginUserTwitter(driver, email_value, password_value, user_value))
        if result != "Your account is locked!":
                like = input_message_in_textbox(sf.like_tweet(driver, url, url))
                if like == "Like Twitter! Ok!" or "Like Tweet! Fail because you already like this tweet!":
                        count = count +1
                        check1 = True
                        input_message_in_textbox("Inserting data to the database...")
                        loadActions(email_value, check1, False, False, url, user_value)
                input_message_in_textbox(sf.get_unlock_more_twitter(driver))
                input_message_in_textbox(sf.closeSession(driver))
                sleep(1)
        return count

def values_action_like(button_entry, entry_twitter_url):
        button_entry_get = int(button_entry.get())
        url = entry_twitter_url.get()
        data = ff.update_values_like(url, button_entry_get)
        return_accounts = return_avaliable_accounts_for_actions(url)
        return button_entry_get, url, data, return_accounts

def update_label_action_like(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, 
                        twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action):
        
        return_accounts = return_avaliable_accounts_for_actions(entry_twitter_url.get())
        twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts}')
        if return_accounts == 0:
                twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts} \n You cannot make interactions in this tweet!!')
                twitter_widgets_configures('invalid', entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
                temp.set_twitter_actions(None)
        
def twitter_give_like(driver, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, 
                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        try:
                button_entry_get, url, data, return_accounts = values_action_like(button_entry, entry_twitter_url)
                user_try = 1
                count = 0
                input_message_in_textbox(f"Users selected : {button_entry_get}")
                for key, value in data.items():
                        # Variables para almacenar los valores
                        actions_if_vpn(ff.get_preferences(), label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        while_check_internet()
                        id_value = key
                        email_value = value['email']
                        password_value = value['password']
                        user_value = value['user']
                        count = step_action_like(user_try, user_value, driver, email_value, password_value, url, count)
                        user_try = user_try + 1
                        
                input_message_in_textbox(f"Successfully completed {count} likes out of {user_try-1}")
                
                update_label_action_like(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, 
                                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        except TimeoutError:
                input_message_in_textbox("Something has failed with IMAP Server!")
        except requests.exceptions.Timeout:
                input_message_in_textbox("Error: Connection timed out.")
        except requests.exceptions.RequestException as e:
                input_message_in_textbox(f"Error: {e}")

########################################################################################################################################

def step_action_follow(user_try, user_value, driver, email_value, password_value, url, count):
        input_message_in_textbox(f"User try: {user_try}")
        input_message_in_textbox(f"Actions for user {user_value}")
        result = input_message_in_textbox(sf.loginUserTwitter(driver, email_value, password_value, user_value))
        if result != "Your account is locked!":
                follow = input_message_in_textbox(sf.follow_user(driver, url, url))
                if follow == "Follow User Twitter! Ok!" or "Follow user! Fail because you already follow this user!":
                        count = count +1
                        check = True
                        input_message_in_textbox("Inserting data to the database...")
                        loadFollow(email_value, check, url, user_value)
                input_message_in_textbox(sf.get_unlock_more_twitter(driver))        
                input_message_in_textbox(sf.closeSession(driver))
                sleep(1)
        return count

def values_action_follow(button_entry, entry_twitter_url):
        button_entry_get = int(button_entry.get())
        url = entry_twitter_url.get()
        data = ff.update_values_follow(url, button_entry_get)
        return_accounts = return_avaliable_accounts_for_follow(entry_twitter_url.get())
        # primero sin update
        return button_entry_get, url, data, return_accounts

def update_label_action_follow(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow,
                        twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action):
        return_accounts = return_avaliable_accounts_for_follow(entry_twitter_url.get())

        twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts}')
        if return_accounts == 0:
                twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts} \n You cannot make interactions in this tweet!!')
                twitter_widgets_configures('invalid', entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
                temp.set_twitter_actions(None)
                temp.set_twitter_follow(None)

def actions_if_vpn(preferences_user, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        if preferences_user == 'on':
                input_message_in_textbox("Connecting to VPN...")
                vpn_switch_status_label, vpn_switch_location_label, vpn_switch_ip_label = temp.get_vpn_values()
                vpn_connect_clicked(label_profile_vpn_status, vpn_switch_status_label, label_profile_vpn_location,
                        vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label)
        else:
                return None

def check_internet_connection():
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        sleep(1)
        input_message_in_textbox("Waiting for connection...")
        try:
                response = requests.get("https://www.google.com")
                if response.status_code == 200:
                        input_message_in_textbox("Connection established!")
                        return True
                else:
                        return False
        except requests.ConnectionError:
                return False

def while_check_internet():
        while True:
                if check_internet_connection():
                        break

def twitter_give_follow(driver, entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        try:
                button_entry_get, url, data, return_accounts = values_action_follow(button_entry, entry_twitter_url)
                user_try = 1
                count = 0
                input_message_in_textbox(f"Users selected : {button_entry_get}")
                for key, value in data.items():
                        # Variables para almacenar los valores
                        actions_if_vpn(ff.get_preferences(), label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip)
                        while_check_internet()
                        id_value = key
                        email_value = value['email']
                        password_value = value['password']
                        user_value = value['user']
                        count = step_action_follow(user_try, user_value, driver, email_value, password_value, url, count)
                        user_try += 1
                input_message_in_textbox(f"Successfully completed {count} following actions out of {user_try-1}")
                #! Tras realizar la acción actualizar la label!!!!
                update_label_action_follow(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow,
                                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        except TimeoutError:
                input_message_in_textbox("Something has failed with IMAP Server!")
        except requests.exceptions.Timeout:
                input_message_in_textbox("Error: Connection timed out.")
        except requests.exceptions.RequestException as e:
                input_message_in_textbox(f"Error: {e}")
        
def loadActions(email, check1, check2, check3, url, user):
        
        data = {
                "email": email,
                "like": check1,
                "retweet": check2,
                "comment": check3,
        }
        
        ff.set_load_values_actions(url, data, user)

def loadFollow(email, check, url, user):
        
        data = {
                "email": email,
                "follow": check
        }

        ff.set_load_values_follow(url, data, user)

def return_available_accounts_twitter():
        return ff.get_count_values_unlocked_ff()

def return_avaliable_accounts_for_follow(entry_twitter_url):
        return ff.update_count_values_follow(entry_twitter_url)

def return_avaliable_accounts_for_actions(entry_twitter_url):
        return ff.update_count_values_actions(entry_twitter_url)

def isCommentEmpty(comment):
        if comment == "":
                return True
        return False

def twitter_popup_comment_go_button(scrollable_frame_entries):
        comments_list_ = []
        for i, comment_entries in enumerate(scrollable_frame_entries):
                comment = comment_entries.get()
                comments_list_.append(comment)
        set_comments_list(comments_list_)
        return comments_list_       

def twitter_popup_comment_window(button_entry, instance, entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip):
        entry_value = int(button_entry.get())
        popup_comment_window = ctk.CTkToplevel()
        popup_comment_window.title("Comments window")
        popup_comment_window.geometry("250x300")
        popup_comment_window.lift()
        popup_comment_window.focus()

        # create scrollable frame
        scrollable_popup_frame = ctk.CTkScrollableFrame(popup_comment_window, label_text="Comments")
        scrollable_popup_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        scrollable_popup_frame.grid_columnconfigure(0, weight=2)
        scrollable_frame_entries = []

        def check_comments_inputs():
                # Verificar si hay texto en todos los inputs
                inputs_filled = all(entry.get() != "" for entry in scrollable_frame_entries)

                # Habilitar o deshabilitar el botón en consecuencia
                if inputs_filled:
                        popup_comment_window_button.configure(state="normal")
                else:
                        popup_comment_window_button.configure(state="disabled")

        for i in range(entry_value):
                comment_entries = ctk.CTkEntry(master=scrollable_popup_frame, placeholder_text=f"Type your comment {i+1}", width=300)
                comment_entries.grid(row=i, column=0, padx=10, pady=(0, 20))
                setattr(instance, f"comment_entries_{i}", comment_entries)
                scrollable_frame_entries.append(comment_entries)
                comment_entries.bind("<KeyRelease>", lambda event: check_comments_inputs())

        set_scrollable_frame_entries(scrollable_frame_entries)
        popup_comment_window_button = ctk.CTkButton(scrollable_popup_frame, text='Go!', command=lambda:[ twitter_popup_comment_go_button(scrollable_frame_entries), twitter_give_comment(entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action, label_profile_vpn_status,label_profile_vpn_location, label_profile_vpn_ip) , close_comment_window(popup_comment_window)], state="disabled")
        popup_comment_window_button.grid(row=entry_value, column=0)

        check_comments_inputs()

def close_comment_window(popup_comment_window):
        popup_comment_window.destroy()
        
def widget_normal_actions(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                                entry_twitter_url, twitter_checkbox_follow):
        twitter_widgets_states('normal', twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        twitter_widgets_configures('actions', entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        temp.set_twitter_actions(1)
        temp.set_twitter_follow(None)

def widget_disabled_invalid(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                                entry_twitter_url, twitter_checkbox_follow):
        twitter_widgets_states('disabled', twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        twitter_widgets_configures('invalid', entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        temp.set_twitter_actions(None)
        temp.set_twitter_follow(None)

def widget_disabled_follow(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                                entry_twitter_url, twitter_checkbox_follow):
        twitter_widgets_states('disabled', twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        twitter_widgets_configures('follow', entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        temp.set_twitter_follow(1)
        temp.set_twitter_actions(None)

def widget_invalid_twitter(twitter_label_accounts, return_accounts, entry_twitter_url, twitter_checkbox_follow,
                                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action):
        twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts} \n You cannot make interactions in this tweet!!')
        twitter_widgets_configures('invalid', entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        temp.set_twitter_actions(None)
        temp.set_twitter_follow(None)

def check_result_actions(url_check_result, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                        entry_twitter_url, twitter_checkbox_follow, twitter_label_accounts):
        url = entry_twitter_url.get()
        return_accounts = return_avaliable_accounts_for_actions(url)
        twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts}')
        if url_check_result == 'actions':
                widget_normal_actions(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                                entry_twitter_url, twitter_checkbox_follow)
        return return_avaliable_accounts_for_actions(url)

def check_result_follow(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like,
                        twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action):
        return_accounts = return_avaliable_accounts_for_follow(entry_twitter_url.get())
        twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts}')
        if return_accounts == 0:
                widget_invalid_twitter(twitter_label_accounts, return_accounts, entry_twitter_url, twitter_checkbox_follow,
                                                twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        else:
                widget_disabled_follow(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                                                entry_twitter_url, twitter_checkbox_follow)
        return return_accounts
        
def last_step_twitter_url_actions(twitter_label_accounts, return_accounts, entry_twitter_url, button_entry):
        twitter_label_accounts.configure(text=f'Max interactions available: {return_accounts}')
        twitter_status(entry_twitter_url, button_entry)

def twitter_url_actions(url, entry_twitter_url, button_entry, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_checkbox_follow, twitter_button_action, twitter_label_accounts):
        url_check_result = twitter_url_check(url, button_entry)
        
        if url_check_result == "actions":
                temp.set_twitter_interactions(return_avaliable_accounts_for_actions(url))
                return_accounts = check_result_actions(url_check_result, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                                entry_twitter_url, twitter_checkbox_follow, twitter_label_accounts)
                if return_accounts == 0:
                        widget_disabled_invalid(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                                                        entry_twitter_url, twitter_checkbox_follow)
        elif url_check_result == 'follow':
                temp.set_twitter_interactions(return_avaliable_accounts_for_follow(url))
                return_accounts = check_result_follow(entry_twitter_url, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like,
                                        twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action)
        else:
                widget_disabled_invalid(twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action,
                                                                entry_twitter_url, twitter_checkbox_follow)
                return_accounts = 0
                temp.set_twitter_interactions(0)
        temp.get_button_increase().configure(command=lambda:increase(button_entry, int(temp.get_twitter_interactions())))        
        last_step_twitter_url_actions(twitter_label_accounts, temp.get_twitter_interactions(), entry_twitter_url, button_entry)

def type_actions(entry_twitter_url, twitter_checkbox_follow, twitter_button_action, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt):
        entry_twitter_url.configure(border_color="green")
        twitter_checkbox_follow.configure(state='disabled')
        twitter_checkbox_follow.deselect()
        
def type_follow(entry_twitter_url, twitter_checkbox_follow, twitter_button_action,twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt):
        entry_twitter_url.configure(border_color="green")
        twitter_checkbox_follow.configure(state='normal')
        twitter_button_action.configure(state='normal')
        twitter_checkbox_like.deselect()
        twitter_checkbox_rt.deselect()
        twitter_checkbox_cmnt.deselect()

def type_invalid(entry_twitter_url, twitter_checkbox_follow, twitter_button_action, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt):
        entry_twitter_url.configure(border_color="red")
        twitter_checkbox_like.deselect()
        twitter_checkbox_rt.deselect()
        twitter_checkbox_cmnt.deselect()
        twitter_checkbox_follow.configure(state='disabled')
        twitter_checkbox_follow.deselect()      

def twitter_widgets_configures(type, entry_twitter_url, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action):
        type_function_map = {
        'actions': type_actions,
        'follow': type_follow,
        'invalid': type_invalid
        }

        if type in type_function_map:
                type_function_map[type](entry_twitter_url, twitter_checkbox_follow, twitter_button_action, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt)

# change checkbox and button status on twitter option
def twitter_widgets_states(state, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action):
        twitter_checkbox_like.configure(state=state)
        twitter_checkbox_rt.configure(state=state)
        twitter_checkbox_cmnt.configure(state=state)
        twitter_button_action.configure(state=state)

def twitter_status(entry_twitter_url, button_entry):
        if not entry_twitter_url.get():
                temp.set_twitter_url(None)
        else:
                temp.set_twitter_url(entry_twitter_url.get())
        temp.set_button_status(button_entry.get())

################################################ LOGOUT ##################################################

def logout_container(options_frame):
        logout_container_frame = ctk.CTkFrame(options_frame)
        logout_container_frame.pack(fill="both", expand=True)
        return logout_container_frame

def logout_label(logout_container_frame):
        logout_label_option = ctk.CTkLabel(logout_container_frame, text='LogOut', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        logout_label_option.pack(padx=(10,10), pady=(10,10))
        return logout_label_option

def logout_label_quest_def(logout_container_frame):
        logout_label_quest = ctk.CTkLabel(logout_container_frame, text="Are you sure?", justify="center")
        logout_label_quest.pack(padx=(20, 10), pady=(10, 10))
        return logout_label_quest
        
def logout_button_yes_def(logout_container_frame, instance):
        logout_button_yes = ctk.CTkButton(logout_container_frame, text="Yes", anchor='center', command=lambda: action_logOut(instance))
        logout_button_yes.pack(side="top", padx=10, pady=10)

def logout_option_content(options_frame, instance):
        logout_container_frame = logout_container(options_frame)
        logout_label(logout_container_frame)
        logout_label_quest_def(logout_container_frame)
        logout_button_yes_def(logout_container_frame, instance)
        input_message_in_textbox("Opened logout menu!")

def logout_user():
        import GraphicUI.ctk_login as login_app
        ff.get_logout()
        login_app.main_window.mainloop() 

def close_main_window(instance):
        instance.destroy()

def action_logOut(instance):
        close_main_window(instance)
        logout_user()  

def configure_disable_option(sidebar_help_button, sidebar_accounts_button, sidebar_unlock_button,
                                sidebar_twitter_button, sidebar_vpn_button, sidebar_logout_button):
        sidebar_help_button.configure(state='normal')
        sidebar_accounts_button.configure(state='normal')
        sidebar_unlock_button.configure(state='normal')
        sidebar_twitter_button.configure(state='normal')
        sidebar_vpn_button.configure(state='normal')
        sidebar_logout_button.configure(state='normal')

def checkButton(button, sidebar_help_button, sidebar_accounts_button, sidebar_unlock_button, 
                sidebar_twitter_button, sidebar_vpn_button, sidebar_logout_button):
        button_widget_map = {
        'help': sidebar_help_button,
        'accounts': sidebar_accounts_button,
        'unlock': sidebar_unlock_button,
        'twitter': sidebar_twitter_button,
        'vpn': sidebar_vpn_button,
        'logout': sidebar_logout_button
        }

        if button in button_widget_map:
                button_widget_map[button].configure(state='disabled')
                
def disable_option_button(button, sidebar_help_button, 
                                sidebar_accounts_button, sidebar_unlock_button, 
                                sidebar_vpn_button, sidebar_twitter_button, 
                                sidebar_logout_button):
        #enable other buttons
        configure_disable_option(sidebar_help_button, sidebar_accounts_button, sidebar_unlock_button,
                                sidebar_twitter_button, sidebar_vpn_button, sidebar_logout_button)
        #disable specific button
        checkButton(button, sidebar_help_button, sidebar_accounts_button, sidebar_unlock_button, 
                sidebar_twitter_button, sidebar_vpn_button, sidebar_logout_button)