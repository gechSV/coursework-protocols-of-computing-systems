from unicodedata import category
from flask import Flask, render_template
from models import *
from routes import *
from json import *

app = Flask(__name__)

# TODO: узнать возможно ли перенести большие функции в отдельный файл?
@app.route("/")
def index(): 
    cat = [] 
    # Получаем данные из таблицы Category для заполнения 
    # каталога категорий на главной странице 
    for index in Category.select():
        cat.append({'id':index.id, 'category':index.category, 'text':index.displayText})
        
    # Запрос курсов валют
    currencyUSD = getСurrencyUSD()
    currencyEUR = getСurrencyEUR()
    
    return render_template("main.html", user='Valery', cat = cat)


if __name__ == "__main__":
    app.run(debug=True)
