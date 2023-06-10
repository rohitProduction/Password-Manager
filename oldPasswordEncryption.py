import bcrypt
from cryptography.fernet import Fernet


def hashPassword(password):
    encoded = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(encoded, salt)
    return hash

def checkPassword(enteredPassword, hashedPassword):
    encoded = enteredPassword.encode('utf-8')
    result = bcrypt.checkpw(encoded, hashedPassword)
    return result

def generateKey():
    key = Fernet.generate_key()

def encryptPassword(password, key):
    f = Fernet(key)
    token = f.encrypt(password.encode('utf-8'))    
    return token     


def decryptPassword(cipherText, f):
    password = f.decrypt(cipherText)
    return password

