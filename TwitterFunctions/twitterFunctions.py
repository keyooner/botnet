import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
import EmailFunctions.createEmail as ce
from selenium.common.exceptions import WebDriverException as exceptions
import FirebaseFunctions.firebaseDatabase as fdb
import RandomProfile.randomProfileTwitter as rpt
from time import sleep
import temp
import re
import EmailFunctions.readEmail as re
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

## VARIABLES WITH IMPORTANT VALOURS TO THE DEVELOP OF THE APP ##
##------------------------------------------------------------##
    #! red_color_like_css 
    #? will help to check if the like is already liked
    #! green_color_retweet_css
    #? will help to check if the retweet is already retweeted
    #! black_color_follow_rgba_css 
    #? will help to check if the user is already followed
    #! url_login
    #? contain the url to login into twitter
    #! url_register
    #? contain the url to register into twitter
    #! selector_mapping
    #? help us to just put a number to choose a method for
    #? indicate the path to selenium
    #! action_mapping
    #? help us to just put a number to choose a method for
    #? indicate the action to made
##------------------------------------------------------------##
################################################################

red_color_like_css = "rgba(249, 24, 128, 1)"
# red_color_like_css = "rgba(248, 24, 128, 1)"
green_color_retweet_css = "rgba(0, 186, 124, 1)"
black_color_follow_rgba_css = "rgba(0, 0, 0, 0)"
url_login = "https://twitter.com/i/flow/login"
url_register = "https://twitter.com/i/flow/signup"

selector_mapping = {
    1: By.CSS_SELECTOR,
    2: By.XPATH,
    3: By.TAG_NAME
}

action_mapping = {
    1: "Retweet",
    2: "Like",
    3: "Comment",
    4: "Follow"
}

######################### HERE ARE THE FUNCTIONS FOR THE REGISTER USER ##########################
## --------------------------------------------------------------------------------------------##

def step1Part1(driver, name, mail):
    actions = [
        ("Check Twitter Register Page", driver, 1, ".r-kwpbio", False, False, None),
        ("Click create account", driver, 1, "div.css-18t94o4:nth-child(5)", True, False, None),
        ("Use mail as creation form", driver, 1, "div.css-18t94o4:nth-child(3) > span:nth-child(1)", True, False, None),
        ("Insert name", driver, 1, "div.r-mk0yit:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)", True, True, name),
        ("Insert mail", driver, 1, "div.r-mk0yit:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)", True, True, mail),
        ]
    
    for action in actions:
        twitter_actions(*action)

def step1Part2(driver, month, day, year):
    actions2 = [
        ("Insert month", driver, 1, "#SELECTOR_1", True, True, month),
        ("Insert day", driver, 1, "#SELECTOR_2", True, True, str(day)),
        ("Insert year", driver, 1, "#SELECTOR_3", True, True, str(year))
    ]
    
    for action2 in actions2:
        twitter_actions(*action2, split = False)

def step1Part3(driver):
    actions3 = [
        ("Header click to wait", driver, 2, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]", True, False, None),
        ("Go next 1", driver, 2, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div", True, False, None)
    ]
    
    for action3 in actions3:
        twitter_actions(*action3)

def while_check_internet():
        while True:
                if check_internet_connection():
                        break

def check_internet_connection():
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        sleep(1)
        try:
                response = requests.get("https://www.google.com")
                if response.status_code == 200:
                        return True
                else:
                        return False
        except requests.ConnectionError:
                return False

def step1CreateUserTwitter(driver, mail, name, year, month, day):
    
    # Go to register page
    while_check_internet()
    
    go_page("Twitter Register Page", driver, url_register, "https://twitter.com/i/flow/signup")
    
    step1Part1(driver, name, mail)
    
    step1Part2(driver, month, day, year)

    step1Part3(driver)

    return "Step 1! Create User! Ok!"

def step2CreateUserTwitter(driver):
    twitter_actions("Go next 2", driver, 2, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div", True, False, None)
    return "Step 2! Create User! Ok!"

def step3CreateUserTwitter(driver):
    twitter_actions("Go next 2", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div", True, False, None)
    return "Step 3! Create User! Ok!"

def step4CreateUserTwitter(driver, email, password):
    insertCode(driver, email, password)
    return "Step 4! Create User! Ok!"

def stepVerifyCreateUserTwitter(driver):
    
    if check_authetication_step(driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]"):
        while True:
            print("Esperando a que autentifiques la cuenta...")
            if check_authetication_step(driver, 2, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/h1/span/span"):
                break
        return "Verify was succesful!"
            #Te enviamos un código
            # Introducir código -> /html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input
    return "Not needed verify account!"     

def step5CreateUserTwitter(driver, password):
    try:
        selector = get_type_selector(2)
        action, div = find_element(driver, selector, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input")
        if action != "Find elements! OK!":
            return False
        split_word_clear(password, driver, div, selector, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input")
        # /html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/h1
        sleep(1)
        twitter_actions("Insert password button!", driver, 2, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div", True, False, None)
        return "Step 5! Create User! Ok!"
    except ValueError:
        return False
    # /html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input

def step6DiscardImageProfile(driver):
    twitter_actions("Discard photo profile!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div", True, False, None)
    return "Step 6! Create User! Ok!"

def step7IntroduceUSername(driver, username):
    try:
        selector = get_type_selector(2)
        action, div = find_element(driver, selector, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input ")
        if action != "Find elements! OK!":
            return False
        split_word_clear(username, driver, div, selector, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input ")
        sleep(2)
        twitter_actions("Insert username button!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div", True, False, None)
        return "Step 7! Create User! Ok!" 
    except ValueError:
        return False

def step8SkipNotifications(driver):
    twitter_actions("Skip notifications button!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div", True, False, None)

def step9CreateUserTwitter(driver):
    actions = [
        ("Language spoken", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/label[2]/div[2]/label/div/div/input", True, False, None),
        ("Button next language", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div", True, False, None),
        ("We pick 1 random theme", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div/div/div[3]/div/div/div/li[1]/div/div/div/div/div/div/div", True, False, None),
        ("We pick 2 random theme", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div/div/div[3]/div/div/div/li[2]/div/div/div/div/div/div/div", True, False, None),
        ("We pick 3 random theme", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/section/div/div/div/div/div[3]/div/div/div/li[3]/div/div/div/div/div/div/div", True, False, None),
        ("Button next 1", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div", True, False, None),
        ("Button next 2", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div", True, False, None),
        ("Follow random user", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/section/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div/div", True, False, None),
        ("Click finish creation", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div", True, False, None),
    ]
    
    for action in actions:
        twitter_actions(*action)
    
    return "Step 9! Create User! Ok!"

def step10ChangeImageProfile(driver):
    actions = [
        ("Go profile", driver, 2, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[8]", True, False, None),
        ("Setup profile", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[2]/a/div", True, False, None),
        ("Insert photo", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div/input", False, True, rpt.randomImage(), False),
        ("Apply photo", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div", True, False, None),
    ]
    
    for action in actions:
        twitter_actions(*action)
    
    sleep(1)
    
    actions2 = [
        ("Button next", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div", True, False, None),
        ("Skip pick header", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div", True, False, None),
        ("Skip insert bio", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div", True, False, None),
        ("Skip pick location", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div", True, False, None),
        ("See profile", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div", True, False, None),
    ]
    
    for action2 in actions2:
        twitter_actions(*action2)

# Function that try if the account is locked by twitter
def verifyIsAccountLocked(driver, email):
    if check_account_status(driver, 2, "/html/body/div[2]/div/div[1]"):
        print("Tu cuenta está bloqueada")
        twitter_actions("Unlock button clicked!", driver, 2, "/html/body/div[2]/div/form/input[6]", True, False, None)
        while True:
            print("Autentica la cuenta")
            if check_account_status(driver, 2, "/html/body/div[2]/div/div[1]") == True:
                twitter_actions("Continue to Twitter", driver, 2, "/html/body/div[2]/div/form/input[6]", True, False, None)
                print("Cuenta autenticada")
                # fdb.updateValues(temp.get_email(), temp.get_password(), email, "locked")
                fdb.updateValues(temp.get_email(), temp.get_password(), email, "unlocked")
                return True
    return False

def check_authetication_step(driver, type, element):
    
    selector = get_type_selector(type)
    try:
        action, div = find_element(driver, selector, element)
        if action != "Find elements! OK!":
            return False
        return True
    except ValueError:
        return False

# Function that try if the account is locked by twitter
def verifyIsAccountLocked(driver):
    if check_account_status(driver, 2, "/html/body/div[2]/div/div[1]"):
        twitter_actions("Unlock button clicked!", driver, 2, "/html/body/div[2]/div/form/input[6]", True, False, None)
        while True:
            if check_account_status(driver, 2, "/html/body/div[2]/div/div[1]") == True:
                twitter_actions("Continue to Twitter", driver, 2, "/html/body/div[2]/div/form/input[6]", True, False, None)
                return True
    return False

################ HERE ARE THE FUNCTIONS IN RELATION WITH THE CHECK COLORS FOR TWITTER #################
## --------------------------------------------------------------------------------------------------##
            #! get_rgb_value --> will receive the code of the color and split into R,G,B
            #? EXAMPLE --> RGB (1,1,1) = R(1), G(1), B(1)
            #! Params -> color_string
                # color_string --> receive the string of the color
## --------------------------------------------------------------------------------------------------##
            #! get_rgba_value --> will receive the code of the color and split into R,G,B,A
            #? EXAMPLE --> RGBA (1,1,1,1) = R(1), G(1), B(1), A(1)
            #! Params -> color_string
                # color_string --> receive the string of the color
## --------------------------------------------------------------------------------------------------##
            #! check_rgb_values --> will receive R1,G1,B1 (1ST COLOR) and R2,G2,B2 (2ND COLOR)
            #? Will check if both colors are the same in format rgb
            #! Params -> r1, g1, b1, r2, g2, b2
## --------------------------------------------------------------------------------------------------##
            #! check_rgba_values --> will receive R1,G1,B1,A1 (1ST COLOR) and R2,G2,B2,A2 (2ND COLOR)
            #? Will check if both colors are the same in format rgba
            #! Params -> r1, g1, b1, a1, r2, g2, b2, a2
## --------------------------------------------------------------------------------------------------##

# Function that get the rgb value
def get_rgb_value(color_string):
    # Get the RGB values of a string in rgb format(...)
    r, g, b = map(int, color_string[color_string.index("(")+1:color_string.index(")")].split(", "))
    return r, g, b

# Function that get the rgb value
def get_rgba_value(color_string):
    # Get the RGBA values of a string in rgb format(...)
    rgba_values = list(map(int, color_string[color_string.index("(")+1:color_string.index(")")].split(", ")))
    if len(rgba_values) == 3:
        rgba_values.append(0)
    r, g, b, a = rgba_values
    return r, g, b, a

# Function that check the rgb values
def check_rgb_values(r1, g1, b1, r2, g2, b2):
    # Check if are the same colours
    if r1 == r2 and g1 == g2 and b1 == b2:
        return("Fail because you already like this tweet!")
    return("Ok!")

# Function that check the rgb values
def check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2):
    # Check if are the same colours
    if r1 == r2 and g1 == g2 and b1 == b2 and a1 == a2:
        return("Fail because you already like this tweet!")
    return("Ok!")

## ----------------------------------------------END-------------------------------------------------##
#######################################################################################################

#################### HERE ARE THE FUNCTIONS IN RELATION WITH THE CODES OF TWITTER #####################
## --------------------------------------------------------------------------------------------------##
            #! get_rgb_value --> will receive the code of the color and split into R,G,B
            #? EXAMPLE --> RGB (1,1,1) = R(1), G(1), B(1)
            #! Params -> color_string
                # color_string --> receive the string of the color
## --------------------------------------------------------------------------------------------------##
            #! get_rgba_value --> will receive the code of the color and split into R,G,B,A
            #? EXAMPLE --> RGBA (1,1,1,1) = R(1), G(1), B(1), A(1)
            #! Params -> color_string
                # color_string --> receive the string of the color
## --------------------------------------------------------------------------------------------------##
            #! check_rgb_values --> will receive R1,G1,B1 (1ST COLOR) and R2,G2,B2 (2ND COLOR)
            #? Will check if both colors are the same in format rgb
            #! Params -> r1, g1, b1, r2, g2, b2
## --------------------------------------------------------------------------------------------------##
            #! check_rgba_values --> will receive R1,G1,B1,A1 (1ST COLOR) and R2,G2,B2,A2 (2ND COLOR)
            #? Will check if both colors are the same in format rgba
            #! Params -> r1, g1, b1, a1, r2, g2, b2, a2
## --------------------------------------------------------------------------------------------------##

def get_user_profile(driver, type, element, user):
    selector = get_type_selector(type)
    try: 
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
    except TimeoutException:
        return False
    
    if div_action.text in [
        f"@{user}"
    ]:
        return True
    return False

# This function will check if your account is locked in the login because as a result of an unusual activity
def get_login_locked(driver, type, element):
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else, remove-unnecessary-cast

    selector = get_type_selector(type)
    try: 
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
    except TimeoutException:
        return False
    
    if div_action.text in [
        "Introduce tu número de teléfono o nombre de usuario",
        "Enter your phone number or username",
    ]:
        return True
    return False

def unlock_more(driver, type, element):
    selector = get_type_selector(type)
    try: 
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
    except TimeoutException:
        return False
    
    if div_action.text in [
        "Unlock more on Twitter",
        "You've unlocked more on Twitter"
    ]:
        return True
    return False

# This function will check if your account is locked by suspicious activity
def get_suspicious_activity(driver, type, element):
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else, remove-unnecessary-cast

    selector = get_type_selector(type)
    
    try:
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
    except TimeoutException:
        return False

    if div_action.text in [
        "Revisa tu correo electrónico",
        "Check your email",
    ]:
        return True
    return False

# This function will check if your account is locked by suspicious activity
def get_boost_security(driver, type, element):
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else, remove-unnecessary-cast

    selector = get_type_selector(type)
    
    try:
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
    except TimeoutException:
        return False

    if div_action.text in [
        "Boost your account security"
    ]:
        return True
    return False

# You’re in control
# /html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/span/span/span
# click button:
# /html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]

def get_you_are_in_control(driver, type, element):
    
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else, remove-unnecessary-cast

    selector = get_type_selector(type)
    
    try:
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
    except TimeoutException:
        return False

    if div_action.text in [
        "You’re in control"
    ]:
        return True
    return False

# This function will check if your account is locked by suspicious activity
def get_blue_verification(driver, type, element):
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else, remove-unnecessary-cast

    selector = get_type_selector(type)
    
    try:
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
    except TimeoutException:
        return False

    if div_action.text in [
        "Who are you?"
    ]:
        return True
    return False

def stepInsertCode(driver, code):
    actions = [
        ("Insert code!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input", True, True, code),
        ("Press button next!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div", True, False, None),
    ]
    
    for action in actions:
        twitter_actions(*action)
    
def insertCode(driver, email, password):
    
    while True:
        code = re.readMailTwitter(email, password)
        if code != None:
            break
        print("Esperando recibir el código de Twitter...")
        sleep(1)
    
    stepInsertCode(driver, code)
        
    return "Insert Code! Ok!"

def stepInsertCodeSuspicious(driver, code):
    actions =[
        ("Insert code", driver, 2, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input", True, True, code),
        ("Press button", driver, 2, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div", True, False, None),
    ]
    
    for action in actions:
        twitter_actions(*action)

def insertCodeSuspicious(driver, email, password):
    while True:
        code = re.readMailSuspiciousActivity(email, password)
        if code != None:
            break
        print("Esperando recibir el código de Twitter...")
        sleep(1)

    stepInsertCodeSuspicious(driver, code)
        
    return "Insert Suspicious Code! Ok!"


def unlock_more_on_twitter(driver, type, element):
    selector = get_type_selector(type)
    try: 
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
    except TimeoutException:
        return False
    
    if div_action.text in [
        "Unlock more on Twitter",
        "You've unlocked more on Twitter"
    ]:
        return True
    return False

## ----------------------------------------------END-------------------------------------------------##
#######################################################################################################


# Function that check the answers
def check_answer(answer, user):
    # Check if are the same colours
    if answer != f"/{user}":
        return("Fail because you already comment this tweet!")
    return("Ok!")

# Function to split the word (Ex. JHON -> J H O N)
def split_word(word, driver, div_element, selector, element):
    for letter in word:
        div_element.send_keys(letter)
        # Get the element to sen the keys
        WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element_value((selector, element), word[:word.index(letter) + 1]))
        # Send the word letter by letter
    div_element.send_keys(Keys.RETURN)
    return "Split word! Ok!"

# Function to split the word (Ex. JHON -> J H O N) but before use the clear
def split_word_clear(word, driver, div_element, selector, element):
    div_element.clear()
    for letter in word:
        div_element.send_keys(letter)
        # Get the element to sen the keys
        WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element_value((selector, element), word[:word.index(letter) + 1]))
        # Send the word letter by letter
    div_element.send_keys(Keys.RETURN)
    return "Split word! Ok!"

# Function to no split the word and send directly the entire word (depend on the element we have to send it like this)
def no_split_word(word, driver, div_element, selector, element):
    div_action = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((selector, element))
    )
    div_element.send_keys(word)
    
    return "Split No word! Ok!"

def stepCheckAccount(driver, selector, element, locked_text, unlocked_text):
    div_action = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((selector, element))
    )
    
    if div_action.text == locked_text:
        return True
    
    if div_action.text == unlocked_text:
        return True

# This function check if the account is locked or unlocked
def check_account_status(driver, type, element, locked_text="Your account has been locked.", unlocked_text="Account unlocked."):
    selector = get_type_selector(type)
    
    try:
        action, div = find_element(driver, selector, element)
    except ValueError:
        return False
    
    if action != "Find elements! OK!":
        return False
    
    if stepCheckAccount(driver, selector, element, locked_text, unlocked_text):
        return True

    return False

# This function will check if the tweet is already commented (If true --> commented)
def get_already_comment(driver, type, element, user):
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else, remove-unnecessary-cast
    selector = get_type_selector(type)
    
    div_action = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((selector, element))
    )
    
    if div_action.text == f"@{user}":
        return True
    return False

# This function will get the type and return the type of selector
def get_type_selector(type):
    # Obtain the type of selector and validate
    if type not in selector_mapping:
        return "Tipo de selector no válido"
    # Obtain the type of selector
    return selector_mapping[type]

# This function will get the type and return the type of selector
def get_type_action(type):
    # Obtain the type of selector and validate
    if type not in action_mapping:
        return "Tipo de selector no válido"
    # Obtain the type of selector
    return action_mapping[type]

# This function will check if the element is in the web 
def find_element(driver, selector, element):
    try:
        action = "Find elements! OK!"
        div_action = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((selector, element))
        )
        
        return action, div_action
    
    except TimeoutException:
        return "Fail! Time error"
    
    except ValueError:
        return "Fail! We didn't find the element"

# This function will click the element
def click_action(div_action):
    try:
        div_action.click()
        return "Click action! Ok!"
    except TimeoutError:
        return "Fail! Time error"

def checkSendKeys(send_keys, word_send_keys, driver, div_action, selector, element, split, clear):
    if send_keys != False:
        
        if split:
            return split_word(word_send_keys, driver, div_action, selector, element)
        elif clear:
            return split_word_clear(word_send_keys, driver, div_action, selector, element)
        else:
            return no_split_word(word_send_keys, driver, div_action, selector, element)
    else:
        return"No send keys action!"
    
def checkClickActions(driver, div_action, click):
    if click:
        return click_action(div_action)
    else:
        return "NO click action!"
        
# Function to made actions in twitter web page
def twitter_actions(action, driver, type, element, click, send_keys, word_send_keys, split = True, clear = False):
    try:
        selector = get_type_selector(type)

        # We got the element
        log, div_action = find_element(driver, selector, element)
        
        # If we receive that click is True
        log2 = checkClickActions(driver, div_action, click)

        log3 = checkSendKeys(send_keys, word_send_keys, driver, div_action, selector, element, split, clear)

        return f"{action} OK!" + "\n" + log + "\n" + log2 + "\n" + log3

    except TimeoutException:
        return "Fail! Time error!"

    except ValueError:
        return "Fail! We didn't find the element!"

# Function that go to the page
def go_page(log, driver, url, expected_url):
    try:
        while_check_internet()
        # Open the url
        driver.get(url)
        # Maximize the window
        driver.maximize_window()
        actual_url = driver.current_url
        # It check the expected url with actual url
        if expected_url == actual_url:
            return f"{log} Ok!"
        else:
            raise Exception(f"{log} Fail! You are not correct web!")

    except NoSuchElementException as e:
        return f"{log} Fail no element found in the page!: \n{str(e)}"

    except Exception as e:
        return f"{log} Fail! \n{str(e)}"

def get_color(driver, type, element):
    try:
        selector = get_type_selector(type)
        # We got the element
        action, div_element = find_element(driver, selector, element)
        if action != "Find elements! OK!":
            raise Exception(f"Fail! We couldn'd find the element!")
        return div_element.value_of_css_property("color")
    except TimeoutException:
        return "Fail! Time error!"
    
    except ValueError:
        return "Fail! We didn't find the element!"

def get_background_color(driver, type, element):
    try:
        selector = get_type_selector(type)
        # We got the element
        action, div_element = find_element(driver, selector, element)
        if action != "Find elements! OK!":
            raise Exception(f"Fail! We couldn'd find the element!")
        return div_element.value_of_css_property("background-color")
    except TimeoutException:
        return "Fail! Time error!"
    
    except ValueError:
        return "Fail! We didn't find the element!"

def get_rgb_values(rgba):
    # Function that get the rgb valu
    r, g, b, a = map(int, rgba[rgba.index("(")+1:rgba.index(")")].split(", "))
    return f"rgb({str(r)}, {str(g)}, {str(b)})"

def get_answer(driver, type, element):
    try:
        selector = get_type_selector(type)
        # We got the element
        action, div_element = find_element(driver, selector, element)
        if action != "Find elements! OK!":
            raise Exception(f"Fail! We couldn'd find the element!")
        return div_element.get_attribute('href')
    except TimeoutException:
        return "Fail! Time error!"
    
    except ValueError:
        return "Fail! We didn't find the element!"

def languageTwitter(driver):
    
    twitter_actions("Checkbox click!", driver, 2,
                    "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/label[2]/div[2]/label/div/div/input",
                    True, False, None)
    
    twitter_actions("Next button!", driver, 2,
                    "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div",
                    True, False, None)
    
    return "Language Twitter ok!"

def entertainmentTwitter(driver):
    actions =[
        ("Music selected!", driver, 2,
                    "//*[@id='verticalGridItem-0-categoryrecommendations-1666488626164269056']/div/div/div/div",
                    True, False, None),
        ("Press button", driver, 2, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div", True, False, None),
        ("Insert password", driver, 2, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input", True, True, password),
    ]
    
    for action in actions:
        print(twitter_actions(*action))
        
    twitter_actions("Music selected!", driver, 2,
                    "//*[@id='verticalGridItem-0-categoryrecommendations-1666488626164269056']/div/div/div/div",
                    True, False, None)

def skipNotifications(driver):
    
    twitter_actions("Skip notifications", driver, 2,
                    "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]",
                    True, False, None)
    
    return "Skip notifications! Ok!"

def skipImage(driver):
    
    twitter_actions("Omit Upload image now", driver, 2, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div", True, False, None)
    
    return "Skip image! OK!"

def continue_creating_user(driver, locked):
    if locked:
        twitter_actions()
    else:
        skipNotifications(driver)

def insertImageProfile(driver, image):
    
    twitter_actions("Upload Image!", driver, 2,
                    "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div/input",
                    False, True, image, split = False)
    
    twitter_actions("Apply image!", driver, 2, "//*[@id='layers']/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div",
                    True, False, None)
    
    twitter_actions("Click Next Button!", driver, 2, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div",
                    True, False, None)
    
    return "Upload Image! Ok!"

# Function to close the actual session
def closeSession(driver):
    actions = [
    ("Open tab for close session", driver, 2, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[4]", True, False, None),
    ("Click close session", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div/span", True, False, None),
    ("Click close session", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div", True, False, None),]
    
    for action in actions:
        twitter_actions(*action)

# Function to accept the cookies
def acceptCookies(driver):
    twitter_actions("Accept Cookies!", driver, 2, "//*[@id='layers']/div/div/div/div/div/div[2]/div[1]", True, False, None)

def accountLocked(driver):
    twitter_actions("Click Button!", driver, 1, "/html/body/div[2]/div/form/input[6]", True, False, None)
    twitter_actions("Click Button", driver, 1, "//*[@id='home_children_button']", True, False, None)
    
def insertUsername(driver, username):
    
    twitter_actions("Username enter!", driver, 2,
                    "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
                    ,True, True, username, True, True)
    
    twitter_actions("Header click to wait", driver, 1, "#modal-header", True, False, None)
    
    twitter_actions("Click Next Button!", driver, 2,
                    "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div",
                    True, False, None)
    
    return "Insert username! Ok!"

def checkColorStep1(driver):
    return get_background_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div")

def checkColorFollowUser_1(driver):
    # Get the RGB values
    r1, g1, b1, a1 = get_rgba_value(checkColorStep1(driver))
    r2, g2, b2, a2 = get_rgba_value(black_color_follow_rgba_css)
    
    return check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)

def checkColorStep2(driver):
    return get_background_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div")


def checkColorFollowUser_2(driver):
    # Get the RGB values
    r1, g1, b1, a1 = get_rgba_value(checkColorStep2(driver))
    r2, g2, b2, a2 = get_rgba_value(black_color_follow_rgba_css)
    
    return check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)

def split_register(driver, email_twitter, profile, year, month, day, email, password, data, password_twitter, user_twitter):
    
    step1CreateUserTwitter(driver, email_twitter, profile, year, month, day)
    
    step2CreateUserTwitter(driver)
    
    fdb.loadValues(email, password, data)
    
    step3CreateUserTwitter(driver)
    
    stepVerifyCreateUserTwitter(driver)
    
    step4CreateUserTwitter(driver, email_twitter, password_twitter)
    
    step5CreateUserTwitter(driver, password_twitter)
    
    step6DiscardImageProfile(driver)
    
    step7IntroduceUSername(driver, user_twitter)
    
    step8SkipNotifications(driver)
    
    step9CreateUserTwitter(driver)
    
    verifyIsAccountLocked(driver)
    
    acceptCookies(driver)
    
    step10ChangeImageProfile(driver)
    
    return "Create register step ok!"

