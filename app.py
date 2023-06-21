import socket
import platform
from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def display_page():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    pythonversion = platform.python_version()
    return render_template("index.html", IP=ipaddress, HOST=hostname, PYTHONVERSION=pythonversion)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
