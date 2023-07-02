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
        check = tf.checkColorFollowUser_1(driver)
        if check != "Ok!":
            raise Exception("Follow user! Fail because you already follow this user!")
        print("Botón siguiendo usuario")
        tf.twitter_actions("Follow user", driver, 2, "//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div", True, False, None)
        check = tf.checkColorFollowUser_2(driver)
        
        if check != "Ok!":
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


# TODO Rename this here and in `comment_tweet`
def go_comment(driver, comment, user, arg3):
    tf.twitter_actions("Check and click Comment tweet", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[1]/div", True, False, None)
    tf.twitter_actions("Click and send Comment tweet", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div", True, True, comment, False, False)
    tf.twitter_actions("Click reply!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]", True, False, None)
    sleep(1)

    if tf.get_already_comment(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[3]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[1]", user):
        
        sleep(2)
        
        if tf.unlock_more(driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/span"):
                tf.twitter_actions("Click ok in button!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div", True, False, None)
        return "Comment Twitter! Ok!"
        
    return arg3

def retweet_tweet(driver, url, expected_url):
    try:
        tf.go_page("Go to tweet", driver, url, expected_url)
        tf.twitter_actions("Get element for Retweet tweet", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[2]", False, False, None)

        # Get the color of the element
        color = tf.get_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[2]/div/div")
        # Get the RGB values
        r1, g1, b1, a1 = tf.get_rgba_value(color)
        r2, g2, b2, a2 = tf.get_rgba_value(green_color_retweet_css)
        
        check = tf.check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)
        if check != "Ok!":
            raise Exception("Retweet Tweet! Fail because you already retweet this tweet!")
        
        print(tf.twitter_actions("Retweet Tweet Click", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[2]", True, False, None))
        print(tf.twitter_actions("Choose Retweet Option Tweet Click", driver, 2, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div", True, False, None))
        
        sleep(1)
        
        color = tf.get_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[2]/div/div")
        # Get the RGB values
        r1, g1, b1, a1 = tf.get_rgba_value(color)
        check = tf.check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)
        
        sleep(2)
        
        if check != "Ok!":
            if tf.unlock_more(driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/span"):
                tf.twitter_actions("Click ok in button!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div", True, False, None)
            return "Retweet Twitter! Ok!"
        
        return "Something has failed! Retry!"

    except TimeoutException:
        return "Retweet Twitter! Time Error!"

    except Exception as e:
        return f"{e}"

def like_tweet(driver, url, expected_url):
    # sourcery skip: hoist-similar-statement-from-if, hoist-statement-from-if, remove-unnecessary-else, swap-if-else-branches
    try:
        tf.go_page("Go to tweet", driver, url, expected_url)
        tf.twitter_actions("Get element for Like tweet", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]/div", False, False, None)
        
        # Get the color of the element
        color = tf.get_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]/div/div")
        
        if color == "Fail! We didn't find the element!":
            color = tf.get_color(driver, 1, ".r-1bwzh9t")

        # Get the RGB values
        r1, g1, b1, a1 = tf.get_rgba_value(color)
        r2, g2, b2, a2 = tf.get_rgba_value(red_color_like_css)

        check = tf.check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)
        
        if check != "Ok!":
            raise Exception("Like Tweet! Fail because you already like this tweet!")
        
        tf.twitter_actions("Liking Tweet", driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]", True, False, None)
        
        sleep(1)
        
        # Get the color of the element
        color = tf.get_color(driver, 2, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]/div/div")
        
        # Get the RGB values
        r1, g1, b1, a1 = tf.get_rgba_value(color)
        r2, g2, b2, a2 = tf.get_rgba_value(red_color_like_css)
        
        check = tf.check_rgba_values(r1, g1, b1, a1, r2, g2, b2, a2)
        
        sleep(2)
        
        if check != "Ok!":
            if tf.unlock_more(driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/span"):
                tf.twitter_actions("Click ok in button!", driver, 2, "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div", True, False, None)
                return "Like Twitter! Ok!"
            else:
                return "Like Twitter! Ok!"
        else:
            return "Something has failed! Retry!"

    except TimeoutException:
        return "Like Twitter! Time Error!"

    except Exception as e:
        return f"{e}"

def loginUserTwitter(driver, email, password, user):
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
        
    if tf.check_account_status(driver, 2, "/html/body/div[2]/div/div[1]"):
        # fdb.updateValues(temp.get_email(), temp.get_password(), email, "locked")
        fdb.updateValues("danifdezloz@gmail.com", "Dani5Fdez", email, "locked")
        return "Your account is locked!"
    
    sleep(1)
    
    tf.acceptCookies(driver)
    
    # /html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span
    if tf.get_user_profile(driver, 2, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span", user):
        return "Login User! Ok!"
    
    if driver.current_url == "https://twitter.com/account/access":
        fdb.updateValues("danifdezloz@gmail.com", "Dani5Fdez", email, "locked")
        return "Your account is locked!"
    
    return "Something has failed retry!"

def registerUserTwitter(driver, email, password):
    try:
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
        
        ce.createMail(data)
        
        tf.split_register(driver, email_twitter, profile, year, month, day,
                        email, password, data, password_twitter, user_twitter)
        
        try_newAccount(driver, user_twitter)
        
        return "Create User! Ok!"
        
    except exceptions as e:
        if "not connected to DevTools" in str(e):
            ce.deleteMail(email_twitter)
            fdb.deleteValues(email, password)
            return "Ups! Seem you close the page before finishing the process"
    
    except KeyboardInterrupt as e:
        ce.deleteMail(email_twitter)
        fdb.deleteValues(email, password)
        return "Ups! Seem you close the page before finishing the process"

## --------------------------------------------END-------------------------------------------- ##
#################################################################################################

######################### HERE ARE THE FUNCTIONS FOR THE GUI OF THE APP #########################
## --------------------------------------------------------------------------------------------##
            #! action_n_times --> will like, retweet, comment or follow n times
            #? If you alredy liked on the tweet, it will indicate 
            #? that the like has already been made
            #! Params -> driver, data, url, expected_url, selector, comment = "", user = ""
                # driver -> use the web browser
                # data -> dictionary with email, password, user for Twitter
                # url -> url given 
                # expected_ulr -> check if the url doesn't redirect
                # selector  -> help to make the action could be:
                    # 1 -> Retweet
                    # 2 -> Like
                    # 3 -> Comment
                    # 4 -> Follow
                # comment -> introduce the comment to write in the timeline
                # user -> to check if the comment has already made
## --------------------------------------------------------------------------------------------##
            #! full_action_n_times --> will like, retweet, comment or follow n times
            #? If you alredy liked on the tweet, it will indicate 
            #? that the like has already been made
            #! Params -> driver, data, url, expected_url, comment, user
                # driver -> use the web browser
                # data -> dictionary with email, password, user for Twitter
                # url -> url given 
                # expected_ulr -> check if the url doesn't redirect
                # comment -> introduce the comment to write in the timeline
                # user -> to check if the comment has already made
## --------------------------------------------------------------------------------------------##

# Function to make action in relation with 
def action_n_times(driver, data, url, expected_url, type, comment = "", user = ""):
    selector = tf.get_type_action(type)
    
    # For that will like the tweet n times
    for key, value in data.items():
        
        # Extract the valours of email, password, user
        email = value['email']
        password = value['password']
        user = value['user']
        
        # Function to log into the account
        loginUserTwitter(driver, email, password, user)
        # Function to accept the cookies
        tf.acceptCookies(driver)
        
        # Depend on the selector will make a different action
        if selector == "Retweet":
            # Action for retweet tweet
            retweet_tweet(driver, url, expected_url)
        elif selector == "Like":
            # Action of like tweet
            like_tweet(driver, url, expected_url)
        elif selector == "Comment":
            comment_tweet(driver, url, expected_url, comment, user)
        elif selector == "Follow":
            follow_user(driver, url, expected_url)
            
        # Close session for the next user
        tf.closeSession(driver)
        # We wait 2 seconds for the next user
        sleep(2)

def full_action_n_times(driver, data, url, expected_url, comment, user):
    # For that will like the tweet n times
    for key, value in data.items():
        
        # Extract the valours of email, password, user
        email = value['email']
        password = value['password']
        user = value['user']
        
        # Function to log into the account
        loginUserTwitter(driver, email, password, user)
        # Function to accept the cookies
        tf.acceptCookies(driver)

        retweet_tweet(driver, url, expected_url)
        like_tweet(driver, url, expected_url)
        # comment_tweet(driver, url, expected_url, comment, user)
            
        # Close session for the next user
        tf.closeSession(driver)
        # We wait 2 seconds for the next user
        sleep(2)
        
        return "Action completed"
## --------------------------------------------END-------------------------------------------- ##
#################################################################################################

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