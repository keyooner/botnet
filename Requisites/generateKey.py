from cryptography.fernet import Fernet
import os.path as path

# Generate the key and save it
def generateKey():
    
    if not path.exists("key.key"):
        
        key = Fernet.generate_key()
        
        with open("key.key", "wb") as archive_key:
            archive_key.write(key)
            
        print("Key has been generated!")
        
    else:
        print("Key already exists!")
