import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

lista_noticias=[]
response = requests.get('https://www.linkedin.com/search/results/people/?keywords=arquiteto&origin=SWITCH_SEARCH_VERTICAL&sid=.1Y') #link da busca

content = response.content
site = BeautifulSoup(content, 'html.parser' )
print(site.prettify())