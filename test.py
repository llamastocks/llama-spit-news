from bs4 import BeautifulSoup
import requests
inicio= input("Fecha Inicio:")
fin= input("Fecha Fin:")
option=input("Tipo de cambio: ¿compra/venta?:")
if option=="compra":
    url="https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04639PD/html/%s/%s/" %(inicio,fin)
else:
    url="https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04640PD/html/%s/%s/" %(inicio,fin)


contenido=requests.get(url, verify=False).text

soup=BeautifulSoup(contenido,"html5lib")

t=soup.find("div",{"class":"barra-resultados"})
data=t.tbody.find_all("tr")
data2=t.tbody.find_all("tr")


titulos=[]
tabla={}
for th in data[0].find_all("th"):
    titulos.append(th.text.replace("\t","").strip())

print(titulos)


datos=[]

tabla=[]

x=0
while x<(len(data2)-1):
    
    for td in data2[x+1].find_all("td"):
        datos.append(td.text.replace("\n","").strip())
    
    x=x+1

#datos es la tabla desordenada

fx_ask=[]

#mapa={"hola":1,"chau":2}
#print(mapa["hola"])
i=0
while i<(len(datos)):
    mapa={"date":datos[i],"fx":datos[i+1]}
    fx_ask.append(mapa)
    i=i+2

print (fx_ask)










