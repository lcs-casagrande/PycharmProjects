import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

lista_noticias=[]
response = requests.get('https://g1.globo.com/')

content = response.content
site = BeautifulSoup(content, 'html.parser' )
#Noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})
print(site)
print(noticias)
for noticia in noticias:

     #titulo
    titulo = noticia.find('a', attrs={'class':'feed-post-link'})

    #print(titulo.text)
    #print(titulo['href']) #link da noticia

    #subtitulo
    #print(noticia.prettify())
    subtitulo = noticia.find('div',attrs={'class': 'bstn-fd-relatedtext'})
    if (subtitulo):
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])


    #print()
#news = pd.DataFrame(lista_noticias,columns=['Título', 'Subtítulo','Link'])
#news.to_excel('noticias.xlsx', index=False)
#print(news )