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
def symmetric_encrypt(message, key, verbose = False):
    """Encripts the message using symmetric AES algorythm.
        
    :param message: <str> Message for encryption;
    :param key: <object> symmetric key;
    :return: <object> Message encrypted with key
            
    """

    key_MD5 = transform_password(key)
    message_hash = SHA256.new(message.encode())
    message_with_hash = message.encode() + message_hash.hexdigest().encode() 
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key_MD5, AES.MODE_CFB, iv)
    encrypted_message = iv + cipher.encrypt(message_with_hash)
    if verbose:
        print(f'Message was encrypted into: {encrypted_message.hex()}')
    return encrypted_message
def symmetric_decrypt(encr_message, key, verbose = False):
    """Decripts the message using private_key and check it's hash
        
    :param encrypted_message: <object> Encrypted message
    :param key: <object> symmetric key;
    :return: <object> Message decripted with key
            
    """
    key_MD5 = transform_password(key)   
    
    bsize = AES.block_size 
    dsize = SHA256.digest_size*2
    
    iv = Random.new().read(bsize)
    cipher = AES.new(key_MD5, AES.MODE_CFB, iv)
    decrypted_message_with_hesh = cipher.decrypt(encr_message)[bsize:]
    decrypted_message = decrypted_message_with_hesh[:-dsize]
    digest = SHA256.new(decrypted_message).hexdigest()
    
    if digest==decrypted_message_with_hesh[-dsize:].decode():
        if verbose:
        	print(f"Success!\nEncrypted hash is {decrypted_message_with_hesh[-dsize:].decode()}\nDecrypted hash is {digest}")
        return decrypted_message.decode()
    else:
        print(f"Encryption was not correct: the hash of decripted message doesn't match with encrypted hash\nEncrypted hash is {decrypted_message_with_hesh[-dsize:]}\nDecrypted hash is {digest}")
