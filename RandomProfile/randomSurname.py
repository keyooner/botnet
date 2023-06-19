from random import *
from faker import Faker

faker = Faker("es_ES")

# Function that generate the surname of the Profile Data
def generateSurname():
    return faker.last_name()