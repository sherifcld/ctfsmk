# Challenge: Audio Steganography
**Category:** Forensics
**Difficulty:** Hard

## Description
Ada pesan rahasia yang tersembunyi di dalam file audio ini. Bisakah kamu mendengarnya? Atau mungkin kamu harus melihat lebih dalam...

## Flag
`CTF{lsb_4ud10_st3g0_1s_tr1cky}`

## Solution
Data disembunyikan menggunakan teknik Least Significant Bit (LSB) pada frame audio WAV. Gunakan script Python untuk mengekstrak bit terakhir dari setiap byte audio.
