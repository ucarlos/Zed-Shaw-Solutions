
# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 07/20/2020 at 11:12 PM
#
# App.py
#
# -----------------------------------------------------------------------------

from flask import Flask
from flask import render_template
from flask import request
# What does this do?
app = Flask(__name__)


# @app.route("/hello")
@app.route("/hello", methods=["POST", "GET"])
def index():
    # Second Part
    # name = request.args.get('name', 'Nobody')

    # greeting = f"Hello, {name}" if name else "Hello World"

    # return render_template("index.html", greeting=greeting)

    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"

        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

# First Part
# @app.route('/')
# def hello_world():
#     greeting = "World"
#     return render_template("index.html", greeting=greeting)


if __name__ == "__main__":
    app.run()
