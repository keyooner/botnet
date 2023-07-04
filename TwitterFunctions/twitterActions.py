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
import TwitterFunctions.twitterFunctions as tf

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

############# HERE ARE THE FUNCTIONS IN RELATION WITH THE FINAL ACTIONS FOR TWITTER #############
## --------------------------------------------------------------------------------------------##
            #! follow_user --> will follow the user in the url fiven
            #? If you are already following the user, it will indicate that 
            #? you cannot follow them again.
            #! Params -> driver, url, expeteced_url
                # driver -> use the web browser
                # url -> url given 
                # expected_ulr -> check if the url doesn't redirect
## --------------------------------------------------------------------------------------------##
            #! comment_tweet --> will comment the tweet passed in the url given
            #? If you alredy commented on the tweet, it will indicate 
            #? that the comment has already been made
            #! Params -> driver, url, expected_url, comment, user
                # driver -> use the web browser
                # url -> url given 
                # expected_ulr -> check if the url doesn't redirect
                # comment -> the text that you are going to comment
                # user -> we need user to check if you has already commented
## --------------------------------------------------------------------------------------------##
            #! retweet_tweet --> will retweet the tweet passed in the url given
            #? If you alredy retweeted on the tweet, it will indicate 
            #? that the retweet has already been made
            #! Params -> driver, url, expected_url
                # driver -> use the web browser
                # url -> url given 
                # expected_ulr -> check if the url doesn't redirect            
## --------------------------------------------------------------------------------------------##
            #! like_tweet --> will like the tweet passed in the url given
            #? If you alredy liked on the tweet, it will indicate 
            #? that the like has already been made
            #! Params -> driver, url, expected_url
                # driver -> use the web browser
                # url -> url given 
                # expected_ulr -> check if the url doesn't redirect
## --------------------------------------------------------------------------------------------##
            #! loginUserTwitter --> will login into twitter
            #? Make al the steps to login into the account and check if twitter suspects of
            #? the account to insert the user and continue the login
            #! Params -> driver, email, password, user
                # driver -> use the web browser
                # email -> email of the account created
                # password -> password of the account created
                # user -> we need user if the account is under suspect
## --------------------------------------------------------------------------------------------##
#################################################################################################
                            
# Function to follow a user in twitter
def follow_user(driver, url, expected_url):
    try:
        tf.go_page("Go to Twitter User Page", driver, url, expected_url)
        tf.twitter_actions("Check follow button", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div", False, False, None)

        if tf.checkColorFollowUser_1(driver) != "Ok!":
            raise Exception("Follow user! Fail because you already follow this user!")
        
        tf.twitter_actions("Follow user", driver, 2, "//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div", True, False, None)
        
        if tf.checkColorFollowUser_2(driver) != "Ok!":
            return "Follow User Twitter! Ok!"
        
        return "Something has failed! Retry!"
    
    except TimeoutException:
        return "Follow User Twitter! Time Error!"

    except Exception as e:
        return f"{e}"
    
# Function to comment a tweet 
def comment_tweet(driver, url, expected_url, comment, user):
    try:
        
        tf.go_page("Go to tweet", driver, url, expected_url)

        if tf.get_already_comment(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[3]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]", user):
            raise Exception("Comment Tweet! Fail because you already comment this tweet!")

        return go_comment(
            driver, comment, user, "Something has failed! Retry!"
        )
    except TimeoutException:
        return go_comment(
            driver, comment, user, "Comment Twitter! Time Error!"
        )
    except Exception as e:
        return f"{e}"

def stepComment(driver, comment):
    tf.twitter_actions("Check and click Comment tweet", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[1]/div", True, False, None)
    tf.twitter_actions("Click and send Comment tweet", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div", True, True, comment, False, False)
    tf.twitter_actions("Click reply!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]", True, False, None)

# TODO Rename this here and in `comment_tweet`
def go_comment(driver, comment, user, arg3):
    
    stepComment(driver, comment)
    
    sleep(1)

    if tf.get_already_comment(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[3]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]", user):
        
        sleep(1)
        
        if tf.unlock_more(driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/span"):
                tf.twitter_actions("Click ok in button!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div", True, False, None)
        
        return "Comment Twitter! Ok!"
        
    return arg3

def rtRGB_1(driver):

    # Get the color of the element
    color = tf.get_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[2]/div/div")
    # Get the RGB values
    r1, g1, b1, a1 = tf.get_rgba_value(color)
    r2, g2, b2, a2 = tf.get_rgba_value(green_color_retweet_css)

    return tf.check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)

def rtRGB_2(driver):
    
    color = tf.get_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[2]/div/div")
    
    # Get the RGB values
    r1, g1, b1, a1 = tf.get_rgba_value(color)
    r2, g2, b2, a2 = tf.get_rgba_value(green_color_retweet_css)
    
    return tf.check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)

def stepRT(driver):
    tf.twitter_actions("Retweet Tweet Click", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[2]", True, False, None)
    tf.twitter_actions("Choose Retweet Option Tweet Click", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div", True, False, None)
        

def retweet_tweet(driver, url, expected_url):
    try:
        tf.go_page("Go to tweet", driver, url, expected_url)
        tf.twitter_actions("Get element for Retweet tweet", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[2]", False, False, None)

        if rtRGB_1!= "Ok!":
            raise Exception("Retweet Tweet! Fail because you already retweet this tweet!")
        
        stepRT(driver)
        
        sleep(1)
        
        if rtRGB_2 != "Ok!":
            if tf.unlock_more(driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/span"):
                tf.twitter_actions("Click ok in button!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div", True, False, None)
            return "Retweet Twitter! Ok!"
        
        return "Something has failed! Retry!"

    except TimeoutException:
        return "Retweet Twitter! Time Error!"

    except Exception as e:
        return f"{e}"

def likeRGB_1(driver):
            # Get the color of the element
        color = tf.get_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]/div/div")
        
        if color == "Fail! We didn't find the element!":
            color = tf.get_color(driver, 1, ".r-1bwzh9t")

        # Get the RGB values
        r1, g1, b1, a1 = tf.get_rgba_value(color)
        r2, g2, b2, a2 = tf.get_rgba_value(red_color_like_css)

        return tf.check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)

def likeRGB_2(driver):
    # Get the color of the element
    color = tf.get_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]/div/div")
    
    # Get the RGB values
    r1, g1, b1, a1 = tf.get_rgba_value(color)
    r2, g2, b2, a2 = tf.get_rgba_value(red_color_like_css)
    
    return tf.check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)

def get_unlock_more_like(driver):
    # sourcery skip: hoist-similar-statement-from-if, hoist-statement-from-if, remove-unnecessary-else, swap-if-else-branches
    if likeRGB_2(driver) != "Ok!":
        if tf.unlock_more(driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/span"):
            tf.twitter_actions("Click ok in button!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div", True, False, None)
            return "Like Twitter! Ok!"
        else:
            return "Like Twitter! Ok!"
    else:
        return "Something has failed! Retry!"
    
def like_tweet(driver, url, expected_url):
    # sourcery skip: hoist-similar-statement-from-if, hoist-statement-from-if, remove-unnecessary-else, swap-if-else-branches
    try:
        tf.go_page("Go to tweet", driver, url, expected_url)
        tf.twitter_actions("Get element for Like tweet", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]/div", False, False, None)
        
        if likeRGB_1(driver) != "Ok!":
            raise Exception("Like Tweet! Fail because you already like this tweet!")
        
        tf.twitter_actions("Liking Tweet", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]", True, False, None)
        
        sleep(1)
        
        return get_unlock_more_like(driver)

    except TimeoutException:
        return "Like Twitter! Time Error!"

    except Exception as e:
        return f"{e}"
    
def login_locked(driver, user):
    if tf.get_login_locked(driver, 2, "//*[@id='modal-header']/span/span"):
    
        tf.twitter_actions("Insert user!", driver, 2, 
                        "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
                        True, True, user)
        
        tf.twitter_actions("Click next button!", driver, 2,
                        "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div",
                        True, False, None)
    
def suspicious_activity(driver, email, password):
    if tf.get_suspicious_activity(driver, 2, "//*[@id='modal-header']/span/span"):
        tf.insertCodeSuspicious(driver, email, password)
        
def account_locked(driver, email):
    if tf.check_account_status(driver, 2, "/html/body/div[2]/div/div[1]"):
        fdb.updateValues(temp.get_email(), temp.get_password(), email, "locked")
        return "Your account is locked!"

    if driver.current_url == "https://twitter.com/account/access":
        fdb.updateValues("danifdezloz@gmail.com", "Dani5Fdez", email, "locked")
        return "Your account is locked!"

def loginUserStep1(driver, email):
    actions = [
        ("Check Twitter Login Page", driver, 1, "div.r-1867qdf:nth-child(2)", False, False, None),
        ("Login User", driver, 1, ".r-30o5oe", True, True, email),
        ("Check and Click Next Button", driver, 1, "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div", True, False, None),
    ]
    
    for action in actions:
        tf.twitter_actions(*action)

def loginUserStep2(driver, password):
    actions2 =[    
        ("Login Password", driver, 1, ".r-homxoj", True, True, password),
        #("Check and Click Next Button", driver, 2, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div", True, False, None)
        ("Check and Click Next Button", driver, 1, "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div > div", True, False, None)
    ]
    
    for action2 in actions2:
        tf.twitter_actions(*action2)
    
def loginUserTwitter(driver, email, password, user):
    #! First Step we go to the login page and we check that we don't redirect to another one
    tf.go_page("Twitter Login Page", driver, url_login, "https://twitter.com/i/flow/login")
    
    #! We use this for make a chain of actions, first we check that we are in the login form
    #! Then we insert the credentials of the email, last one click on next button
    loginUserStep1(driver, email)

    login_locked(driver, user)
    
    loginUserStep2(driver, password)
    
    suspicious_activity(driver, email, password)
    
    if account_locked(driver, email) == "Your account is locked!":
        return "Your account is locked!"
    
    sleep(1)
    
    tf.acceptCookies(driver)

    if tf.get_user_profile(driver, 2, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span", user):
        return "Login User! Ok!"
    
    return "Something has failed retry!"

def registerUserTwitter(driver, email, password):
    try:

        data, email_twitter, password_twitter, user_twitter, month, day, year, profile = infoProfile()
        
        ce.createMail(data)
        
        tf.split_register(driver, email_twitter, profile, year, month, day,
                        email, password, data, password_twitter, user_twitter)
        
        try_newAccount(driver, user_twitter)
        
        return "Create User! Ok!"
        
    except exceptions as e:
        if "not connected to DevTools" in str(e):
            deleteAccount(email_twitter, email, password)
            return "Ups! Seem you close the page before finishing the process"
    
    except KeyboardInterrupt as e:
        deleteAccount(email_twitter, email, password)
        return "Ups! Seem you close the page before finishing the process"

## --------------------------------------------END-------------------------------------------- ##
#################################################################################################
def infoProfile():
    data = ce.generateProfile()
    
    email_twitter = data["email"]
    password_twitter = data["password"]
    user_twitter = data["user"]
    month = data["month"]
    day = data["day"]
    year = data["year"]
    name = data ["name"]
    surname = data["surname"]
    profile = f"{name} {surname}"
    
    return data, email_twitter, password_twitter, user_twitter, month, day, year, profile

def deleteAccount(email_twitter, email, password):
    ce.deleteMail(email_twitter)
    fdb.deleteValues(email, password)

def try_newAccount(driver, user_twitter):
    
    tf. verifyIsAccountLocked(driver)
    follow_user(driver, "https://twitter.com/TFM_Botnet_", "https://twitter.com/TFM_Botnet_")
    
    tf.verifyIsAccountLocked(driver)
    like_tweet(driver, "https://twitter.com/TFM_Botnet_/status/1674334209156997120", "https://twitter.com/TFM_Botnet_/status/1674334209156997120")
    
    tf.verifyIsAccountLocked(driver)
    retweet_tweet(driver, "https://twitter.com/TFM_Botnet_/status/1674334209156997120", "https://twitter.com/TFM_Botnet_/status/1674334209156997120")
    
    tf.verifyIsAccountLocked(driver)
    comment_tweet(driver, "https://twitter.com/TFM_Botnet_/status/1674334209156997120", "https://twitter.com/TFM_Botnet_/status/1674334209156997120", "Checked!", user_twitter)
    
    return "All actions has been tried!"

def loginUserTwitterLocked(driver, email, password, user):
    #! First Step we go to the login page and we check that we don't redirecto to another one
    tf.go_page("Twitter Login Page", driver, url_login, "https://twitter.com/i/flow/login")
    
    #! We use this for make a chain of actions, first we check that we are in the login form
    #! Then we insert the credentials of the email, last one click on next button
    actions = [
        ("Check Twitter Login Page", driver, 1, "div.r-1867qdf:nth-child(2)", False, False, None),
        ("Login User", driver, 1, ".r-30o5oe", True, True, email),
        ("Check and Click Next Button", driver, 1, "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div", True, False, None),
    ]
    
    for action in actions:
        tf.twitter_actions(*action)
    
    if tf.get_login_locked(driver, 2, "//*[@id='modal-header']/span/span"):
        
        tf.twitter_actions("Insert user!", driver, 2, 
                        "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
                        True, True, user)
        
        tf.twitter_actions("Click next button!", driver, 2,
                        "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div",
                        True, False, None)
        
    actions2 =[    
        ("Login Password", driver, 1, ".r-homxoj", True, True, password),
        #("Check and Click Next Button", driver, 2, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div", True, False, None)
        ("Check and Click Next Button", driver, 1, "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div > div", True, False, None)
    ]
    
    for action2 in actions2:
        tf.twitter_actions(*action2)
    
    if tf.get_suspicious_activity(driver, 2, "//*[@id='modal-header']/span/span"):
        tf.insertCodeSuspicious(driver, email, password)
    
    tf.verifyIsAccountLocked(driver)
        
    if tf.check_account_status(driver, 2, "/html/body/div[2]/div/div[1]"):
        # fdb.updateValues(temp.get_email(), temp.get_password(), email, "locked")
        fdb.updateValues("danifdezloz@gmail.com", "Dani5Fdez", email, "locked")
        return "Your account is locked!"
    
    # /html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span
    if tf.get_user_profile(driver, 2, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span", user):
        return "Login User! Ok!"
    
    return "Something has failed retry!"

# Function to close the actual session
def closeSession(driver):
    actions = [
    ("Open tab for close session", driver, 2, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[4]", True, False, None),
    ("Click close session", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div/span", True, False, None),
    ("Click close session", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div", True, False, None),]
    
    for action in actions:
        tf.twitter_actions(*action)
    return "Clossed Session!"

def acceptCookies(driver):
    tf.twitter_actions("Accept Cookies!", driver, 2, "//*[@id='layers']/div/div/div/div/div/div[2]/div[1]", True, False, None)
    return "Cookies has been accepted!"