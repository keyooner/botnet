from random import *
import string

# Function that generate random characteres
def generateCharacters(characters):
    # Min 8 leters
    intent = 1
    leters = []
    # Generate 8 random leters
    while intent <= characters:
        leters.append(choice(string.ascii_letters.lower()))
        intent += 1
    # Join the list of leters to generate a random word
    return "".join(leters)

# Function that generate random numbers
def generateNumbers(numbers):
    # Min 8 numbers
    intent = 1
    generated_numbers = []
    # Generate 8 random numbers
    while intent <= numbers:
        generated_numbers.append(str(randint(0, 9)))
        intent += 1
    # Join the list of numbers to generate a random large number
    return "".join(generated_numbers)

# Function that generate special characters
def generateSpecialCharacters(number_characters):
    # List with the special characters
    character_especial = ("@", "#", "_", "-", "$")
    # Min 1 special character
    intent = 1 # try
    # List of generated characters
    characters_specials_generated = []
    # We generate min 1 special character
    while intent <= number_characters:
        characters_specials_generated.append(choice(character_especial))
        intent += 1
    # Join the list of special characters to generate a random word
    return "".join(characters_specials_generated)

# Function that generate a random pass
def generatePass(characters, numbers, number_characters):
    # Min 8 characters
    if (characters < 8):
        return "¡Error! The password must contain at least 8 characters"
    # Min 8 numbers
    elif (numbers < 8):
        return "¡Error! The password must contain at least 8 numbers"
    # Min 1 special character
    elif (number_characters < 1):
        return "¡Error! The password must contain at least 1 special character"
    else:
        return generateCharacters(characters) + generateSpecialCharacters(number_characters) + generateNumbers(numbers)