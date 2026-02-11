from Crypto.Util.number import getPrime, bytes_to_long

FLAG = b"CTF{fr4nkl1n_r31t3r_r3l4t3d_m3ss4g3_4tt4ck}"
m = bytes_to_long(FLAG)
e = 3

p = getPrime(1024)
q = getPrime(1024)
n = p * q

# f(x) = ax + b
a = 1
b = 1337
m1 = m
m2 = (a * m + b) % n

c1 = pow(m1, e, n)
c2 = pow(m2, e, n)

with open("output.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c1 = {c1}\n")
    f.write(f"c2 = {c2}\n")
    f.write(f"a = {a}\n")
    f.write(f"b = {b}\n")
