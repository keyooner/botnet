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
preferences_user = 'on'
button_increase = None
button_decrease = None
vpn_switch_status_label = None
vpn_switch_location_label = None
vpn_switch_ip_label = None
button_status = None
label_accounts = None

def set_label_accounts(new_label_accounts):
    global label_accounts
    label_accounts = new_label_accounts

def get_label_accounts():
    return label_accounts

def set_button_status(new_button_status):
    global button_status
    button_status = new_button_status

def get_button_status():
    return button_status

def set_button_decrease(new_button_decrease):
    global button_decrease
    button_decrease = new_button_decrease

def get_button_decrease():
    return button_decrease

def set_button_increase(new_button_increase):
    global button_increase
    button_increase = new_button_increase

def get_button_increase():
    return button_increase

def set_vpn_values(new_vpn_switch_status_label, new_vpn_switch_location_label, new_vpn_switch_ip_label):
    global vpn_switch_status_label
    global vpn_switch_location_label
    global vpn_switch_ip_label
    vpn_switch_status_label = new_vpn_switch_status_label
    vpn_switch_location_label = new_vpn_switch_location_label
    vpn_switch_ip_label = new_vpn_switch_ip_label
    
def get_vpn_values():
    return vpn_switch_status_label, vpn_switch_location_label, vpn_switch_ip_label
    
def set_preferences_user(new_preferences_user):
    global preferences_user
    preferences_user = preferences_user

def get_preferences_user():
    return preferences_user

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