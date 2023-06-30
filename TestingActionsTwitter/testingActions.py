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
email = "nrbcavid60586332@raptoragency.es"
password = "Pfvgnegg_$85749456"
user = "JeV3ene19"
# url = "https://twitter.com/TFM_Botnet_/status/1674334209156997120"
url = "https://twitter.com/TFM_Botnet_"

# function.step1CreateUserTwitter(driver, "asjodjoidsjios@as.com", "Dani5Fdez", "1996", "Julio", "17")
# function.step2CreateUserTwitter(driver)
# function.step3CreateUserTwitter(driver)

# print(function.registerUserTwitter(driver, "danifdezloz@gmail.com", "Dani5Fdez"))
function.loginUserTwitter(driver, email, password, user)
# function.step10ChangeImageProfile(driver)
# print(function.loginUserTwitter(driver, email, password, user))
# print(function.verifyIsAccountLocked(driver))
# print(function.step10ChangeImageProfile(driver))
# function.acceptCookies(driver)
# print(function.like_tweet(driver, url, url))
# print(function.follow_user(driver, url, url))
# print(function.comment_tweet(driver, url, url, "Checked!", user))
# print(function.retweet_tweet(driver, url, url))
sleep(5)