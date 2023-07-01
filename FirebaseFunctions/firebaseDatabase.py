# Import of the class with the authentication code
import FirebaseFunctions.firebaseAuthentication as fa
# Firebase library for Wrapper API Client
import firebase
from collections import Counter

def getLastValue(email, password):
        # We try to initialize app
        firebase = fa.initializeApp()

        db = firebase.database()

        # Get a reference to the auth service
        auth = firebase.auth()

        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)
        try:
                snapshot = db.child("created_users").child(user["localId"]).get(token = user['idToken']).val()
                ids = tuple(id_.replace('ID-', '') for id_ in snapshot.keys())
                sorted_ids = sorted(ids, key=lambda x: int(x))
                last_id = int(sorted_ids[-1])
                return last_id + 1
        except:
                return 1

def loadValues(email, password, data: dict):
        # We try to initialize app
        firebase = fa.initializeApp()

        db = firebase.database()

        # Get a reference to the auth service
        auth = firebase.auth()
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        id = getLastValue(email, password)

        db.child("created_users").child(email_local).child(f"ID-{id}").set(data, token)

def updateValues(email, password, email_find, update_state):
        
        firebase = fa.initializeApp()
        
        db = firebase.database()
        
        auth = firebase.auth()
        
        user = auth.sign_in_with_email_and_password(email = email, password = password)
        
        email_local = user['localId']
        token =  user['idToken']
        
        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        
        # Creamos un diccionario para almacenar los valores
        values = {}
        for item in data.each():
                key = item.key()
                value = item.val()
                values[key] = value
        
        id = find_id_by_email(email_find, values)
        
        db.child("created_users").child(email_local).child(id).update({"state": update_state}, token)
        
        return f"{id}: has been updated!"

def deleteValues(email, password):
        # We try to initialize app
        firebase = fa.initializeApp()

        db = firebase.database()

        # Get a reference to the auth service
        auth = firebase.auth()
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        id = getLastValue(email, password)

        # Remove the last value
        db.child("created_users").child(email_local).child(f"ID-{id-1}").remove(token)


def loadValuesInUser(email, password, data: dict):
        # We try to initialize app
        firebase = fa.initializeApp()

        db = firebase.database()

        # Get a reference to the auth service
        auth = firebase.auth()
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        db.child("created_users").child(email_local).set(data, token)

def get_values(email, password):
        # Intentamos inicializar la aplicación
        firebase = fa.initializeApp()

        db = firebase.database()

        # Obtenemos una referencia al servicio de autenticación
        auth = firebase.auth()
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        
        # Creamos un diccionario para almacenar los valores
        values = {}
        for item in data.each():
                key = item.key()
                value = item.val()
                values[key] = value
        
        return values

def get_values_unlocked(email, password):
        # Intentamos inicializar la aplicación
        firebase = fa.initializeApp()

        db = firebase.database()

        # Obtenemos una referencia al servicio de autenticación
        auth = firebase.auth()
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        
        # Creamos un diccionario para almacenar los valores desbloqueados
        unlocked_values = {}
        for item in data.each():
                key = item.key()
                value = item.val()
                if value.get('state') == 'unlocked':
                        unlocked_values[key] = value

        if len(unlocked_values) == 0:
                return 0
        else:
                return len(unlocked_values)

def get_values_for_actions(email, password, n_times: int):
        # Intentamos inicializar la aplicación
        firebase = fa.initializeApp()

        db = firebase.database()

        # Obtenemos una referencia al servicio de autenticación
        auth = firebase.auth()
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        
        # Creamos un diccionario para almacenar los valores desbloqueados
        unlocked_values = {}
        count = 0
        for index, item in enumerate(data.each()):
                print(index)
                if count >= n_times:
                        break
                
                key = item.key()
                value = item.val()
                if value.get('state') == 'unlocked':
                        email_twitter = value.get('email')
                        password_twitter = value.get('password')
                        user_twitter = value.get("user")
                        unlocked_values[key] = {'email': email_twitter, 'password': password_twitter, "user": user_twitter}
                        count = len(unlocked_values)
        return unlocked_values

def reorder_ids(data):
    sorted_ids = sorted(data.keys())  # Ordenamos las claves de forma ascendente
    new_data = {}

    for i, old_id in enumerate(sorted_ids, start=1):
        new_id = f"ID-{i}"
        new_data[new_id] = data[old_id]

    return new_data

def upload_updated_values(email, password, data):
    firebase = fa.initializeApp()
    db = firebase.database()
    auth = firebase.auth()

    user = auth.sign_in_with_email_and_password(email=email, password=password)
    email_local = user['localId']
    token = user['idToken']

    for id, value in data.items():
        db.child("created_users").child(email_local).child(id).set(value, token)

def remove_duplicates(data):
    unique_data = {}  # Diccionario para almacenar los valores únicos

    # Conjunto para realizar la comparación de valores únicos
    unique_set = set()

    for id, value in data.items():
        # Convierte el diccionario de valores en una tupla ordenada
        value_tuple = tuple(sorted(value.items()))

        # Si la tupla no está en el conjunto de valores únicos, se agrega al diccionario
        if value_tuple not in unique_set:
            unique_data[id] = value
            unique_set.add(value_tuple)

    return unique_data

def updateDatabase(email, password):
        
        # First get the values of the databse
        loadValuesInUser(email, password, (remove_duplicates(reorder_ids(get_values(email, password)))))
        
        return "Database updated!"

def find_id_by_email(email, data):
        for id_, values in data.items():
                if values["email"] == email:
                        return id_
        return None

# upload_updated_values("danifdezloz@gmail.com", "Dani5Fdez",reorder_ids(get_values("danifdezloz@gmail.com", "Dani5Fdez")))

def loadValuesActionsTwitter(email, password, url, data: dict, user_twitter):
        # We try to initialize app
        firebase = fa.initializeApp()

        db = firebase.database()

        # Get a reference to the auth service
        auth = firebase.auth()
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        id = getLastValue(email, password)

        db.child("action_users").child(email_local).child(url).child(user_twitter).set(data, token)

def loadValuesFollow(email, password, url, data: dict, user_twitter):
        # We try to initialize app
        firebase = fa.initializeApp()

        db = firebase.database()

        # Get a reference to the auth service
        auth = firebase.auth()
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        id = getLastValue(email, password)

        db.child("follow_users").child(email_local).child(url).child(user_twitter).set(data, token)