import requests

# Configura las credenciales de Ghost VPN
username = 'ricardovaldesgaciia@gmail.com'
password = '2x4m??T7MAmH'

# URL de inicio de sesión de Ghost VPN
login_url = 'https://my.cyberghostvpn.com/es_ES/login'

# URL para conectar Ghost VPN
connect_url = 'https://ghostvpn.com/es_ES/connect'

# Crea una sesión de requests
session = requests.session()

# Realiza la solicitud de inicio de sesión
login_payload = {
    'username': username,
    'password': password
}
response = session.post(login_url, data=login_payload)

# Verifica si el inicio de sesión fue exitoso
if response.status_code == 200:
    print('Inicio de sesión exitoso')

    # Realiza la solicitud para conectar Ghost VPN
    connect_payload = {
        'action': 'connect',
        'server': 'servidor_de_destino'  # reemplaza con el servidor que desees
    }
    response = session.post(connect_url, data=connect_payload)

    # Verifica si la conexión fue exitosa
    if response.status_code == 200:
        print('Ghost VPN conectado')
    else:
        print('Error al conectar Ghost VPN:', response.text)
else:
    print('Error de inicio de sesión:', response.text)
