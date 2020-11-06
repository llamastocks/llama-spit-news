from pymongo import MongoClient
import datetime

date=datetime.datetime.now()+datetime.timedelta(hours=0,minutes=-180)
print(date)
client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.llamastocks

db.news.remove({"Fecha":{"$lt":date}})
