from flask import Flask

# python -m venv .venv
# py -3 -m venv .venv
# source -m venv .venv
# pip .venv/Script/Activate

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello Galaxy!</p>"

@app.route("/greet")
def greet():
    return "<p>Kumusta ka!</p>"

@app.route("/show-product")
def show_product():
    return "<p>Tooth Pick : 1k per piece</p>"

@app.route("/show-name")
def show_name():
    return "<p>Name : Rick Allen Alaro</p>"

@app.route("/show-address")
def show_address():
    return "<p>Address : ALIP Laguna</p>"