from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

FLAG = b"CTF{p4dd1ng_0r4cl3_1s_st1ll_r3l3v4nt_2026}"
KEY = os.urandom(16)

def encrypt():
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(FLAG, 16))
    return (iv + ct).hex()

def decrypt(data):
    try:
        data = bytes.fromhex(data)
        iv = data[:16]
        ct = data[16:]
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), 16)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    print("Welcome to the Padding Oracle challenge!")
    print(f"Encrypted Flag: {encrypt()}")
    while True:
        try:
            user_input = input("Submit ciphertext (hex): ")
            if decrypt(user_input):
                print("Valid padding!")
            else:
                print("Invalid padding!")
        except EOFError:
            break
