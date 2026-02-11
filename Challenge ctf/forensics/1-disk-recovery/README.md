# Challenge: Log Analysis
**Category:** Forensics
**Difficulty:** Medium

## Description
Server kami baru saja diserang. Seseorang mencoba mencuri database kami menggunakan teknik Blind SQL Injection. Bisakah kamu merekonstruksi password admin dari log yang ada?

## Flag
`CTF{bl1nd_sql1_l0g_4n4lys1s}`

## Solution
Analisis `access.log`, perhatikan waktu respon atau parameter yang dikirim. Cari pola di mana penyerang mencoba menebak karakter demi karakter menggunakan `ASCII(SUBSTR(...))`.
