import bcrypt
from cryptography.fernet import Fernet
import os, binascii
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# salt = b'$2a$12$qFr/jik3efyVT85YcjNSw.'
# hash = "$2a$12$qFr/jik3efyVT85YcjNSw.tjuyPEHQsaotIugqlzuKrIgHYBY/4l2"

# Derive key from password and hash the key
def hashPassword(password):
    encodedPassword = password.encode('utf-8')
    salt = bcrypt.gensalt().encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    #key = pbkdf2_hmac("sha256", encoded, salt, 50000, 64)
    key = base64.urlsafe_b64encode(kdf.derive(encodedPassword))
    hash = bcrypt.hashpw(key, salt)
    return hash, salt, key

# Derive key from entered password and check if that key matches the hashed key
def checkPassword(enteredPassword, hashedKey, salt):
    encodedPassword = enteredPassword.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(encodedPassword))
    return bcrypt.checkpw(key, hashedKey), key
    #newHash = bcrypt.hashpw(key, salt)
    #return newHash == hashedPassword

# Encrypt password with derived key
def encryptPassword(password, key):
    password = password.encode('utf-8')
    f = Fernet(key)
    encryptedPassword = f.encrypt(password).decode('utf-8')
    return encryptedPassword

# Decrypt password with derived key
def decryptPassword(cipherText, key):
    f = Fernet(key)
    password = f.decrypt(cipherText).decode('utf-8')
    return password

# def checkPassword(enteredPassword, hashedPassword):
#     salt = b'$2a$12$Wdj6gWr1tNqluUyD8IUGIu'
#     hash = "$2a$12$Wdj6gWr1tNqluUyD8IUGIujWt8DfBBxMYWvLBcig926TVADsWWdcC"
#     encoded = enteredPassword.encode('utf-8')
#     key = pbkdf2_hmac("sha256", encoded, salt, 50000, 64)
#     newHash = bcrypt.hashpw(key, salt)
#     print(key)
#     print(newHash == hash)
#     #result = bcrypt.checkpw(encoded, hashedPassword)
#     return newHash

# def generateKey():
#     key = Fernet.generate_key()
#     print(key)

# def encryptPassword(password):
#     password = b"password"
#     salt = os.urandom(16)
#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,
#         salt=salt,
#         iterations=390000,
#     )
#     print(kdf)
#     key = base64.urlsafe_b64encode(kdf.derive(password))
#     f = Fernet(key)
#     token = f.encrypt(password)    
#     return token
#     # key = Fernet.generate_key()
#     # # f = Fernet(key)
#     # key = b'\x98\x85k\x9d+\xfb\x03\xcd\x972W\xec\xbe\xd4\x11\x1b\xe1\x91\xdf\xbc\x1e\x08\x17\xdfR\x1d2\x13\xe5\xa4M\x01p\xc7,\x0b\xcd=\xcf\x14\x86P.H\xc3\x9e!\xb8\xf4Oq\x9fGSKeNKo\xff\xa6\xe5Y\x83'
#     # key = base64.urlsafe_b64encode(key.derive(password))
#     # f = Fernet(key)
#     # # the plaintext is converted to ciphertext
#     # token = f.encrypt(password.encode('utf-8'))    
#     # return token     


# def decryptPassword(cipherText, f):
#     password = f.decrypt(cipherText)
#     return password

