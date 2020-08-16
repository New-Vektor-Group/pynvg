from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random
def transform_password(password_str):
    """Transform the password string into 32 bit MD5 hash
        
    :param password_str: <str> password in plain text;
    :return: <str> Transformed password fixed length
            
    """
    h = MD5.new()
    h.update(password_str.encode())
    return h.hexdigest()
