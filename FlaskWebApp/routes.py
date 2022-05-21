from asyncio.windows_utils import BUFSIZE
import datetime
from datetime import *
import json
import requests
from json import *

# Запрос курса доллара относительно рубля
def getСurrencyUSD():
    url = "https://api.apilayer.com/fixer/latest?symbols=RUB,EUR&base=USD"
    payload = {}
    # Код доступа к сервису https://apilayer.com/
    headers= {
        "apikey": "Z6lNP3E3PWCw6OiKRyKbqKitGRPgmk6M"
    }           
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    retText = response.text
    retJson =  json.loads(retText) 
    return retJson

# Запрос курса евро относительно рубля
def getСurrencyEUR():
    url = "https://api.apilayer.com/fixer/latest?symbols=RUB,EUR&base=EUR"
    payload = {}
    # Код доступа к сервису https://apilayer.com/
    headers= {
        "apikey": "Z6lNP3E3PWCw6OiKRyKbqKitGRPgmk6M"
    }           
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    retText = response.text
    retJson =  json.loads(retText) 
    return retJson


def saveLog(log):
    dt_now = datetime.now()
    f = open('ServerLogs.txt', 'a')
    f.write('\n' + dt_now.strftime('%Y-%m-%d %H:%M:%S') + '\n   ' + log + '\n')
    f.close()
