import secrets
import string

def passGenerator(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    first_letter = secrets.choice(letters)

    password = [first_letter]

    password.append(secrets.choice(letters))
    password.append(secrets.choice(numbers))
    password.append(secrets.choice(symbols))

    passCharacters = letters + numbers + symbols

    for i in range (length - 3):
        password.append(secrets.choice(passCharacters))
    
    ignore_first = password[1:]
    secrets.SystemRandom().shuffle(ignore_first)
    complete_password = [first_letter] + ignore_first
    return "".join(complete_password)