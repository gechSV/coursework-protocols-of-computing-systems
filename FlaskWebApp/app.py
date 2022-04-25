from flask import Flask, render_template
from models import *

app = Flask(__name__)

with db:
    db.create_tables([Category, NewsPost])


@app.route("/")
def index():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
