import TwitterFunctions.twitterActions as function
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import FirebaseFunctions.firebaseDatabase as fdb
import re

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
# email = "ekmuroxf55734774@raptoragency.es"
# password = "Vajaqxbf_$19613930"
# user = "EricA3febr197"
    
email = "xkuzpbcn49334694@raptoragency.es"
password = "Zbcdwzly-@69740615"
user = "ALast28noviem19"

url = "https://twitter.com/TFM_Botnet_/status/1674334209156997120"
# url = "https://twitter.com/TFM_Botnet_"

print(function.loginUserTwitterLocked(driver, email, password, user))


# print(function.loginUserTwitter(driver, email, password, user))
# # print(function.verifyIsAccountLocked(driver))
# # print(function.step10ChangeImageProfile(driver))
# # print(function.acceptCookies(driver))
# #print(function.follow_user(driver, url, url))
# print(function.retweet_tweet(driver, url, url))
# sleep(300)
# print(function.closeSession(driver))

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
# print(function.loginUserTwitter(driver, email, password, user))
# print(function.verifyIsAccountLocked(driver))
# print(function.step10ChangeImageProfile(driver))
# print(function.acceptCookies(driver))
# print(function.follow_user(driver, url, url))
# print(function.closeSession(driver))
# sleep(300)
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

# follow = function.follow_user(driver, url, url)