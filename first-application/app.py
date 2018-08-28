from flask import Flask

app = Flask(__name__)

@app.route('/')  #home page of the site

def home():
    return "fuck you, world"

app.run(port = 5000)
