from pymongo import MongoClient
import datetime

date_1=datetime.datetime.now()+datetime.timedelta(hours=0,minutes=-180)
date_2=datetime.datetime.now()
print(date_1)
print(date_2)
client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.llamastocks

db.news.remove({"Fecha":{"$lt":date_1,"$gt":date_2}})
