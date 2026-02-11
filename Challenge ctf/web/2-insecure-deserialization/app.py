from flask import Flask, request, make_response
import pickle
import base64

app = Flask(__name__)

@app.route('/')
def index():
    session = request.cookies.get('session')
    if not session:
        user_data = {'username': 'guest', 'admin': False}
        session = base64.b64encode(pickle.dumps(user_data)).decode()
        resp = make_response("Welcome guest! Set your session cookie to become admin.")
        resp.set_cookie('session', session)
        return resp
    
    try:
        user_data = pickle.loads(base64.b64decode(session))
        if user_data.get('admin'):
            return "Welcome admin! The flag is CTF{p1ckl3_d3s3r14l1z4t10n_rce}"
        return f"Welcome {user_data.get('username')}!"
    except Exception:
        return "Invalid session!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
