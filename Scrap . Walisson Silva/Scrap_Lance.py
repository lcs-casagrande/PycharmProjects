import requests
from bs4 import BeautifulSoup
import re
import math
import pandas as pd
from datetime import timedelta


tem = []
hor = []
val = []
ven = []
tit = []
inicio = []
fim = []
data = []

for pag in range(1,203):
    url = f'https://www.lance24h.com.br/Leiloes_Arrematados.php?Pagina={pag}'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    valores = soup.findAll('div', attrs={'class': 'ExtSubInf3'})
    titulos = soup.findAll('h3', attrs={'class': 'ExtTitulo1'})
    vencedores = soup.findAll('div', attrs={'class': 'ExtSubInf2'})
    horas = soup.findAll('div', attrs={'class': 'ExtInf1 ExtInf1B'})
    print(url)

    for valor in valores:
        valor = valor.get_text().strip()
        #print(valor)
        val.append(valor)

    for titulo in titulos:
        titulo = titulo.get_text().strip()
        #print(titulo)
        tit.append(titulo)

    for vencedor in vencedores:
        vencedor = vencedor.get_text().strip()
        #print(vencedor)
        ven.append(vencedor)

    for hora in horas:
        #print(hora)
        hora = hora.get_text().strip()
        hor.append(hora)
        tempo1 = (hora[23:45].strip())
        tempo2 = (hora[79:110].strip())
        #print(f'inicio {tempo1}')
        #print(f'fim {tempo2}')
        dia = hora[20:33]
        #print(dia)
        inicio.append(tempo1)
        fim.append(tempo2)
        data.append(dia)

lances ={'hora':hor,'valor':val,'vencedor':ven,'titulo':tit,'inicio':inicio,'fim': fim,'data':data}
lance = pd.DataFrame(lances)
lance.to_csv('lance_csv')
#lance = spark.read.csv('df_tabela1_csv', header = True, inferSchema=True)
#lance.show()