# Challenge: XSS CSP Bypass
**Category:** Web Exploitation
**Difficulty:** Hard

## Description
Website kami memiliki filter XSS yang... yah, tidak ada. Tapi jangan khawatir, kami menggunakan Content Security Policy (CSP) yang sangat ketat!

## Flag
`CTF{xss_csp_bypass_via_cdn}`

## Solution
Meskipun CSP membatasi `script-src` ke `self` dan `cdnjs.cloudflare.com`, kamu bisa mencari endpoint JSONP yang rentan di CDN tersebut (seperti AngularJS atau library lain) untuk mengeksekusi JavaScript kustom.
