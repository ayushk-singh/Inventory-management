import hashlib
from main import code
import os


def authentication():
    def signup():
        username = input("Enter username address: ")
        pwd = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("credentials.txt", "w") as f:
                f.write(username + "\n")
                f.write(hash1)
            f.close()
            print("You have registered successfully!")
            print("Login to open admin panel")
            os.system('pause')

            
        else:
            print("Password is not same as above! \n")
            os.system('pause')

    def login():
            username = input("Enter username: ")
            pwd = input("Enter password: ")
            auth = pwd.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open("credentials.txt", "r") as f:
                stored_username, stored_pwd = f.read().split("\n")
            f.close()
            if username == stored_username and auth_hash == stored_pwd:
                print("Logged in Successfully!")
                code()
            else:
                print("Login failed! \n")
                os.system('pause')
        

    while 1:
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            signup()
        elif ch == 2:
            login()
        else:
            print("Wrong Choice!")
            os.system('pause')

