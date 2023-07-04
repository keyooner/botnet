email = "danifdezloz@gmail.com"
password = "Dani5Fdez"
vpn_mode = 'on'
vpn_status = 'Disconnected'
vpn_location = ''
vpn_ip = ''
twitter_url = None
twitter_interactions = None
twitter_actions = None
twitter_follow = None


def set_credentials(new_email, new_password):
    global email, password
    email = new_email
    password = new_password

def set_twitter_url(new_twitter_url):
    global twitter_url
    twitter_url = new_twitter_url

def set_twitter_interactions(new_twitter_interactions):
    global twitter_interactions
    twitter_interactions = new_twitter_interactions

def set_twitter_actions(new_twitter_actions):
    global twitter_actions
    twitter_actions = new_twitter_actions

def set_twitter_follow(new_twitter_follow):
    global twitter_follow
    twitter_follow = new_twitter_follow

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

def get_twitter_interactions():
    return twitter_interactions

def get_twitter_actions():
    return twitter_actions

def get_twitter_follow():
    return twitter_follow

def get_vpn_mode():
    return vpn_mode

def get_vpn_status():
        return f'VPN Status: {vpn_status}'

def get_vpn_location():
    return '' if vpn_location == '' else f'Location: {vpn_location}'

def get_vpn_ip():
    return '' if vpn_ip == '' else f'Ip: {vpn_ip}'