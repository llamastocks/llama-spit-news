#Fase 1: extracción de lista de empresas listadas en BVL

from bs4 import BeautifulSoup
import requests

url="https://www.smv.gob.pe/Frm_InformacionFinanciera?data=A70181B60967D74090DCD93C4920AA1D769614EC12"
contenido=requests.get(url, verify=False).text

soup=BeautifulSoup(contenido,"html5lib")

p=soup.find("select",{"class":"form-control"})

bvl=[]

for option in p.find_all("option"):
    bvl.append(option.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url="https://www.smv.gob.pe/Frm_InformacionFinanciera?data=A70181B60967D74090DCD93C4920AA1D769614EC12"


driver=webdriver.Firefox()
driver.get(url)

t=driver.find_element_by_id("MainContent_cboTipo_1")
t.click()

#Elige la empresa

sbox=driver.find_element_by_class_name("BotonCombo")
sbox.send_keys(bvl[5])
sbox.submit()

wait=WebDriverWait(driver,100)

wait.until(EC.presence_of_element_located((By.ID,"MainContent_cbBuscar")))
wait.until(EC.visibility_of_element_located((By.ID,"MainContent_cbBuscar")))
wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))


submit=driver.find_element_by_id("MainContent_cbBuscar")

submit.click()

year=[]

wait.until(EC.presence_of_element_located((By.ID,"MainContent_grdInfoFinanciera")))

contenido=driver.page_source
soup=BeautifulSoup(contenido,"html5lib")
p=soup.find("table",{"class":"CentrarDiv"})

x=0
y=0    
for td in p.find_all("td"):
    if x==0:
        year.append(td.text.replace("\n","").strip())
        x=x+1
    elif (x==2 and td.text!="Estado Financieros"):
        year.pop()
        x=x+1
    elif x==3:
        x=x-3
    else:
        x=x+1

print(len(year))
print(len(info))