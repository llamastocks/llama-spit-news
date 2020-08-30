from pymongo import MongoClient
client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.elcomercio_economia
db.noticias.remove()
db=client.reuters
db.noticias.remove()