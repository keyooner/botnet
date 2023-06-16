import customtkinter as ctk
import os
from time import sleep
import random

class VpnFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name = 'VPN Frame', **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = ctk.CTkLabel(self, text = self.header_name)
        self.header.grid(row = 4, column = 2, padx = 10, pady = 10)

        self.login_frame_button = ctk.CTkButton(self, text = 'Connect VPN', command = connect_vpn)
        self.login_frame_button.grid(row = 3, column = 2, padx = 10, pady = 10)

def connect_vpn():

    # Use correctly
    ''' 
        Open a terminal on linux with Windscribe-cli installed and type: windscribe login
        Enter your credentials
        And lanuch vpn button
    '''
    # list of VPN server codes
    codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
                "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]

    try:

        # connect to VPN
        os.system("windscribe connect")
        while True:

            # assigning a random VPN server code
            choiceCode = random.choice(codeList)

            # changing IP after a particular time period
            sleep(random.randrange(120, 300))

            # connecting to a different VPN server
            print("!!! Changing the IP Address........")
            os.system(f"windscribe connect {choiceCode}")

    except Exception:

        # disconnect VPN
        os.system("windscribe disconnect")
        print("sorry, some error has occurred..!!")