import hashlib
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def hash_password(password):
    return hashlib.sha256(cipher_suite.encrypt(password.encode())).hexdigest()

