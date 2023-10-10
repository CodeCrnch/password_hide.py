from getpass import getpass

password = "CodeCrunch"

login = getpass("Enter password: ")

if login == password:
    print("You are logged in!")
else:
    print("Incorrect password!")