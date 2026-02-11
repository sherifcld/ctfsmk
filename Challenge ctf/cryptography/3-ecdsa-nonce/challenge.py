import os
from hashlib import sha256
from Crypto.Util.number import getPrime, bytes_to_long, inverse

# Simplified ECDSA-like challenge
# P-256 curve parameters (truncated for simplicity in this conceptual challenge)
q = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
g = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296 # x-coordinate of G

FLAG = b"CTF{n0nc3_r3us3_d3str0ys_ECDSA_123}"
d = bytes_to_long(os.urandom(32)) % q # private key

def sign(msg, k):
    h = bytes_to_long(sha256(msg).digest())
    r = pow(g, k, q) # simplified r
    s = (inverse(k, q) * (h + r * d)) % q
    return r, s

msg1 = b"I love cryptography"
msg2 = b"I hate reused nonces"
k = bytes_to_long(os.urandom(32)) % q

r1, s1 = sign(msg1, k)
r2, s2 = sign(msg2, k)

with open("output.txt", "w") as f:
    f.write(f"q = {q}\n")
    f.write(f"g = {g}\n")
    f.write(f"msg1 = {msg1.hex()}\n")
    f.write(f"r1 = {r1}\n")
    f.write(f"s1 = {s1}\n\n")
    f.write(f"msg2 = {msg2.hex()}\n")
    f.write(f"r2 = {r2}\n")
    f.write(f"s2 = {s2}\n")
    f.write(f"\n# Recover the private key d to decrypt the flag\n")
    # To keep it simple, we'll provide the flag encrypted with d
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    key = sha256(str(d).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pad(FLAG, 16))
    f.write(f"encrypted_flag = {ct.hex()}\n")
