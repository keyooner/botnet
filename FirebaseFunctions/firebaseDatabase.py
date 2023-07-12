# Import of the class with the authentication code
import FirebaseFunctions.firebaseAuthentication as fa
# Firebase library for Wrapper API Client
import firebase
import temp
from collections import Counter

firebase = fa.initializeApp()
db = firebase.database()
auth = firebase.auth()

def getLastValue(email, password):  # sourcery skip: do-not-use-bare-except
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
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        id = getLastValue(email, password)

        db.child("created_users").child(email_local).child(f"ID-{id}").set(data, token)

def updateValues(email, password, email_find, update_state):
        # sourcery skip: avoid-builtin-shadow
        
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

def deleteValues(email, password):  # sourcery skip: avoid-builtin-shadow

        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        id = getLastValue(email, password)

        # Remove the last value
        db.child("created_users").child(email_local).child(f"ID-{id-1}").remove(token)


def loadValuesInUser(email, password, data: dict):

        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        db.child("created_users").child(email_local).set(data, token)

def get_values(email, password):
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

def get_count_values_unlocked(email, password): # sourcery skip: assign-if-exp, dict-comprehension, simplify-len-comparison

        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        data_dict = data.val()
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        unlocked_values = {}
        for key, value in sorted_data.items():
                if value.get('state') == 'unlocked':
                        unlocked_values[key] = value

        if len(unlocked_values) == 0:
                return 0
        else:
                return len(unlocked_values)
        
def get_count_values_locked(email, password):  # sourcery skip: assign-if-exp, dict-comprehension, simplify-len-comparison

        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        data_dict = data.val()
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        locked_values = {}
        for key, value in sorted_data.items():
                if value.get('state') == 'locked':
                        locked_values[key] = value

        if len(locked_values) == 0:
                return 0
        else:
                return len(locked_values)

def get_values_unlocked(email, password):  # sourcery skip: assign-if-exp, dict-comprehension, simplify-len-comparison

        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        data_dict = data.val()
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        unlocked_values = {}
        for key, value in sorted_data.items():
                if value.get('state') == 'unlocked':
                        unlocked_values[key] = value

        if len(unlocked_values) == 0:
                return 0
        else:
                return unlocked_values

def get_values_locked(email, password):  # sourcery skip: assign-if-exp, dict-comprehension, simplify-len-comparison
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        data_dict = data.val()
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        locked_values = {}
        for key, value in sorted_data.items():
                if value.get('state') == 'locked':
                        locked_values[key] = value

        if len(locked_values) == 0:
                return 0
        else:
                return locked_values

def get_values_for_actions(email, password, n_times: int):
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("created_users").child(email_local).get(token)
        # Convertir el objeto FirebaseResponse en un diccionario
        data_dict = data.val()
        
        # Ordenar los elementos del diccionario por clave
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        unlocked_values = {}
        count = 0
        for key, value in sorted_data.items():
                if count >= n_times:
                        break
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

        user = auth.sign_in_with_email_and_password(email=email, password=password)
        email_local = user['localId']
        token = user['idToken']
        db.child("created_users").remove(token)
        for id, value in data.items():
                db.child("created_users").child(email_local).child(id).set(value, token)
        return "Uploaded database"

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

def find_id_by_email(email, data):  # sourcery skip: use-next
        for id_, values in data.items():
                if values["email"] == email:
                        return id_
        return None

def loadValuesActionsTwitter(email, password, url, data: dict, user_twitter):
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        existing_data = db.child("action_users").child(email_local).child(url).child(user_twitter).get(token = user['idToken']).val()
        
        if existing_data:
                
                comment = existing_data.get("comment", False)
                like = existing_data.get("like", False)
                retweet = existing_data.get("retweet", False)
                
                if comment:
                        data["comment"] = comment
                if like:
                        data["like"] = like
                if retweet:
                        data["retweet"] = retweet
                        
        db.child("action_users").child(email_local).child(url).child(user_twitter).set(data, token)

def loadValuesFollow(email, password, url, data: dict, user_twitter):
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        # id = getLastValue(email, password)

        db.child("follow_users").child(email_local).child(url).child(user_twitter).set(data, token)

def get_values_for_follow(email, password, url, n_items):
        # # sourcery skip: collection-builtin-to-comprehension, comprehension-to-generator, inline-immediately-returned-variable

        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("follow_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('follow') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                
                return dict(list(filtered_data2.items())[:n_items])

def get_count_values_for_follow(email, password, url):
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("follow_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('follow') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                
                return len(filtered_data2)

def get_values_for_like(email, password, url, n_items):
        # sourcery skip: collection-builtin-to-comprehension, comprehension-to-generator, inline-immediately-returned-variable
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("action_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('like') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                
                return dict(list(filtered_data2.items())[:n_items])

def get_count_values_for_like(email, password, url):
        # # sourcery skip: collection-builtin-to-comprehension, comprehension-to-generator, inline-immediately-returned-variable
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("action_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('like') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                
                return len(filtered_data2)

def get_values_for_rt(email, password, url, n_items):
        # sourcery skip: collection-builtin-to-comprehension, comprehension-to-generator, inline-immediately-returned-variable
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("action_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('retweet') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                
                return dict(list(filtered_data2.items())[:n_items])

def get_count_values_for_rt(email, password, url):
        # # sourcery skip: collection-builtin-to-comprehension, comprehension-to-generator, inline-immediately-returned-variable
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("action_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('retweet') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                
                return len(filtered_data2)
        
def get_values_for_comment(email, password, url, n_items):
        # sourcery skip: collection-builtin-to-comprehension, comprehension-to-generator, inline-immediately-returned-variable
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("action_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('comment') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                
                return dict(list(filtered_data2.items())[:n_items])

def get_count_values_for_comment(email, password, url):
        # # sourcery skip: collection-builtin-to-comprehension, comprehension-to-generator, inline-immediately-returned-variable
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("action_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('comment') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                
                return len(filtered_data2)

def get_count_values_for_actions(email, password, url):
        # # sourcery skip: collection-builtin-to-comprehension, comprehension-to-generator, inline-immediately-returned-variable
        # Intentamos iniciar sesión. Si esto falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos todos los valores existentes para el usuario
        data = db.child("action_users").child(email_local).child(url).get(token)
        if data.val() is None:
                values ={}
        else:
        # Creamos un diccionario para almacenar los valores
                values = {}
                for item in data.each():
                        key = item.key()
                        value = item.val()
                        values[key] = value
                
        filtered_values = {key: value for key, value in values.items() if value.get('like') == True}
        filtered_values_2 = {key: value for key, value in values.items() if value.get('retweet') == True}
        filtered_values_3 = {key: value for key, value in values.items() if value.get('comment') == True}

        # Obtenemos los valores de los usuarios existentes en otra fuente
        data2 = get_values_unlocked(temp.get_email(), temp.get_password())
        
        if data2 is None:
                return 0
        else:
                emails_data1 = set([v['email'] for v in filtered_values.values()])
                filtered_data2 = {k: v for k, v in data2.items() if v['email'] not in emails_data1}
                emails_data2 = set([v['email'] for v in filtered_values.values()])
                filtered_data3 = {k: v for k, v in data2.items() if v['email'] not in emails_data2}
                emails_data3 = set([v['email'] for v in filtered_values.values()])
                filtered_data4 = {k: v for k, v in data2.items() if v['email'] not in emails_data3}
                
                # Comprobar los tres conjuntos de datos filtrados y retornar el valor mínimo
                if len(filtered_data2) > 0 and len(filtered_data3) > 0 and len(filtered_data4) > 0:
                        return min(len(filtered_data2), len(filtered_data3), len(filtered_data4))
                else:
                        return 0

# print(len(get_values_for_like("danifdezloz@gmail.com", "Dani5Fdez", "TFM_Botnet_-1674334209156997120", 2)))
# print(len(get_count_values_for_like("danifdezloz@gmail.com", "Dani5Fdez", "TFM_Botnet_-1674334209156997120")))
# print(upload_updated_values("danifdezloz@gmail.com", "Dani5Fdez", reorder_ids((get_values("danifdezloz@gmail.com", "Dani5Fdez")))))