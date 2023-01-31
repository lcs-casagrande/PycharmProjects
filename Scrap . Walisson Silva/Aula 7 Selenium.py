import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('window-size=400,800')
#options.add_argument('--headless')

navegador = webdriver.Chrome(options=options)
navegador.get('https://www.airbnb.com.br/')
sleep(3)
input_place = navegador.find_element(By.CLASS_NAME,'button')
sleep(3)
input_place.send_keys('São Paulo')
sleep(3)
input_place.submit()



#navegador.find_element(By.CSS_SELECTOR,'button > img')
#site = BeautifulSoup(navegador.page_source, 'html.parser')
#print(site.prettify())
sleep(5)
