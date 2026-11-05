from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from getpass import getpass
import os

ph = PasswordHasher()


def setup_masterpassw():
    print("--------------------------------\n")
    print("   Create a Master Password!\n")
    print("--------------------------------\n")

    print("Note that your master password must have a minimum length of 12 characters.")
    while True:
        masterpassw = getpass("Create your master password: ")
        confirmation = "Confirm your master password: "

        if len(masterpassw) < 12:
            print(
                "Your master password must have a minimum length of 12 characters. Try again!"
            )
            continue

        if masterpassw != confirmation:
            print("The passwords don't match. Try again!")
            continue

        password_hash = ph.hash(masterpassw)

        with open("master_password.hash", "w") as file:
            file.write(password_hash)
