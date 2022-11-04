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
id = soup.find('div', id = 'g_3_Qm3Xtsxr')
cla = soup.find('div', attrs={'class': 'event__part event__part--home event__part--1'})
print(site.status_code)
print(soup)

print(cla)
print(id)

#for int in id:
    #print(int)

'''index = quant_itens.find(' ')
quant = quant_itens[:index]
print(quant)x
print(index)'''
