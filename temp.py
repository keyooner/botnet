email = None
password = None

vpn_mode = 'on'
vpn_status = 'Disconnected'
vpn_location = ''
vpn_ip = ''
twitter_url = None

def set_credentials(new_email, new_password):
    global email, password
    email = new_email
    password = new_password

def set_twitter_url(new_twitter_url):
    global twitter_url
    twitter_url = new_twitter_url

def set_vpn_mode(new_status_value):
    global vpn_mode
    vpn_mode = new_status_value

def set_vpn_status(new_status):
    global vpn_status
    vpn_status = new_status

def set_vpn_location(new_location):
    global vpn_location
    vpn_location = new_location

def set_vpn_ip(new_ip):
    global vpn_ip
    vpn_ip = new_ip

def get_email():
    return email

def get_password():
    return password

def get_twitter_url():
    return twitter_url

def get_vpn_mode():
    return vpn_mode

def get_vpn_status():
        return f'VPN Status: {vpn_status}'

def get_vpn_location():
    return '' if vpn_location == '' else f'Location: {vpn_location}'

def get_vpn_ip():
    return '' if vpn_ip == '' else f'Ip: {vpn_ip}'