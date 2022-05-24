from unicodedata import category
from flask import Flask, render_template
from models import *
from routes import *
from json import *
import datetime as dt

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
    return render_template("main.html", cat = cat, currency = getСurrency(), dateTime = dt_now.strftime('%d.%m.%Y'), weather = getWeather())

    


if __name__ == "__main__":
    app.run(debug=True)
