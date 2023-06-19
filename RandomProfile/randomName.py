from random import *
from faker import Faker

faker = Faker("es_ES")
# Function that generate the name
def generateName():
    # List with the gender
    list_gender = ("male", "female")
    # Random choice of gender
    gender = choice(list_gender)
    # Depends of the gender generate a random female or male name
    if gender == "female":
        name = faker.first_name_female()
    if gender == "male":
        name = faker.first_name_male()
    # Return the gender and the name generated
    return gender, name