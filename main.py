from passwords import pass_generator
from credentials import new_credential, get_credentials


def main():
    credentials = get_credentials()

    while True:
        print("\n- - - Credential Manager - - -")
        print("1) Add a login credential.")
        print("2) View current credentials.")
        print("3) Exit.")

        option = int(input("\nChoose your option: "))

        if option == 1:
            add_credential(credentials)
        elif option == 2:
            show_credentials(credentials)
        elif option == 3:
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Try again!")


def add_credential(credentials):
    print("\n- - - New credential! - - -\n")
    website = input("Website: ")
    user = input("User: ")
    option = input("\nDo you wish to generate a password? (Y/N): ").lower()

    if option == "y":
        length = int(input("Enter the length of your desired password: "))

        if length < 4:
            print("The password must be at least 4 characters long. Try again!")
            return

        password = pass_generator(length)

    elif option == "n":
        password = input("Enter your password : ")

    else:
        print(("Invalid option. Enter Y or N!"))
        return

    new_credential(credentials, website, user, password)
    print("Done! Your credential has been created successfully.")


def show_credentials(credentials):
    if not credentials:
        print("No credentials have been added yet!")
        return

    for i, val in enumerate(credentials, start=1):
        print("\nCredential", i)
        print("Website: ", val["website"])
        print("Username: ", val["username"])
        print("Password: ", "*" * len(val["password"]))


if __name__ == "__main__":
    main()
