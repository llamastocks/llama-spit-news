import newspaper
import re
import requests
import imaplib
import email
from bs4 import BeautifulSoup
from newspaper import Article
from pymongo import MongoClient
import datetime
import smtplib
from email.mime.text import MIMEText

username="llamastocks@zohomail.com"
password="mauricio96Silva"

imap=imaplib.IMAP4_SSL("imap.zoho.com")

(retcode,capabilities)=imap.login(username,password)
imap.select("INBOX")

(retcode,messages)=imap.search(None,"(SUBJECT SPIT UNSEEN)")

links=[]
n=0
for num in messages[0].split():
    n=n+1
    typ,data=imap.fetch(num,"(RFC822)")
    for response_part in data:
        if isinstance(response_part,tuple):
            original=email.message_from_bytes(data[0][1])
            for part in original.walk():
                if part.get_content_type()=="text/plain":
                    body=part.get_payload(decode=True).decode("utf-8")
                    links.append(body)
            typ,data=imap.store(num,"+FLAGS","\\Seen")        

if links is not None:
    url=re.search("(?P<url>https?://[^\s]+)",links[0]).group("url")
            




    article=Article(url,language="es")
    article.download()
    article.parse()
    article.nlp()

    articulo=[
    article.title,
    article.url,
    article.text,

    ]
    total=[]
    total.append("\n\n".join(str(x) for x in articulo))
    total="\n\n".join(total)
    s=smtplib.SMTP("smtp.zoho.com",587)
    msg=MIMEText(total)
    sender="llamastocks@zohomail.com"
    recipients="cwhcorreo@gmail.com"
    msg["Subject"]="Respuesta"
    msg["From"]=sender
    msg["To"]=recipients
    s.starttls()
    s.login("llamastocks@zohomail.com","mauricio96Silva")
    s.sendmail(sender,recipients,msg.as_string())
else:
    pass