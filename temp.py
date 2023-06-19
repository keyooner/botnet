email = None
password = None

def set_credentials(new_email, new_password):
    global email, password
    email = new_email
    password = new_password

def get_email():
    return email

def get_password():
    return password