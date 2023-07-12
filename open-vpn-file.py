from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
import time

settings = initialize_VPN(save=1, area_input = ['Europe'])

initialize_VPN(stored_settings=1)

for _ in range(3):
    rotate_VPN()
    print('\nDo whatever you want here (e.g.scraping). Pausing for 10 seconds...\n')
    time.sleep(10)

terminate_VPN()