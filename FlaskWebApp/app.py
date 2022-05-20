from unicodedata import category
from flask import Flask, render_template
from models import *
from routes import *
from json import *

app = Flask(__name__)

# with db:
#     db.create_tables([Category, NewsPost])
#     cat = Category(category='Sport', displayText='Ч по спорту?')
#     cat.save()


@app.route("/")
def index(): 
    # Получаем категории
    cat = []  
    for index in Category.select():
        cat.append({'id':index.id, 'category':index.category, 'text':index.displayText})
    return render_template("main.html", user='Valery', cat = cat)


if __name__ == "__main__":
    app.run(debug=True)

# cat = Category.get(Category.id == 1)
    # print (cat.displayText)