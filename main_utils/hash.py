from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import base64

# uses https://www.pycryptodome.org version 3.9.9
PASS = "42534645565466546435T3453"
def base64Encoding(input):
  dataBase64 = base64.b64encode(input)
  dataBase64P = dataBase64.decode("UTF-8")
  return dataBase64P

def base64Decoding(input):
    return base64.decodebytes(input.encode("ascii"))

def generateSalt32Byte():
  return get_random_bytes(32)

def aesCbcPbkdf2EncryptToBase64(plaintext:str , password:str = PASS ):
  passwordBytes = password.encode("ascii")
  salt = generateSalt32Byte()
  PBKDF2_ITERATIONS = 15000
  encryptionKey = PBKDF2(passwordBytes, salt, 32, count=PBKDF2_ITERATIONS, hmac_hash_module=SHA256)
  cipher = AES.new(encryptionKey, AES.MODE_CBC)
  ciphertext = cipher.encrypt(pad(plaintext.encode("ascii"), AES.block_size))
  ivBase64 = base64Encoding(cipher.iv)
  saltBase64 = base64Encoding(salt)
  ciphertextBase64 = base64Encoding(ciphertext)
  return saltBase64 + ":" + ivBase64 + ":" + ciphertextBase64

def aesCbcPbkdf2DecryptFromBase64(ciphertextBase64:str, password:str = PASS): 
  passwordBytes = password.encode("ascii")
  data = ciphertextBase64.split(":")
  salt = base64Decoding(data[0])
  iv = base64Decoding(data[1])
  ciphertext = base64Decoding(data[2])
  PBKDF2_ITERATIONS = 15000
  decryptionKey = PBKDF2(passwordBytes, salt, 32, count=PBKDF2_ITERATIONS, hmac_hash_module=SHA256)
  cipher = AES.new(decryptionKey, AES.MODE_CBC, iv)
  decryptedtext = unpad(cipher.decrypt(ciphertext), AES.block_size)
  decryptedtextP = decryptedtext.decode("UTF-8")
  return decryptedtextP


def hash(data:str)->(str):
    """Data to hash

    Args:
        data (str): org data
    Returns:
        str: hash data
    """
    return aesCbcPbkdf2EncryptToBase64(plaintext=data)

def unhash(data:str)->(str):
    """Data hash to org data

    Args:
        data (str): hash data
    Returns:
        str: org data
    """
    return aesCbcPbkdf2DecryptFromBase64(ciphertextBase64=data)