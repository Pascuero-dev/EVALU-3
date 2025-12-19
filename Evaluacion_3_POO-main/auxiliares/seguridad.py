import hashlib
import os
import hmac

class Seguridad:
    @staticmethod
    def encriptar_pass(password):
        # Crea un salt aleatorio y genera el hash seguro (SHA256)
        salt = os.urandom(16)
        hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hash_obj

    @staticmethod
    def validar_pass(password, almacenado):
        # Separa el salt del hash guardado y verifica
        salt = almacenado[:16]
        hash_guardado = almacenado[16:]
        hash_nuevo = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return hmac.compare_digest(hash_guardado, hash_nuevo)