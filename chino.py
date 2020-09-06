import newspaper
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from pymongo import MongoClient
import datetime
import smtplib
from email.mime.text import MIMEText

url="https://elcomercio.pe/tvmas/television/comicos-ambulantes-los-ambulantes-de-la-risa-el-sueldo-de-los-comicos-la-indisciplina-y-mas-secretos-del-polemico-programa-secretos-de-la-tv-tripita-cachay-panamericana-television-efrain-aguilar-noticia/"


article=Article(url,language="es")
article.download()
article.parse()
article.nlp()

articulo=[
article.title,
article.publish_date,
article.url,
article.text,

]
total=[]
total.append("\n\n".join(str(x) for x in articulo))

s=smtplib.SMTP("smtp.zoho.com",587)
msg=MIMEText(total)
sender="llamastocks@zohomail.com"
recipients="cwhcorreo@gmail.com"
msg["Subject"]=articulo[0]
msg["From"]=sender
msg["To"]=recipients
s.starttls()
s.login("llamastocks@zohomail.com","mauricio96Silva")
s.sendmail(sender,recipients,msg.as_string())