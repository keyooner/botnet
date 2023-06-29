email = None
password = None
vpn_switch_status_value = 'on'
vpn_switch_status = 'Disconnected'
vpn_switch_location = ''
vpn_switch_ip = ''

def set_credentials(new_email, new_password):
    global email, password
    email = new_email
    password = new_password

def set_vpn_switch_status_value(new_status_value):
    global vpn_switch_status_value
    vpn_switch_status_value = new_status_value

def set_vpn_switch_status(new_status):
    global vpn_switch_status
    vpn_switch_status = new_status

def set_vpn_switch_location(new_location):
    global vpn_switch_location
    vpn_switch_location = new_location

def set_vpn_switch_ip(new_ip):
    global vpn_switch_ip
    vpn_switch_ip = new_ip

def get_email():
    return email

def get_password():
    return password

def get_vpn_switch_status_value():
    return vpn_switch_status_value

def get_vpn_switch_status():
        return f'VPN Status: {vpn_switch_status}'

def get_vpn_switch_location():
    return '' if vpn_switch_location == '' else f'Location: {vpn_switch_location}'

def get_vpn_switch_ip():
    return '' if vpn_switch_ip == '' else f'Ip: {vpn_switch_ip}'