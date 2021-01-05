from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime
import requests
import json

client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.llamatest

today=datetime.datetime.now().date()
last_week=datetime.timedelta(days=-7)
last_week=today+last_week

today=today.strftime("%Y-%m-%d")
last_week=last_week.strftime("%Y-%m-%d")


for doc in db.price_stock.find():
    url="https://dataondemand.bvl.com.pe/v1/stock-quote/share-values/"+doc["ticker"]+"?startDate="+last_week+"&endDate="+today
    contenido=requests.get(url, verify=False).text
    soup=BeautifulSoup(contenido,"html5lib")
    p=json.loads(soup.text)
    price=sorted(p["values"], key=lambda x:x[0])
    try:
        date_price=price[len(price)-1]
        print(date_price)
    except IndexError:
        print(price)