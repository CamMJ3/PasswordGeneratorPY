from passwords import pass_generator
from credentials import new_credential

def main():
    while True:
        print("\n- - - Password Generator - - -")
        print("1) Generate a new password.")
        print("2) Generate multiple passwords.")
        print("3) Exit.")

        option = int(input("\nChoose your option: "))

        if option == 1:
            one_password()
        elif option == 2:
            multiple_passwords()
        elif option == 3:
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Try again!")

def one_password():
    length = int(input("\nEnter the length of your desired password: "))

    if length < 4:
        print("The password must be at least 4 characters long. Try again!")
        return
    
    new_pass = pass_generator(length)
    print("Done! Your password is: ", new_pass)

def multiple_passwords():
    length = int(input("\nEnter the length of your desired passwords: "))

    if length < 4:
        print("The password must be at least 4 characters long. Try again!")
        return

    num_pass = int(input("Enter the number of required passwords: "))
    print()

    for i in range(num_pass):
        new_pass = pass_generator(length)
        print(f"{i + 1}. {new_pass}")

if __name__ == "__main__": 
    main()