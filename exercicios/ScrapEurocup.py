import requests
from bs4 import BeautifulSoup
import re
import math
import pandas as pd

#url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'
url = 'https://www.flashscore.com/basketball/usa/nba/results/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
quant_itens = soup.find('div', attrs={'class': ''})

print(quant_itens)


    #print(titulo.text)
    #print(titulo['href']) #link da noticia

    #subtitulo
    #print(noticia.prettify())


    #print()
#news = pd.DataFrame(lista_noticias,columns=['Título', 'Subtítulo','Link'])
#news.to_excel('noticias.xlsx', index=False)
#print(news )