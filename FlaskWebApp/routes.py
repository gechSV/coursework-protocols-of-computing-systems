from asyncio.windows_utils import BUFSIZE
from datetime import *
from lib2to3.pytree import convert
from turtle import speed
from xml.etree.ElementTree import tostring
import requests
import json
import datetime as dt

# библиотека для запроса курса валют у Центр банка РФ 
from pycbrf.toolbox import ExchangeRates, Banks



def getСurrency():
    """Выполняет запрос к сервису ЦБ и возвращает dict"""
    dt_now = dt.datetime.now()
    dt_yesterday = dt_now - dt.timedelta(days=1)
    
    # запрос актуального курса
    rates = ExchangeRates(dt_now.strftime('%Y-%m-%d'))
    # запрос старого курса
    rates_yesterday = ExchangeRates(dt_yesterday.strftime('%Y-%m-%d'))

    r = 2
    return {'USD':round(rates['USD'].value, r), 'EUR':round(rates['EUR'].value, r), 
            'CNY':round(rates['CNY'].value/10, r), 'GBP':round(rates['GBP'].value, r),
            'USD_Y':round(rates['USD'].value, r) - round(rates_yesterday['USD'].value, r),
            'EUR_Y':round(rates['EUR'].value, r) - round(rates_yesterday['EUR'].value, r), 
            'CNY_Y':round(rates['CNY'].value, r) - round(rates_yesterday['CNY'].value, r),
            'GBP_Y':round(rates['GBP'].value, r) - round(rates_yesterday['GBP'].value, r)} 

def getWeather():
    """Запрос погоды"""
    # указываем нужный нам город s_city
    s_city = "Chita,RU"
    # в city_id запишем id нужного нам города
    city_id = 2025339
    # ключ для сервиса https://home.openweathermap.org/
    appid = "f23c7a3c6b169e36a1495cc39156c2f8"

    # получаем id города, в нашем случае можно этого не делать, тк 
    # город фиксирован - Chita,RU и мы знаем его id - 2025339
    # try:
    #     res = requests.get("http://api.openweathermap.org/data/2.5/find",
    #             params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    #     data = res.json()
    #     cities = ["{} ({})".format(d['name'], d['sys']['country'])
    #             for d in data['list']]
    #     print("city:", cities)
    #     city_id = data['list'][0]['id']
    #     print('city_id=', city_id)
    # except Exception as e:
    #     print("Exception (find):", e)
    #     pass

    # Получаем текущую погоду
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        # давление
        print('pressure:', data['main']['pressure'])
        # влажность
        print('humidity:', data['main']['humidity'])
        # ветер
        print('wind:', data['wind']['speed'])
        # условия
        print("conditions:", data['weather'][0]['description'])
        # температура на данный момент
        print("temp:", data['main']['temp'])
        # минимальная
        print("temp_min:", data['main']['temp_min'])
        # максимальная
        print("temp_max:", data['main']['temp_max'])

        return {'pressure':data['main']['pressure'], 'humidity':data['main']['humidity'], 'wind':data['wind']['speed'],
        "conditions":data['weather'][0]['description'].capitalize(), "temp":round(data['main']['temp']), 
        "temp_min": data['main']['temp_min'], "temp_max":data['main']['temp_max'], 'name':data['name']} 

    except Exception as e:
        print("Exception (weather):", e)
        pass




# # LayerAPI 100 запросов в месяц, закончились)
# # Запрос курса доллара относительно рубля
# def getСurrencyUSD():
#     url = "https://api.apilayer.com/fixer/latest?symbols=RUB&base=USD"
#     payload = {}
#     # Код доступа к сервису https://apilayer.com/
#     headers= {
#         "apikey": "Z6lNP3E3PWCw6OiKRyKbqKitGRPgmk6M"
#     }           
#     response = requests.request("GET", url, headers=headers, data = payload)
#     status_code = response.status_code
#     retText = response.text
#     retJson =  json.loads(retText) 
#     return {'currency': retJson['rates']['RUB']}
    
# # Запрос курса евро относительно рубля
# def getСurrencyEUR():
#     url = "https://api.apilayer.com/fixer/latest?symbols=RUB,EUR&base=EUR"
#     payload = {}
#     # Код доступа к сервису https://apilayer.com/
#     headers= {
#         "apikey": "Z6lNP3E3PWCw6OiKRyKbqKitGRPgmk6M"
#     }           
#     response = requests.request("GET", url, headers=headers, data = payload)
#     status_code = response.status_code
#     retText = response.text
#     retJson =  json.loads(retText) 
#     return {'currency': retJson['rates']['RUB']}


def saveLog(log):
    dt_now = datetime.now()
    f = open('ServerLogs.txt', 'a')
    f.write('\n' + dt_now.strftime('%Y-%m-%d %H:%M:%S') + '\n   ' + log + '\n')
    f.close()
