import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('window-size=800,800')
#options.add_argument('--headless')

navegador = webdriver.Chrome(options=options)
navegador.get('https://www.linkedin.com/')

sleep(.3)
email = navegador.find_element(By.ID,'session_key')
email.send_keys('5511974645103')
senha = navegador.find_element(By.ID,'session_password')
senha.send_keys('balotelli9')
senha.submit()

sleep(3)
lupa = navegador.find_element(By.CLASS_NAME,'search-global-typeahead__collapsed-search-button')
lupa.click()
sleep(3)
busca = navegador.find_element(By.TAG_NAME,'input')
busca.send_keys('advogado')
sleep(3)
enter = navegador.find_element(By.ID,'global-nav-typeahead')
busca.submit()
#busca_enter = navegador.find_element(By.NAME,'button > Vagas')
#busca_enter.click()

#busca_enter.submit()
sleep(2)
