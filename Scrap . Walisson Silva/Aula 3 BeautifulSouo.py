import requests
from bs4 import BeautifulSoup
response = requests.get('https://g1.globo.com/')

content = response.content
site = BeautifulSoup(content, 'html.parser' )
#Noticia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#titulo
titulo = noticia.find('a', attrs={'class':'feed-post-link'})

print(titulo.text)

#subtitulo
print(noticia.prettify())
#subtitulo = noticia.find('div',attrs={'class': 'bstn-fd-relatedtext'})
#print(subtitulo.text)