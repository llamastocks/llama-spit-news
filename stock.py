from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
import json

url="https://dataondemand.bvl.com.pe/v1/stock-quote/share"
contenido=requests.get(url, verify=False).text

soup=BeautifulSoup(contenido,"html5lib")

p=json.loads(soup.text)
firms=[]
for items in p:
    entry={"ticker":items["nemonico"],"emisor":items["companyName"]}
    firms.append(entry)


client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.llamastocks

for firm in firms:
    result=db.stocks.update({"ticker":firm["ticker"]},firm,upsert=True)


