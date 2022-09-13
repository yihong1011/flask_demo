from flask import Flask
<<<<<<< HEAD
=======
from flask import render_template
>>>>>>> 9087ba6 (Initial commit)

app = Flask(__name__)

@app.route("/")
def hello_world():
<<<<<<< HEAD
    return "<p>Hello, World!</p>"
=======
    return render_template("test.html")
>>>>>>> 9087ba6 (Initial commit)
