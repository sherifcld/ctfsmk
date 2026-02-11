from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.after_request
def add_csp(response):
    # CSP that allows scripts from a trusted CDN (which might have vulnerable JSONP endpoints)
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://cdnjs.cloudflare.com;"
    return response

@app.route('/')
def index():
    name = request.args.get('name', 'Guest')
    # Vulnerable to XSS
    template = f"<h1>Hello, {name}!</h1><p>Welcome to our secure site.</p>"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
