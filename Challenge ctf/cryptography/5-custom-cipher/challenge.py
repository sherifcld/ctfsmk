import os
from Crypto.Util.number import getPrime, bytes_to_long

FLAG = b"CTF{l4tt1c3_b4s3d_hnp_1s_r34lly_h4rd_992}"
m = bytes_to_long(FLAG)

p = getPrime(512)
alpha = bytes_to_long(os.urandom(64)) % p # secret

# Hidden Number Problem: find alpha given t_i and a_i such that
# |(a_i * alpha) % p - t_i| < p / 2^k
# We'll use k=128 bits of information leaked for each sample
k = 128
samples = 40
results = []

for _ in range(samples):
    a = bytes_to_long(os.urandom(64)) % p
    res = (a * alpha) % p
    # Leak only the most significant bits
    t = (res >> k) << k
    results.append((a, t))

with open("output.txt", "w") as f:
    f.write(f"p = {p}\n")
    f.write(f"k = {k}\n")
    f.write(f"samples = {results}\n")
    
    # Flag encrypted with alpha
    from hashlib import sha256
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    key = sha256(str(alpha).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pad(FLAG, 16))
    f.write(f"\nencrypted_flag = {ct.hex()}\n")
