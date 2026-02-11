from Crypto.Util.number import getPrime, bytes_to_long

FLAG = b"CTF{br04dc4st_4tt4ck_1s_cl4ss1c_RSA}"
m = bytes_to_long(FLAG)
e = 3

def get_params():
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    c = pow(m, e, n)
    return n, c

results = []
for _ in range(3):
    results.append(get_params())

with open("output.txt", "w") as f:
    for n, c in results:
        f.write(f"n = {n}\n")
        f.write(f"c = {c}\n\n")
