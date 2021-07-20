from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options #se usa esta nueva librería para usar options
import time
''' con este programita se aparecen en el buscador las 11 opciones de la palabra Jessica, pero le quitamos la interfaz para 
que solo aparezca en el shell'''

chrome_options = Options()#si o si debe ser en ingles, tanto el chrome_options como el options()
chrome_options.add_argument("--headless")#esto es lo que hace que no se vean las pantallas y se lo metemos al webdriver de abajo


variable = "Jessica" 

driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("https://www.google.com.ar")
time.sleep(1)
buscar = driver.find_element_by_name("q")
buscar.send_keys(variable)
time.sleep(3)

for i in range(1,11):
	buscando = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text


	print( buscando)

driver.close()