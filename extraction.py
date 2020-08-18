#Fase 1: extracción de lista de empresas listadas en BVL
#Hay que descargar Beautiful Soup
from bs4 import BeautifulSoup
import requests

url="https://www.smv.gob.pe/Frm_InformacionFinanciera?data=A70181B60967D74090DCD93C4920AA1D769614EC12"
contenido=requests.get(url, verify=False).text

soup=BeautifulSoup(contenido,"html5lib")

p=soup.find("select",{"class":"form-control"})

bvl=[]

for option in p.find_all("option"):
    bvl.append(option.text)

firms=[98,99,100,113,127,131,140,159,168,194,200,108,212,220,222,223,224]


#Fase 1 Completa: Lista de empresas listadas en BVL extraída
#bvl=lista de empresas con informacion financiera en SMV
#Fase 2: Entrada a webpage y extracción de id
#Usar Selenium para interactuar con pagina de SMV
#Hay que descargar Selenium
for firm in firms:
    input_1=["i","c"]
    input_2=["t","a"]
    input_3=["1","2","3","4"]
    for a in input_1:
        type=a
        for b in input_2:
            period=b
            if period=="t":
                for c in input_3:

                    quarter=c
                    url="https://www.smv.gob.pe/Frm_InformacionFinanciera?data=A70181B60967D74090DCD93C4920AA1D769614EC12"

                    from selenium import webdriver
                    from selenium.webdriver.common.by import By
                    from selenium.webdriver.support.ui import WebDriverWait
                    from selenium.webdriver.support import expected_conditions as EC
                    from selenium.webdriver.support.ui import Select
                    from selenium.common.exceptions import StaleElementReferenceException


                    driver=webdriver.Firefox()
                    driver.get(url)
                    wait=WebDriverWait(driver,100)

                    def loop_is_text_present(text,max_attempts=3):
                        attempt=1
                        while True:
                            try:
                                return driver.find_element_by_id(text)
                            except StaleElementReferenceException:
                                if attempt==max_attempts:
                                    raise
                                attempt+=1
                    #Elige la empresa

                    sbox=driver.find_element_by_class_name("BotonCombo")
                    sbox.send_keys(bvl[firm])
                    sbox.submit()

                    #Se eligió a la empresa y la página se carga nuevamente


                    #Elige si desea datos individuales o consolidados
                    if type=="i":
                        pass
                    else:
                        try:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTipo_1")))
                            t=driver.find_element_by_id("MainContent_cboTipo_1")
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))            
                            driver.execute_script("arguments[0].click()",t)
                        except:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTipo_1")))
                            t=driver.find_element_by_id("MainContent_cboTipo_1")
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))            
                            driver.execute_script("arguments[0].click()",t)

                    wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboPeriodo_1")))
                    wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboPeriodo_1")))

                    #Elige si desea datos trimestrales o anuales
                    if period=="t":
                        wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                        if quarter=="1":
                            try:
                                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                                q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))            
                                q.select_by_value("1")
                            except:
                                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                                q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                                q.select_by_value("1")
                        elif quarter=="2":
                            try:
                                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                                q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))            
                                q.select_by_value("2")
                            except:
                                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                                q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                                q.select_by_value("2")             
                        elif quarter=="3":
                            try:
                                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                                q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                                q.select_by_value("3")
                            except:
                                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                                q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                                q.select_by_value("3")
                        elif quarter=="4":
                            try:
                                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                                q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                                q.select_by_value("4")
                            except:
                                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                                q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                                q.select_by_value("4")
                    else:
                        try:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboPeriodo_1")))
                            m=driver.find_element_by_id("MainContent_cboPeriodo_1")
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))
                            driver.execute_script("arguments[0].click()",m)
                            wait.until_not(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                        except:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboPeriodo_1")))
                            m=driver.find_element_by_id("MainContent_cboPeriodo_1")
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))
                            driver.execute_script("arguments[0].click()",m)
                            wait.until_not(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))


                    #La pagina se recarga con el nuevo nombre y en forma consolidada


                    wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                    wait.until(EC.presence_of_element_located((By.ID,"MainContent_cbBuscar")))
                    wait.until(EC.visibility_of_element_located((By.ID,"MainContent_cbBuscar")))


                    submit=driver.find_element_by_id("MainContent_cbBuscar")
                    wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))

                    submit.click()

                    #La pagina carga todos los estados financieros consolidados
                    #por empresa
                    #Fase 3:Extracción de id




                    wait.until(EC.presence_of_element_located((By.ID,"MainContent_grdInfoFinanciera")))

                    contenido=driver.page_source
                    soup=BeautifulSoup(contenido,"html5lib")
                    p=soup.find("table",{"class":"CentrarDiv"})

                    pages=[]

                    for td in p.find_all("tr",{"class":"grid_paginado"}):
                        pages.append(td.text.strip())

                    if not pages:
                        pass
                    else:
                        pages=len(pages[0])

                    #pages:indica el número de paginas que hay en la empresa,
                    #si hay mas de una pagina

                    info=[]
                    year=[]

                    #Acá empieza el loop

                    if not pages:
                        for link in p.find_all("a",{"title":"Ver detalle de Estados Financieros"}):
                            info.append(link.get("href"))

                        #Hasta acá se logró obtener los links por año, falta
                        #relacionar de que año se trata y no modificar el orden
                        x=0    
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
                    else:
                        y=1
                        while y<=pages:
                            
                            for link in p.find_all("a",{"title":"Ver detalle de Estados Financieros"}):
                                info.append(link.get("href"))

                            #Hasta acá se logró obtener los links por año, falta
                            #relacionar de que año se trata y no modificar el orden
                            x=0    
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
                            
                            if y==pages:
                                pass
                            else:
                                link=driver.find_element_by_link_text(f"{y+1}")
                                driver.execute_script("arguments[0].click()",link)
                                wait.until(EC.presence_of_element_located((By.LINK_TEXT,f"{y}")))
                                contenido=driver.page_source
                                soup=BeautifulSoup(contenido,"html5lib")
                                p=soup.find("table",{"class":"CentrarDiv"})

                            y=y+1



                    if len(info)==0:
                        print("No hay Referencia para extraer")
                        continue

                    #year:Lista de años 
                    #info:Lista de links correspondiente a los estados financieros
                    #según empresa, tipo de EEFF, Período y trimestre

                    #Entrar a estado financiero de primer año en lista 
                    #Parte 1: Extracción de link completado, se puede entrar directamente
                    #En esta parte se debe extraer los estados financieros deseados
                    #Fase 1: Ordenar lista

                    m=0
                    while m<=len(year)-1:

                        url=f"https://www.smv.gob.pe/{info[m]}"
                        driver.get(url)
                        wait.until(EC.presence_of_element_located((By.CLASS_NAME,"contenedor_centrado")))
                        contenido=driver.page_source


                        soup=BeautifulSoup(contenido,"html5lib")

                        eeff=soup.find_all("table",{"class":"contenedor_centrado"})




                        #eeff[1]:Balance General
                        #eeff[3]:Estado de Resultados
                        #eeff[5]:Patrimonio
                        #eeff[7]:Flujo Efectivo
                        #eeff[9]:Resultados INtegrales
                        #eeff[11]:Firmantes
                        from collections import OrderedDict
                        #Para nuestros propositos solo obtendremos el BBGG y EERR
                        #Se puede extraer los demás menos el Patrimonio
                        balances=[1,3]
                        p={}

                        for balance in balances:
                            headers=[]
                            for th in eeff[balance].find_all("th"):
                                headers.append(th.text.replace("\n","").strip())
                        
                        
                            x=0
                            cuentas=[]
                            año_actual=[]
                            ejercicio_pasado=[]
                        #solo usaremos para balance general y estado de resultados
                            for td in eeff[balance].find_all("td"):
                                if x==0:
                                    cuentas.append(td.text.replace("\n","").strip())
                                    x=x+1
                                elif x==len(headers)-2:
                                    año_actual.append(td.text.replace("\n","").strip())
                                    x=x+1
                                elif x==len(headers)-1:
                                    ejercicio_pasado.append(td.text.replace("\n","").strip())
                                    x=x-len(headers)+1
                                else:
                                    x=x+1
                            
                            if len(cuentas)<=1:
                                print("Estado financiero "+a+" "+b+" "+c+" "+str(balance)+" está vacío en año "+year[m])
                                continue
                            
                            año_actual=["0" if x=="" else x for x in año_actual]
                            ejercicio_pasado=["0" if x=="" else x for x in ejercicio_pasado]
                            año_actual=[round(float(t.replace(" ","").replace(",","").replace("(","-").replace(")","")),3) for t in año_actual]
                            ejercicio_pasado=[round(float(t.replace(",","").replace("(","-").replace(")","")),3) for t in ejercicio_pasado]
                            cuentas=[t.replace(" ","_") for t in cuentas]
                            
                            d={}
                            e={}
                            x=0
                            while x<=len(cuentas)-1:
                                d[f"{x}"]=(cuentas[x],año_actual[x])
                                e[f"{x}"]=(cuentas[x],ejercicio_pasado[x])
                                x=x+1


                            p["año_actual_"+str(balance)]=d
                            p["ejercicio_pasado_"+str(balance)]=e
                        
                        if len(cuentas)<=1:
                            print("Estado financiero "+a+" "+b+" "+c+" "+str(balance)+" está vacío en año "+year[m])
                            m=m+1
                            continue

                        #Se creo un diccionario para el ejercicio actual y ejercicio pasado
                        #de balance general y estado de resultados

                        if type=="i":
                            tipo="Individual"
                        else:
                            tipo="Consolidado"

                        if period=="t":
                            periodicidad="Trimestral"
                        else:
                            periodicidad="Anual"

                        InfoGeneral={"Razón_Social":bvl[firm],
                                "Año_de_Ejercicio_actual":int(year[m]),
                                "Año_de_Ejercicio_pasado":int(year[m])-1,
                                "Tipo_de_Información":tipo,
                                "Periodicidad":periodicidad,
                                "Trimestre":quarter,
                                "Balance_General_del_ejercicio_actual":p["año_actual_1"],
                                "Balance_General_del_ejercicio_pasado":p["ejercicio_pasado_1"],
                                "Estado_de_Resultado_del_ejercicio_actual":p["año_actual_3"],
                                "Estado_de_Resultado_del_ejercicio_pasado":p["ejercicio_pasado_3"]
                        }


                        from pymongo import MongoClient
                        client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")

                        db=client.business

                        result=db.reviews.insert_one(InfoGeneral)
                        m=m+1

                    driver.quit()

            else:
                quarter=""

                url="https://www.smv.gob.pe/Frm_InformacionFinanciera?data=A70181B60967D74090DCD93C4920AA1D769614EC12"

                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC
                from selenium.webdriver.support.ui import Select
                from selenium.common.exceptions import StaleElementReferenceException


                driver=webdriver.Firefox()
                driver.get(url)
                wait=WebDriverWait(driver,100)

                def loop_is_text_present(text,max_attempts=3):
                    attempt=1
                    while True:
                        try:
                            return driver.find_element_by_id(text)
                        except StaleElementReferenceException:
                            if attempt==max_attempts:
                                raise
                            attempt+=1
                #Elige la empresa

                sbox=driver.find_element_by_class_name("BotonCombo")
                sbox.send_keys(bvl[firm])
                sbox.submit()

                #Se eligió a la empresa y la página se carga nuevamente


                #Elige si desea datos individuales o consolidados
                if type=="i":
                    pass
                else:
                    try:
                        wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                        wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTipo_1")))
                        t=driver.find_element_by_id("MainContent_cboTipo_1")
                        wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))            
                        driver.execute_script("arguments[0].click()",t)
                    except:
                        wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                        wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTipo_1")))
                        t=driver.find_element_by_id("MainContent_cboTipo_1")
                        wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))            
                        driver.execute_script("arguments[0].click()",t)

                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboPeriodo_1")))
                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboPeriodo_1")))

                #Elige si desea datos trimestrales o anuales
                if period=="t":
                    wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                    if quarter=="1":
                        try:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                            q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))            
                            q.select_by_value("1")
                        except:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                            q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                            q.select_by_value("1")
                    elif quarter=="2":
                        try:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                            q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))            
                            q.select_by_value("2")
                        except:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                            q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                            q.select_by_value("2")             
                    elif quarter=="3":
                        try:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                            q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                            q.select_by_value("3")
                        except:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                            q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                            q.select_by_value("3")
                    elif quarter=="4":
                        try:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                            q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                            q.select_by_value("4")
                        except:
                            wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                            wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboTrimestre")))
                            q=Select(loop_is_text_present("MainContent_cboTrimestre",3))
                            wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                            q.select_by_value("4")
                else:
                    try:
                        wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                        wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboPeriodo_1")))
                        m=driver.find_element_by_id("MainContent_cboPeriodo_1")
                        wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))
                        driver.execute_script("arguments[0].click()",m)
                        wait.until_not(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))
                    except:
                        wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                        wait.until(EC.presence_of_element_located((By.ID,"MainContent_cboPeriodo_1")))
                        m=driver.find_element_by_id("MainContent_cboPeriodo_1")
                        wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))
                        driver.execute_script("arguments[0].click()",m)
                        wait.until_not(EC.element_to_be_clickable((By.ID,"MainContent_cboTrimestre")))


                #La pagina se recarga con el nuevo nombre y en forma consolidada


                wait.until(EC.invisibility_of_element_located((By.ID,"myLoading")))
                wait.until(EC.presence_of_element_located((By.ID,"MainContent_cbBuscar")))
                wait.until(EC.visibility_of_element_located((By.ID,"MainContent_cbBuscar")))


                submit=driver.find_element_by_id("MainContent_cbBuscar")
                wait.until(EC.element_to_be_clickable((By.ID,"MainContent_cbBuscar")))

                submit.click()

                #La pagina carga todos los estados financieros consolidados
                #por empresa
                #Fase 3:Extracción de id




                wait.until(EC.presence_of_element_located((By.ID,"MainContent_grdInfoFinanciera")))

                contenido=driver.page_source
                soup=BeautifulSoup(contenido,"html5lib")
                p=soup.find("table",{"class":"CentrarDiv"})

                pages=[]

                for td in p.find_all("tr",{"class":"grid_paginado"}):
                    pages.append(td.text.strip())

                if not pages:
                    pass
                else:
                    pages=len(pages[0])

                #pages:indica el número de paginas que hay en la empresa,
                #si hay mas de una pagina

                info=[]
                year=[]

                #Acá empieza el loop

                if not pages:
                    for link in p.find_all("a",{"title":"Ver detalle de Estados Financieros"}):
                        info.append(link.get("href"))

                    #Hasta acá se logró obtener los links por año, falta
                    #relacionar de que año se trata y no modificar el orden
                    x=0    
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
                else:
                    y=1
                    while y<=pages:
                        
                        for link in p.find_all("a",{"title":"Ver detalle de Estados Financieros"}):
                            info.append(link.get("href"))

                        #Hasta acá se logró obtener los links por año, falta
                        #relacionar de que año se trata y no modificar el orden
                        x=0    
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
                        
                        if y==pages:
                            pass
                        else:
                            link=driver.find_element_by_link_text(f"{y+1}")
                            driver.execute_script("arguments[0].click()",link)
                            wait.until(EC.presence_of_element_located((By.LINK_TEXT,f"{y}")))
                            contenido=driver.page_source
                            soup=BeautifulSoup(contenido,"html5lib")
                            p=soup.find("table",{"class":"CentrarDiv"})

                        y=y+1



                if len(info)==0:
                    print("No hay Referencia para extraer")
                    continue

                #year:Lista de años 
                #info:Lista de links correspondiente a los estados financieros
                #según empresa, tipo de EEFF, Período y trimestre

                #Entrar a estado financiero de primer año en lista 
                #Parte 1: Extracción de link completado, se puede entrar directamente
                #En esta parte se debe extraer los estados financieros deseados
                #Fase 1: Ordenar lista

                m=0
                while m<=len(year)-1:

                    url=f"https://www.smv.gob.pe/{info[m]}"
                    driver.get(url)
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"contenedor_centrado")))
                    contenido=driver.page_source


                    soup=BeautifulSoup(contenido,"html5lib")

                    eeff=soup.find_all("table",{"class":"contenedor_centrado"})




                    #eeff[1]:Balance General
                    #eeff[3]:Estado de Resultados
                    #eeff[5]:Patrimonio
                    #eeff[7]:Flujo Efectivo
                    #eeff[9]:Resultados INtegrales
                    #eeff[11]:Firmantes
                    from collections import OrderedDict
                    #Para nuestros propositos solo obtendremos el BBGG y EERR
                    #Se puede extraer los demás menos el Patrimonio
                    balances=[1,3]
                    p={}

                    for balance in balances:
                        headers=[]
                        for th in eeff[balance].find_all("th"):
                            headers.append(th.text.replace("\n","").strip())
                    
                    
                        x=0
                        cuentas=[]
                        año_actual=[]
                        ejercicio_pasado=[]
                    #solo usaremos para balance general y estado de resultados
                        for td in eeff[balance].find_all("td"):
                            if x==0:
                                cuentas.append(td.text.replace("\n","").strip())
                                x=x+1
                            elif x==len(headers)-2:
                                año_actual.append(td.text.replace("\n","").strip())
                                x=x+1
                            elif x==len(headers)-1:
                                ejercicio_pasado.append(td.text.replace("\n","").strip())
                                x=x-len(headers)+1
                            else:
                                x=x+1

                        


                        año_actual=["0" if x=="" else x for x in año_actual]
                        ejercicio_pasado=["0" if x=="" else x for x in ejercicio_pasado]
                        if len(cuentas)<=1:
                            print("Estado financiero "+a+" "+b+" "+c+" "+str(balance)+" está vacío en año "+year[m])
                            continue
                        año_actual=[round(float(t.replace(",","").replace("(","-").replace(")","")),3) for t in año_actual]
                        ejercicio_pasado=[round(float(t.replace(",","").replace("(","-").replace(")","")),3) for t in ejercicio_pasado]
                        cuentas=[t.replace(" ","_") for t in cuentas]
                    
                        d={}
                        e={}
                        x=0
                        while x<=len(cuentas)-1:
                            d[f"{x}"]=(cuentas[x],año_actual[x])
                            e[f"{x}"]=(cuentas[x],ejercicio_pasado[x])
                            x=x+1


                        p["año_actual_"+str(balance)]=d
                        p["ejercicio_pasado_"+str(balance)]=e

                    if len(cuentas)<=1:
                        print("Estado financiero "+a+" "+b+" "+c+" "+str(balance)+" está vacío en año "+year[m])
                        m=m+1
                        continue


                    #Se creo un diccionario para el ejercicio actual y ejercicio pasado
                    #de balance general y estado de resultados

                    if type=="i":
                        tipo="Individual"
                    else:
                        tipo="Consolidado"

                    if period=="t":
                        periodicidad="Trimestral"
                    else:
                        periodicidad="Anual"

                    InfoGeneral={"Razón_Social":bvl[firm],
                            "Año_de_Ejercicio_actual":int(year[m]),
                            "Año_de_Ejercicio_pasado":int(year[m])-1,
                            "Tipo_de_Información":tipo,
                            "Periodicidad":periodicidad,
                            "Trimestre":quarter,
                            "Balance_General_del_ejercicio_actual":p["año_actual_1"],
                            "Balance_General_del_ejercicio_pasado":p["ejercicio_pasado_1"],
                            "Estado_de_Resultado_del_ejercicio_actual":p["año_actual_3"],
                            "Estado_de_Resultado_del_ejercicio_pasado":p["ejercicio_pasado_3"]
                    }


                    from pymongo import MongoClient
                    client=MongoClient("mongodb+srv://root_bobsburguers:yoQnE9BsxD8YqpqL@bobsburguerscluster-z0q0x.mongodb.net/test?retryWrites=true&w=majority")

                    db=client.business

                    result=db.reviews.insert_one(InfoGeneral)
                    m=m+1

                driver.quit()

