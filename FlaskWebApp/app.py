from hashlib import new
from random import random
from turtle import width
from unicodedata import category
from flask import Flask, render_template, url_for
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


if __name__ == "__main__":
    app.run(debug=True)
