# Challenge: PCAP Decryption
**Category:** Forensics
**Difficulty:** Hard

## Description
Kami mencegat komunikasi antara client dan server. Sepertinya mereka menggunakan enkripsi kustom yang sangat sederhana.

## Flag
`CTF{pcap_x0r_d3crypt1on_fun}`

## Solution
Analisis `stream.txt`. Kuncinya adalah `supersecret`. XOR-kan data terenkripsi di Packet 4 dengan kunci tersebut untuk mendapatkan flag.
