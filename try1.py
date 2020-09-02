from pymongo import MongoClient
import datetime
import smtplib
from email.mime.text import MIMEText

client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.llamastocks


total=[]
for doc in db.news.find().sort("Fecha",-1):
    if doc["Fecha"]>=datetime.datetime.now()+datetime.timedelta(hours=5,minutes=-180):
        del doc["_id"],doc["Article"]
        doc["Fecha"]=doc["Fecha"]+datetime.timedelta(hours=-5)
        
        total.append("\n".join(str(x) for x in doc.values()))

total="\n\n".join(total)

if not total:
    pass
else:
    

    s=smtplib.SMTP("smtp.zoho.com",587)
    msg=MIMEText(total)
    sender="llamastocks@zohomail.com"
    recipients="llamastocks@zohomail.com"
    msg["Subject"]="Noticias"
    msg["From"]=sender
    msg["To"]=recipients
    s.starttls()
    s.login("llamastocks@zohomail.com","mauricio96Silva")
    s.sendmail(sender,recipients,msg.as_string())
    
