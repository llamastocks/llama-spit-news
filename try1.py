from pymongo import MongoClient
import datetime
import smtplib
from email.mime.text import MIMEText

client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.llamastocks


total=["Noticias últimas 3 horas\n\n"]
for doc in db.news.find().sort("Fecha",-1):
    if (doc["Fecha"]>=datetime.datetime.now()+datetime.timedelta(hours=5,minutes=-180) and doc["Fecha"] is not None):
        del doc["_id"],doc["Article"]
        doc["Fecha"]=doc["Fecha"]+datetime.timedelta(hours=-5)
        temp=["<br><table><tr><th><a href="+doc["URL"]+">"+doc["Titulo"]+"</a></th></tr>","<tr><td>Fuente: "+doc["Section"]+" - "+doc["Source"]+"</td></tr>","<tr><td>"+str(doc["Fecha"])+"</td></tr></table></br>"]
        total.append("\n".join(str(x) for x in temp))

total="\n\n".join(total)

if not total:
    pass
else:
    

    s=smtplib.SMTP("smtp.zoho.com",587)
    msg=MIMEText(total,"html")
    sender="llamastocks@zohomail.com"
    recipients=["daniela.delcarpiosilva@gmail.com","alonsotakamure@hotmail.com","victorcastromonte2013@gmail.com"]
    msg["Subject"]="Noticias"
    msg["From"]=sender
    msg["To"]=sender
    s.starttls()
    s.login("llamastocks@zohomail.com","mauricio96Silva")
    s.sendmail(sender,[sender]+recipients,msg.as_string())
    
