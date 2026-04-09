from passwords import passGenerator

def main():
    print("\n- - - Password Generator - - -")
    length = int(input("\nEnter the length of your desired password: "))
    if length < 3:
        print("The password must be at least 3 characters long. Try again!")
        return
    newPassword = passGenerator(length)
    print("Done! Your password is: ", newPassword)

if __name__ == "__main__": 
    main()