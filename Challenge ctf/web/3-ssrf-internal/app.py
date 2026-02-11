from flask import Flask, request
import requests

app = Flask(__name__)

# Internal service (simulated)
@app.route('/internal/flag')
def internal_flag():
    if request.remote_addr != '127.0.0.1':
        return "Access Denied!", 403
    return "CTF{ssrf_t0_1nt3rn4l_h0st_f0und}"

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "Provide a URL via ?url="
    
    # Very basic blacklist bypass challenge
    if "localhost" in url or "127.0.0.1" in url:
        return "Forbidden host!", 403
    
    try:
        # User could use http://[::1]/internal/flag or other bypasses
        response = requests.get(url, timeout=5)
        return response.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
