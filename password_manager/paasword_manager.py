import os
from cryptography.fernet import Fernet

def encrptData(dataToEncrypt):
    message = dataToEncrypt
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage , key


def appendNew():
    file = open("PasswordVault.txt",'a')

    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")

    new_password,key=encrptData(password)
    
    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + str(new_password,'UTF-8') + "\n"
    web = "Website: " + website + "\n"
    key = "key: " + str(key,'UTF-8') + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write(key)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

def checkExistence():
    if os.path.exists("PasswordVault.txt"):
        appendNew()
    else:
        file = open("PasswordVault.txt", 'w')
        appendNew()


if __name__ == '__main__':
    checkExistence()        