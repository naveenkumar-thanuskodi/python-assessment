from flask import Flask

app = Flask(__name__)

@app.route("/book/home")
def hello_world():
    return "<p>Python Assessment - Book Store</p>"