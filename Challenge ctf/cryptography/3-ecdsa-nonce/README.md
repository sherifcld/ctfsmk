# Challenge: ECDSA Nonce Reuse
**Category:** Cryptography
**Difficulty:** Hard

## Description
Kenapa harus pakai angka random yang berbeda tiap saat? Seseorang menggunakan nonce `k` yang sama untuk dua tanda tangan berbeda.

## Flag
`CTF{n0nc3_r3us3_d3str0ys_ECDSA_123}`

## Solution
Dengan dua signature $(r, s_1)$ dan $(r, s_2)$ untuk pesan $h_1$ dan $h_2$, kamu bisa menghitung $k = (h_1 - h_2) / (s_1 - s_2) \pmod{q}$. Setelah mendapatkan $k$, kamu bisa menghitung private key $d$.
