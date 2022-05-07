from flask import Flask, render_template
from models import *
from routes import *

app = Flask(__name__)

with db:
    db.create_tables([Category, NewsPost])
    cat = Category(category='Sport')
    cat.save()


@app.route("/")
def index():
    return render_template("main.html", user='Valery')


if __name__ == "__main__":
    app.run(debug=True)

