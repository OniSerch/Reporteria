import hashlib
import os

def hash(password):
    salt = os.urandom(16)  # 16 bytes = 32 caracteres hex
    hashed = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex() + hashed  # salt + hash concatenado

def verificar(password, hashed_with_salt):
    salt_hex = hashed_with_salt[:32]  # primeros 16 bytes en hex
    hash_real = hashed_with_salt[32:]
    salt = bytes.fromhex(salt_hex)
    return hashlib.sha256(salt + password.encode()).hexdigest() == hash_real
