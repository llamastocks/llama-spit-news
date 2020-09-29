from pymongo import MongoClient

client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")
db=client.business

inicio=2016
total=[]
for doc in db.reviews.find(
    {"Razón_Social":"FERREYCORP S.A.A."
    ,"Año_de_Ejercicio_actual":{"$gte":inicio}
    ,"Periodicidad":"Anual"
    ,"Tipo_de_Información":"Consolidado"
    }):
    
    
    balance=tuple(doc["Balance_General_del_ejercicio_actual"].values())
    accounts=tuple(item[0] for item in balance)
    total.append(accounts)

print(len(set(total)))
    