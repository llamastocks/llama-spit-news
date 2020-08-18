#Fase 1: extracción de lista de empresas listadas en BVL
def list_bvl():
    from bs4 import BeautifulSoup
    import requests

    url="https://www.smv.gob.pe/Frm_InformacionFinanciera?data=A70181B60967D74090DCD93C4920AA1D769614EC12"
    contenido=requests.get(url, verify=False).text

    soup=BeautifulSoup(contenido,"html5lib")

    p=soup.find("select",{"class":"form-control"})

    bvl=[]

    for option in p.find_all("option"):
        bvl.append(option.text)

    return bvl


#Con la función list_bvl se obtiene la lista
#de empresas con EEFF en SMV, la lista se llamará bvl