from requests import get
import RandomProfile.randomEmail as randomEmail
import RandomProfile.randomPass as randomPass
import RandomProfile.randomName as randomName
import RandomProfile.randomSurname as randomSurname
import RandomProfile.randomProfileTwitter as rpf
import const

# Function to generate a random Profile
def generateProfile():
    email = f"{randomEmail.generateEmail(8, 8)}@{const.DOMINIO}"
    password = capitalizeCharacters(randomPass.generatePass(8, 8, 2))
    gender, name = randomName.generateName()
    surname = randomSurname.generateSurname()
    day = str(rpf.random_day())
    month = str(rpf.random_month())
    year = str(rpf.random_year())
    user = rpf.randomUser(name, surname, day, month, year)

    print("==== PROFILE CREATED ====\n")
    print(  f"\nThe user has been created with the following parameters:\n"
            f"email: {email}\n"
            f"password: {password}\n"
            f"gender: {gender}\n"
            f"name: {name}\n"
            f"surname: {surname}\n"
            f"day: {day}\n"
            f"month: {month}\n"
            f"year: {year}\n"
            f"user: {user}\n"
            f"state: unlocked\n")
    print("==== END PROFILE CREATED ==== \n")

    return {"email": email,
            "password": password,
            "name": name,
            "surname": surname,
            "gender": gender,
            "day": day,
            "month": month,
            "year": year,
            "user": user,
            "state": "unlocked"}

# Function that obtain parameters from the const.py
def getCpanelParameters():
    return const.CPANEL_API_TOKEN, const.CPANEL_BASE_URL, const.CPANEL_USERNAME

def capitalizeCharacters(characters):
    if len(characters) > 0:
        return characters[0].capitalize() + characters[1:]
    else:
        return characters

def generateParameters():
    # Profile data
    data = generateProfile()
    email = data["email"]
    password = data["password"]
    
    # Basic data for the configuration of Mail
    domain = const.DOMINIO
    # Quota in megabytes
    quota = 10
    skip = 0
    welcome = 1
        
    # Parameters to send the mail
    return {
        "email": email,
        "password": password,
        "domain": domain,
        "quota": quota,
        "skip_update_db": skip,
        "send_welcome_email": welcome,
    }

def createMail(data):
    # sourcery skip: inline-variable, move-assign-in-block, use-fstring-for-concatenation
    # Import variables of CPANEL API
    CPANEL_API_TOKEN, CPANEL_BASE_URL, CPANEL_USERNAME = getCpanelParameters()

    # Basics Commands
    # add_pop -> create mail
    # delete_pop -> delete mail
    # passwd_pop -> change pass
    endpoint = "/execute/Email/add_pop"
    
    # Basic data for the configuration of Mail
    domain = const.DOMINIO
    # Quota in megabytes
    quota = 10
    skip = 0
    welcome = 1
    
    # Parameters to send the mail
    parameters = {
        "email": data["email"].split("@")[0],
        "password": data["password"],
        "domain": domain,
        "quota": quota,
        "skip_update_db": skip,
        "send_welcome_email": welcome,
    }

    # Encabezado para crear en cpanel el usuario
    encabezado = {
        "Authorization": f"cpanel {CPANEL_USERNAME}:{CPANEL_API_TOKEN}"
    }

    # Variable que contiene la url para generar usuarios
    url = CPANEL_BASE_URL + endpoint
    print(f"URL: {url}")
    resultado = get(url=url, headers=encabezado, params=parameters, verify=True)
    print(" ==== Código web ==== ")
    print(resultado.text)
    print(" ==== Fin código web ==== ")

    # Obtenemos el código 200 OK aunque la petición ha sido denegada. Comprobar ['errores']
    if resultado.status_code != 200:
        raise Exception("Error creando la petición de cuenta de correo!")

    # Extraemos datos de la respuesta
    respuesta = resultado.json()

    # Si es correcto debería ser "usuario+dominio"
    datos = respuesta.get("data")
    errores = respuesta.get("errores")
    advertencias = respuesta.get("warnings")
    mensajes = respuesta.get("messages")
    estado = respuesta.get("status")
    metadata = respuesta.get("metadata")

    # Imprimimos los codigo respuesta
    print(f"Código de estado de respuesta: {resultado.status_code}")

    # Si el estado es 0 -> Fail, si es 1 -> Éxito
    if estado == 0:
        print("¡Error! Revisa los errores")
    elif estado == 1:
        print("¡Éxito!")
    print(f"Estado: {estado}")

    # Datos está vacio si falla. Contiene usuario+dominio en éxito
    if datos:
        print(f"Datos: {datos}")

    # Traemos metadatos
    if metadata:
        print(f"Metadata: {metadata}")

    # Mensaje esta vacio si falla. Si tiene exito contiene un string vacio en una lista
    if mensajes:
        print(" ==== Mensajes ==== ")
        for mensaje in mensajes:
            print(f"Mensaje - {mensaje}")

    # Advertencias está vacío cuando tiene exito y fallo durante los test
    if advertencias:
        print(" ==== Advertencias ==== ")
        for advertencia in advertencias:
            print(f"Advertencia - {advertencia}")

    # Errores está vacío cuando tiene éxito, contiene mensajes cuando falla
    if errores:
        print(" ==== Errores ==== ")
        for error in errores:
            print(f"Error - {error}")

    return f"Se han creado la cuenta de correo {data['email']}"

def deleteMail(email_user_twitter):
    # sourcery skip: inline-variable, move-assign-in-block, use-fstring-for-concatenation
    # Import variables of CPANEL API
    CPANEL_API_TOKEN, CPANEL_BASE_URL, CPANEL_USERNAME = getCpanelParameters()

    # Basics Commands
    # add_pop -> create mail
    # delete_pop -> delete mail
    # passwd_pop -> change pass
    endpoint = "/execute/Email/delete_pop"
    
    # Basic data for the configuration of Mail
    domain = const.DOMINIO
    skip = 0
    
    # Parameters to send the mail
    parameters = {
        "email": email_user_twitter.split("@")[0],
        "domain": domain,
        "skip_update_db": skip,
    }

    # Encabezado para crear en cpanel el usuario
    encabezado = {
        "Authorization": f"cpanel {CPANEL_USERNAME}:{CPANEL_API_TOKEN}"
    }

    # Variable que contiene la url para generar usuarios
    url = CPANEL_BASE_URL + endpoint
    print(f"URL: {url}")
    resultado = get(url=url, headers=encabezado, params=parameters, verify=True)
    print(" ==== Código web ==== ")
    print(resultado.text)
    print(" ==== Fin código web ==== ")

    # Obtenemos el código 200 OK aunque la petición ha sido denegada. Comprobar ['errores']
    if resultado.status_code != 200:
        raise Exception("Error creando la petición de cuenta de correo!")

    # Extraemos datos de la respuesta
    respuesta = resultado.json()

    # Si es correcto debería ser "usuario+dominio"
    datos = respuesta.get("data")
    errores = respuesta.get("errores")
    advertencias = respuesta.get("warnings")
    mensajes = respuesta.get("messages")
    estado = respuesta.get("status")
    metadata = respuesta.get("metadata")

    # Imprimimos los codigo respuesta
    print(f"Código de estado de respuesta: {resultado.status_code}")

    # Si el estado es 0 -> Fail, si es 1 -> Éxito
    if estado == 0:
        print("¡Error! Revisa los errores")
    elif estado == 1:
        print("¡Éxito!")
    print(f"Estado: {estado}")

    # Datos está vacio si falla. Contiene usuario+dominio en éxito
    if datos:
        print(f"Datos: {datos}")

    # Traemos metadatos
    if metadata:
        print(f"Metadata: {metadata}")

    # Mensaje esta vacio si falla. Si tiene exito contiene un string vacio en una lista
    if mensajes:
        print(" ==== Mensajes ==== ")
        for mensaje in mensajes:
            print(f"Mensaje - {mensaje}")

    # Advertencias está vacío cuando tiene exito y fallo durante los test
    if advertencias:
        print(" ==== Advertencias ==== ")
        for advertencia in advertencias:
            print(f"Advertencia - {advertencia}")

    # Errores está vacío cuando tiene éxito, contiene mensajes cuando falla
    if errores:
        print(" ==== Errores ==== ")
        for error in errores:
            print(f"Error - {error}")

    return f"Se ha borrado la cuenta de correo {email_user_twitter}"