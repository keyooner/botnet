import TwitterFunctions.seleniumFunctions as function
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
email = "xzxsvejb23119767@raptoragency.es"
password = "Kpojtgke$$47380624"
user = "9d1iie2ASmg7u87"
# url = "https://twitter.com/IbaiLlanos/status/1672341358365794306"
url = "https://twitter.com/IbaiLlanos"

# function.step1CreateUserTwitter(driver, "asjodjoidsjios@as.com", "Dani5Fdez", "1996", "Julio", "17")
# function.step2CreateUserTwitter(driver)
# function.step3CreateUserTwitter(driver)

print(function.registerUserTwitter(driver, "danifdezloz@gmail.com", "Dani5Fdez"))

# function.loginUserTwitter(driver, email, password, user)
# function.acceptCookies(driver)
# print(function.like_tweet(driver, url, url))
# print(function.retweet_tweet(driver, url, url))
# print(function.comment_tweet(driver, url, url, "Grande Ibai!", user))
# print(function.follow_user(driver, url, url))