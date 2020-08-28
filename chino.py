import newspaper
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from pymongo import MongoClient

url="https://elcomercio.pe/politica/congreso-el-fin-de-la-votacion-a-traves-de-portavoces-tras-el-pronunciamiento-del-tc-noticia/"


article=Article(url,language="es")
article.download()
article.parse()
article.nlp()
articulo={
"Titulo":article.title,
"Fecha":article.publish_date,
"URL":article.url,
"Article":article.text,
"Keywords":article.keywords
}
client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.elcomercio_economia
result=db.noticias.update(articulo,articulo,upsert=True)