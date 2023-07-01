import io
import re
import sys
import temp
import datetime
import customtkinter as ctk
import FirebaseFunctions.firebaseDatabase as fdb
from CTkTable import *

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

def accounts_option_table(options_frame):
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

def vpn_connect_clicked(vpn_switch_var, label_profile_vpn_status, 
                vpn_switch_status_label, label_profile_vpn_location, 
                vpn_switch_location_label, label_profile_vpn_ip, vpn_switch_ip_label):
        from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
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
                temp.set_vpn_mode('off')

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
        
        temp.set_vpn_status("Disconnected")
        label_profile_vpn_status.configure(text=temp.get_vpn_status())
        vpn_switch_status_label.configure(text=temp.get_vpn_status())
        label_profile_vpn_location.configure(text=temp.get_vpn_location())
        vpn_switch_location_label.configure(text=temp.get_vpn_location())
        label_profile_vpn_ip.configure(text=temp.get_vpn_ip())
        vpn_switch_ip_label.configure(text=temp.get_vpn_ip())