import os.path as path
import const
import re

def checkPrivateKey():
    print("\n\u23f3 Checking file of Private Key... \u231b\n")
    print("              ....CHECKING....              \n")
    if not path.exists("key.key"):
        print("\u274c Could't find your Private Key file required to store safe information. Please follow the next steps:\n" +
              "   * If you have created your own key pls rename to key.key\n" +
              "   * If you haven't create pls generate a Private Key as key.key following the Documentation")
        return False
    else:
        print("\u2705 Private Key file it's created")
    print("\n              ....CHECKED....                \n")
    return True

def checkFirebase():
    print("\n\u23f3 Checking file of Firebase... \u231b\n")
    print("              ....CHECKING....              \n")
    if not path.exists("firebase-sdk.json"):
        print("\u274c Could't find your firebase file to use Firebase Application. Please follow the next steps:\n" +
              "   * If you have imported your file pls rename to firebase-sdk.json\n" +
              "   * If you haven't imported pls go to your firebase application, download and import into the project")
    else:
        print("\u2705 Firebase file it's created!")

        with open("firebase-sdk.json", "r") as file_open:
            datos = file_open.read()
            file_compare = "type"
            if re.search(file_compare, datos):
                print("\u274c Your file firebase-sdk.json is not encrypted. Pls, encrypt it following the Documentation! ")
            else:
                print("\u2705 Firebase file it's encrypted!")
    print("\n              ....CHECKED....                \n")

def checkConst():
    print("\n\u23f3 Checking variables in file const.py... \u231b\n")
    print("              ....CHECKING....              ")
    if not path.exists("const.py"):
        print("\u274c Could't find your const file to use the API's that requires the projeclsct. Please follow the next steps:\n" +
              "   * If you have created your file pls rename to const.py\n" +
              "   * If you haven't created pls create a file named as const.py following the Documentation")
    else:
        # We are going to check that variables are created
        # We check Variables of CPANEL
        print("\n                   CPANEL                   \n")
        checkVariablesCPANEL()
        
        # We check Variables of Server
        print("                   SERVER                   \n")
        checkVariablesServer()
        
    print("\n              ....CHECKED....                \n")
        
    print(  "      All variables was checked.      \n"+ 
            "      If there is something wrong.      \n" +
            "      Read the documentation!      \n")

def checkVariablesCPANEL():
    # First CPANEL_API_TOKEN
    try: 
        cpanel_api_token = const.CPANEL_API_TOKEN
    except AttributeError: 
        cpanel_api_token = None

    if cpanel_api_token is not None:
        print("\u2705 CPANEL_API_TOKEN is created!")
    else:
        print("\u274c You should create variable CPANEL_API_TOKEN. Pls, read documentation!")

    # Second CPANEL_BASE_URL
    try: 
        cpanel_base_url = const.CPANEL_BASE_URL
    except AttributeError: 
        cpanel_base_url = None

    if cpanel_base_url is not None:
        print("\u2705 CPANEL_BASE_URL is created!")
    else:
        print("\u274c You should create variable CPANEL_BASE_URL. Pls, read documentation!")

    # Third CPANEL_USERNAME
    try:
        cpanel_username = const.CPANEL_USERNAME
    except AttributeError:
        cpanel_username = None
        
    if cpanel_username is not None:
        print("\u2705 CPANEL_USERNAME is created!\n")
    else:
        print("\u274c You should create variable CPANEL_USERNAME. Pls, read documentation!\n")

def checkVariablesServer():
    # First IMAP_SERVER
    try: 
        imap_server = const.IMAP_SERVER
    except AttributeError: 
        imap_server = None

    if imap_server is not None:
        print("\u2705 IMAP_SERVER is created!")
    else:
        print("\u274c You should create variable IMAP_SERVER. Pls, read documentation!")
        
    # Second DOMINIO
    try: 
        dominio = const.DOMINIO
    except AttributeError: 
        dominio = None

    if dominio is not None:
        print("\u2705 DOMINIO is created!")
    else:
        print("\u274c You should create variable DOMINIO. Pls, read documentation!")
        
def checkRequisites():
    checkPrivateKey()
    checkFirebase()
    checkConst()
    return "Funcion ejecutada"

checkRequisites()