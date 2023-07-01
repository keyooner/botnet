import TwitterFunctions.twitterActions as function
import TwitterFunctions.seleniumFunctions as function2
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import FirebaseFunctions.firebaseDatabase as fdb
import re

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
email = "xzxsvejb23119767@raptoragency.es"
password = "Kpojtgke$$47380624"
user = "9d1iie2ASmg7u87"

def loadActions(email, check1, check2, check3, url, user):
    
    data = {
        "email": email,
        "like": check1,
        "retweet": check2,
        "comment": check3,
    }
    
    username, numbers = split_url_actions(url)
    
    fdb.loadValuesActionsTwitter("danifdezloz@gmail.com", "Dani5Fdez", f"{username}-{numbers}", data, user)

def loadFollow(email, check, url, user):
    
    data = {
        "email": email,
        "follow": check
    }
    
    username = split_url_follow(url)
    print(username)
    fdb.loadValuesFollow("danifdezloz@gmail.com", "Dani5Fdez", username, data, user)
    
def split_url_actions(url):
    # Utilizamos una expresión regular para extraer "TFM_Botnet_" y los números
    pattern = r"(https://twitter.com/)([A-Za-z0-9_]+)(/status/)([0-9]+)"
    matches = re.search(pattern, url)

    if matches:
        username = matches.group(2)  # "TFM_Botnet_"
        numbers = matches.group(4)  # "1674334209156997120"
        return username, numbers
    
    else:
        return None

def split_url_follow(url):
    # Utilizamos una expresión regular para extraer "TFM_Botnet_" y los números
    pattern = r"(https://twitter.com/)([A-Za-z0-9_]+)"
    matches = re.search(pattern, url)

    if matches:
        username = matches.group(2)  # "TFM_Botnet_"
        return username
    
    else:
        return None
    
# email = "wmpkizhg96696548@raptoragency.es"
# password = "Oktebufk$_79375481"
# user = "RamiP3agost199"
# url = "https://twitter.com/TFM_Botnet_/status/1674334209156997120"
url = "https://twitter.com/TFM_Botnet_"

# function.step1CreateUserTwitter(driver, "asjodjoidsjios@as.com", "Dani5Fdez", "1996", "Julio", "17")
# function.step2CreateUserTwitter(driver)
# function.step3CreateUserTwitter(driver)

# data = fdb.get_values("danifdezloz@gmail.com", "Dani5Fdez")
# limit = 20  # Número de veces que quieres iterar
# count = 0

# for i in range(1, limit + 1):
#     id = f"ID-{i}"
    
#     if id in data:
#         values = data[id]
#         # Desglosar los valores en atributos individuales
#         email = values['email']
#         day = values['day']
#         gender = values['gender']
#         month = values['month']
#         name = values['name']
#         password = values['password']
#         state = values['state']
#         surname = values['surname']
#         user = values['user']
#         year = values['year']
        
#         function.loginUserTwitter(driver, email, password, user)
#         function.acceptCookies(driver)
#         function.try_newAccount(driver, user)
        
#         count += 1
        
#     if count >= limit:
#         break
    
# print(function.registerUserTwitter(driver, "danifdezloz@gmail.com", "Dani5Fdez"))
# print(function.loginUserTwitterLocked(driver, email, password, user))
# function.step10ChangeImageProfile(driver)
print(function.loginUserTwitter(driver, email, password, user))
# print(function.verifyIsAccountLocked(driver))
# print(function.step10ChangeImageProfile(driver))
function.acceptCookies(driver)

# like = function.like_tweet(driver, url, url)
# if like == "Like Twitter! Ok!" or "Like Tweet! Fail because you already like this tweet!":
#     check1 = True
# sleep(1)
# # print(function.follow_user(driver, url, url))
# comment = function.comment_tweet(driver, url, url, "Checked!", user)
# if comment == "Comment Twitter! Ok!" or "Comment Tweet! Fail because you already comment this tweet!":
#     check3 = True
# sleep(1)
# retweet = function.retweet_tweet(driver, url, url)
# if retweet == "Retweet Twitter! Ok!" or "Retweet Tweet! Fail because you already retweet this tweet!":
#     check2 = True
# sleep(1)

follow = function.follow_user(driver, url, url)

if follow == "Follow User Twitter! Ok!" or "Follow user! Fail because you already follow this user!":
    check = True
sleep(1)

loadFollow(email, check, url, user)
