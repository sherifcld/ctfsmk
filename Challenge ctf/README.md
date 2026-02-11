# CTF Challenge Set 2026

Koleksi challenge CTF yang mencakup Cryptography, Web Exploitation, dan Forensics.

## Struktur Direktori
- `cryptography/`: 5 challenge (Medium - Ultimate Hard)
- `web/`: 5 challenge (Medium - Hard)
- `forensics/`: 5 challenge (Medium - Hard)

## Challenge List

### Cryptography
1. **Padding Oracle** (Medium): Serangan Padding Oracle pada AES-CBC.
2. **RSA Broadcast** (Hard): Hastad's Broadcast Attack dengan e=3.
3. **ECDSA Nonce Reuse** (Hard): Pemulihan kunci privat melalui penggunaan kembali nonce (k).
4. **RSA Related Message** (Ultimate Hard): Franklin-Reiter Related Message Attack.
5. **Hidden Number Problem** (Ultimate Hard): Serangan Lattice (LLL) pada HNP.

### Web Exploitation
1. **Blind SQLi** (Medium): SQL Injection berbasis waktu/boolean.
2. **Insecure Deserialization** (Medium/Hard): RCE melalui Python Pickle.
3. **SSRF Internal** (Hard): Server-Side Request Forgery untuk mengakses layanan internal.
4. **XSS CSP Bypass** (Hard): Bypass Content Security Policy menggunakan trusted CDN.
5. **Prototype Pollution** (Hard): Eksploitasi Prototype Pollution di Node.js untuk RCE.

### Forensics
1. **Log Analysis** (Medium): Menganalisis log akses web untuk menemukan payload SQLi.
2. **Memory Analysis** (Hard): Menganalisis dump memori (simulasi output Volatility).
3. **PCAP Decryption** (Hard): Mendekripsi aliran TCP yang di-XOR dengan kunci.
4. **Audio Steganography** (Hard): Least Significant Bit (LSB) steganography pada file WAV.
5. **Log Forensics** (Hard): Analisis log multi-tahap (SSH, sudo, bash history).
