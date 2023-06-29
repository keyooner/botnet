import TwitterFunctions.seleniumFunctions as function
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
# email = "xzxsvejb23119767@raptoragency.es"
# password = "Kpojtgke$$47380624"
# user = "9d1iie2ASmg7u87"
email = "aspfpeqy37046531@raptoragency.es"
password = "Sjsmfevh$_28760679"
user = "Vid3en1"
url = "https://twitter.com/TFM_Botnet_/status/1674334209156997120"
# url = "https://twitter.com/TFM_Botnet_"

# function.step1CreateUserTwitter(driver, "asjodjoidsjios@as.com", "Dani5Fdez", "1996", "Julio", "17")
# function.step2CreateUserTwitter(driver)
# function.step3CreateUserTwitter(driver)

#print(function.registerUserTwitter(driver, "danifdezloz@gmail.com", "Dani5Fdez"))
# function.loginUserTwitter(driver, "ekmuroxf55734774@raptoragency.es", "Vajaqxbf_$19613930", "EricA3febr197")
# function.step10ChangeImageProfile(driver)
print(function.loginUserTwitter(driver, email, password, user))
# print(function.verifyIsAccountLocked(driver))
# print(function.step10ChangeImageProfile(driver))
function.acceptCookies(driver)
print(function.like_tweet(driver, url, url))
sleep(300)
# print(function.retweet_tweet(driver, url, url))
# print(function.comment_tweet(driver, url, url, "Grande Ibai!", user))
# print(function.follow_user(driver, url, url))