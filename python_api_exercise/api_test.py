#!/usr/bin/python3


import site
site.addsitedir("/Users/a0j0b83/.pyenv/versions/3.7.12/lib/python3.7/site-packages")

from flask import Flask, request
app = Flask(__name__)

@app.route("/index")

def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
     app.run(debug = True)


