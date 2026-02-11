# Challenge: SSRF Internal
**Category:** Web Exploitation
**Difficulty:** Hard

## Description
Kami memiliki proxy internal untuk mengambil konten dari web lain. Kami sudah memblokir `localhost` dan `127.0.0.1` untuk keamanan maksimal.

## Flag
`CTF{ssrf_t0_1nt3rn4l_h0st_f0und}`

## Solution
Bypass filter hostname dengan menggunakan alternatif seperti IPv6 `[::1]`, representasi decimal IP, atau DNS rebinding untuk mengakses `/internal/flag`.
