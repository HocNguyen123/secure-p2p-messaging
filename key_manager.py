from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key(password, salt, iterations=100_000):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    return kdf.derive(password.encode())

def rotate_key(password, base_salt, counter):
    dynamic_salt = base_salt + counter.to_bytes(2, 'big')
    return derive_key(password, dynamic_salt)
