# web scrap selenius
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get('https://www.google.com')
sleep(2)
elemento = navegador.find_element(By.TAG_NAME,'input')

#navegador.find_element()
elemento.send_keys('data')
#print(elemento)