from email.mime import image
from flask import *
from models import *
from routes import *
from json import *
import datetime as dt

from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

# TODO: узнать возможно ли перенести большие функции в отдельный файл?
@app.route("/")
def index(): 
    dt_now = dt.datetime.now()
    cat = [] 
    newsPost = []

    # Получаем данные из таблицы Category для заполнения 
    # каталога категорий на главной странице 
    for index in Category.select():
        cat.append({'id':index.id, 'category':index.category, 'text':index.displayText})

    # random.shuffle(sequence, [rand]) 
    for index in NewsPost.select():
        newsPost.append({'id':index.id, 'date':index.date, 'title':index.title, 'text':index.text, 'img':index.image})

    return render_template("main.html", cat = cat, currency = getСurrency(),
                            dateTime = dt_now.strftime('%d.%m.%Y'), weather = getWeather(), 
                            newsPost = newsPost, countNews = len(newsPost), 
                            markingUp = markingUp(len(newsPost)))

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    newsPost = []
    dt_now = dt.datetime.now()

    for index in NewsPost.select():
        newsPost.append({'id':index.id, 'categoryId': index.category_id, 
        'date':index.date, 'title':index.title, 'text':index.text, 'img':index.image})

    return render_template("admin.html", newsPost=newsPost, len = len(newsPost)+1, date = dt_now.strftime('%d.%m.%Y') )

@app.route("/addData", methods=['GET', 'POST'])
def addData():
    if request.method == 'POST':
        new = NewsPost.create(id = request.form['id'], category = request.form['idCat'], 
                              date = request.form['date'], title = request.form['title'], 
                              text = request.form['text'], image = request.form['img'])
        return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)
