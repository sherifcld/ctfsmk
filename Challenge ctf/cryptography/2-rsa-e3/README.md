# Challenge: RSA Broadcast
**Category:** Cryptography
**Difficulty:** Hard

## Description
Pesan yang sama dikirim ke 3 penerima berbeda dengan modulus yang berbeda tetapi exponent `e=3` yang sama.

## Flag
`CTF{br04dc4st_4tt4ck_1s_cl4ss1c_RSA}`

## Solution
Gunakan Chinese Remainder Theorem (CRT) untuk menggabungkan 3 ciphertext menjadi $m^3 \pmod{n_1 n_2 n_3}$, lalu ambil akar pangkat tiga.
