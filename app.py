
from flask import Flask, render_template

from cats import cats
from dogs import dogs

app = Flask(__name__)
app.register_blueprint(cats)
app.register_blueprint(dogs)

@app.route("/")
def home():
    return render_template('index.html')

