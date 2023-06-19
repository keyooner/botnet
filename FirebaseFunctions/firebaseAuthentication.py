import CryptographyFunctions.cryptographyFunctions as crypto
import json
# Firebase library for Wrapper API Client
import pyrebase
import const
def initializeApp():
    config = const.CONFIG
    
    # We return the parameters of the initialize app
    return pyrebase.initialize_app(config)

def createUser(email, password):
    # We try to initialize app
    firebase = initializeApp()
    
    # Get a reference to the auth service# Get a reference to the auth service
    auth = firebase.auth()
    
    # We try to create the user if this fails, throw exception
    try:
        auth.create_user_with_email_and_password(email = email, password = password)
        error = f"User have been created correctly. With the email'{email}'"
        verify = True
        return error, verify
    except Exception as e:
        return _errorFirebaseCreateUser(e)

def loginUser(email, password):
    # We try to initialize app
    firebase = initializeApp()

    # Get a reference to the auth service
    auth = firebase.auth()
    # We try to sign in if this fails, throw exception
    try:
        auth.sign_in_with_email_and_password(email = email, password = password)
        error = f"You have been sign in correctly. With the email '{email}'"
        verify = True
        return error, verify

    except Exception as e:
        return _errorFirebaseLoginUser(e)

def logOutUser():
    # We try to initiliaze app
    firebase = initializeApp()
    
    # Get a reference to the auth service
    auth = firebase.auth()
    
    try:
        auth.current_user = None
        return "You have been disconnected!"
    
    except Exception as e:
        return f"Error {e}"
    
def recoverPassword(email):
    # We try to initialize app
    firebase = initializeApp()

    # Get a reference to the auth service
    auth = firebase.auth()
    # We try to sign in if this fails, throw exception
    try:
        auth.send_password_reset_email(email)
        error = f"The mail was sent to: '{email}.\n Please check your inbox.'"
        verify = True
        return error, verify

    except Exception as e:
        return _errorFirebaseLoginUser(e)    

# Control error for Firebase Create User
def _errorFirebaseCreateUser(e):
    # We get the error code of the json that return the function
    message = json.loads(e.args[1])['error']['message']

    verify = False
    if "INVALID_PASSWORD" in message:
        error = "Your password it's incorrect!"
    elif "TOO_MANY_ATTEMPTS_TRY_LATER" in message:
        error = "Too many attempts. Please, try again later!"
    elif "EMAIL_NOT_FOUND" in message:
        error = "There is no user record corresponding to this identifier. The user may have been deleted."
    elif "USER_DISABLED" in message:
        error = "The user account has been disabled by an administrator."
    else:
        error = "There is an error, please try again later."

    return error, verify

# Control error for Firebase Login User
def _errorFirebaseLoginUser(e):
    # We get the error code of the json that return the function
    message = json.loads(e.args[1])['error']['message']

    verify = False
    if "INVALID_PASSWORD" in message:
        error = "Your password it's incorrect!"
    elif "TOO_MANY_ATTEMPTS_TRY_LATER" in message:
        error = "Too many attempts. Please, try again later!"
    elif "EMAIL_NOT_FOUND" in message:
        error = "There is no user record corresponding to this identifier. The user may have been deleted."
    elif "USER_DISABLED" in message:
        error = "The user account has been disabled by an administrator."
    else:
        error = "There is an error, please try again later."

    return error, verify
