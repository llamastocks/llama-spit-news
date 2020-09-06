from pymongo import MongoClient
import pymongo
import datetime

client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.llamastocks

cursor=db.news.aggregate([{"$group":{"_id":{"Titulo":"$Titulo","Fecha":"$Fecha"},"unique_ids":{"$addToSet":"$_id"},"count":{"$sum":1}}},{"$match":{"count":{"$gt":1}}}])

response=[]
for doc in cursor:
    del doc["unique_ids"][0]
    for id in doc["unique_ids"]:
        response.append(id)

db.news.remove({"_id":{"$in":response}})


