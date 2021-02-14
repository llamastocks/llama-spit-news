from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime as dt
import requests
import json
from datetime import datetime

client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.llamastocks

today=dt.datetime.now().date()
last_week=dt.timedelta(days=-7)
last_week=today+last_week

today=today.strftime("%Y-%m-%d")
last_week=last_week.strftime("%Y-%m-%d")


for doc in db.stocks.find():
    url="https://dataondemand.bvl.com.pe/v1/issuers/stock/"+doc["ticker"]+"?startDate="+last_week+"&endDate="+today
    contenido=requests.get(url, verify=False).text
    soup=BeautifulSoup(contenido,"html5lib")
    p=json.loads(soup.text)
    price=sorted(p, key=lambda x:x["date"])
    try:
        date_price=price[len(price)-1]
        if date_price["close"]!=0:
            cotizacion={"ticker":doc["ticker"],"date":datetime.strptime(date_price["date"],"%Y-%M-%d"),"last_price":date_price["close"]}     
        else:
            cotizacion={"ticker":doc["ticker"],"date":datetime.strptime(date_price["date"],"%Y-%M-%d"),"last_price":date_price["yesterdayClose"]}

        result=db.price.update({"ticker":cotizacion["ticker"],"date":cotizacion["date"]},cotizacion,upsert=True)
    except IndexError:
        pass