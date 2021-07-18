from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

variable = "Jessica"

driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("https://www.google.com.ar")
time.sleep(1)
buscar = driver.find_element_by_name("q")
buscar.send_keys(variable)

for i in range(1,11):
	buscando = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text
	print( buscando)
driver.close()


'''NOTA: el xpath que saqué es de la barra de busqueda que tira 10 opciones + la busqueda suma 11, ese xpath es diferente porque
no es directamente el de la barra de busqueda, es el xpath de las opciones que despliega. Se debe modificar el numero que arriba dice +str(1)+
porque justo ahi es donde sale el for y el conteo.