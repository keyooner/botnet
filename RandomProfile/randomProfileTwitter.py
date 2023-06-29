import random
from faker import Faker
from unidecode import unidecode
import os

def random_month():
    month = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre'
    }
    
    return month[random.randint(1, 12)]

def random_year (): return random.randint(1960, 2002)

def random_day ():
    month = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
    
    return month[random.randint(1, 12)]

def randomUser(name, surname, day, month, year):
    username = name[:random.randint(1, len(name))] + surname[:random.randint(0, len(surname))] + day[:random.randint(1, len(day))] + month[:random.randint(1, len(month))] + year[:random.randint(1, len(year))]
    username_return = unidecode(username.replace(" ", "_").replace("ñ", "n"))
    if len(username_return) > 15:
        return ''.join(random.sample(username_return, k=min(15, len(username_return))))
    
    return username_return     

def randomImage():

    ruta = r"RandomProfile/Images"

    # Obtener la lista de archivos en la ruta
    archivos = os.listdir(ruta)

    # Filtrar solo los archivos de imagen (opcional)
    archivos_imagenes = [archivo for archivo in archivos if archivo.endswith((".png", ".jpg", ".jpeg"))]

    # Seleccionar una imagen aleatoria
    imagen_aleatoria = random.choice(archivos_imagenes)

    # Ruta completa de la imagen seleccionada
    return os.path.normpath(os.path.join(os.getcwd(), ruta, imagen_aleatoria))


print(randomImage())