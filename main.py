from passwords import pass_generator
from credentials import new_credential

def main():
    while True:
        print("\n- - - Credential Manager - - -")
        print("1) Add a login credential.")
        print("2) Exit.")

        option = int(input("\nChoose your option: "))

        if option == 1:
            add_credential()
        elif option == 2:
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Try again!")

def add_credential():
    print("\n- - - New credential! - - -\n")
    website = input("\nWebsite: ")
    user = input("\nUser: ")
    option = input(("\nDo you wish to generate a password? (Y/N): ")).lower()

    if option == "y":
        length = int(input("\nEnter the length of your desired password: "))
        
        if length < 4:
            print("The password must be at least 4 characters long. Try again!")
            return
        
        password = pass_generator(length)

    else:
        password = input("Enter your password : ")

    new_credential(website, user, password)
    print("Done! Your credential has been created successfully.")

if __name__ == "__main__": 
    main() 