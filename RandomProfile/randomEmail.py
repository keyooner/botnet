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

# Function that generate a random email with the numbers and characters
def generateEmail(characters, numbers):
    # Min characters 8
    if (characters < 8):
        return "¡Error! The mail should contain min 8 characters."
    # Min numbers 8
    elif (numbers < 8):
        return "¡Error! The mail should contain min 8 numbers."
    # If everything ok. 
    else:
        return str(generateCharacters(characters) + generateNumbers(numbers))