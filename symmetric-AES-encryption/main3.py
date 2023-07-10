from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'\xe9\x06\x9fh\rL\xf0Wb\x0eb\xac\x0c\xd95C\xfc:*}\xbe\x8c\xee\xd5\xae`\xc4O\xeb/\xf5T'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
    
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)
