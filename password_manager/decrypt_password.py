from cryptography.fernet import Fernet
  
message = input("Please enter the password here to decrypt: ")
res = bytes(message, 'utf-8')
key = input("Please enter the Key here to decrypt: ")
fernet = Fernet(bytes(key, 'utf-8'))
decMessage = fernet.decrypt(res).decode() 
print("decrypted string: ", decMessage)