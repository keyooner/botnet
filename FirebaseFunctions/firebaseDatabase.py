# Import of the class with the authentication code
import FirebaseFunctions.firebaseAuthentication as fa
# Firebase library for Wrapper API Client
import firebase
import temp
import os
import base64
from cryptography.fernet import Fernet

firebase = fa.initializeApp()
db = firebase.database()
auth = firebase.auth()

def generate_key():
        if not os.path.exists("key.key"):
                key = Fernet.generate_key()
                with open("key.key", "wb") as file_key:
                        file_key.write(key)
                        
generate_key()

def encrypt_value(value):
        if not os.path.exists("key.key"):
                raise Exception("There is no key. Please generate one!.")
        
        with open("key.key", "rb") as file_key:
                key = file_key.read()
        
        fernet = Fernet(key)
        encrypted_value = fernet.encrypt(value.encode())
        return base64.b64encode(encrypted_value).decode()

def decrypt_value(encrypted_value):
        if not os.path.exists("key.key"):
                raise Exception("There is no key. Please generate one!.")
        
        with open("key.key", "rb") as file_key:
                key = file_key.read()
        
        fernet = Fernet(key)
        decrypted_value = fernet.decrypt(base64.b64decode(encrypted_value)).decode()
        return decrypted_value

def encrypt_existing_passwords(email, password):
        # Intentamos iniciar sesión. Si falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        # Obtenemos los valores actuales del usuario
        current_data = db.child("created_users").child(email_local).get(token).val()

        # Encriptamos las contraseñas existentes y actualizamos la estructura de datos
        encrypted_data = {}
        for key, value in current_data.items():
                encrypted_values = {}  
                for nested_key, nested_value in value.items():
                        if nested_key == "password":
                                encrypted_values[nested_key] = encrypt_value(str(nested_value))
                        else:
                                encrypted_values[nested_key] = nested_value
                encrypted_data[key] = encrypted_values

        # Guardamos los valores encriptados en la base de datos
        db.child("created_users").child(email_local).update(encrypted_data, token)

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
        
def getLastValueUser(email, password):
        try:
                # Iniciar sesión en Firebase con el email y contraseña proporcionados
                user = auth.sign_in_with_email_and_password(email=email, password=password)

                # Obtener el diccionario de usuarios creados desde la base de datos
                snapshot = db.child("created_users").child(user["localId"]).get(token=user['idToken']).val()

                # Obtener una lista de los IDs (quitando el prefijo 'ID-') y ordenarlos
                ids = [int(id_.replace('ID-', '')) for id_ in snapshot.keys()]
                sorted_ids = sorted(ids)

                if sorted_ids:
                        # Obtener el último ID y el nombre de usuario asociado a ese ID
                        last_id = 'ID-' + str(sorted_ids[-1])
                        return snapshot[last_id]['user']
                else:
                        # Si no hay IDs en la lista, devolver None o algún valor que indique que no hay usuarios creados aún.
                        return None
        except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante el proceso y devolver un valor predeterminado (por ejemplo, None).
                print(f"Error: {e}")
        return None

def getLastValueEmail(email, password):
        try:
                # Iniciar sesión en Firebase con el email y contraseña proporcionados
                user = auth.sign_in_with_email_and_password(email=email, password=password)

                # Obtener el diccionario de usuarios creados desde la base de datos
                snapshot = db.child("created_users").child(user["localId"]).get(token=user['idToken']).val()

                # Obtener una lista de los IDs (quitando el prefijo 'ID-') y ordenarlos
                ids = [int(id_.replace('ID-', '')) for id_ in snapshot.keys()]
                sorted_ids = sorted(ids)

                if sorted_ids:
                        # Obtener el último ID y el nombre de usuario asociado a ese ID
                        last_id = 'ID-' + str(sorted_ids[-1])
                        return snapshot[last_id]['email']
                else:
                        # Si no hay IDs en la lista, devolver None o algún valor que indique que no hay usuarios creados aún.
                        return None
        except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante el proceso y devolver un valor predeterminado (por ejemplo, None).
                print(f"Error: {e}")
        return None

def loadValues(email, password, data: dict):
        # Intentamos iniciar sesión. Si falla, lanzamos una excepción
        user = auth.sign_in_with_email_and_password(email=email, password=password)

        email_local = user['localId']
        token = user['idToken']

        id = getLastValue(email, password)

        encrypted_data = {
                f"ID-{id}": {
                **data,
                "password": encrypt_value(data["password"])  # Se encripta la contraseña
                }
        }

        # Guardamos los valores actualizados en la base de datos
        db.child("created_users").child(email_local).update(encrypted_data, token)

def loadValuesPreferences(email, password, data):
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        db.child("preferences_users").child(email_local).set(data, token)

def getValuesPreferences(email, password):
        # We try to sign in if this fails, throw exception
        user = auth.sign_in_with_email_and_password(email = email, password = password)

        email_local = user['localId']
        token =  user['idToken']

        return db.child("preferences_users").child(email_local).get(token).val()
        
        
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
        db.child("created_users").child(email_local).child(f"ID-{id}").remove(token)

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

                # Desciframos la contraseña si existe
                if "password" in value:
                        value["password"] = decrypt_value(value["password"])

                values[key] = value

        return values

def get_count_values(email, password):
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

                # Desciframos la contraseña si existe
                if "password" in value:
                        value["password"] = decrypt_value(value["password"])

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
        if data_dict is None:
                return 0
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        unlocked_values = {}
        for key, value in sorted_data.items():
                if value.get('state') == 'unlocked':
                        if 'password' in value:
                                value['password'] = decrypt_value(value['password'])
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
        if data_dict is None:
                return 0
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        locked_values = {}
        for key, value in sorted_data.items():
                if value.get('state') == 'locked':
                        if 'password' in value:
                                value['password'] = decrypt_value(value['password'])
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
        
        if data_dict is None:
                return 0

        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        unlocked_values = {}
        for key, value in sorted_data.items():
                if value.get('state') == 'unlocked':
                        if 'password' in value:
                                value['password'] = decrypt_value(value['password'])
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
        
        if data_dict is None:
                return 0
        
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        locked_values = {}
        for key, value in sorted_data.items():
                if value.get('state') == 'locked':
                        if 'password' in value:
                                value['password'] = decrypt_value(value['password'])
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
        if data_dict is None:
                return 0
        # Ordenar los elementos del diccionario por clave
        sorted_data = {k: data_dict[k] for k in sorted(data_dict, key=lambda x: int(x.split('-')[1]))}
        # Creamos un diccionario para almacenar los valores desbloqueados
        unlocked_values = {}
        count = 0
        for key, value in sorted_data.items():
                if count >= n_times:
                        break
                if value.get('state') == 'unlocked':
                        if 'password' in value:
                                value['password'] = decrypt_value(value['password'])
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
                emails_data2 = set([v['email'] for v in filtered_values_2.values()])
                filtered_data3 = {k: v for k, v in data2.items() if v['email'] not in emails_data2}
                emails_data3 = set([v['email'] for v in filtered_values_3.values()])
                filtered_data4 = {k: v for k, v in data2.items() if v['email'] not in emails_data3}
                
                # Comprobar los tres conjuntos de datos filtrados y retornar el valor mínimo
                if len(filtered_data2) > 0 and len(filtered_data3) > 0 and len(filtered_data4) > 0:
                        return min(len(filtered_data2), len(filtered_data3), len(filtered_data4))
                else:
                        return 0

# print(len(get_values_for_like("danifdezloz@gmail.com", "Dani5Fdez", "TFM_Botnet_-1674334209156997120", 2)))
# print(len(get_count_values_for_like("danifdezloz@gmail.com", "Dani5Fdez", "TFM_Botnet_-1674334209156997120")))
# print(upload_updated_values("danifdezloz@gmail.com", "Dani5Fdez", reorder_ids((get_values("danifdezloz@gmail.com", "Dani5Fdez")))))