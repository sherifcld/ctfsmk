from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (1, "admin", "CTF{bl1nd_sql1_1s_t3d10us_but_w0rth_1t}")')
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    c.execute(query)
    user = c.fetchone()
    conn.close()
    
    if user:
        return jsonify({"status": "success", "message": "Logged in!"})
    else:
        return jsonify({"status": "error", "message": "Login failed."})

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)
