# Challenge: Insecure Deserialization
**Category:** Web Exploitation
**Difficulty:** Medium/Hard

## Description
Session manager kami menggunakan Python Pickle untuk menyimpan data user. Sangat efisien, bukan?

## Flag
`CTF{p1ckl3_d3s3r14l1z4t10n_rce}`

## Solution
Eksploitasi kerentanan `pickle.loads` dengan membuat payload kustom yang menjalankan perintah atau mengubah atribut `admin` menjadi `True`. Kamu bisa menggunakan class dengan method `__reduce__` untuk mendapatkan RCE.
