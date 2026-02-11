# Challenge: Memory Analysis
**Category:** Forensics
**Difficulty:** Hard

## Description
Kami menemukan aktivitas mencurigakan pada workstation salah satu karyawan. Kami berhasil mengambil dump memorinya. Apa yang dilakukan malware tersebut?

## Flag
`CTF{memory_analysis_is_cool}`

## Solution
Analisis output Volatility di `evidence.txt`. Temukan koneksi jaringan yang mencurigakan dan string yang dikirim. Base64 decode string `Q1RGem1lbW9yeV9hbmFseXNpc19pcyVjb29s` (ingat untuk menyesuaikan format flag).
