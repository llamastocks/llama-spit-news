from bs4 import BeautifulSoup
import requests
import urllib
import PyPDF2,io


url="https://www.bvl.com.pe/inf_hhii_3dias.html"
contenido=requests.get(url, verify=False).text

soup=BeautifulSoup(contenido,"html.parser")


links=[]
for link in soup.find_all("a"):
    links.append(link.get("href"))

response=requests.get(links[0],verify=False).content

pdf_content=io.BytesIO(response)
pdf_reader=PyPDF2.PdfFileReader(pdf_content)

print(pdf_reader.getPage(0).extractText())

