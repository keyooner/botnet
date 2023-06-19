import EmailFunctions.createEmail as ce
import FirebaseFunctions.firebaseDatabase as fdb
import FirebaseFunctions.firebaseAuthentication as fa
import TwitterFunctions.seleniumFunctions as function
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException as exceptions
from webdriver_manager.chrome import ChromeDriverManager
import RandomProfile.randomProfileTwitter as rpf

# Crear opciones del navegador
#options = EdgeOptions()

# Configurar opciones adicionales si es necesario
# options.add_argument("--opcion_adicional")

# Crear instancia del controlador para Edge
#driver = Edge(options=options)

# Create an instance of driver for Firefox
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Crear instancia del controlador para Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

def introduceValuesFirebaseDB(email, password):
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
        
        function.createUserTwitter(driver, email_twitter, profile, password_twitter, month, day, year)
        
        fdb.loadValues(email, password, data)
        
        function.insertCode(driver, email_twitter, password_twitter)
        
        image = rpf.randomImage()
        
        # function.insertImageProfile(driver, image)
        
        function.step_create_user(driver)
        
        # function.skipNotifications(driver)
        
        # function.insertUsername(driver, user_twitter)
        
        # function.languageTwitter(driver)
        
        # fdb.loadValues(email, password, data)

        return(data)
    
    except exceptions as e:
        if "not connected to DevTools" in str(e):
            print("Deleting data created...")
            ce.deleteMail(email_twitter)
            fdb.deleteValues(email, password)
            return "Ups! Seem you close the page before finishing the process"
    
    except KeyboardInterrupt as e:
        print("Deleting data created...")
        ce.deleteMail(email_twitter)
        fdb.deleteValues(email, password)
        return "Ups! Seem you close the page before finishing the process"

