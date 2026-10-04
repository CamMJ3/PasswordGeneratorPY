import secrets
import string

def pass_generator(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    first_letter = secrets.choice(letters)

    password = [first_letter,
                secrets.choice(secrets.choice(letters)),
                secrets.choice(secrets.choice(numbers)),
                secrets.choice(secrets.choice(symbols))]

    pass_characters = letters + numbers + symbols

    for _ in range (length - 4):
        password.append(secrets.choice(pass_characters))
    
    remaining = password[1:]
    secrets.SystemRandom().shuffle(remaining)

    return "".join([first_letter] + remaining)