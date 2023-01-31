#obter produtso mercado livre
import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja?')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result '
                                           'shops__cardStyles ui-search-result--core andes-card--padding-default'})

#print(url_base + produto)
for produto in produtos:
    titulo = produto.find('h2', attrs={'class':'ui-search-item__title shops__item-title'})
    #titulo = produto.find('h2', attrs={'class':'ui-search-result__content-wrapper shops__result-content-wrapper'})

    link = produto.find('a', attrs={'class':'ui-search-link'})

    reais = produto.find('span', attrs={'class':'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class':'price-tag-cents'})
    if (centavos):
        centavos = centavos
    else:
        centavos = 0

    #print(produto.prettify())
    #print('titulo do produto:', titulo)
    print('titulo do produto:', titulo.text)
    #print('Link do produto:', link)
    print('Link do produto:', link['href'])
    print(f'Preço do produto: R${reais.text},{centavos.text}')
    print('\n')