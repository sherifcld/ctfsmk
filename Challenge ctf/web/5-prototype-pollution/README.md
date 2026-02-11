# Challenge: Prototype Pollution
**Category:** Web Exploitation
**Difficulty:** Hard

## Description
Update profilmu di server Node.js kami yang super cepat!

## Flag
`CTF{pr0t0typ3_p0llut1on_2_rc3}`

## Solution
Gunakan payload JSON yang menargetkan `__proto__` untuk mempolusi objek global. Di Node.js, ini sering kali bisa dikombinasikan dengan library lain untuk mendapatkan Remote Code Execution (RCE).
