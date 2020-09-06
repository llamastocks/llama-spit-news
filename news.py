import newspaper
import requests
import nltk
from bs4 import BeautifulSoup
from newspaper import Article
from pymongo import MongoClient

sections=[("economia","Economia"),("politica","Politica"),("mundo","Mundo")]
for section in sections:
    url="https://elcomercio.pe/"+section[0]
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
        article.nlp()
        key=", ".join(article.keywords)

        articulo={
        "Titulo":article.title,
        "Fecha":article.publish_date,
        "URL":article.url,
        "Article":article.text,
        "Keywords":"Palabras clave: "+key,
        "Section":section[1],
        "Source":"El Comercio"
        }
        
        client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
        db=client.llamastocks
        result=db.news.update({"Titulo":articulo["Titulo"],"Fecha":articulo["Fecha"]},articulo,upsert=True)
        
    print("Se han actualizado las noticias de sección "+section[1])    

