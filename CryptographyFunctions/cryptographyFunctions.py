from cryptography.fernet import Fernet
# import os.path as path
import json

# We need to open the key to operate with it
def openKey():
    return open("key.key", "rb").read()

# Encode the message that you input (First, you need to .encode() the message)
def encodeMessage(message):
    key = openKey()
    f = Fernet(key)
    return f.encrypt(message.encode())

# Decode the message that you input
def decodeMessage(message):
    key = openKey()
    f = Fernet(key)
    return f.decrypt(message)

# Encode file
def encodeFile(file):
    key = openKey()
    f = Fernet(key)
    with open(file, "rb") as file_open:
        file_info = file_open.read()
    encrypted_data = f.encrypt(file_info)
    with open(file, "wb") as file_open:
        file_open.write(encrypted_data)

# Decode file
def decodeFile(file):
    key = openKey()
    f = Fernet(key)
    with open(file, "rb") as file_open:
        encrypted_data = file_open.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file, "wb") as file_open:
        file_open.write(decrypted_data)

# Decode files of type JSON
def decodeJSON():
    decodeFile("firebase-sdk.json")
    
    with open("firebase-sdk.json", "r") as of:
        file_json = json.load(of)
    
    encodeFile("firebase-sdk.json")
    
    return file_json
