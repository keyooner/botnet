from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd
import openvpn_api

# firefox_driver_path = "/geckodriver.exe"
# Crea una instancia del controlador de Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
usuario = "PruebaRapt88196"
password = "Twitter123"
red_color_css = "rgb(249, 24, 128)"

url = "https://twitter.com/i/flow/login"

id_tweet= "1657462457038675969"

# colores
def get_rgb_value(color_string):
    # Obtener los valores RGB de una cadena en formato rgb(...)
    r, g, b = map(int, color_string[color_string.index("(")+1:color_string.index(")")].split(", "))
    return r, g, b

def introduceKeys(word, driver, div_element, css_selector):
    for letter in word:
        div_element.send_keys(letter)
        WebDriverWait(driver, 0.5).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, css_selector), word[:word.index(letter) + 1]))
        
        div_element.send_keys(Keys.RETURN)
    
def goPage(url):
    try:
        driver.get(url)
        driver.maximize_window()
        expected_url = "https://twitter.com/i/flow/login"
        actual_url =  driver.current_url
        
        if expected_url == actual_url:
            return "Go Page! Ok!"
        else:
            raise Exception("Go Page! Fail you are not in the Web Page!")

    except NoSuchElementException as e:
        
        return "Go Page! Fail no element found in the page!: \n" + str(e)
    
    except Exception as e:
        
        return "Go Page! Fail! \n" + str(e)


def checkCurrentPage():
    try:
        # Esperar un máximo de 5 segundos a que aparezca un elemento
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.r-1867qdf:nth-child(2)"))
        )
        
        return "Check page! Ok!"
        
    except TimeoutException:
        
        return "Check page! Time Error!"

def checkButtonNextUser():
    try:
        # Esperar un máximo de 5 segundos a que encuentre el botón siguiente
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"))
        )
        
        # Clica en el botón siguiente
        div_element.click()
        
        return "Check Button Next User! Ok!"
    
    except TimeoutException:
        
        return "Check Button Next User! Time Error!"

def loginUserTwitter(usuario):
    try:
        # Esperar un máximo de 5 segundos a que aparezca un elemento
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".r-30o5oe"))
        )
        
        # Encontrar el elemento div por su selector CSS o cualquier otro método
        div_element.click()
        div_element.clear()
        # Introducir la clave letra a letra
        introduceKeys(usuario, driver, div_element, ".r-30o5oe")
        
        #for letra in usuario:
            # div_element.send_keys(letra)
            # WebDriverWait(driver, 0.5).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, ".r-30o5oe"), usuario[:usuario.index(letra) + 1]))
        
        #div_element.send_keys(Keys.RETURN)
        
        checkButtonNextUser()

        return "Login User! Ok!"
    
    except TimeoutException:
        
        return "Login User! Time Error!"

def checkButtonLogin():
    try:
        # Esperar un máximo de 5 segundos a que encuentre el botón siguiente
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"))
        )
        
        # Clica en el botón siguiente
        div_element.click()
        
        return "Check Button Login! Ok!"
    
    except TimeoutException:
        
        return "Check Button Login! Time Error!"

def loginPassTwitter(password):
    try:
        # Esperar un máximo de 5 segundos a que aparezca un elemento
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".r-homxoj"))
        )
        
        # Encontrar el elemento div por su selector CSS o cualquier otro métod
        div_element.click()
        div_element.clear()
        
        # Introducir la clave letra a letra
        for letra in password:
            div_element.send_keys(letra)
            WebDriverWait(driver, 0.5).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, ".r-homxoj"), password[:password.index(letra) + 1]))
        
        div_element.send_keys(Keys.RETURN)
        # sendKeys(div_element, password)
        # div_element.send_keys(password)
        
        checkButtonLogin()
        
        return "Login Pass! Ok!"
        
    except TimeoutException:
        
        return "Login Pass! Time Error!"

def goTweet(id_tweet):
    try:
        driver.get(f"https://twitter.com/AveAveces/status/{id_tweet}")
        driver.maximize_window()
    
        expected_url = f"https://twitter.com/AveAveces/status/{id_tweet}"
        actual_url =  driver.current_url
        
        if expected_url == actual_url:
            return "Go Tweet! Ok!"
        else:
            raise Exception("Go Tweet! Fail you are not in the Web Page!")

    except NoSuchElementException as e:
        
        return "Go Tweet! Fail no element found in the page!: \n" + str(e)
    
    except Exception as e:
        
        return "Go Tweet! Fail! \n" + str(e)

def likeTweet():
    try:
        # Esperar un máximo de 5 segundos a que aparezca un elemento
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]/div/div/div/div"))
        )

        color = div_element.value_of_css_property("color")
        print(f"color: {color}")
        print(f"color_css: {red_color_css}")
        
        # Obtener los valores RGB de color1
        r1, g1, b1 = get_rgb_value(color)
        print(r1, g1, b1)

        # Obtener los valores RGB de color2
        r2, g2, b2 = get_rgb_value(red_color_css)
        print(r2, g2, b2)
        
        if r1 == r2 and g1 == g2 and b1 == b2:
            raise Exception("Like Tweet! Fail because you already like this tweet!")
        
        # Esperar un máximo de 5 segundos a que aparezca un elemento
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div[3]/div/div/div"))
        )
        div_element.click()
        return "Like Twitter! Ok!"

    except TimeoutException:

        return "Like Twitter! Time Error!"

    except Exception as e:
        
        print(str(e))
        return "Like Tweet! Fail"

goPage(url)
checkCurrentPage()
print(loginUserTwitter(usuario))
loginPassTwitter(password)
goTweet(id_tweet)
print(likeTweet())

# def createAccount():
#     driver.get("https://twitter.com/")
#     driver.maximize_window()
        
#     # Esperar un máximo de 5 segundos a que aparezca un elemento
#     div_element = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "a.r-1sw30gj > div:nth-child(1)"))
#     )
#     div_element.click()
    
#     # Esperar un máximo de 5 segundos a que aparezca un elemento
#     div_element = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".r-kwpbio"))
#     )
    
#     # Esperar un máximo de 5 segundos a que aparezca un elemento
#     div_element = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div.css-18t94o4:nth-child(5) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"))
#     )

#     div_element.click()

# createAccount()

# print("Probando el me gusta")

# driver.find_element(
#     By.XPATH,
#     "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[7]/div/div[3]"
#     ).click()

# sleep(2)

# print("Probando el retweet")

# driver.find_element(
#     By.XPATH,
#     "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[7]/div/div[2]"
#     ).click()

# sleep(2)

# # Encontrar el elemento div por su selector CSS o cualquier otro método
# div_element = driver.find_element(
#     By.XPATH, 
#     '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]'
# )

# sleep(1)

# div_element = driver.find_element(
#     By.XPATH, 
#     '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div/div[2]'
# ).click()

# sleep(2)

# print("Probando el responder")

# driver.find_element(
#     By.XPATH,
#     "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[7]/div/div[1]"
#     ).click()

# sleep(2)

# # Encontrar el elemento div por su selector CSS o cualquier otro método
# div_element = driver.find_element(
#     By.XPATH, 
#     '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]'
# )

# sleep(2)

# div_element.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div").click()
# div_element.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div").clear()
# div_element.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div").send_keys(r"Hola me comes la polla")