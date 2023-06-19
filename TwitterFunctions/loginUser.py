import seleniumFunctions as function
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


url_login = "https://twitter.com/i/flow/login"
usuario = "PruebaRapt88196"
password = "Twitter123"
mail = "prueba@tonto.com"
month = "junio"
day = 26
year = 1994
tweet_url = "https://twitter.com/IbaiLlanos/status/1661821870440857600"
answer = "Esto es una prueba!"
follow_url = "https://twitter.com/AlfredoAlvarezz"

print(function.loginUserTwitter(driver, usuario, password))
# print(function.createUserTwitter(driver, mail, usuario, password, month, day, year))
# print(function.like_tweet(driver, tweet_url, "https://twitter.com/IbaiLlanos/status/1661821870440857600"))
# print(function.retweet_tweet(driver, tweet_url, "https://twitter.com/IbaiLlanos/status/1661821870440857600"))
# print(function.comment_tweet(driver, tweet_url, "https://twitter.com/IbaiLlanos/status/1661821870440857600", answer))
# print(function.follow_user(driver, follow_url, "https://twitter.com/AlfredoAlvarezz"))