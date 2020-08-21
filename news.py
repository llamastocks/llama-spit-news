import newspaper
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from pymongo import MongoClient


url="https://elcomercio.pe/economia"
contenido=requests.get(url, verify=False).text

soup=BeautifulSoup(contenido,"html.parser")
p=soup.find_all("div",{"class":"story-item__wrapper-item w-full"})
links=[]
for a in p:
    for b in a.find_all("a",{"class":"story-item__title block overflow-hidden primary-font line-h-xs mt-10"}):
        links.append(b.get("href"))

for link in links:
    url="https://elcomercio.pe"+link
    article=Article(url,language="es")
    article.download()
    article.parse()
    articulo={
    "Titulo":article.title,
    "Fecha":article.publish_date,
    "URL":article.url
    }

    client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
    db=client.elcomercio_economia
    result=db.noticias.update(articulo,articulo,upsert=True)
    
    
#hola die como estas
