import io
import re
import sys
import temp
import datetime
import customtkinter as ctk
import TwitterFunctions.seleniumFunctions as sf
import FirebaseFunctions.firebaseDatabase as fdb
import FirebaseFunctions.firebaseAuthentication as fba
from CTkTable import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN

################################################ DRIVER ##################################################

def get_driver():
        return webdriver.Chrome(service = Service(ChromeDriverManager().install()))

############################################### TEXTBOX ##################################################

def test_return_variable():
        return 'return variable'

def input_message_in_textbox(textbox, entry):
        date_time = datetime.datetime.now()
        textbox.configure(state="normal")
        textbox.insert("0.0", f"[{date_time}] $: {entry.get()}" + f" {test_return_variable()}" "\n\n")
        entry.delete(0, ctk.END)
        textbox.configure(state="disabled")

############################################### ACCOUNTS ##################################################

def accounts_option_content(options_frame):
        #create scrollable frame for table
        scrollable_table_frame = ctk.CTkScrollableFrame(options_frame, fg_color="transparent", label_text="Accounts")
        scrollable_table_frame.pack(side="top", padx=(20, 0), pady=(20, 0), fill="both", expand=True)
        scrollable_table_frame.grid_rowconfigure(0, weight=0)
        scrollable_table_frame.grid_columnconfigure(0, weight=1)
        scrollable_table_frame_values = []

        #accounts available
        data = fdb.get_values(temp.get_email(), temp.get_password())
        header_values = [['             EMAIL            ', ' PASSWORD ', '      USERNAME      ']]
        header_table = CTkTable(scrollable_table_frame, row=1, column=3, values=header_values, header_color="#8370F7", hover=True)
        header_table.grid(row=0 % 3, column=0, padx=10, pady=(0, 20), sticky="ew")
        

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
        create_account_button = ctk.CTkButton(button_frame, text="Create Account")
        create_account_button.pack(side="left", padx=(20, 10), pady=(10, 10), fill="x", expand=True)
        create_unlock_button = ctk.CTkButton(button_frame, text="Unlock Account/s")
        create_unlock_button.pack(side="left", padx=(20, 10), pady=(10, 10), fill="x", expand=True)

############################################### VPN ##################################################

def vpn_option_content(options_frame, label_profile_vpn_status, label_profile_vpn_location, label_profile_vpn_ip):
        vpn_container_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        vpn_container_frame.pack(fill="x", expand=True)

        vpn_label_option = ctk.CTkLabel(vpn_container_frame, text='Vpn', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        vpn_label_option.pack(padx=(10,10), pady=(10,10))

        vpn_switch_label = ctk.CTkLabel(master=vpn_container_frame, text="Do you want to use VPN?")
        vpn_switch_label.pack(side="left", padx=(10,10), pady=(10,10), fill="both", expand=True)

        vpn_switch_var = ctk.StringVar(value=temp.get_vpn_mode())
        vpn_switch = ctk.CTkSwitch(master=vpn_container_frame, 
                                        text="Vpn On/Off", 
                                        command=lambda: vpn_connect_clicked(vpn_switch_var, label_profile_vpn_status, 
                                        vpn_switch_status_label, label_profile_vpn_location, vpn_switch_location_label, 
                                        label_profile_vpn_ip, vpn_switch_ip_label), 
                                        variable=vpn_switch_var, onvalue='on', offvalue='off')
        vpn_switch.pack(side="left", padx=(20, 10), pady=(10, 10), fill="both", expand=True)

        vpn_container_frame_2 = ctk.CTkFrame(options_frame, fg_color="transparent")
        vpn_container_frame_2.pack(fill="x", expand=True)

        vpn_switch_status_label = ctk.CTkLabel(vpn_container_frame_2, text=temp.get_vpn_status(), justify='center')
        vpn_switch_status_label.pack(padx=(10,10), pady=(10,10))

        vpn_switch_location_label = ctk.CTkLabel(master=options_frame, text=temp.get_vpn_location())
        vpn_switch_location_label.pack(side="left", padx=(10,10), pady=(10,10), fill="both", expand=True)

        vpn_switch_ip_label = ctk.CTkLabel(master=options_frame, text=temp.get_vpn_ip())
        vpn_switch_ip_label.pack(side="left", padx=(10,10), pady=(10,10), fill="both", expand=True)

def vpn_connect_clicked(vpn_switch_var, label_profile_vpn_status, 
                vpn_switch_status_label, label_profile_vpn_location, 
                vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):
        temp.set_vpn_mode('on')
        temp.set_vpn_status('Connected')
        if vpn_switch_var.get() == 'on':
                stdout = sys.stdout
                exit_prints = io.StringIO()
                sys.stdout = exit_prints
                initialize_VPN(stored_settings=1)
                rotate_VPN()
                sys.stdout = stdout
                prints_exits = exit_prints.getvalue()
                vpn_location = re.search(r'Connecting you to\s*(.*)', prints_exits)
                vpn_ip = re.search(r'your new ip-address is:\s*(.*)', prints_exits)
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
        else:
                terminate_VPN()
                vpn_labels_off(
                        label_profile_vpn_status,
                        vpn_switch_status_label,
                        label_profile_vpn_location,
                        vpn_switch_location_label,
                        label_profile_vpn_ip,
                        vpn_switch_ip_label,
                )

def vpn_labels_on(vpn_location, vpn_ip, label_profile_vpn_status, 
                vpn_switch_status_label, label_profile_vpn_location, 
                vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):
        
        temp.set_vpn_location(vpn_location)
        temp.set_vpn_ip(vpn_ip)
        label_profile_vpn_status.configure(text=temp.get_vpn_status())
        vpn_switch_status_label.configure(text=temp.get_vpn_status())
        label_profile_vpn_location.configure(text=temp.get_vpn_location())
        vpn_switch_location_label.configure(text=temp.get_vpn_location())
        label_profile_vpn_ip.configure(text=f"{temp.get_vpn_ip()}")
        vpn_switch_ip_label.configure(text=temp.get_vpn_ip())

def vpn_labels_off(label_profile_vpn_status, 
                vpn_switch_status_label, label_profile_vpn_location, 
                vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):
        temp.set_vpn_mode('off')
        temp.set_vpn_status("Disconnected")
        temp.set_vpn_location('')
        temp.set_vpn_ip('')

        label_profile_vpn_status.configure(text=temp.get_vpn_status())
        vpn_switch_status_label.configure(text=temp.get_vpn_status())
        label_profile_vpn_location.configure(text=temp.get_vpn_location())
        vpn_switch_location_label.configure(text=temp.get_vpn_location())
        label_profile_vpn_ip.configure(text=temp.get_vpn_ip())
        vpn_switch_ip_label.configure(text=temp.get_vpn_ip())

############################################### TWITTER ##################################################

def twitter_url_check(url, button_entry):
        tweet_url = r'^https?://twitter\.com/[A-Za-z0-9_]{1,15}/status/\d+$'
        follow_url = r'^https?://twitter\.com/[A-Za-z0-9_]{1,15}$'
        if re.match(tweet_url, url) and (int(button_entry.get()) > 0):
                return "actions"
        elif re.match(follow_url, url) and (int(button_entry.get()) > 0):
                return "follow"
        
def twitter_checkCheckbox(entry_twitter_url, button_entry, twitter_checkbox_cmnt, twitter_popup_comment_window, twitter_checkbox_like):
        if twitter_url_check(entry_twitter_url.get(), button_entry) in ['actions','follow',]:

                if  twitter_checkbox_cmnt.get() == 1:
                        twitter_popup_comment_window()

                if twitter_checkbox_like.get() == 1:
                        print(sf.action_n_times(get_driver(), fdb.get_values_for_actions(temp.get_email(), temp.get_password(), int(button_entry.get())), entry_twitter_url.get(), 
                                entry_twitter_url.get(), 2))

def return_available_accounts_twitter():
        return fdb.get_values_unlocked(temp.get_email(), temp.get_password())

def twitter_popup_comment_window(button_entry, instance):
        entry_value = int(button_entry.get())
        popup_comment_window = ctk.CTkToplevel()
        popup_comment_window.title("Comments window")
        popup_comment_window.geometry("250x300")
        popup_comment_window.focus()

        # create scrollable frame
        scrollable_popup_frame = ctk.CTkScrollableFrame(popup_comment_window, label_text="Comments")
        scrollable_popup_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        scrollable_popup_frame.grid_columnconfigure(0, weight=2)
        scrollable_frame_entries = []
        for i in range(entry_value):
                comment_entries = ctk.CTkEntry(master=scrollable_popup_frame, placeholder_text=f"Type your comment {i+1}", width=300)
                comment_entries.grid(row=i, column=0, padx=10, pady=(0, 20))
                setattr(instance, f"comment_entries_{i}", comment_entries)
                scrollable_frame_entries.append(comment_entries)

        popup_comment_window_button = ctk.CTkButton(scrollable_popup_frame, text='Go!')
        popup_comment_window_button.grid(row=entry_value, column=0)

################################################ LOGOUT ##################################################

def logout_option_content(options_frame, instance):
        #create logout container frame
        logout_container_frame = ctk.CTkFrame(options_frame)
        logout_container_frame.pack(fill="both", expand=True)

        #label option selected
        logout_label_option = ctk.CTkLabel(logout_container_frame, text='LogOut', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        logout_label_option.pack(padx=(10,10), pady=(10,10))

        logout_label_quest = ctk.CTkLabel(logout_container_frame, text="Are you sure?", justify="center")
        logout_label_quest.pack(padx=(20, 10), pady=(10, 10))

        #button option selected
        logout_button_yes = ctk.CTkButton(logout_container_frame, text="Yes", anchor='center', command=lambda: action_logOut(instance))
        logout_button_yes.pack(side="top", padx=10, pady=10)

def logout_user():
        import GraphicUI.ctk_login as login_app
        fba.logOutUser()
        login_app.main_window.mainloop() 

def close_main_window(instance):
        instance.destroy()

def action_logOut(instance):
        close_main_window(instance)
        logout_user()  

############################################### DISABLE BUTTONS ##################################################

def disable_option_button(button, sidebar_vpn_button, sidebar_accounts_button, sidebar_twitter_button, sidebar_logout_button):
        #enable other buttons
        sidebar_vpn_button.configure(state='normal')
        sidebar_accounts_button.configure(state='normal')
        sidebar_twitter_button.configure(state='normal')
        sidebar_logout_button.configure(state='normal')
        #disable specific button
        if button == 'accounts':
                sidebar_accounts_button.configure(state='disabled')
        elif button == 'twitter':
                sidebar_twitter_button.configure(state='disabled')
        elif button == 'vpn':
                sidebar_vpn_button.configure(state='disabled')
        elif button == 'logout':
                sidebar_logout_button.configure(state='disabled')