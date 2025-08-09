import bcrypt

Master_pwd = input("Enter your Master password: ")

def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            for line in file.readlines():
                user,pwd=line.strip().split("|")
                print(f"User: {user} | Password: {pwd}")
    except FileNotFoundError:
        print("No passwords found. Please add a password first.")

def add_password():
    name = input("Enter the name for the password: ")
    pwd = input("Enter the password: ")
    hash_pwd=bcrypt.hashpw(pwd,bcrypt.gensalt())
    with open("passwords.txt", "a") as file:
        file.write(f"{name}|{hash_pwd}\n")


while True:
    mode = input(
        "Would like to add a new password or view existing passwords? (add/view) press (q) to quit : ").lower()
    if mode == "q":
        print("Exiting the program.")
        break
    elif mode == "view":
        view_passwords()
    elif mode == "add":
        add_password()
    else:
        print("Invalid option. Please try again.")
        continue
